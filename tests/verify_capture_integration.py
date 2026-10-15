#!/usr/bin/env python3
"""Exercise the capture CLI against real REA and a local Chromium fixture.

This POSIX harness verifies the capture kit, not any Explee screen or behavior.
"""

from __future__ import annotations

import functools
import hashlib
import http.server
import json
import os
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def free_port():
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        return listener.getsockname()[1]


def main():
    browser = os.environ.get("REA_BROWSER_EXECUTABLE") or shutil.which("chromium")
    if not browser:
        raise RuntimeError("Set REA_BROWSER_EXECUTABLE to an installed Chromium-family executable.")
    directory = ROOT / "evidence" / "verification"
    directory.mkdir(parents=True, exist_ok=True)
    capture_path = directory / ("fixture-" + str(time.time_ns()))

    class FixtureHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    handler = functools.partial(FixtureHandler, directory=str(ROOT / "tests" / "fixtures"))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    page = f"http://127.0.0.1:{server.server_port}/index.html"
    port = free_port()
    try:
        with tempfile.TemporaryDirectory(prefix="rea-fixture-") as profile:
            with (directory / "chromium.log").open("wb") as log:
                process = subprocess.Popen([
                    browser, "--headless", "--disable-gpu", "--disable-background-networking",
                    "--no-first-run", "--no-default-browser-check",
                    f"--remote-debugging-port={port}", f"--user-data-dir={profile}", page,
                ], stdout=log, stderr=log, start_new_session=True)
                try:
                    discovery = f"http://127.0.0.1:{port}/json/version"
                    deadline = time.monotonic() + 20
                    while True:
                        if process.poll() is not None:
                            raise RuntimeError("Chromium exited before exposing CDP; inspect chromium.log.")
                        try:
                            with urllib.request.urlopen(discovery, timeout=0.5) as response:
                                json.load(response)
                            break
                        except OSError:
                            if time.monotonic() >= deadline:
                                raise TimeoutError("Chromium did not expose its CDP endpoint.")
                            time.sleep(0.1)
                    command = [
                        sys.executable, str(ROOT / "scripts" / "capture_explee.py"),
                        "--cdp-endpoint", f"http://127.0.0.1:{port}",
                        "--source-url", page, "--output", str(capture_path),
                        "--label", "synthetic-fixture", "--observation-seconds", "1.2",
                        "--analyze-bundle",
                    ]
                    captured = subprocess.run(command, capture_output=True, text=True, timeout=120)
                    print(captured.stdout, end="")
                    if captured.returncode:
                        print(captured.stderr, file=sys.stderr, end="")
                        receipt = capture_path / "receipt.json"
                        if receipt.is_file():
                            print(receipt.read_text(encoding="utf-8"), file=sys.stderr)
                        return captured.returncode
                    receipt = json.loads((capture_path / "receipt.json").read_text(encoding="utf-8"))
                    assert receipt["status"] == "captured"
                    assert receipt["source_url"] == page
                    for artifact in receipt["artifacts"]:
                        content = (capture_path / artifact["path"]).read_bytes()
                        assert len(content) == artifact["bytes"]
                        assert hashlib.sha256(content).hexdigest() == artifact["sha256"]
                    png = (capture_path / "screenshot.png").read_bytes()
                    assert png[:8] == b"\x89PNG\r\n\x1a\n"
                    inspection = json.loads((capture_path / "inspect_web_page.json").read_text())
                    network = inspection["normalized_result"]["network"]
                    sample_url = page.rsplit("/", 1)[0] + "/sample.json"
                    requests = [entry for entry in network["requests"] if entry["url"] == sample_url]
                    assert any(entry["method"] == "GET" and entry["status"] == 200
                               and entry["body_shapes"]["status"] == "included"
                               and entry["body_shapes"]["response"]["root_type"] == "object"
                               for entry in requests)
                    assert network["prior_activity_available"] is False
                    assert (capture_path / "evidence-bundle.json").is_file()
                    print("PASS: real REA capture, screenshot, post-attach traffic, export, and artifact digests.")
                    print("Synthetic fixture only; no Explee behavior was verified.")
                finally:
                    if process.poll() is None:
                        os.killpg(process.pid, signal.SIGTERM)
                        try:
                            process.wait(timeout=5)
                        except subprocess.TimeoutExpired:
                            os.killpg(process.pid, signal.SIGKILL)
                            process.wait(timeout=5)
    finally:
        server.shutdown()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
