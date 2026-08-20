"""Protocol-gated conformal proxy and strictly past-only temporal summaries."""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Any, Iterable, Mapping, Sequence

import numpy as np

from .score_contracts import validate_probabilities


def fit_conformal_proxy(probabilities: np.ndarray, y_index: Sequence[int], profile: Mapping[str, Any], *, probability_atol: float) -> dict[str, Any]:
    if not bool(profile.get("enabled")):
        return {"status": "INELIGIBLE", "reason": "PROTOCOL_GATE_DISABLED"}
    p = validate_probabilities(probabilities, atol=probability_atol)
    y = np.asarray(y_index, dtype=int)
    if len(y) != len(p):
        raise ValueError("Conformal labels and probabilities differ in length")
    alpha = float(profile["alpha"])
    min_support = int(profile["min_support"])
    if len(y) < min_support:
        return {"status": "INELIGIBLE", "reason": "INSUFFICIENT_CONFORMAL_SUPPORT", "support": len(y), "minimum": min_support}
    scores = 1.0 - p[np.arange(len(y)), y]
    quantile_level = min(1.0, np.ceil((len(scores) + 1) * (1.0 - alpha)) / len(scores))
    quantile = float(np.quantile(scores, quantile_level, method=str(profile["quantile_method"])))
    return {"status": "ELIGIBLE", "alpha": alpha, "quantile": quantile, "quantile_level": quantile_level, "support": len(y), "score_definition": "1-p_true"}


def apply_conformal_proxy(probabilities: np.ndarray, state: Mapping[str, Any], *, probability_atol: float) -> dict[str, Any]:
    if state.get("status") != "ELIGIBLE":
        return {"status": "INELIGIBLE", "reason": state.get("reason", "UNKNOWN")}
    p = validate_probabilities(probabilities, atol=probability_atol)
    inclusion = (1.0 - p) <= float(state["quantile"])
    set_size = inclusion.sum(axis=1)
    return {"status": "ELIGIBLE", "set_size": set_size, "singleton": set_size == 1, "empty": set_size == 0}


def summarize_past(
    rows: Iterable[Mapping[str, Any]],
    profile: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Return features computed only from earlier rows in each reset group."""
    if not bool(profile.get("enabled")):
        return []
    order_field = str(profile["order_field"])
    reset_fields = list(profile["reset_fields"])
    value_field = str(profile["value_field"])
    history_length = int(profile["history_length"])
    if history_length < 1:
        raise ValueError("history_length must be positive")
    materialized = list(rows)
    sorted_rows = sorted(materialized, key=lambda row: tuple(row.get(f) for f in reset_fields) + (row[order_field],))
    if materialized != sorted_rows:
        raise ValueError("Temporal rows must already be in governed causal order")
    history: dict[tuple[Any, ...], deque[float]] = defaultdict(lambda: deque(maxlen=history_length))
    result: list[dict[str, Any]] = []
    last_order: dict[tuple[Any, ...], Any] = {}
    for row in materialized:
        key = tuple(row.get(field) for field in reset_fields)
        order = row[order_field]
        if key in last_order and order <= last_order[key]:
            raise ValueError("Temporal order is not strictly increasing within reset key")
        prior = list(history[key])
        result.append({"row_id": row.get("record_id"), "past_count": len(prior), "past_mean": float(np.mean(prior)) if prior else None, "causal_cutoff": order, "reset_key": list(key)})
        history[key].append(float(row[value_field]))
        last_order[key] = order
    return result

