"""Calibration protocol and shared numerical helpers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from typing import Any, Mapping, Sequence

import numpy as np

from ..errors import ContractViolation
from ..identity import sha256_json
from ..score_contracts import ScoreView, validate_probabilities


def labels_to_indices(labels: Sequence[Any], class_order: Sequence[str]) -> np.ndarray:
    mapping = {str(label): index for index, label in enumerate(class_order)}
    converted = []
    for value in labels:
        if isinstance(value, (int, np.integer)) and 0 <= int(value) < len(class_order):
            converted.append(int(value))
            continue
        try:
            converted.append(mapping[str(value)])
        except KeyError as exc:
            raise ContractViolation(f"Unknown label outside class_order: {exc.args[0]}") from exc
    indices = np.asarray(converted, dtype=np.int64)
    return indices


def stable_softmax(logits: np.ndarray) -> np.ndarray:
    z = np.asarray(logits, dtype=np.float64)
    shifted = z - z.max(axis=1, keepdims=True)
    exp = np.exp(shifted)
    return exp / exp.sum(axis=1, keepdims=True)


def clipped_nll(probabilities: np.ndarray, y_index: np.ndarray, epsilon: float) -> float:
    if not 0 < epsilon < 0.5:
        raise ValueError("epsilon must lie in (0, 0.5)")
    p = np.clip(probabilities[np.arange(len(y_index)), y_index], epsilon, 1.0)
    return float(-np.mean(np.log(p)))


@dataclass
class FittedCalibrator(ABC):
    method_id: str
    method_family: str
    class_order: tuple[str, ...]
    score_type: str
    parameters: dict[str, Any] = field(default_factory=dict)
    optimizer_result: dict[str, Any] = field(default_factory=dict)
    convergence_status: str = "NOT_RUN"
    eligibility_status: str = "ELIGIBLE"
    fallback_reason: str | None = None
    diagnostic_only: bool = False

    @abstractmethod
    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        """Apply fitted calibration without refitting."""

    def serialize(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["calibrator_type"] = type(self).__name__
        payload["state_sha256"] = sha256_json(payload)
        return payload


def require_support(y_index: np.ndarray, profile: Mapping[str, Any]) -> dict[str, Any]:
    n = int(len(y_index))
    class_counts = np.bincount(y_index)
    min_total = int(profile["min_total_support"])
    min_per_class = int(profile["min_per_class_support"])
    if n < min_total:
        raise ContractViolation(f"Support {n} below min_total_support={min_total}")
    if class_counts.size == 0 or int(class_counts.min()) < min_per_class:
        raise ContractViolation(f"Per-class support {class_counts.tolist()} below {min_per_class}")
    return {"total": n, "per_class": class_counts.tolist()}


def fit_calibrator(
    source: ScoreView,
    labels: Sequence[Any],
    method_profile: Mapping[str, Any],
    rng: np.random.Generator,
    *,
    probability_atol: float,
) -> FittedCalibrator:
    from .factory import create_calibrator

    calibrator = create_calibrator(method_profile, source.class_order, source.score_type)
    y_index = labels_to_indices(labels, source.class_order)
    if len(y_index) != len(source.values):
        raise ContractViolation("Score and label row counts differ")
    return calibrator.fit(source, y_index, method_profile, rng, probability_atol=probability_atol)


def apply_calibrator(fitted: FittedCalibrator, apply_view: ScoreView, *, probability_atol: float) -> np.ndarray:
    if tuple(apply_view.class_order) != tuple(fitted.class_order):
        raise ContractViolation("Apply-view class order differs from fitted calibrator")
    output = fitted.apply(apply_view, probability_atol=probability_atol)
    return validate_probabilities(output, atol=probability_atol)


def serialize_calibrator(fitted: FittedCalibrator) -> dict[str, Any]:
    return fitted.serialize()
