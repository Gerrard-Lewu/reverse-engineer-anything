"""User-visible capture boundaries, without requiring a browser or REA."""

import subprocess
import asyncio
import base64
import hashlib
import importlib.util
import json
import sys
import tempfile
from types import SimpleNamespace
import unittest
from pathlib import Path
from unittest.mock import patch
from contextlib import asynccontextmanager, redirect_stdout
import io


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "capture_explee.py"
SPEC = importlib.util.spec_from_file_location("capture_explee", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
sys.modules["capture_explee"] = MODULE
SERIES_SPEC = importlib.util.spec_from_file_location("capture_explee_series", ROOT / "scripts" / "capture_explee_series.py")
SERIES = importlib.util.module_from_spec(SERIES_SPEC)
SERIES_SPEC.loader.exec_module(SERIES)


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

    def test_invalid_cached_package_is_rejected_before_output_creation(self):
        cases = [
            ({"name": "other", "version": "6.4.0", "bin": {"rea-agents": "scripts/rea.mjs"}}, "must be rea-agents"),
            ({"name": "rea-agents", "version": "6.3.0", "bin": {"rea-agents": "scripts/rea.mjs"}}, "must be rea-agents"),
            ({"name": "rea-agents", "version": "6.4.0", "bin": {"rea-agents": "../other.mjs"}}, "unexpected dispatcher"),
            ({"name": "rea-agents", "version": "6.4.0", "bin": {"rea-agents": "scripts/rea.mjs"}}, "runtime is missing"),
        ]
        for package, message in cases:
            with self.subTest(message=message, package=package), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "package.json").write_text(json.dumps(package), encoding="utf-8")
                output = root / "capture"
                result = self.run_capture(output, "--rea-package-root", str(root))
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stderr)
                self.assertFalse(output.exists())

    def test_unreadable_cached_package_is_rejected_before_output_creation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "package.json").write_text("not JSON", encoding="utf-8")
            output = root / "capture"
            result = self.run_capture(output, "--rea-package-root", str(root))
            self.assertEqual(result.returncode, 2)
            self.assertIn("Cannot read", result.stderr)
            self.assertFalse(output.exists())


class ReaLauncherTests(unittest.TestCase):
    def test_default_windows_launcher_remains_pinned_npx(self):
        installed = {"npx": "existing-npx.cmd", "cmd.exe": "existing-cmd.exe"}
        with patch.object(MODULE.sys, "platform", "win32"), patch.object(
            MODULE.shutil, "which", side_effect=installed.get
        ):
            self.assertEqual(MODULE.rea_launch(), (
                "existing-cmd.exe", ["/d", "/c", "existing-npx.cmd", "-y", "rea-agents@6.4.0", "mcp"]
            ))

    def test_cached_dispatcher_bypasses_npm_and_preserves_mcp_mode(self):
        with tempfile.TemporaryDirectory(prefix="rea package ") as directory:
            root = Path(directory).resolve()
            (root / "scripts").mkdir()
            (root / "dist").mkdir()
            (root / "scripts" / "rea.mjs").write_text("", encoding="utf-8")
            (root / "dist" / "main.js").write_text("", encoding="utf-8")
            (root / "package.json").write_text(json.dumps({
                "name": "rea-agents", "version": "6.4.0",
                "bin": {"rea-agents": "scripts/rea.mjs"},
            }), encoding="utf-8")
            with patch.object(MODULE.shutil, "which", return_value="existing-node") as which:
                self.assertEqual(MODULE.rea_launch(root),
                                 ("existing-node", [str(root / "scripts" / "rea.mjs"), "mcp"]))
            which.assert_called_once_with("node")


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


class RetainedInspectionTests(unittest.TestCase):
    EVIDENCE_ID = "ev_fixed_inspection"
    RESULT = {"target": {"target_id": "selected", "url": MODULE.EXPLEE_URL},
              "completeness": {"status": "policy_filtered"}, "accessibility_text": "Fixture page"}

    def budget_error(self):
        return {"error": {"code": "resource_constraint", "category": "resource_constraint",
                          "message": "The operation completed, but its complete MCP response exceeds the stdio response budget. The analysis result was not truncated. Export retained evidence to consume the complete analysis, or use complete CLI JSON output.",
                          "details": {"operation": "inspect_web_page", "resource": "transport",
                                      "reported_limits": {"boundary": "mcp-response", "constraint": "receive-buffer",
                                          "evidence_id": self.EVIDENCE_ID,
                                          "evidence_reference": {"kind": "retained-evidence", "evidence_id": self.EVIDENCE_ID}}}}}

    def retained(self, **changes):
        return {"evidence_id": self.EVIDENCE_ID, "operation": "inspect_web_page",
                "normalized_result": self.RESULT, **changes}

    def recover(self, folder, records, error=None):
        artifacts, receipt = [], {}
        bundle_bytes = json.dumps({"records": records}).encode("utf-8")

        async def export(arguments):
            Path(arguments["path"]).write_bytes(bundle_bytes)
            return SimpleNamespace(structuredContent={"normalized_result": {"exported": True}},
                                   content=[], isError=False)

        result = asyncio.run(MODULE.recover_retained_inspection(
            error or self.budget_error(), Path(folder), artifacts, receipt, export))
        return result, artifacts, receipt, bundle_bytes

    def test_complete_retained_record_and_export_are_preserved_with_hash(self):
        with tempfile.TemporaryDirectory() as folder:
            result, artifacts, receipt, data = self.recover(folder, [self.retained()])
            self.assertEqual(result, self.RESULT)
            self.assertEqual((Path(folder) / "retained-inspection-bundle.json").read_bytes(), data)
            hashed = next(item for item in artifacts if item["path"] == "retained-inspection-bundle.json")
            self.assertEqual(hashed["sha256"], hashlib.sha256(data).hexdigest())
            retained = json.loads((Path(folder) / "inspect_web_page-retained.json").read_text(encoding="utf-8"))
            self.assertEqual(retained, self.retained())
            self.assertEqual(receipt["response_budget_recovery"]["evidence_id"], self.EVIDENCE_ID)
            coverage = {"coverage": [], "limitations": []}
            MODULE.record_coverage(coverage, "inspect_web_page", result, MODULE.EXPLEE_URL, "selected")

    def test_missing_ambiguous_wrong_operation_or_missing_result_fail_closed(self):
        cases = [[], [self.retained(), self.retained()],
                 [self.retained(operation="capture_web_screenshot")],
                 [self.retained(evidence_id="ev_other")], [self.retained(normalized_result=None)]]
        for records in cases:
            with self.subTest(records=records), tempfile.TemporaryDirectory() as folder:
                with self.assertRaises(RuntimeError):
                    self.recover(folder, records)
                self.assertFalse((Path(folder) / "inspect_web_page-retained.json").exists())

    def test_other_errors_never_invoke_export(self):
        errors = [self.budget_error() for _ in range(4)]
        errors[0]["error"]["message"] = "Operation failed"
        errors[1]["error"]["code"] = "execution_failure"
        errors[2]["error"]["details"]["operation"] = "capture_web_screenshot"
        errors[3]["error"]["details"]["reported_limits"]["evidence_reference"]["evidence_id"] = "ev_other"
        for error in errors:
            with self.subTest(error=error), tempfile.TemporaryDirectory() as folder:
                with self.assertRaisesRegex(RuntimeError, "not a completed"):
                    self.recover(folder, [self.retained()], error)
                self.assertEqual(list(Path(folder).iterdir()), [])

    def test_failed_or_missing_export_cannot_recover(self):
        for failed in [True, False]:
            with self.subTest(export_is_error=failed), tempfile.TemporaryDirectory() as folder:
                async def export(arguments):
                    return SimpleNamespace(structuredContent={"error": {"code": "fixture_failure"}},
                                           content=[], isError=failed)
                with self.assertRaisesRegex(RuntimeError, "could not export"):
                    asyncio.run(MODULE.recover_retained_inspection(
                        self.budget_error(), Path(folder), [], {}, export))
                self.assertFalse((Path(folder) / "inspect_web_page-retained.json").exists())


class SharedSeriesTests(unittest.TestCase):
    def options(self):
        return SimpleNamespace(rea_package_root=None, rea_launch=("unused", []),
                               cdp_endpoint="http://127.0.0.1:9222", target_id="selected")

    def test_supplied_session_is_borrowed_without_initialization(self):
        connection = (object(), object(), object())
        async def borrow():
            async with MODULE.rea_session(None, connection) as actual:
                self.assertIs(actual, connection)
        asyncio.run(borrow())

    def test_command_rejection_preserves_existing_evidence_and_origin_scope(self):
        with tempfile.TemporaryDirectory() as folder:
            valid = {"source_url": MODULE.EXPLEE_URL, "label": "fixture", "output": str(Path(folder) / "new")}
            cases = [{**valid, "source_url": "https://other.example/"},
                     {**valid, "output": folder}, {**valid, "observation_seconds": True},
                     {**valid, "observation_seconds": float("nan")}, {**valid, "extra": True}]
            for command in cases:
                with self.subTest(command=command), self.assertRaises(ValueError):
                    SERIES.validate_command(command, self.options())
            self.assertEqual(list(Path(folder).iterdir()), [])
            parsed = SERIES.validate_command(valid, self.options())
            self.assertFalse(parsed.output.exists())
            self.assertEqual(parsed.target_id, "selected")

    def test_six_states_share_one_session_and_seventh_is_not_created(self):
        with tempfile.TemporaryDirectory() as folder:
            commands = [json.dumps({"source_url": MODULE.EXPLEE_URL, "label": str(i),
                                    "output": str(Path(folder) / str(i))}) + "\n" for i in range(7)]
            lines = iter(commands)
            opened, captured = [], []
            connection = (object(), object(), object())
            @asynccontextmanager
            async def session(options):
                opened.append(True)
                yield connection
            async def read_line():
                return next(lines, "")
            async def capture(args, supplied):
                self.assertIs(supplied, connection)
                captured.append(args.label)
                return 0
            with redirect_stdout(io.StringIO()) as stdout:
                code = asyncio.run(SERIES.run_series(self.options(), read_line, capture, session))
            self.assertEqual(code, 0)
            self.assertEqual(len(opened), 1)
            self.assertEqual(captured, [str(i) for i in range(6)])
            self.assertFalse((Path(folder) / "6").exists())
            self.assertIn("READY", stdout.getvalue())

    def test_quit_finishes_without_capture_or_output(self):
        @asynccontextmanager
        async def session(options):
            yield (None, None, None)
        async def read_line():
            return '{"quit": true}\n'
        async def capture(args, supplied):
            self.fail("quit must not capture")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(asyncio.run(SERIES.run_series(self.options(), read_line, capture, session)), 0)

    def test_series_returns_failure_after_failed_state_then_quit(self):
        with tempfile.TemporaryDirectory() as folder:
            lines = iter([json.dumps({"source_url": MODULE.EXPLEE_URL, "label": "fixture",
                                      "output": str(Path(folder) / "failed-state")}), '{"quit": true}'])
            @asynccontextmanager
            async def session(options):
                yield (None, None, None)
            async def read_line():
                return next(lines, "")
            async def capture(args, supplied):
                return 1
            with redirect_stdout(io.StringIO()) as output:
                code = asyncio.run(SERIES.run_series(self.options(), read_line, capture, session))
            self.assertEqual(code, 1)
            self.assertIn('"exit_code": 1', output.getvalue())
            self.assertIn('"states": 1', output.getvalue())

    def test_failure_after_recovery_preserves_provenance_without_success_status(self):
        with tempfile.TemporaryDirectory() as folder:
            args = SimpleNamespace(output=Path(folder), label="fixture", source_url=MODULE.EXPLEE_URL)
            recovery = {"evidence_id": "ev_fixture", "export": "retained-inspection-bundle.json"}
            async def later_failure(args, artifacts, connection, context):
                context.update({"status": "captured", "session_evidence_scope": "cumulative_shared_session",
                                "rea_launcher": "installed_dispatcher", "response_budget_recovery": recovery})
                artifacts.append({"path": "retained-inspection-bundle.json", "sha256": "fixture"})
                raise RuntimeError("fixture screenshot failure")
            with patch.object(MODULE, "capture", later_failure), redirect_stdout(io.StringIO()):
                code = asyncio.run(MODULE.capture_with_receipt(args, (None, None, None)))
            receipt = json.loads((Path(folder) / "receipt.json").read_text(encoding="utf-8"))
            self.assertEqual(code, 1)
            self.assertEqual(receipt["status"], "failed")
            self.assertEqual(receipt["session_evidence_scope"], "cumulative_shared_session")
            self.assertEqual(receipt["rea_launcher"], "installed_dispatcher")
            self.assertEqual(receipt["response_budget_recovery"], recovery)
            self.assertEqual(receipt["errors"], [{"type": "RuntimeError", "message": "fixture screenshot failure"}])
            self.assertEqual(len(receipt["artifacts"]), 1)


if __name__ == "__main__":
    unittest.main()
