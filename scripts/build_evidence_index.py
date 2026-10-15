#!/usr/bin/env python3
"""Validate source/capture artifact hashes and build a bounded evidence index."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def verify_file(base: Path, relative: str, expected: str, size: int | None = None):
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError(f"Artifact path leaves its declared evidence folder: {relative}")
    content = path.read_bytes()
    if hashlib.sha256(content).hexdigest() != expected:
        raise ValueError(f"Artifact checksum differs: {relative}")
    if size is not None and len(content) != size:
        raise ValueError(f"Artifact byte count differs: {relative}")


def main():
    registry = read_json(ROOT / "evidence/public/sources.json")
    source_ids = {source["source_id"] for source in registry["sources"]}
    response_ids = {response["response_id"] for response in registry["raw_responses"]}
    for source in registry["sources"]:
        verify_file(ROOT, source["excerpt_path"], source["excerpt_sha256"])
        if any(view["response_id"] not in response_ids for view in source["views"]):
            raise ValueError(f"Unknown retrieval record for {source['source_id']}")
    for response in registry["raw_responses"]:
        verify_file(ROOT, response["path"], response["sha256"])
    operations = read_json(ROOT / "evidence/public/documented-operations.json")["operations"]
    api_text = (ROOT / "evidence/public/source-004.txt").read_text(encoding="utf-8")
    for operation in operations:
        if operation["source_id"] not in source_ids:
            raise ValueError("Documented operation has an unknown source ID.")
        if operation["path"] not in api_text:
            raise ValueError(f"Operation path is absent from the retrieved API views: {operation['path']}")
        if any(value not in response_ids for value in operation["response_ids"]):
            raise ValueError("Documented operation has an unknown retrieval record.")

    captures = []
    for receipt_path in sorted((ROOT / "evidence/captures").glob("*/receipt.json")):
        receipt = read_json(receipt_path)
        for artifact in receipt["artifacts"]:
            verify_file(receipt_path.parent, artifact["path"], artifact["sha256"], artifact["bytes"])
        captures.append({
            "receipt": str(receipt_path.relative_to(ROOT)), "status": receipt["status"],
            "source_url": receipt["source_url"], "label": receipt["label"],
            "acceptance": "pending screenshot, state, and evidence review",
        })
    documents = []
    for path in [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]:
        documents.append({"path": str(path.relative_to(ROOT)),
                          "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    index = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "partial_source_coverage",
        "source_target": "https://explee.com/app-auto-gtm/p/40610",
        "public_source_count": len(registry["sources"]),
        "retrieval_record_count": len(registry["raw_responses"]),
        "documented_public_operation_count": len(operations),
        "public_operations_executed": 0,
        "accepted_authenticated_capture_count": 0,
        "sources": registry["sources"],
        "diagnostics": [entry for entry in registry["raw_responses"] if entry["is_error"]],
        "source_capture_receipts": captures,
        "documents": documents,
        "gaps": [
            "Signed-in Explee screens and interactions have not been captured in this workspace.",
            "Full OpenAPI JSON, private requests, frontend bundles and style/assets remain unverified.",
            "Synthetic REA verification is tooling evidence, not Explee behavior evidence.",
        ],
    }
    destination = ROOT / "evidence/index.json"
    destination.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Verified {len(registry['sources'])} source views, {len(registry['raw_responses'])} retrieval records, "
          f"{len(operations)} documented paths, and {len(captures)} capture receipts.")
    print(destination)


if __name__ == "__main__":
    main()
