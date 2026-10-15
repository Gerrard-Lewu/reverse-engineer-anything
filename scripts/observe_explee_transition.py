#!/usr/bin/env python3
"""Observe one operator-driven, read-only Explee navigation through real REA.

The operator uses the existing browser controls during the printed observation
window. This helper does not click, navigate, or change account settings.
"""
import argparse
import asyncio
import os
import shutil
import sys
from pathlib import Path
from importlib.metadata import version

from capture_explee import (REA_VERSION, endpoint, source_url, origin, timestamp,
    evidence_of, result_of, write_json, record_coverage, describe_exception)


async def observe(args, artifacts):
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    receipt = {"kind": "operator_driven_read_transition", "status": "in_progress",
        "started_at": timestamp(), "label": args.label, "initial_url": args.initial_url,
        "final_url": args.final_url, "target_id": args.target_id,
        "rea_version": REA_VERSION, "mcp_version": version("mcp"),
        "observation_seconds": args.observation_seconds, "artifacts": artifacts,
        "coverage": [], "limitations": ["Cross-call visual/document alignment is not atomic; review browser action timing and saved frames before acceptance."]}
    npm = shutil.which("npx")
    if not npm:
        raise RuntimeError("Use an existing Node/npm installation.")
    command, command_args = npm, ["-y", f"rea-agents@{REA_VERSION}", "mcp"]
    if sys.platform == "win32":
        command, command_args = shutil.which("cmd.exe") or "cmd.exe", ["/d", "/c", npm, *command_args]
    params = StdioServerParameters(command=command, args=command_args, env=dict(os.environ))
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            initialized = await asyncio.wait_for(session.initialize(), 120)
            catalog = await asyncio.wait_for(session.list_tools(), 45)
            needed = {"binary_session", "list_browser_targets", "inspect_web_page", "export_evidence_bundle"}
            selected = {tool.name: tool for tool in catalog.tools if tool.name in needed}
            if set(selected) != needed:
                raise RuntimeError("Required REA tools unavailable.")
            write_json(args.output, "tool-schemas.json", {"server": initialized.serverInfo.model_dump(mode="json"),
                "tools": [selected[name].model_dump(mode="json") for name in sorted(selected)]}, artifacts)

            def retain(name, response):
                record = evidence_of(response)
                write_json(args.output, name + ".json", record, artifacts)
                if record.get("evidence_id"):
                    artifacts[-1]["rea_evidence_id"] = record["evidence_id"]
                return result_of(record)

            async def call(tool, arguments, name=None):
                response = await asyncio.wait_for(session.call_tool(tool, arguments), 120)
                result = retain(name or tool, response)
                if response.isError:
                    raise RuntimeError(f"REA {tool} failed; retained its record.")
                return response, result

            failure = None
            try:
                _, state = await call("binary_session", {"expected_package_version": REA_VERSION})
                if state.get("server_identity", {}).get("package", {}).get("version") != REA_VERSION:
                    raise RuntimeError("REA version differs from the pin.")
                scope = {"cdp_endpoint": args.cdp_endpoint, "allowed_origins": [origin(args.initial_url)]}
                _, discovered = await call("list_browser_targets", scope)
                matches = [t for t in discovered.get("targets", [])
                    if (t.get("target_id") or t.get("id")) == args.target_id and t.get("url") == args.initial_url]
                if len(matches) != 1:
                    raise RuntimeError("Initial source target/URL differs from selected state.")
                target = {**scope, "target_id": args.target_id}
                inspection = asyncio.create_task(session.call_tool("inspect_web_page", {**target,
                    "observation_ms": round(args.observation_seconds * 1000),
                    "include_accessibility_text": True, "include_script_sources": True,
                    "include_json_body_shapes": True}))
                await asyncio.sleep(1)
                receipt["operator_window_notified_at"] = timestamp()
                print(f"OBSERVING {args.observation_seconds:g}s: perform the recorded read-only navigation now.", flush=True)
                response = await asyncio.wait_for(inspection, 120)
                inspected = retain("inspect_web_page", response)
                if response.isError:
                    receipt["limitations"].append("Transition inspection failed; its error is retained. No request-shape acceptance is implied.")
                else:
                    actual = inspected.get("target", {}).get("url")
                    if actual not in {args.initial_url, args.final_url}:
                        raise RuntimeError("Inspection reported an unexpected source route.")
                    record_coverage(receipt, "inspect_web_page", inspected, actual, args.target_id)
                _, final_targets = await call("list_browser_targets", scope, "final-browser-targets")
                final_matches = [t for t in final_targets.get("targets", [])
                    if (t.get("target_id") or t.get("id")) == args.target_id]
                receipt["observed_final_url"] = final_matches[0].get("url") if len(final_matches) == 1 else None
                receipt["limitations"].append("No screenshots are taken by this observer. Capture the final state with capture_explee.py separately; request inclusion does not prove a business transition.")
                receipt["status"] = ("recorded_transition_pending_review"
                    if not response.isError and receipt["observed_final_url"] == args.final_url
                    else "transition_not_confirmed")
            except BaseException as error:
                failure = error
                raise
            finally:
                try:
                    bundle = args.output / "evidence-bundle.json"
                    await call("export_evidence_bundle", {"path": str(bundle)})
                    if not bundle.is_file():
                        raise RuntimeError("Evidence export file unavailable.")
                    import hashlib
                    data = bundle.read_bytes()
                    artifacts.append({"path": bundle.name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
                except Exception as export_error:
                    if failure is None:
                        raise
                    write_json(args.output, "export-error.json", {"error_type": type(export_error).__name__,
                        "error": str(export_error), "limitation": "Session export failed; the original error remains authoritative."}, artifacts)
    receipt["finished_at"] = timestamp()
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cdp-endpoint", type=endpoint, required=True)
    parser.add_argument("--target-id", required=True)
    parser.add_argument("--initial-url", type=source_url, required=True)
    parser.add_argument("--final-url", type=source_url, required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--observation-seconds", type=float, default=30)
    args = parser.parse_args()
    if origin(args.initial_url) != "https://explee.com" or origin(args.final_url) != "https://explee.com":
        parser.error("Both routes must be on the selected Explee origin.")
    if not 1 <= args.observation_seconds <= 60:
        parser.error("Observation seconds must be between 1 and 60.")
    args.output = args.output.expanduser().absolute()
    if args.output.exists() or args.output.is_symlink():
        parser.error("Choose a new output directory; existing evidence is preserved.")
    args.output.mkdir(parents=True, exist_ok=False)
    artifacts = []
    try:
        receipt = asyncio.run(observe(args, artifacts))
    except (Exception, KeyboardInterrupt) as error:
        receipt = {"kind": "operator_driven_read_transition", "status": "failed", "label": args.label,
            "finished_at": timestamp(), "errors": describe_exception(error), "artifacts": artifacts}
    write_json(args.output, "receipt.json", receipt, [])
    print(f"{receipt['status']}: {args.output}", flush=True)
    return 0 if receipt["status"] == "recorded_transition_pending_review" else 1


if __name__ == "__main__":
    raise SystemExit(main())
