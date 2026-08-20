"""Scalar temperature scaling for genuine logits or authorized log probabilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

import numpy as np
from scipy.optimize import minimize_scalar

from ..errors import IneligibleMethod
from ..score_contracts import ScoreView, validate_logits
from .base import FittedCalibrator, clipped_nll, require_support, stable_softmax


def _legal_logits(view: ScoreView, probability_atol: float) -> np.ndarray:
    if view.score_type == "logit":
        return validate_logits(view.values)
    if view.score_type == "log_probability" and view.legal_log_probability_transform:
        return validate_logits(view.values)
    if view.score_type == "probability" and view.legal_log_probability_transform:
        p = np.asarray(view.values, dtype=np.float64)
        if np.any(p <= probability_atol):
            raise IneligibleMethod("Authorized log-probability conversion requires strictly positive probabilities")
        return np.log(p)
    raise IneligibleMethod("Temperature scaling requires genuine logits or Protocol-authorized legal log probabilities")


@dataclass
class TemperatureCalibrator(FittedCalibrator):
    def fit(
        self,
        source: ScoreView,
        y_index: np.ndarray,
        profile: Mapping[str, Any],
        rng: np.random.Generator,
        *,
        probability_atol: float,
    ) -> "TemperatureCalibrator":
        del rng
        support = require_support(y_index, profile)
        logits = _legal_logits(source, probability_atol)
        bounds = tuple(float(v) for v in profile["log_temperature_bounds"])
        epsilon = float(profile["nll_epsilon"])

        def objective(log_temperature: float) -> float:
            temperature = float(np.exp(log_temperature))
            return clipped_nll(stable_softmax(logits / temperature), y_index, epsilon)

        result = minimize_scalar(objective, bounds=bounds, method="bounded", options={"xatol": float(profile["optimizer_tolerance"])})
        if not result.success or not np.isfinite(result.fun):
            raise RuntimeError(f"Temperature optimization failed: {result.message}")
        temperature = float(np.exp(result.x))
        if not temperature > 0:
            raise RuntimeError("Temperature must be positive")
        self.parameters = {"temperature": temperature, "log_temperature": float(result.x), "support": support}
        self.optimizer_result = {"optimizer": "scipy.minimize_scalar.bounded", "success": bool(result.success), "fun": float(result.fun), "nfev": int(result.nfev), "message": str(result.message)}
        self.convergence_status = "CONVERGED"
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        logits = _legal_logits(view, probability_atol)
        return stable_softmax(logits / float(self.parameters["temperature"]))

