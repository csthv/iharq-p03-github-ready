"""A2 confidence-floor selection/application and A3 feature-specific risk curves."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

import numpy as np

from .identity import sha256_json
from .metrics import error_vector, selective_risk


def acceptance_mask(values: Sequence[float], threshold: float, operator: str, tie_policy: str) -> np.ndarray:
    x = np.asarray(values, dtype=float)
    if not np.all(np.isfinite(x)):
        raise ValueError("Selective feature contains non-finite values")
    if operator == ">=":
        return x >= threshold if tie_policy == "ACCEPT_EQUAL" else x > threshold
    if operator == "<=":
        return x <= threshold if tie_policy == "ACCEPT_EQUAL" else x < threshold
    raise ValueError("operator must be >= or <=")


def complete_thresholds(values: Sequence[float], operator: str) -> np.ndarray:
    unique = np.unique(np.asarray(values, dtype=float))
    if operator == ">=":
        return np.concatenate(([np.nextafter(unique.max(), np.inf)], unique[::-1], [np.nextafter(unique.min(), -np.inf)]))
    if operator == "<=":
        return np.concatenate(([np.nextafter(unique.min(), -np.inf)], unique, [np.nextafter(unique.max(), np.inf)]))
    raise ValueError("operator must be >= or <=")


def _exact_risk_rows(
    feature_values: Sequence[float],
    probabilities: np.ndarray,
    y_index: Sequence[int],
    operator: str,
    tie_policy: str,
    *,
    probability_atol: float,
) -> list[dict[str, Any]]:
    """Compute the complete threshold curve in O(n log n), preserving exact semantics.

    The former implementation rebuilt an n-element Boolean mask and revalidated the
    complete probability matrix for every unique threshold. This implementation
    validates once, uses stable sorted cumulative error counts, and emits the same
    all-unique-values-plus-endpoints curve without reducing its cardinality.
    """
    values = np.asarray(feature_values, dtype=float)
    if values.ndim != 1 or not len(values) or not np.all(np.isfinite(values)):
        raise ValueError("Selective feature must be a non-empty finite vector")
    if tie_policy not in {"ACCEPT_EQUAL", "REJECT_EQUAL"}:
        raise ValueError("tie_policy must be ACCEPT_EQUAL or REJECT_EQUAL")
    errors = error_vector(probabilities, y_index, probability_atol=probability_atol)
    if errors.shape != values.shape:
        raise ValueError("Selective feature and probability rows differ")
    order = np.argsort(values, kind="stable")
    sorted_values = values[order]
    prefix_errors = np.concatenate(([0.0], np.cumsum(errors[order], dtype=np.float64)))
    total_errors = float(prefix_errors[-1])
    total = len(values)
    rows: list[dict[str, Any]] = []
    for threshold in complete_thresholds(values, operator):
        threshold = float(threshold)
        if operator == ">=":
            side = "left" if tie_policy == "ACCEPT_EQUAL" else "right"
            split = int(np.searchsorted(sorted_values, threshold, side=side))
            accepted_count = total - split
            accepted_errors = total_errors - float(prefix_errors[split])
        elif operator == "<=":
            side = "right" if tie_policy == "ACCEPT_EQUAL" else "left"
            split = int(np.searchsorted(sorted_values, threshold, side=side))
            accepted_count = split
            accepted_errors = float(prefix_errors[split])
        else:
            raise ValueError("operator must be >= or <=")
        rows.append(
            {
                "threshold": threshold,
                "accepted_count": accepted_count,
                "rejected_count": total - accepted_count,
                "coverage": float(accepted_count / total),
                "risk": float(accepted_errors / accepted_count) if accepted_count else None,
            }
        )
    return rows


def select_rule(
    feature_values: Sequence[float],
    probabilities: np.ndarray,
    y_index: Sequence[int],
    target_profile: Mapping[str, Any],
    *,
    probability_atol: float,
) -> dict[str, Any]:
    operator = str(target_profile["operator"])
    tie_policy = str(target_profile["tie_policy"])
    rows = _exact_risk_rows(feature_values, probabilities, y_index, operator, tie_policy, probability_atol=probability_atol)
    target_type = str(target_profile["target_type"])
    target_value = float(target_profile["target_value"])
    if target_type == "maximum_risk":
        eligible = [row for row in rows if row["risk"] is not None and float(row["risk"]) <= target_value]
        if not eligible:
            raise ValueError("No non-empty threshold satisfies the maximum-risk target")
        best_coverage = max(float(row["coverage"]) for row in eligible)
        eligible = [row for row in eligible if float(row["coverage"]) == best_coverage]
        chosen = min(eligible, key=lambda row: (float(row["risk"]), float(row["threshold"])))
    elif target_type == "target_coverage":
        distance = min(abs(float(row["coverage"]) - target_value) for row in rows)
        eligible = [row for row in rows if abs(float(row["coverage"]) - target_value) == distance]
        preference = str(target_profile["coverage_tie_preference"])
        if preference == "NOT_EXCEED":
            lawful = [row for row in eligible if float(row["coverage"]) <= target_value]
            eligible = lawful or eligible
        elif preference == "AT_LEAST":
            lawful = [row for row in eligible if float(row["coverage"]) >= target_value]
            eligible = lawful or eligible
        chosen = min(eligible, key=lambda row: (float("inf") if row["risk"] is None else float(row["risk"]), float(row["threshold"])))
    else:
        raise ValueError(f"Unsupported target_type={target_type}")
    rule_payload = {"feature_id": target_profile["feature_id"], "operator": operator, "threshold_value": chosen["threshold"], "tie_policy": tie_policy, "target_profile_id": target_profile["target_profile_id"]}
    return {"rule": rule_payload, "rule_sha256": sha256_json(rule_payload), "selection_metrics": chosen, "candidate_count": len(rows), "candidates": rows}


def apply_rule(feature_values: Sequence[float], probabilities: np.ndarray, y_index: Sequence[int], rule: Mapping[str, Any], *, probability_atol: float) -> dict[str, Any]:
    mask = acceptance_mask(feature_values, float(rule["threshold_value"]), str(rule["operator"]), str(rule["tie_policy"]))
    metrics = selective_risk(probabilities, y_index, mask, probability_atol=probability_atol)
    return {"acceptance_mask": mask, "acceptance_mask_sha256": sha256_json(mask.astype(int).tolist()), **metrics}


def build_risk_coverage(
    feature_values: Sequence[float],
    probabilities: np.ndarray,
    y_index: Sequence[int],
    profile: Mapping[str, Any],
    *,
    probability_atol: float,
) -> list[dict[str, Any]]:
    operator = str(profile["operator"])
    tie_policy = str(profile["tie_policy"])
    return [
        {"point_index": index, **row}
        for index, row in enumerate(_exact_risk_rows(feature_values, probabilities, y_index, operator, tie_policy, probability_atol=probability_atol))
    ]
