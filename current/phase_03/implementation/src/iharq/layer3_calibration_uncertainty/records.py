"""Record construction and field-contract enforcement for P03 families."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any, Mapping

import yaml

from .identity import deterministic_id, sha256_json
from .models import ExecutionContext, TerminalStatus


def load_field_contract(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)
    if not isinstance(payload, dict) or "record_families" not in payload:
        raise ValueError("Invalid P03 record field contract")
    return payload


def required_fields(contract: Mapping[str, Any], family: str) -> list[str]:
    try:
        return list(contract["record_families"][family]["required_fields"])
    except KeyError as exc:
        raise KeyError(f"Unknown record family: {family}") from exc


def validate_record_fields(record: Mapping[str, Any], family: str, contract: Mapping[str, Any]) -> None:
    missing = [name for name in required_fields(contract, family) if name not in record]
    if missing:
        raise ValueError(f"{family} missing fields: {', '.join(missing)}")
    if record.get("phase_id") != "P03" or record.get("layer_id") != "L3":
        raise ValueError(f"{family} has invalid phase/layer identity")
    payload = dict(record)
    observed = payload.pop("payload_sha256", None)
    expected = sha256_json(payload)
    if observed != expected:
        raise ValueError(f"{family} payload_sha256 mismatch")


def make_record(
    family: str,
    context: ExecutionContext,
    producer_module: str,
    family_payload: Mapping[str, Any],
    contract: Mapping[str, Any],
    *,
    source_artifact_ids: list[str] | None = None,
    source_sha256s: list[str] | None = None,
    lineage_parent_ids: list[str] | None = None,
    lifecycle_status: str = "ACTIVE",
    terminal_status: str = TerminalStatus.SUCCESS,
    supersedes: list[str] | None = None,
    invalidated_by: list[str] | None = None,
    limitations: list[str] | None = None,
    failure_code: str | None = None,
) -> dict[str, Any]:
    base = {
        "schema_id": f"{family}.v1",
        "schema_version": "1.0.0",
        "record_id": "",
        "phase_id": "P03",
        "layer_id": "L3",
        "run_id": context.run_id,
        "config_sha256": context.config_sha256,
        "protocol_snapshot_id": context.protocol_snapshot_id,
        "created_at_utc": context.created_at_utc,
        "producer_module": producer_module,
        "source_artifact_ids": source_artifact_ids or [],
        "source_sha256s": source_sha256s or [],
        "lineage_parent_ids": lineage_parent_ids or [],
        "lifecycle_status": lifecycle_status,
        "terminal_status": str(terminal_status),
        "supersedes": supersedes or [],
        "invalidated_by": invalidated_by or [],
        "limitations": limitations or [],
        "failure_code": failure_code,
    }
    base.update(deepcopy(dict(family_payload)))
    missing = [name for name in required_fields(contract, family) if name not in base and name not in {"record_id", "payload_sha256"}]
    if missing:
        raise ValueError(f"Cannot build {family}; family payload missing: {', '.join(missing)}")
    id_payload = {k: v for k, v in base.items() if k not in {"record_id", "payload_sha256", "created_at_utc"}}
    base["record_id"] = deterministic_id(f"P03-{family}", id_payload)
    base["payload_sha256"] = sha256_json(base)
    validate_record_fields(base, family, contract)
    return base

