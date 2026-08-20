"""High-confidence wrong-case mining on evaluation-only labels."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

import numpy as np

from .score_contracts import validate_probabilities


def mine_high_confidence_errors(
    probabilities: np.ndarray,
    y_index: Sequence[int],
    row_metadata: Sequence[Mapping[str, Any]],
    profile: Mapping[str, Any],
    *,
    class_order: Sequence[str],
    probability_atol: float,
) -> list[dict[str, Any]]:
    p = validate_probabilities(probabilities, atol=probability_atol)
    y = np.asarray(y_index, dtype=int)
    if len(y) != len(p) or len(row_metadata) != len(p):
        raise ValueError("HCW inputs differ in length")
    threshold = float(profile["confidence_threshold"])
    predicted = p.argmax(axis=1)
    confidence = p.max(axis=1)
    mask = (predicted != y) & (confidence >= threshold)
    indices = np.flatnonzero(mask)
    indices = indices[np.argsort(-confidence[indices], kind="stable")]
    rows = []
    for rank, index in enumerate(indices, start=1):
        meta = row_metadata[int(index)]
        rows.append({
            "subject_id": meta.get("subject_id"),
            "session_id": meta.get("session_id"),
            "window_id": meta.get("window_id"),
            "confidence": float(confidence[index]),
            "predicted_class": class_order[int(predicted[index])],
            "true_class": class_order[int(y[index])],
            "error_rank": rank,
            "group_ids": list(meta.get("group_ids", [])),
            "decision_time_export_prohibited": True,
            "row_source_id": meta.get("record_id"),
        })
    return rows

