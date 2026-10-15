"""User-visible capture boundaries, without requiring a browser or REA."""

import subprocess
import base64
import hashlib
import importlib.util
import sys
import tempfile
from types import SimpleNamespace
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "capture_explee.py"
SPEC = importlib.util.spec_from_file_location("capture_explee", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CaptureCommandTests(unittest.TestCase):
    def run_capture(self, output, *arguments):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--output", str(output), *arguments],
            capture_output=True,
            text=True,
            timeout=10,
        )

    def test_remote_debug_endpoint_is_rejected_before_output_creation(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "capture"
            result = self.run_capture(output, "--cdp-endpoint", "http://example.com:9222")
            self.assertEqual(result.returncode, 2)
            self.assertIn("literal loopback", result.stderr)
            self.assertFalse(output.exists())

    def test_endpoint_credentials_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "capture"
            result = self.run_capture(
                output, "--cdp-endpoint", "http://user:password@127.0.0.1:9222"
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("literal loopback", result.stderr)
            self.assertFalse(output.exists())

    def test_existing_capture_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "capture"
            output.mkdir()
            marker = output / "prior-evidence.json"
            marker.write_text('{"preserve":true}', encoding="utf-8")
            result = self.run_capture(output)
            self.assertEqual(result.returncode, 2)
            self.assertIn("new output directory", result.stderr)
            self.assertEqual(marker.read_text(encoding="utf-8"), '{"preserve":true}')
            self.assertEqual(list(output.iterdir()), [marker])


class ScreenshotIntegrityTests(unittest.TestCase):
    # A fixed 1x1 PNG independent of REA and the capture implementation.
    PNG = base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aH1sAAAAASUVORK5CYII="
    )

    def response(self, digest=None):
        artifact = {
            "media_type": "image/png", "data_base64": base64.b64encode(self.PNG).decode("ascii"),
            "bytes": len(self.PNG), "sha256": digest or hashlib.sha256(self.PNG).hexdigest(),
        }
        return SimpleNamespace(structuredContent={"normalized_result": {"artifact": artifact}}, content=[])

    def test_structured_png_bytes_are_preserved(self):
        self.assertEqual(MODULE.screenshot_bytes(self.response()), self.PNG)

    def test_mismatched_screenshot_digest_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "digest differs"):
            MODULE.screenshot_bytes(self.response("0" * 64))


class CaptureCoverageTests(unittest.TestCase):
    def test_same_origin_route_change_cannot_be_reported_as_selected_page(self):
        receipt = {"coverage": [], "limitations": []}
        result = {"target": {"target_id": "selected", "url": "https://explee.com/other"}}
        with self.assertRaisesRegex(RuntimeError, "source URL changed"):
            MODULE.record_coverage(receipt, "inspect_web_page", result, MODULE.EXPLEE_URL, "selected")

    def test_truncated_dom_is_a_material_coverage_gap(self):
        receipt = {"coverage": [], "limitations": []}
        result = {
            "target": {"target_id": "selected", "url": MODULE.EXPLEE_URL},
            "completeness": {"status": "truncated", "truncated_sections": ["dom"]},
        }
        MODULE.record_coverage(receipt, "inspect_web_page", result, MODULE.EXPLEE_URL, "selected")
        self.assertTrue(receipt["limitations"])


if __name__ == "__main__":
    unittest.main()
