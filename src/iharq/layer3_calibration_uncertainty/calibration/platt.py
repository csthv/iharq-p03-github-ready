"""Binary Platt/sigmoid calibration with explicit L2 regularization."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

import numpy as np
from scipy.optimize import minimize

from ..errors import IneligibleMethod
from ..score_contracts import ScoreView, score_to_probabilities, validate_logits
from .base import FittedCalibrator, require_support


def _binary_score(view: ScoreView, probability_atol: float, epsilon: float) -> np.ndarray:
    if len(view.class_order) != 2:
        raise IneligibleMethod("Platt calibration is binary-only")
    if view.score_type == "logit":
        z = validate_logits(view.values)
        return z[:, 1] - z[:, 0]
    p = score_to_probabilities(view, probability_atol=probability_atol)[:, 1]
    p = np.clip(p, epsilon, 1.0 - epsilon)
    return np.log(p) - np.log1p(-p)


def _sigmoid(x: np.ndarray) -> np.ndarray:
    positive = x >= 0
    out = np.empty_like(x, dtype=np.float64)
    out[positive] = 1.0 / (1.0 + np.exp(-x[positive]))
    exp = np.exp(x[~positive])
    out[~positive] = exp / (1.0 + exp)
    return out


@dataclass
class PlattCalibrator(FittedCalibrator):
    def fit(
        self,
        source: ScoreView,
        y_index: np.ndarray,
        profile: Mapping[str, Any],
        rng: np.random.Generator,
        *,
        probability_atol: float,
    ) -> "PlattCalibrator":
        del rng
        support = require_support(y_index, profile)
        epsilon = float(profile["nll_epsilon"])
        x = _binary_score(source, probability_atol, epsilon)
        y = (y_index == 1).astype(np.float64)
        l2 = float(profile["l2_penalty"])

        def objective(theta: np.ndarray) -> tuple[float, np.ndarray]:
            a, b = theta
            q = _sigmoid(a * x + b)
            q_clip = np.clip(q, epsilon, 1.0 - epsilon)
            loss = -np.mean(y * np.log(q_clip) + (1.0 - y) * np.log1p(-q_clip)) + 0.5 * l2 * a * a
            residual = q - y
            grad = np.array([np.mean(residual * x) + l2 * a, np.mean(residual)])
            return float(loss), grad

        result = minimize(lambda t: objective(t), np.array([1.0, 0.0]), method="L-BFGS-B", jac=True, options={"ftol": float(profile["optimizer_tolerance"]), "maxiter": int(profile["max_iterations"])})
        if not result.success or not np.all(np.isfinite(result.x)):
            raise RuntimeError(f"Platt optimization failed: {result.message}")
        self.parameters = {"slope": float(result.x[0]), "intercept": float(result.x[1]), "support": support}
        self.optimizer_result = {"optimizer": "scipy.L-BFGS-B", "success": bool(result.success), "fun": float(result.fun), "nit": int(result.nit), "message": str(result.message)}
        self.convergence_status = "CONVERGED"
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        x = _binary_score(view, probability_atol, 1e-15)
        q = _sigmoid(float(self.parameters["slope"]) * x + float(self.parameters["intercept"]))
        return np.column_stack([1.0 - q, q])

