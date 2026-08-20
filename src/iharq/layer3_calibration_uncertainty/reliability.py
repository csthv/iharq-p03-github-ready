"""Reliability audit orchestration with raw comparator and deterioration visibility."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

import numpy as np

from .metrics import expected_calibration_error, multiclass_brier, negative_log_likelihood, reliability_bins


def audit_reliability(
    probabilities: np.ndarray,
    y_index: Sequence[int],
    metric_profile: Mapping[str, Any],
    binning_profile: Mapping[str, Any],
    *,
    probability_atol: float,
    raw_comparator: Mapping[str, float] | None = None,
) -> dict[str, Any]:
    bins = reliability_bins(probabilities, y_index, binning_profile, probability_atol=probability_atol)
    metrics = {
        "brier": multiclass_brier(probabilities, y_index, probability_atol=probability_atol),
        "nll": negative_log_likelihood(probabilities, y_index, epsilon=float(metric_profile["nll_epsilon"]), probability_atol=probability_atol),
        "calibration_error": expected_calibration_error(bins),
    }
    deterioration: dict[str, Any] = {"status": "NOT_APPLICABLE", "deltas": {}}
    if raw_comparator is not None:
        deltas = {name: float(metrics[name] - raw_comparator[name]) for name in metrics}
        tolerance = float(metric_profile["deterioration_tolerance"])
        deterioration = {"status": "DETERIORATED" if any(delta > tolerance for delta in deltas.values()) else "NOT_DETERIORATED", "deltas": deltas, "tolerance": tolerance}
    return {"support_count": len(probabilities), "metrics": metrics, "bins": bins, "direction": {"brier": "lower", "nll": "lower", "calibration_error": "lower"}, "denominator": "all eligible evaluation rows", "deterioration": deterioration}

