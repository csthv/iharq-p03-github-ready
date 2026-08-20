"""Probability, logit, log-probability, hard-label, and class-order safety."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from .errors import ContractViolation, IneligibleMethod


@dataclass(frozen=True)
class ScoreView:
    values: np.ndarray
    score_type: str
    class_order: tuple[str, ...]
    source_id: str
    legal_log_probability_transform: bool = False


def validate_class_order(observed: Sequence[str], expected: Sequence[str]) -> tuple[str, ...]:
    observed_tuple = tuple(str(x) for x in observed)
    expected_tuple = tuple(str(x) for x in expected)
    if observed_tuple != expected_tuple:
        raise ContractViolation(f"Class order mismatch: observed={observed_tuple}, expected={expected_tuple}")
    if len(set(observed_tuple)) != len(observed_tuple) or len(observed_tuple) < 2:
        raise ContractViolation("Class order must contain at least two unique labels")
    return observed_tuple


def validate_probabilities(values: np.ndarray, *, atol: float) -> np.ndarray:
    p = np.asarray(values, dtype=np.float64)
    if p.ndim != 2 or p.shape[1] < 2:
        raise ContractViolation(f"Expected [n,k>=2] probability matrix, got {p.shape}")
    if not np.all(np.isfinite(p)):
        raise ContractViolation("Probability matrix contains non-finite values")
    if np.any(p < -atol) or np.any(p > 1.0 + atol):
        raise ContractViolation("Probability values lie outside [0,1]")
    row_sums = p.sum(axis=1)
    if not np.allclose(row_sums, 1.0, atol=atol, rtol=0.0):
        raise ContractViolation("Probability rows do not sum to one; normalization is never implicit")
    return p


def validate_logits(values: np.ndarray) -> np.ndarray:
    z = np.asarray(values, dtype=np.float64)
    if z.ndim != 2 or z.shape[1] < 2 or not np.all(np.isfinite(z)):
        raise ContractViolation("Logits must be a finite [n,k>=2] matrix")
    return z


def softmax(logits: np.ndarray) -> np.ndarray:
    z = validate_logits(logits)
    shifted = z - z.max(axis=1, keepdims=True)
    exp = np.exp(shifted)
    return exp / exp.sum(axis=1, keepdims=True)


def score_to_probabilities(view: ScoreView, *, probability_atol: float) -> np.ndarray:
    if view.values.shape[1] != len(view.class_order):
        raise ContractViolation("Score width does not match class_order")
    if view.score_type == "probability":
        return validate_probabilities(view.values, atol=probability_atol)
    if view.score_type == "log_probability":
        if not view.legal_log_probability_transform:
            raise IneligibleMethod("Log-probability transform was not authorized in the frozen Protocol")
        p = np.exp(np.asarray(view.values, dtype=np.float64))
        return validate_probabilities(p, atol=probability_atol)
    if view.score_type == "logit":
        return softmax(view.values)
    if view.score_type == "hard_label":
        raise IneligibleMethod("Hard-label-only sources are diagnostic-only and calibration-ineligible")
    raise ContractViolation(f"Unknown score_type={view.score_type!r}")


def eligibility(view: ScoreView, *, expected_class_order: Sequence[str], probability_atol: float) -> dict[str, object]:
    reasons: list[str] = []
    try:
        validate_class_order(view.class_order, expected_class_order)
        score_to_probabilities(view, probability_atol=probability_atol)
    except (ContractViolation, IneligibleMethod) as exc:
        reasons.append(type(exc).__name__ + ":" + str(exc))
    hard = view.score_type == "hard_label"
    eligible = not reasons and not hard
    return {
        "score_type": view.score_type,
        "score_shape": list(np.asarray(view.values).shape),
        "class_order": list(view.class_order),
        "probability_available": view.score_type in {"probability", "log_probability", "logit"},
        "logit_available": view.score_type == "logit",
        "hard_label_only": hard,
        "calibration_eligible": eligible,
        "A2_eligible": eligible,
        "A3_eligible": eligible,
        "reason_codes": reasons,
    }

