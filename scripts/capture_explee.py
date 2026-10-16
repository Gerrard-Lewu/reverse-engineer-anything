#!/usr/bin/env python3
"""Capture one explicitly selected browser page using passive REA MCP tools.

Run on the same computer as the source browser. No navigation, sending, or
configuration writes are performed. Each invocation needs a new output folder.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import hashlib
import json
import os
import shutil
import sys
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit


REA_VERSION = "6.4.0"
EXPLEE_URL = "https://explee.com/app-auto-gtm/p/40610"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
COMPLETED_RESPONSE_BUDGET_MESSAGE = (
    "The operation completed, but its complete MCP response exceeds the stdio response budget. "
    "The analysis result was not truncated. Export retained evidence to consume the complete analysis, "
    "or use complete CLI JSON output."
)


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def endpoint(value: str) -> str:
    try:
        url = urlsplit(value)
        valid = (
            url.scheme == "http"
            and url.hostname in {"127.0.0.1", "::1"}
            and url.port is not None
            and url.username is None
            and url.password is None
            and url.path in {"", "/"}
            and not url.query
            and not url.fragment
        )
    except ValueError:
        valid = False
    if not valid:
        raise argparse.ArgumentTypeError(
            "Use a literal loopback CDP endpoint with an explicit port, "
            "such as http://127.0.0.1:9222, without credentials or extra paths."
        )
    return value.rstrip("/")


def origin(value: str) -> str:
    url = urlsplit(value)
    if url.scheme not in {"http", "https"} or not url.hostname:
        raise ValueError("The source URL must be an absolute HTTP(S) URL.")
    if url.username is not None or url.password is not None:
        raise ValueError("The source URL must not contain transport credentials.")
    url.port  # Validate any supplied port.
    return f"{url.scheme}://{url.netloc}"


def source_url(value: str) -> str:
    try:
        origin(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError(str(error)) from error
    return value


def rea_launch(package_root: Path | None = None) -> tuple[str, list[str]]:
    """Select the official dispatcher without changing the MCP capture protocol."""
    if package_root is not None:
        root = package_root.expanduser().resolve()
        try:
            package = json.loads((root / "package.json").read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise ValueError("Cannot read the supplied REA package.json.") from error
        if not isinstance(package, dict) or package.get("name") != "rea-agents" or package.get("version") != REA_VERSION:
            raise ValueError(f"The supplied package must be rea-agents {REA_VERSION}.")
        bins = package.get("bin")
        if not isinstance(bins, dict) or bins.get("rea-agents") != "scripts/rea.mjs":
            raise ValueError("The supplied REA package has an unexpected dispatcher.")
        dispatcher = root / "scripts" / "rea.mjs"
        runtime = root / "dist" / "main.js"
        if any(not path.is_file() or not path.resolve().is_relative_to(root)
               for path in (dispatcher, runtime)):
            raise ValueError("The supplied REA dispatcher or compiled MCP runtime is missing or outside the package.")
        node = shutil.which("node")
        if node is None:
            raise ValueError("Node.js is missing. Use an existing supported Node.js installation.")
        return node, [str(dispatcher), "mcp"]
    npm = shutil.which("npx")
    if npm is None:
        raise ValueError("npx is missing. Use an existing supported Node.js/npm installation.")
    arguments = ["-y", f"rea-agents@{REA_VERSION}", "mcp"]
    if sys.platform == "win32":
        return shutil.which("cmd.exe") or "cmd.exe", ["/d", "/c", npm, *arguments]
    return npm, arguments


def result_of(record: dict) -> dict:
    result = record.get("normalized_result", record.get("result", record))
    if not isinstance(result, dict):
        raise ValueError("REA returned a non-object result; preserve it and stop.")
    return result


def evidence_of(response) -> dict:
    if response.structuredContent is not None:
        return response.structuredContent
    for block in response.content:
        if getattr(block, "type", None) == "text":
            try:
                value = json.loads(block.text)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                return value
    raise ValueError("REA returned no complete structured JSON record.")


def write_artifact(folder: Path, name: str, content: bytes, artifacts: list) -> None:
    path = folder / name
    with path.open("xb") as stream:
        stream.write(content)
    observed = path.read_bytes()
    if observed != content:
        raise OSError(f"Readback differs for {name}.")
    artifacts.append(
        {"path": name, "bytes": len(observed), "sha256": hashlib.sha256(observed).hexdigest()}
    )


def write_json(folder: Path, name: str, value, artifacts: list) -> None:
    data = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    write_artifact(folder, name, data, artifacts)


def screenshot_bytes(response) -> bytes | None:
    result = result_of(evidence_of(response))
    artifact = result.get("artifact", {})
    if artifact.get("media_type") == "image/png" and artifact.get("data_base64"):
        data = base64.b64decode(artifact["data_base64"], validate=True)
        if not data.startswith(PNG_SIGNATURE):
            raise ValueError("REA's screenshot artifact is not a PNG.")
        if len(data) != artifact.get("bytes"):
            raise ValueError("REA's screenshot artifact byte count differs from its declaration.")
        if hashlib.sha256(data).hexdigest() != artifact.get("sha256"):
            raise ValueError("REA's screenshot artifact digest differs from its declaration.")
        return data
    for block in response.content:
        if getattr(block, "type", None) == "image" and block.mimeType == "image/png":
            data = base64.b64decode(block.data, validate=True)
            if not data.startswith(PNG_SIGNATURE):
                raise ValueError("REA's image block is not a PNG.")
            return data
    return None


def record_coverage(receipt: dict, name: str, result: dict, source: str, target_id: str) -> None:
    if name == "analyze_web_bundle":
        observed_url = result.get("capture", {}).get("target_url")
    else:
        observed_target = result.get("target", {})
        observed_url = observed_target.get("url")
        if observed_target.get("target_id") != target_id:
            raise RuntimeError(f"REA {name} returned a different target identity.")
    if observed_url != source:
        raise RuntimeError(f"The source URL changed during {name}; its saved record is not the selected state.")
    completeness = result.get("completeness", {})
    receipt["coverage"].append({"operation": name, "completeness": completeness})
    material_gap = (
        bool(completeness.get("truncated_sections"))
        or bool(completeness.get("unavailable_sections"))
        or completeness.get("status") in {"truncated", "partial"}
        or bool(completeness.get("dropped_events", {}).get("total", 0))
        or bool(completeness.get("parse_failures", 0))
    )
    if material_gap:
        receipt["limitations"].append(f"{name} reported material incomplete coverage; see its completeness record.")


def retained_inspection_id(record: dict) -> str | None:
    error = record.get("error", {})
    details = error.get("details", {})
    limits = details.get("reported_limits", {})
    evidence_id = limits.get("evidence_id")
    reference = limits.get("evidence_reference", {})
    if (error.get("code") == "resource_constraint"
            and error.get("category") == "resource_constraint"
            and error.get("message") == COMPLETED_RESPONSE_BUDGET_MESSAGE
            and details.get("operation") == "inspect_web_page"
            and details.get("resource") == "transport"
            and limits.get("boundary") == "mcp-response"
            and limits.get("constraint") == "receive-buffer"
            and isinstance(evidence_id, str) and evidence_id.startswith("ev_")
            and reference == {"kind": "retained-evidence", "evidence_id": evidence_id}):
        return evidence_id
    return None


async def recover_retained_inspection(record, output, artifacts, receipt, export):
    evidence_id = retained_inspection_id(record)
    if evidence_id is None:
        raise RuntimeError("REA inspection error is not a completed response-budget result.")
    bundle = output / "retained-inspection-bundle.json"
    response = await export({"path": str(bundle)})
    write_json(output, "retained-inspection-export.json", evidence_of(response), artifacts)
    if response.isError or not bundle.is_file():
        raise RuntimeError("REA could not export retained inspection evidence.")
    data = bundle.read_bytes()
    artifacts.append({"path": bundle.name, "bytes": len(data),
                      "sha256": hashlib.sha256(data).hexdigest()})
    exported = json.loads(data)
    records = exported.get("records") if isinstance(exported, dict) else None
    if not isinstance(records, list):
        raise RuntimeError("Retained inspection export has no records array.")
    matches = [item for item in records if isinstance(item, dict)
               and item.get("evidence_id") == evidence_id]
    if len(matches) != 1 or matches[0].get("operation") != "inspect_web_page":
        raise RuntimeError("Retained inspection Evidence ID is missing, ambiguous or belongs to another operation.")
    retained = matches[0]
    if not isinstance(retained.get("normalized_result"), dict):
        raise RuntimeError("Retained inspection has no complete normalized result.")
    write_json(output, "inspect_web_page-retained.json", retained, artifacts)
    artifacts[-1]["rea_evidence_id"] = evidence_id
    receipt["response_budget_recovery"] = {
        "operation": "inspect_web_page", "evidence_id": evidence_id,
        "original_error": "inspect_web_page.json", "export": bundle.name,
        "retained_record": "inspect_web_page-retained.json",
        "reported_limits": record["error"]["details"]["reported_limits"],
        "limitation": "Original MCP delivery failed; complete retained Evidence was consumed from the real session export.",
    }
    return retained["normalized_result"]


@asynccontextmanager
async def rea_session(args, supplied=None):
    """Own one real MCP session, or borrow an already initialized session."""
    if supplied is not None:
        yield supplied
        return
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    command, command_args = args.rea_launch
    parameters = StdioServerParameters(
        command=command,
        args=command_args,
        env=dict(os.environ),
    )
    async with stdio_client(parameters) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            try:
                initialized = await asyncio.wait_for(session.initialize(), timeout=120)
            except TimeoutError as error:
                raise RuntimeError("REA initialization exceeded 120 seconds; no source capture was attempted.") from error
            try:
                catalog = await asyncio.wait_for(session.list_tools(), timeout=45)
            except TimeoutError as error:
                raise RuntimeError("REA tool discovery exceeded 45 seconds; no source capture was attempted.") from error
            yield session, initialized, catalog


async def capture(args, artifacts: list, connection=None, receipt_context=None) -> dict:
    receipt = receipt_context if receipt_context is not None else {}
    receipt.update({
        "status": "in_progress",
        "kind": "passive_source_capture",
        "source_url": args.source_url,
        "label": args.label,
        "started_at": timestamp(),
        "observation_seconds": args.observation_seconds,
        "cross_call_state_alignment": "not_proven",
        "coverage": [],
        "limitations": [],
        "artifacts": artifacts,
        "rea_launcher": "installed_dispatcher" if args.rea_package_root else "npx",
        "session_evidence_scope": "cumulative_shared_session" if connection is not None else "single_capture_session",
    })
    async with rea_session(args, connection) as (session, initialized, catalog):
        tools = {tool.name: tool for tool in catalog.tools}
        needed = {
            "binary_session", "list_browser_targets", "inspect_web_page",
            "capture_web_screenshot", "export_evidence_bundle",
        }
        if args.analyze_bundle:
            needed.add("analyze_web_bundle")
        missing = needed - tools.keys()
        if missing:
            raise RuntimeError("The connected server lacks tools: " + ", ".join(sorted(missing)))
        write_json(args.output, "tool-schemas.json", {
            "server": initialized.serverInfo.model_dump(mode="json"),
            "protocol_version": initialized.protocolVersion,
            "tools": [tools[name].model_dump(mode="json") for name in sorted(needed)],
        }, artifacts)

        async def call(name: str, arguments: dict):
            response = await asyncio.wait_for(session.call_tool(name, arguments), timeout=120)
            record = evidence_of(response)
            write_json(args.output, f"{name}.json", record, artifacts)
            if record.get("evidence_id"):
                artifacts[-1]["rea_evidence_id"] = record["evidence_id"]
            if response.isError:
                if name == "inspect_web_page" and retained_inspection_id(record) is not None:
                    async def export_retained(arguments):
                        return await asyncio.wait_for(
                            session.call_tool("export_evidence_bundle", arguments), timeout=120)
                    recovered = await recover_retained_inspection(
                        record, args.output, artifacts, receipt, export_retained)
                    return response, recovered
                raise RuntimeError(f"REA {name} failed; inspect its saved JSON record.")
            return response, result_of(record)

        @asynccontextmanager
        async def preserve_session_evidence():
            failure = None
            try:
                yield
            except BaseException as error:
                failure = error
                raise
            finally:
                try:
                    bundle = args.output / "evidence-bundle.json"
                    await call("export_evidence_bundle", {"path": str(bundle)})
                    if not bundle.is_file():
                        raise RuntimeError("REA reported export success but no evidence bundle exists.")
                    data = bundle.read_bytes()
                    artifacts.append({"path": bundle.name, "bytes": len(data),
                                      "sha256": hashlib.sha256(data).hexdigest()})
                except Exception as export_error:
                    if failure is None:
                        raise
                    write_json(args.output, "export-error.json", {
                        "type": type(export_error).__name__, "message": str(export_error),
                        "limitation": "Retained session Evidence could not be exported before teardown.",
                    }, artifacts)

        async with preserve_session_evidence():
            _, state = await call("binary_session", {"expected_package_version": REA_VERSION})
            identity = state.get("server_identity", {})
            if identity.get("package", {}).get("version") != REA_VERSION:
                raise RuntimeError("REA package identity differs from the requested version.")
            receipt["rea_version"] = REA_VERSION
            availability = state.get("tool_availability", [])
            if isinstance(availability, list):
                unavailable = [item["name"] for item in availability
                               if item.get("name") in needed and not item.get("available")]
                if unavailable:
                    raise RuntimeError("REA tools are unavailable: " + ", ".join(unavailable))

            scope = {"cdp_endpoint": args.cdp_endpoint,
                     "allowed_origins": [origin(args.source_url)]}
            _, discovery = await call("list_browser_targets", scope)
            targets = discovery.get("targets", [])
            matches = [target for target in targets if target.get("url") == args.source_url]
            if args.target_id:
                matches = [target for target in matches if target.get("id") == args.target_id
                           or target.get("target_id") == args.target_id]
            if len(matches) != 1:
                raise RuntimeError(
                    f"Expected one target at the exact source URL; found {len(matches)}. "
                    "Inspect list_browser_targets.json and supply --target-id for duplicates. "
                    "Open the intended page manually if it is absent."
                )
            selected = matches[0]
            target_id = selected.get("target_id") or selected.get("id")
            if not target_id:
                raise RuntimeError("Selected REA target has no target identity.")
            receipt["target_id"] = target_id
            target = {**scope, "target_id": target_id}
            print(f"Observing for {args.observation_seconds:g}s. Keep the intended page in view.", flush=True)
            _, page = await call("inspect_web_page", {
                **target,
                "observation_ms": round(args.observation_seconds * 1000),
                "include_accessibility_text": True,
                "include_script_sources": True,
                "include_json_body_shapes": True,
            })
            record_coverage(receipt, "inspect_web_page", page, args.source_url, target_id)
            print("Capture window ended. Leave the page stable while remaining evidence is saved.", flush=True)
            screenshot, screenshot_result = await call("capture_web_screenshot", target)
            record_coverage(receipt, "capture_web_screenshot", screenshot_result, args.source_url, target_id)
            png = screenshot_bytes(screenshot)
            if png is not None:
                write_artifact(args.output, "screenshot.png", png, artifacts)
            else:
                receipt["limitations"].append("Screenshot Evidence was saved, but PNG extraction is unavailable.")
            receipt["screenshot_png_saved"] = png is not None
            receipt["viewport"] = screenshot_result.get("viewport")
            if args.analyze_bundle:
                _, analyzed = await call("analyze_web_bundle", {
                    **target, "include_script_sources": True, "fetch_source_maps": False,
                })
                record_coverage(receipt, "analyze_web_bundle", analyzed, args.source_url, target_id)
            receipt["target_url_alignment"] = "confirmed"
            receipt["status"] = "partial" if receipt["limitations"] else "captured"
    receipt["finished_at"] = timestamp()
    return receipt


def failure_receipt(args, artifacts, error, context=None):
    def describe_exception(value):
        if isinstance(value, BaseExceptionGroup):
            return [detail for child in value.exceptions for detail in describe_exception(child)]
        return [{"type": type(value).__name__, "message": str(value)}]
    print(f"Capture failed; inspect saved records in {args.output}.", file=sys.stderr)
    receipt = {
        "status": "failed", "kind": "passive_source_capture", "label": args.label,
        "source_url": args.source_url, "finished_at": timestamp(),
        "errors": describe_exception(error), "artifacts": artifacts,
    }
    for key in ("session_evidence_scope", "rea_launcher", "response_budget_recovery"):
        if context is not None and key in context:
            receipt[key] = context[key]
    return receipt


def finish_receipt(args, receipt):
    (args.output / "receipt.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"{receipt['status']}: {args.output}", flush=True)
    return 0 if receipt["status"] == "captured" else 1


async def capture_with_receipt(args, connection=None) -> int:
    artifacts = []
    context = {}
    try:
        receipt = await capture(args, artifacts, connection, context)
    except (Exception, KeyboardInterrupt) as error:
        receipt = failure_receipt(args, artifacts, error, context)
    return finish_receipt(args, receipt)


def main() -> int:
    if sys.version_info < (3, 11):
        print("This capture kit requires Python 3.11 or newer.", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cdp-endpoint", type=endpoint, default="http://127.0.0.1:9222")
    parser.add_argument("--source-url", type=source_url, default=EXPLEE_URL)
    parser.add_argument("--target-id", help="Exact REA target identity when the URL has duplicates.")
    parser.add_argument("--label", default="project-overview-desktop")
    parser.add_argument("--output", type=Path, required=True, help="New folder for this one capture.")
    parser.add_argument("--observation-seconds", type=float, default=10)
    parser.add_argument("--analyze-bundle", action="store_true")
    parser.add_argument("--rea-package-root", type=Path,
                        help=f"Existing official rea-agents {REA_VERSION} package; bypass npx startup only.")
    args = parser.parse_args()
    args.output = args.output.expanduser().absolute()
    if args.output.exists() or args.output.is_symlink():
        parser.error("Choose a new output directory; existing evidence is never overwritten.")
    if not 0.1 <= args.observation_seconds <= 60:
        parser.error("--observation-seconds must be between 0.1 and 60.")
    try:
        args.rea_launch = rea_launch(args.rea_package_root)
    except ValueError as error:
        parser.error(str(error))
    try:
        import mcp  # noqa: F401
    except ImportError:
        parser.error("Install this kit's requirements.txt in a Python virtual environment first.")
    args.output.mkdir(parents=True, exist_ok=False)
    artifacts = []
    context = {}
    try:
        receipt = asyncio.run(capture(args, artifacts, receipt_context=context))
    except (Exception, KeyboardInterrupt) as error:
        receipt = failure_receipt(args, artifacts, error, context)
    return finish_receipt(args, receipt)


if __name__ == "__main__":
    raise SystemExit(main())
