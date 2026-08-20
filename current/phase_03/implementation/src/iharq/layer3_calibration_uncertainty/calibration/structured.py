"""Support-gated vector/diagonal and matrix scaling."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

import numpy as np
from scipy.optimize import minimize

from ..errors import IneligibleMethod
from ..score_contracts import ScoreView, validate_logits
from .base import FittedCalibrator, clipped_nll, require_support, stable_softmax


@dataclass
class StructuredScalingCalibrator(FittedCalibrator):
    structure: str = "vector"

    def _logits(self, view: ScoreView) -> np.ndarray:
        if view.score_type != "logit":
            raise IneligibleMethod(f"{self.structure} scaling requires genuine logits")
        return validate_logits(view.values)

    def fit(
        self,
        source: ScoreView,
        y_index: np.ndarray,
        profile: Mapping[str, Any],
        rng: np.random.Generator,
        *,
        probability_atol: float,
    ) -> "StructuredScalingCalibrator":
        del rng, probability_atol
        support = require_support(y_index, profile)
        z = self._logits(source)
        k = z.shape[1]
        epsilon = float(profile["nll_epsilon"])
        l2 = float(profile["l2_penalty"])
        if self.structure == "vector":
            initial = np.concatenate([np.zeros(k), np.zeros(k)])

            def unpack(theta: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
                return np.diag(np.exp(theta[:k])), theta[k:]
        elif self.structure == "matrix":
            initial = np.concatenate([np.eye(k).ravel(), np.zeros(k)])

            def unpack(theta: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
                return theta[: k * k].reshape(k, k), theta[k * k :]
        else:
            raise ValueError(f"Unknown structure={self.structure}")

        def objective(theta: np.ndarray) -> float:
            weight, bias = unpack(theta)
            transformed = z @ weight.T + bias
            penalty = 0.5 * l2 * float(np.sum((weight - np.eye(k)) ** 2) + np.sum(bias**2))
            return clipped_nll(stable_softmax(transformed), y_index, epsilon) + penalty

        result = minimize(objective, initial, method="L-BFGS-B", options={"ftol": float(profile["optimizer_tolerance"]), "maxiter": int(profile["max_iterations"])})
        if not result.success or not np.all(np.isfinite(result.x)):
            raise RuntimeError(f"{self.structure} scaling failed: {result.message}")
        weight, bias = unpack(result.x)
        self.parameters = {"structure": self.structure, "weight": weight.tolist(), "bias": bias.tolist(), "support": support}
        self.optimizer_result = {"optimizer": "scipy.L-BFGS-B", "success": bool(result.success), "fun": float(result.fun), "nit": int(result.nit), "message": str(result.message)}
        self.convergence_status = "CONVERGED"
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        del probability_atol
        z = self._logits(view)
        weight = np.asarray(self.parameters["weight"], dtype=float)
        bias = np.asarray(self.parameters["bias"], dtype=float)
        return stable_softmax(z @ weight.T + bias)

