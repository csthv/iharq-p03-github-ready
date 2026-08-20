"""Mandatory multiclass uncertainty features and eligible member disagreement."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

import numpy as np

from .score_contracts import validate_probabilities


def confidence(probabilities: np.ndarray, *, probability_atol: float) -> np.ndarray:
    return validate_probabilities(probabilities, atol=probability_atol).max(axis=1)


def normalized_entropy(probabilities: np.ndarray, *, epsilon: float, probability_atol: float) -> np.ndarray:
    p = validate_probabilities(probabilities, atol=probability_atol)
    if p.shape[1] < 2:
        raise ValueError("Entropy normalization requires at least two classes")
    safe = np.clip(p, epsilon, 1.0)
    return -np.sum(p * np.log(safe), axis=1) / np.log(p.shape[1])


def top1_top2_margin(probabilities: np.ndarray, *, probability_atol: float) -> np.ndarray:
    p = validate_probabilities(probabilities, atol=probability_atol)
    partitioned = np.partition(p, kth=p.shape[1] - 2, axis=1)
    return partitioned[:, -1] - partitioned[:, -2]


def aligned_member_disagreement(member_probabilities: Sequence[np.ndarray], *, probability_atol: float) -> np.ndarray:
    if len(member_probabilities) < 2:
        raise ValueError("Disagreement requires at least two aligned A4 members")
    stack = np.stack([validate_probabilities(p, atol=probability_atol) for p in member_probabilities], axis=0)
    if len({p.shape for p in member_probabilities}) != 1:
        raise ValueError("A4 member probability arrays are not aligned")
    return np.mean(np.var(stack, axis=0), axis=1)


def extract_uncertainty(
    probabilities: np.ndarray,
    feature_profile: Mapping[str, Any],
    *,
    probability_atol: float,
    member_probabilities: Sequence[np.ndarray] | None = None,
) -> dict[str, Any]:
    epsilon = float(feature_profile["entropy_epsilon"])
    features: dict[str, dict[str, Any]] = {
        "confidence": {"values": confidence(probabilities, probability_atol=probability_atol), "family": "confidence", "direction": "higher_is_more_confident", "decision_time_eligible": True, "alias_of_feature_id": None},
        "normalized_entropy": {"values": normalized_entropy(probabilities, epsilon=epsilon, probability_atol=probability_atol), "family": "entropy", "direction": "lower_is_more_confident", "decision_time_eligible": True, "alias_of_feature_id": None},
        "top1_top2_margin": {"values": top1_top2_margin(probabilities, probability_atol=probability_atol), "family": "margin", "direction": "higher_is_more_confident", "decision_time_eligible": True, "alias_of_feature_id": None},
    }
    conditional = []
    if bool(feature_profile.get("disagreement_enabled")):
        if member_probabilities is None:
            conditional.append({"feature_id": "member_disagreement", "status": "INELIGIBLE", "reason": "ALIGNED_A4_MEMBERS_UNAVAILABLE"})
        else:
            features["member_disagreement"] = {"values": aligned_member_disagreement(member_probabilities, probability_atol=probability_atol), "family": "disagreement", "direction": "lower_is_more_confident", "decision_time_eligible": True, "alias_of_feature_id": None}
    return {"features": features, "conditional_attempts": conditional}


def project_decision_time(feature: Mapping[str, Any]) -> np.ndarray:
    if not bool(feature.get("decision_time_eligible")):
        raise ValueError("Feature is not legal at decision time")
    return np.asarray(feature["values"], dtype=float)

