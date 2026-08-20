"""Consumer-specific handoff construction and full fresh-session validation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable, Mapping

from .identity import deterministic_id, sha256_file, sha256_json


def build_handoff(artifacts: Iterable[Mapping[str, Any]], consumer_profile: Mapping[str, Any]) -> dict[str, Any]:
    artifacts = [dict(item) for item in artifacts]
    required_fields = set(consumer_profile["required_artifact_fields"])
    invalid = []
    for index, artifact in enumerate(artifacts):
        missing = sorted(required_fields - set(artifact))
        if missing:
            invalid.append({"index": index, "missing": missing})
    if invalid:
        raise ValueError(f"Handoff artifact descriptors incomplete: {invalid[:5]}")
    payload = {
        "consumer_id": consumer_profile["consumer_id"],
        "schema_id": consumer_profile["schema_id"],
        "schema_version": consumer_profile["schema_version"],
        "allowed_use": list(consumer_profile["allowed_use"]),
        "prohibited_use": list(consumer_profile["prohibited_use"]),
        "artifacts": artifacts,
        "artifact_count": len(artifacts),
        "limitations": list(consumer_profile.get("limitations", [])),
    }
    payload["handoff_id"] = deterministic_id("P03-HANDOFF", payload)
    payload["payload_sha256"] = sha256_json(payload)
    return payload


def validate_fresh_session_read(path: str | Path, consumer_profile: Mapping[str, Any]) -> dict[str, Any]:
    path = Path(path)
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    expected = consumer_profile["schema_id"]
    if payload.get("schema_id") != expected:
        raise ValueError(f"Consumer expected {expected}, received {payload.get('schema_id')}")
    if int(payload.get("artifact_count", -1)) != len(payload.get("artifacts", [])):
        raise ValueError("Handoff artifact_count mismatch")
    return {"status": "PASS", "path": path.as_posix(), "sha256": sha256_file(path), "consumer_id": consumer_profile["consumer_id"]}
