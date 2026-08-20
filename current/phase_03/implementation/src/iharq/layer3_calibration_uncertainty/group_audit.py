"""Declared group/participant/session/model/branch/budget audit with sparse support."""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Mapping, Sequence

import numpy as np

from .metrics import multiclass_brier, negative_log_likelihood


def audit_groups(
    probabilities: np.ndarray,
    y_index: Sequence[int],
    metadata: Sequence[Mapping[str, Any]],
    group_profile: Mapping[str, Any],
    metric_profile: Mapping[str, Any],
    *,
    probability_atol: float,
) -> dict[str, Any]:
    y = np.asarray(y_index, dtype=int)
    if len(probabilities) != len(y) or len(metadata) != len(y):
        raise ValueError("Group audit inputs differ in length")
    fields = list(group_profile["group_fields"])
    minimum = int(group_profile["minimum_support"])
    rows: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    for field in fields:
        groups: dict[str, list[int]] = defaultdict(list)
        for index, item in enumerate(metadata):
            groups[str(item.get(field, "__MISSING__"))].append(index)
        for group_id, indices in sorted(groups.items()):
            idx = np.asarray(indices, dtype=int)
            support = len(idx)
            sparse = support < minimum
            row = {"group_field": field, "group_id": group_id, "support_count": support, "sparse_support": sparse}
            if sparse:
                row.update({"brier": None, "nll": None, "status": "DIAGNOSTIC_ONLY"})
                warnings.append({"group_field": field, "group_id": group_id, "support_count": support, "minimum_support": minimum, "reason": "SPARSE_GROUP_SUPPORT"})
            else:
                row.update({
                    "brier": multiclass_brier(probabilities[idx], y[idx], probability_atol=probability_atol),
                    "nll": negative_log_likelihood(probabilities[idx], y[idx], epsilon=float(metric_profile["nll_epsilon"]), probability_atol=probability_atol),
                    "status": "ELIGIBLE",
                })
            rows.append(row)
    return {"rows": rows, "sparse_support_warnings": warnings, "group_fields": fields}

