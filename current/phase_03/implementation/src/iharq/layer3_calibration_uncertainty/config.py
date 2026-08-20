"""Strict loading and validation of the P03 execution/configuration freeze."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .errors import GateBlocked
from .identity import canonical_json, sha256_file, sha256_json

REQUIRED_PROTOCOL_PATHS = (
    "protocol_id",
    "protocol_version",
    "owner",
    "status",
    "scientific.calibration.branch_cells",
    "scientific.calibration.pooling_policy",
    "scientific.calibration.support_and_fallback",
    "scientific.roles.role_map",
    "scientific.metrics.metric_profile",
    "scientific.reliability.binning_profile",
    "scientific.reliability.interval_profile",
    "scientific.statistics.multiplicity_profile",
    "scientific.uncertainty.conditional_features",
    "scientific.uncertainty.disagreement_profile",
    "scientific.a2.target_profile",
    "scientific.a2.operator",
    "scientific.a2.tie_policy",
    "scientific.a3.threshold_grid",
    "scientific.a3.working_points",
    "scientific.randomness.seeds",
    "scientific.randomness.repeats",
    "scientific.statistics.equivalence_profile",
    "scientific.evidence.evidence_classes",
)

PLACEHOLDER_MARKERS = ("__REQUIRED__", "__POPULATE__", "TBD", "TODO", "CHANGEME")


def load_structured(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix.lower() == ".json":
            payload = json.load(handle)
        else:
            payload = yaml.safe_load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected object at {path}")
    return payload


def get_path(payload: dict[str, Any], dotted: str) -> Any:
    value: Any = payload
    for key in dotted.split("."):
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def _has_placeholder(value: Any) -> bool:
    if value is None or value == "":
        return True
    if isinstance(value, str):
        upper = value.upper()
        return any(marker in upper for marker in PLACEHOLDER_MARKERS)
    if isinstance(value, dict):
        return any(_has_placeholder(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return len(value) == 0 or any(_has_placeholder(v) for v in value)
    return False


def validate_protocol_freeze(payload: dict[str, Any], *, allow_authoring_fixture: bool = False) -> list[str]:
    missing = [path for path in REQUIRED_PROTOCOL_PATHS if _has_placeholder(get_path(payload, path))]
    if allow_authoring_fixture and payload.get("status") == "NON_SCIENTIFIC_AUTHORING_FIXTURE":
        missing = []
    if missing:
        raise GateBlocked(
            "G03-05-FREEZE",
            "PROTOCOL_POPULATION_INCOMPLETE",
            "Missing or placeholder protocol paths: " + ", ".join(missing),
        )
    if payload.get("status") not in {"FROZEN_FOR_EXECUTION", "NON_SCIENTIFIC_AUTHORING_FIXTURE"}:
        raise GateBlocked("G03-05-FREEZE", "PROTOCOL_NOT_FROZEN", "status must be FROZEN_FOR_EXECUTION")
    if payload.get("status") == "NON_SCIENTIFIC_AUTHORING_FIXTURE" and not allow_authoring_fixture:
        raise GateBlocked("G03-05-FREEZE", "FIXTURE_PROHIBITED_IN_OFFICIAL_RUN", "fixture protocol cannot authorize science")
    return list(REQUIRED_PROTOCOL_PATHS)


def freeze_snapshot(path: str | Path, *, allow_authoring_fixture: bool = False) -> dict[str, Any]:
    payload = load_structured(path)
    validate_protocol_freeze(payload, allow_authoring_fixture=allow_authoring_fixture)
    normalized = canonical_json(payload)
    return {
        "protocol_snapshot_id": payload["protocol_id"],
        "protocol_sha256": sha256_json(payload),
        "source_file_sha256": sha256_file(path),
        "normalized_payload": json.loads(normalized),
    }


def validate_config(payload: dict[str, Any]) -> None:
    for key in ("config_id", "phase_id", "layer_id", "paths", "environment", "execution"):
        if key not in payload:
            raise GateBlocked("G03-05-FREEZE", "CONFIG_FIELD_MISSING", key)
    if payload["phase_id"] != "P03" or payload["layer_id"] != "L3":
        raise GateBlocked("G03-05-FREEZE", "CONFIG_SCOPE_MISMATCH", "Expected P03/L3")
    prohibited = canonical_json(payload).lower()
    secret_literal_markers = ("hf_" + "token=", "bearer" + " ", "api_" + "key:")
    if any(key in prohibited for key in secret_literal_markers):
        raise GateBlocked("G03-05-FREEZE", "CONFIG_SECRET_LITERAL", "Use symbolic environment variables only")


def config_snapshot(path: str | Path) -> dict[str, Any]:
    payload = load_structured(path)
    validate_config(payload)
    return {
        "config_id": payload["config_id"],
        "config_sha256": sha256_json(payload),
        "source_file_sha256": sha256_file(path),
        "normalized_payload": payload,
    }
