"""Layer 0, Evidence Map, Layer 10, analysis, and protocol-record source builders."""

from __future__ import annotations

from collections import Counter
from typing import Any, Iterable, Mapping

from .identity import deterministic_id, sha256_json

EVIDENCE_REQUIRED_FIELDS = (
    "phase_id", "layer_id", "run_id", "config_sha256", "protocol_cell_id",
    "dataset_id", "participant_id", "model_id", "budget_id", "ablation_id",
    "metric_id", "source_record_id", "artifact_path", "artifact_sha256",
    "parent_record_ids", "limitations",
)


def build_evidence_index(rows: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    materialized = [dict(row) for row in rows]
    failures = []
    for index, row in enumerate(materialized):
        missing = [field for field in EVIDENCE_REQUIRED_FIELDS if field not in row]
        if missing:
            failures.append({"row_index": index, "missing": missing})
    if failures:
        raise ValueError(f"Evidence rows are incomplete: {failures[:5]}")
    return {"index_id": deterministic_id("P03-EVIDENCE-INDEX", materialized), "row_count": len(materialized), "rows": materialized, "sha256": sha256_json(materialized)}


def build_protocol_finalization_input(run_ledger: Mapping[str, Any], context: Mapping[str, Any], products: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    products = list(products)
    terminal_counts = Counter(str(row.get("terminal_status", "UNKNOWN")) for row in products)
    payload = {
        "accepted_run_id": context["run_id"],
        "config_sha256": context["config_sha256"],
        "environment_sha256": context["environment_sha256"],
        "protocol_sha256": context["protocol_sha256"],
        "code_sha256": context["code_sha256"],
        "source_manifest_sha256": context["source_manifest_sha256"],
        "run_ledger_sha256": sha256_json(run_ledger),
        "terminal_counts": dict(sorted(terminal_counts.items())),
        "product_record_count": len(products),
        "resource_deviations": context.get("resource_deviations", []),
        "amendments": context.get("amendments", []),
    }
    payload["record_id"] = deterministic_id("P03-PROTOCOL-FINALIZATION", payload)
    return payload


def layer0_candidate_inputs(evidence_rows: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for row in evidence_rows:
        result.append({
            "source_record_id": row["source_record_id"],
            "scope_identity": {key: row.get(key) for key in ("dataset_id", "participant_id", "model_id", "budget_id", "ablation_id")},
            "candidate_only": True,
            "claim_approved": False,
            "evidence_class": row.get("evidence_class"),
            "limitations": row.get("limitations", []),
            "statistical_support_reference": row.get("statistical_support_reference"),
        })
    return result


def source_table_provenance(rows: Iterable[Mapping[str, Any]], family: str) -> dict[str, Any]:
    rows = list(rows)
    return {"family": family, "row_count": len(rows), "source_record_ids": sorted(str(row.get("record_id")) for row in rows), "rows_sha256": sha256_json(rows)}

