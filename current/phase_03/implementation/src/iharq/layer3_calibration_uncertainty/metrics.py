"""Governed reliability, discrimination, and selective-risk metric primitives."""

from __future__ import annotations

from typing import Any, Callable, Mapping, Sequence

import numpy as np

from .score_contracts import validate_probabilities


def validate_targets(y_index: Sequence[int], n: int, k: int) -> np.ndarray:
    y = np.asarray(y_index, dtype=np.int64)
    if y.shape != (n,) or np.any(y < 0) or np.any(y >= k):
        raise ValueError(f"Targets must be shape ({n},) with values in [0,{k})")
    return y


def multiclass_brier(probabilities: np.ndarray, y_index: Sequence[int], *, probability_atol: float) -> float:
    p = validate_probabilities(probabilities, atol=probability_atol)
    y = validate_targets(y_index, len(p), p.shape[1])
    one_hot = np.eye(p.shape[1], dtype=np.float64)[y]
    return float(np.mean(np.sum((p - one_hot) ** 2, axis=1)))


def negative_log_likelihood(probabilities: np.ndarray, y_index: Sequence[int], *, epsilon: float, probability_atol: float) -> float:
    p = validate_probabilities(probabilities, atol=probability_atol)
    y = validate_targets(y_index, len(p), p.shape[1])
    if not 0 < epsilon < 0.5:
        raise ValueError("epsilon must lie in (0,0.5)")
    return float(-np.mean(np.log(np.clip(p[np.arange(len(p)), y], epsilon, 1.0))))


def error_vector(probabilities: np.ndarray, y_index: Sequence[int], *, probability_atol: float) -> np.ndarray:
    p = validate_probabilities(probabilities, atol=probability_atol)
    y = validate_targets(y_index, len(p), p.shape[1])
    return (p.argmax(axis=1) != y).astype(np.float64)


def _bin_edges(confidence: np.ndarray, profile: Mapping[str, Any]) -> np.ndarray:
    count = int(profile["bin_count"])
    if count < 2:
        raise ValueError("bin_count must be >=2")
    mode = str(profile["mode"])
    if mode == "equal_width":
        return np.linspace(0.0, 1.0, count + 1)
    if mode == "equal_mass":
        edges = np.quantile(confidence, np.linspace(0.0, 1.0, count + 1), method=str(profile["quantile_method"]))
        edges[0], edges[-1] = 0.0, 1.0
        return np.maximum.accumulate(edges)
    if mode == "explicit_edges":
        edges = np.asarray(profile["edges"], dtype=float)
        if len(edges) < 3 or edges[0] != 0.0 or edges[-1] != 1.0 or np.any(np.diff(edges) < 0):
            raise ValueError("Explicit bin edges must be sorted and span [0,1]")
        return edges
    raise ValueError(f"Unsupported binning mode={mode}")


def reliability_bins(probabilities: np.ndarray, y_index: Sequence[int], profile: Mapping[str, Any], *, probability_atol: float) -> list[dict[str, Any]]:
    p = validate_probabilities(probabilities, atol=probability_atol)
    y = validate_targets(y_index, len(p), p.shape[1])
    confidence = p.max(axis=1)
    correct = (p.argmax(axis=1) == y).astype(float)
    edges = _bin_edges(confidence, profile)
    rows: list[dict[str, Any]] = []
    for index, (low, high) in enumerate(zip(edges[:-1], edges[1:])):
        if index == len(edges) - 2:
            mask = (confidence >= low) & (confidence <= high)
        else:
            mask = (confidence >= low) & (confidence < high)
        count = int(mask.sum())
        mean_confidence = float(confidence[mask].mean()) if count else None
        accuracy = float(correct[mask].mean()) if count else None
        gap = abs(mean_confidence - accuracy) if count else None
        rows.append({"bin_index": index, "lower": float(low), "upper": float(high), "count": count, "mean_confidence": mean_confidence, "accuracy": accuracy, "absolute_gap": gap})
    if sum(row["count"] for row in rows) != len(p):
        raise AssertionError("Reliability bin partition lost rows")
    return rows


def expected_calibration_error(bin_rows: Sequence[Mapping[str, Any]]) -> float:
    total = sum(int(row["count"]) for row in bin_rows)
    if total == 0:
        raise ValueError("ECE denominator is zero")
    return float(sum(int(row["count"]) * float(row["absolute_gap"] or 0.0) for row in bin_rows) / total)


def accuracy(probabilities: np.ndarray, y_index: Sequence[int], *, probability_atol: float) -> float:
    return float(1.0 - error_vector(probabilities, y_index, probability_atol=probability_atol).mean())


def selective_risk(probabilities: np.ndarray, y_index: Sequence[int], accepted: Sequence[bool], *, probability_atol: float) -> dict[str, float | int | None]:
    errors = error_vector(probabilities, y_index, probability_atol=probability_atol)
    mask = np.asarray(accepted, dtype=bool)
    if mask.shape != errors.shape:
        raise ValueError("Acceptance mask has wrong shape")
    accepted_count = int(mask.sum())
    risk = float(errors[mask].mean()) if accepted_count else None
    return {"accepted_count": accepted_count, "rejected_count": int(len(mask) - accepted_count), "coverage": float(mask.mean()), "risk": risk}


def bootstrap_interval(
    statistic: Callable[[np.ndarray], float],
    n: int,
    profile: Mapping[str, Any],
) -> dict[str, float]:
    repeats = int(profile["repeats"])
    seed = int(profile["seed"])
    confidence_level = float(profile["confidence_level"])
    if repeats < 2 or not 0 < confidence_level < 1:
        raise ValueError("Invalid bootstrap profile")
    rng = np.random.default_rng(seed)
    values = np.array([statistic(rng.integers(0, n, size=n)) for _ in range(repeats)], dtype=float)
    alpha = (1.0 - confidence_level) / 2.0
    return {"lower": float(np.quantile(values, alpha)), "upper": float(np.quantile(values, 1.0 - alpha)), "confidence_level": confidence_level, "repeats": repeats}

