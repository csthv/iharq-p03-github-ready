"""Threshold candidate construction and lifecycle invariants."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping

from .identity import deterministic_id, sha256_json


def register_threshold(candidate: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "threshold_version", "ablation_id", "feature_id", "probability_source_id",
        "selection_dataset_id", "selection_budget_id", "selection_split_id", "selection_role",
        "target_profile_id", "operator", "threshold_value", "tie_policy", "applicability",
        "permissions", "effective_from",
    }
    missing = sorted(required - set(candidate))
    if missing:
        raise ValueError("Threshold candidate missing: " + ", ".join(missing))
    if candidate["operator"] not in {">=", "<="} or candidate["tie_policy"] not in {"ACCEPT_EQUAL", "REJECT_EQUAL"}:
        raise ValueError("Invalid threshold operator/tie policy")
    payload = deepcopy(dict(candidate))
    payload.setdefault("effective_until", None)
    payload.setdefault("supersession_reason", None)
    payload["rule_sha256"] = sha256_json({k: payload[k] for k in ("feature_id", "operator", "threshold_value", "tie_policy", "applicability")})
    payload["threshold_id"] = deterministic_id("P03-THRESHOLD", payload)
    payload["lifecycle_status"] = "ACTIVE"
    return payload


def supersede_threshold(old: Mapping[str, Any], successor_id: str, reason: str, effective_until: str) -> dict[str, Any]:
    if not reason.strip():
        raise ValueError("Supersession reason is mandatory")
    event = {"event": "SUPERSEDE", "threshold_id": old["threshold_id"], "successor_id": successor_id, "reason": reason, "effective_until": effective_until}
    event["event_id"] = deterministic_id("P03-THRESHOLD-EVENT", event)
    return event


def resolve_threshold(records: list[Mapping[str, Any]], query: Mapping[str, Any], consumer: str) -> dict[str, Any]:
    active = []
    for record in records:
        if record.get("lifecycle_status") != "ACTIVE":
            continue
        if consumer not in record.get("permissions", {}).get("consumers", []):
            continue
        if all(record.get(key) == value for key, value in query.items()):
            active.append(dict(record))
    if len(active) != 1:
        raise ValueError(f"Expected exactly one active threshold, found {len(active)}")
    return active[0]

