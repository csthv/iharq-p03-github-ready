"""Binary beta calibration for genuine probability inputs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

import numpy as np
from scipy.optimize import minimize

from ..errors import IneligibleMethod
from ..score_contracts import ScoreView, validate_probabilities
from .base import FittedCalibrator, require_support
from .platt import _sigmoid


@dataclass
class BetaCalibrator(FittedCalibrator):
    def _features(self, view: ScoreView, probability_atol: float, epsilon: float) -> np.ndarray:
        if len(view.class_order) != 2 or view.score_type != "probability":
            raise IneligibleMethod("Beta calibration requires binary genuine probabilities")
        p = validate_probabilities(view.values, atol=probability_atol)[:, 1]
        p = np.clip(p, epsilon, 1.0 - epsilon)
        return np.column_stack([np.log(p), -np.log1p(-p), np.ones(len(p))])

    def fit(
        self,
        source: ScoreView,
        y_index: np.ndarray,
        profile: Mapping[str, Any],
        rng: np.random.Generator,
        *,
        probability_atol: float,
    ) -> "BetaCalibrator":
        del rng
        support = require_support(y_index, profile)
        epsilon = float(profile["nll_epsilon"])
        x = self._features(source, probability_atol, epsilon)
        y = (y_index == 1).astype(np.float64)
        l2 = float(profile["l2_penalty"])

        def objective(theta: np.ndarray) -> tuple[float, np.ndarray]:
            q = _sigmoid(x @ theta)
            q_clip = np.clip(q, epsilon, 1.0 - epsilon)
            loss = -np.mean(y * np.log(q_clip) + (1 - y) * np.log1p(-q_clip)) + 0.5 * l2 * float(theta[:2] @ theta[:2])
            grad = x.T @ (q - y) / len(y)
            grad[:2] += l2 * theta[:2]
            return float(loss), grad

        result = minimize(lambda t: objective(t), np.array([1.0, 1.0, 0.0]), method="L-BFGS-B", jac=True, options={"ftol": float(profile["optimizer_tolerance"]), "maxiter": int(profile["max_iterations"])})
        if not result.success or not np.all(np.isfinite(result.x)):
            raise RuntimeError(f"Beta optimization failed: {result.message}")
        self.parameters = {"a": float(result.x[0]), "b": float(result.x[1]), "c": float(result.x[2]), "support": support, "epsilon": epsilon}
        self.optimizer_result = {"optimizer": "scipy.L-BFGS-B", "success": bool(result.success), "fun": float(result.fun), "nit": int(result.nit), "message": str(result.message)}
        self.convergence_status = "CONVERGED"
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        x = self._features(view, probability_atol, float(self.parameters["epsilon"]))
        theta = np.array([self.parameters["a"], self.parameters["b"], self.parameters["c"]], dtype=float)
        q = _sigmoid(x @ theta)
        return np.column_stack([1.0 - q, q])

