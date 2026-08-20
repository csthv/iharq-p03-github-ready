"""Mandatory identity/raw comparator for A1."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

import numpy as np

from ..score_contracts import ScoreView, score_to_probabilities
from .base import FittedCalibrator


@dataclass
class IdentityCalibrator(FittedCalibrator):
    def fit(
        self,
        source: ScoreView,
        y_index: np.ndarray,
        profile: Mapping[str, Any],
        rng: np.random.Generator,
        *,
        probability_atol: float,
    ) -> "IdentityCalibrator":
        del y_index, profile, rng
        score_to_probabilities(source, probability_atol=probability_atol)
        self.parameters = {"transformation": "identity"}
        self.optimizer_result = {"optimizer": "none", "success": True}
        self.convergence_status = "NOT_APPLICABLE"
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        return score_to_probabilities(view, probability_atol=probability_atol).copy()

