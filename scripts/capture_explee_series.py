#!/usr/bin/env python3
"""Passively capture up to six operator-selected Explee states in one real REA session.

After READY, submit one JSON object per line with source_url, label, output and
optional observation_seconds (default 1). Navigate separately, then submit the
exact stable URL. Submit {"quit": true} or EOF to close only this MCP session.
Complete session exports are cumulative; no Evidence is cleared between states.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from types import SimpleNamespace

from capture_explee import capture_with_receipt, endpoint, origin, rea_launch, rea_session, source_url

MAX_STATES = 6


def validate_command(value, options):
    if not isinstance(value, dict):
        raise ValueError("Submit a JSON object.")
    if value == {"quit": True}:
        return None
    if set(value) - {"source_url", "label", "output", "observation_seconds"}:
        raise ValueError("Unknown capture command fields.")
    if any(not isinstance(value.get(key), str) or not value[key].strip()
           for key in ("source_url", "label", "output")):
        raise ValueError("source_url, label and output must be nonempty strings.")
    url = source_url(value["source_url"])
    if origin(url) != "https://explee.com":
        raise ValueError("Series captures are scoped to https://explee.com.")
    seconds = value.get("observation_seconds", 1)
    if isinstance(seconds, bool) or not isinstance(seconds, (float, int)) or not 0.1 <= seconds <= 60:
        raise ValueError("observation_seconds must be between 0.1 and 60.")
    output = Path(value["output"]).expanduser().absolute()
    if output.exists() or output.is_symlink():
        raise ValueError("Choose a new output directory; existing evidence is never overwritten.")
    return SimpleNamespace(**vars(options), source_url=url, label=value["label"],
                           output=output, observation_seconds=seconds, analyze_bundle=False)


async def run_series(options, read_line=None, capture_state=capture_with_receipt,
                     session_context=rea_session):
    read_line = read_line or (lambda: asyncio.to_thread(sys.stdin.readline))
    failed = False
    async with session_context(options) as connection:
        print("READY: real REA initialized; maximum 6 states; exports are cumulative.", flush=True)
        count = 0
        while count < MAX_STATES:
            line = await read_line()
            if not line:
                break
            try:
                args = validate_command(json.loads(line), options)
            except (ValueError, argparse.ArgumentTypeError, OSError) as error:
                print(json.dumps({"status": "rejected", "message": str(error)}), flush=True)
                continue
            if args is None:
                break
            try:
                args.output.mkdir(parents=True, exist_ok=False)
            except OSError as error:
                print(json.dumps({"status": "rejected", "message": str(error)}), flush=True)
                continue
            count += 1
            code = await capture_state(args, connection)
            failed = failed or code != 0
            print(json.dumps({"status": "state_finished", "state_number": count,
                              "exit_code": code, "output": str(args.output)}), flush=True)
        print(json.dumps({"status": "series_finished", "states": count}), flush=True)
    return 1 if failed else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rea-package-root", type=Path)
    parser.add_argument("--cdp-endpoint", type=endpoint, required=True)
    parser.add_argument("--target-id", required=True)
    options = parser.parse_args()
    if not options.target_id.strip():
        parser.error("--target-id must be nonempty.")
    try:
        options.rea_launch = rea_launch(options.rea_package_root)
        import mcp  # noqa: F401
    except (ValueError, ImportError) as error:
        parser.error(str(error))
    try:
        return asyncio.run(run_series(options))
    except (Exception, KeyboardInterrupt) as error:
        print(f"Series stopped: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
