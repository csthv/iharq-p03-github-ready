"""Protocol-gated quadratic logistic, monotone spline, and isotonic diagnostics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import minimize

from ..errors import IneligibleMethod
from ..score_contracts import ScoreView, score_to_probabilities, validate_probabilities
from .base import FittedCalibrator, clipped_nll, require_support, stable_softmax
from .platt import _sigmoid


@dataclass
class QuadraticLogisticCalibrator(FittedCalibrator):
    def _feature(self, view: ScoreView, atol: float, epsilon: float) -> np.ndarray:
        if len(view.class_order) != 2:
            raise IneligibleMethod("Quadratic logistic calibration is binary-only")
        p = score_to_probabilities(view, probability_atol=atol)[:, 1]
        p = np.clip(p, epsilon, 1.0 - epsilon)
        logit = np.log(p) - np.log1p(-p)
        return np.column_stack([logit, logit**2, np.ones(len(logit))])

    def fit(self, source: ScoreView, y_index: np.ndarray, profile: Mapping[str, Any], rng: np.random.Generator, *, probability_atol: float) -> "QuadraticLogisticCalibrator":
        del rng
        support = require_support(y_index, profile)
        epsilon = float(profile["nll_epsilon"])
        x = self._feature(source, probability_atol, epsilon)
        y = (y_index == 1).astype(float)
        l2 = float(profile["l2_penalty"])

        def objective(theta: np.ndarray) -> tuple[float, np.ndarray]:
            q = _sigmoid(x @ theta)
            q_clip = np.clip(q, epsilon, 1 - epsilon)
            loss = -np.mean(y * np.log(q_clip) + (1 - y) * np.log1p(-q_clip)) + 0.5 * l2 * float(theta[:2] @ theta[:2])
            grad = x.T @ (q - y) / len(y)
            grad[:2] += l2 * theta[:2]
            return float(loss), grad

        result = minimize(lambda t: objective(t), np.array([1.0, 0.0, 0.0]), jac=True, method="L-BFGS-B", options={"ftol": float(profile["optimizer_tolerance"]), "maxiter": int(profile["max_iterations"])})
        if not result.success:
            raise RuntimeError(f"Quadratic logistic failed: {result.message}")
        self.parameters = {"linear": float(result.x[0]), "quadratic": float(result.x[1]), "intercept": float(result.x[2]), "epsilon": epsilon, "support": support}
        self.optimizer_result = {"optimizer": "scipy.L-BFGS-B", "success": True, "fun": float(result.fun), "nit": int(result.nit), "message": str(result.message)}
        self.convergence_status = "CONVERGED"
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        x = self._feature(view, probability_atol, float(self.parameters["epsilon"]))
        theta = np.array([self.parameters["linear"], self.parameters["quadratic"], self.parameters["intercept"]])
        q = _sigmoid(x @ theta)
        return np.column_stack([1 - q, q])


@dataclass
class MonotoneSplineCalibrator(FittedCalibrator):
    """Binary, support-gated PCHIP map built from Protocol-frozen equal-mass bins."""

    def fit(self, source: ScoreView, y_index: np.ndarray, profile: Mapping[str, Any], rng: np.random.Generator, *, probability_atol: float) -> "MonotoneSplineCalibrator":
        del rng
        support = require_support(y_index, profile)
        if len(source.class_order) != 2:
            raise IneligibleMethod("Spline calibration is binary-only in this P03 profile")
        p = score_to_probabilities(source, probability_atol=probability_atol)[:, 1]
        bins = int(profile["spline_bins"])
        if bins < 3:
            raise ValueError("spline_bins must be >=3")
        order = np.argsort(p, kind="stable")
        chunks = np.array_split(order, bins)
        x = np.array([float(np.mean(p[idx])) for idx in chunks if len(idx)], dtype=float)
        y = np.array([float(np.mean(y_index[idx] == 1)) for idx in chunks if len(idx)], dtype=float)
        x, unique = np.unique(x, return_index=True)
        y = y[unique]
        if len(x) < 3:
            raise IneligibleMethod("Spline calibration has fewer than three distinct probability knots")
        if bool(profile["enforce_monotone"]):
            y = np.maximum.accumulate(y)
        y = np.clip(y, 0.0, 1.0)
        self.parameters = {"knots_x": x.tolist(), "knots_y": y.tolist(), "extrapolate": False, "support": support}
        self.optimizer_result = {"optimizer": "PchipInterpolator", "success": True, "bin_count": len(x)}
        self.convergence_status = "CONVERGED"
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        p = score_to_probabilities(view, probability_atol=probability_atol)[:, 1]
        x = np.asarray(self.parameters["knots_x"], dtype=float)
        y = np.asarray(self.parameters["knots_y"], dtype=float)
        q = PchipInterpolator(x, y, extrapolate=False)(np.clip(p, x[0], x[-1]))
        q = np.clip(q, 0.0, 1.0)
        return np.column_stack([1 - q, q])


@dataclass
class IsotonicDiagnosticCalibrator(FittedCalibrator):
    """Exact sklearn isotonic path; factory permits it only under an explicit diagnostic gate."""

    def fit(self, source: ScoreView, y_index: np.ndarray, profile: Mapping[str, Any], rng: np.random.Generator, *, probability_atol: float) -> "IsotonicDiagnosticCalibrator":
        del rng
        require_support(y_index, profile)
        if len(source.class_order) != 2:
            raise IneligibleMethod("Isotonic diagnostic is binary-only")
        from sklearn.isotonic import IsotonicRegression
        p = score_to_probabilities(source, probability_atol=probability_atol)[:, 1]
        model = IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip").fit(p, y_index == 1)
        self.parameters = {"x_thresholds": model.X_thresholds_.tolist(), "y_thresholds": model.y_thresholds_.tolist()}
        self.optimizer_result = {"optimizer": "sklearn.IsotonicRegression", "success": True}
        self.convergence_status = "CONVERGED"
        self.diagnostic_only = True
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        p = score_to_probabilities(view, probability_atol=probability_atol)[:, 1]
        q = np.interp(p, self.parameters["x_thresholds"], self.parameters["y_thresholds"])
        return validate_probabilities(np.column_stack([1 - q, q]), atol=probability_atol)


def _pav_blocks(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Pool-adjacent-violators blocks returned at weighted x centers."""
    order = np.argsort(x, kind="stable")
    xs, ys = x[order], y[order].astype(float)
    blocks: list[dict[str, float]] = []
    for xv, yv in zip(xs, ys):
        blocks.append({"weight": 1.0, "x_sum": float(xv), "y_sum": float(yv)})
        while len(blocks) >= 2:
            left, right = blocks[-2], blocks[-1]
            if left["y_sum"] / left["weight"] <= right["y_sum"] / right["weight"]:
                break
            blocks[-2:] = [{"weight": left["weight"] + right["weight"], "x_sum": left["x_sum"] + right["x_sum"], "y_sum": left["y_sum"] + right["y_sum"]}]
    centers = np.asarray([block["x_sum"] / block["weight"] for block in blocks], dtype=float)
    values = np.asarray([block["y_sum"] / block["weight"] for block in blocks], dtype=float)
    return centers, values


@dataclass
class CenteredIsotonicDiagnosticCalibrator(FittedCalibrator):
    """Binary centered isotonic regression (CIR) diagnostic sensitivity path."""

    def fit(self, source: ScoreView, y_index: np.ndarray, profile: Mapping[str, Any], rng: np.random.Generator, *, probability_atol: float) -> "CenteredIsotonicDiagnosticCalibrator":
        del rng
        support = require_support(y_index, profile)
        if len(source.class_order) != 2:
            raise IneligibleMethod("Centered isotonic regression is binary-only")
        p = score_to_probabilities(source, probability_atol=probability_atol)[:, 1]
        centers, values = _pav_blocks(p, (y_index == 1).astype(float))
        if len(centers) < 2:
            raise IneligibleMethod("CIR requires at least two pooled blocks")
        self.parameters = {"centers": centers.tolist(), "values": values.tolist(), "support": support, "interpolation": "linear_between_weighted_block_centers"}
        self.optimizer_result = {"optimizer": "pool_adjacent_violators_centered", "success": True, "block_count": len(centers)}
        self.convergence_status = "CONVERGED"
        self.diagnostic_only = True
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        p = score_to_probabilities(view, probability_atol=probability_atol)[:, 1]
        q = np.interp(p, np.asarray(self.parameters["centers"]), np.asarray(self.parameters["values"]))
        return validate_probabilities(np.column_stack([1.0 - q, q]), atol=probability_atol)


@dataclass
class DirichletDiagnosticCalibrator(FittedCalibrator):
    """Multiclass Dirichlet calibration using regularized log-probability features."""

    def fit(self, source: ScoreView, y_index: np.ndarray, profile: Mapping[str, Any], rng: np.random.Generator, *, probability_atol: float) -> "DirichletDiagnosticCalibrator":
        del rng
        support = require_support(y_index, profile)
        p = score_to_probabilities(source, probability_atol=probability_atol)
        epsilon = float(profile["nll_epsilon"])
        x = np.log(np.clip(p, epsilon, 1.0))
        k = p.shape[1]
        l2 = float(profile["l2_penalty"])
        initial = np.concatenate([np.eye(k).ravel(), np.zeros(k)])

        def objective(theta: np.ndarray) -> float:
            weight = theta[: k * k].reshape(k, k)
            bias = theta[k * k :]
            q = stable_softmax(x @ weight.T + bias)
            regularizer = 0.5 * l2 * float(np.sum((weight - np.eye(k)) ** 2) + np.sum(bias**2))
            return clipped_nll(q, y_index, epsilon) + regularizer

        result = minimize(objective, initial, method="L-BFGS-B", options={"ftol": float(profile["optimizer_tolerance"]), "maxiter": int(profile["max_iterations"])})
        if not result.success or not np.all(np.isfinite(result.x)):
            raise RuntimeError(f"Dirichlet calibration failed: {result.message}")
        self.parameters = {"weight": result.x[: k * k].reshape(k, k).tolist(), "bias": result.x[k * k :].tolist(), "epsilon": epsilon, "support": support}
        self.optimizer_result = {"optimizer": "scipy.L-BFGS-B", "success": True, "fun": float(result.fun), "nit": int(result.nit), "message": str(result.message)}
        self.convergence_status = "CONVERGED"
        self.diagnostic_only = True
        return self

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        p = score_to_probabilities(view, probability_atol=probability_atol)
        x = np.log(np.clip(p, float(self.parameters["epsilon"]), 1.0))
        weight = np.asarray(self.parameters["weight"], dtype=float)
        bias = np.asarray(self.parameters["bias"], dtype=float)
        return stable_softmax(x @ weight.T + bias)


@dataclass
class VennAbersDiagnosticCalibrator(FittedCalibrator):
    """Binary inductive Venn–Abers predictive interval and single-probability path."""

    def fit(self, source: ScoreView, y_index: np.ndarray, profile: Mapping[str, Any], rng: np.random.Generator, *, probability_atol: float) -> "VennAbersDiagnosticCalibrator":
        del rng
        support = require_support(y_index, profile)
        if len(source.class_order) != 2:
            raise IneligibleMethod("Venn–Abers diagnostic is binary-only")
        p = score_to_probabilities(source, probability_atol=probability_atol)[:, 1]
        self.parameters = {"calibration_scores": p.tolist(), "calibration_labels": (y_index == 1).astype(int).tolist(), "support": support, "combination": "p1/(1-p0+p1)"}
        self.optimizer_result = {"optimizer": "inductive_venn_abers_transductive_isotonic_pair", "success": True}
        self.convergence_status = "CONVERGED"
        self.diagnostic_only = True
        return self

    def apply_interval(self, view: ScoreView, *, probability_atol: float) -> tuple[np.ndarray, np.ndarray]:
        from sklearn.isotonic import IsotonicRegression
        test = score_to_probabilities(view, probability_atol=probability_atol)[:, 1]
        calibration_scores = np.asarray(self.parameters["calibration_scores"], dtype=float)
        calibration_labels = np.asarray(self.parameters["calibration_labels"], dtype=int)
        lower, upper = np.empty(len(test)), np.empty(len(test))
        for index, score in enumerate(test):
            augmented_scores = np.append(calibration_scores, score)
            model0 = IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip").fit(augmented_scores, np.append(calibration_labels, 0))
            model1 = IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip").fit(augmented_scores, np.append(calibration_labels, 1))
            lower[index] = float(model0.predict([score])[0])
            upper[index] = float(model1.predict([score])[0])
        return lower, upper

    def apply(self, view: ScoreView, *, probability_atol: float) -> np.ndarray:
        lower, upper = self.apply_interval(view, probability_atol=probability_atol)
        denominator = 1.0 - lower + upper
        q = np.divide(upper, denominator, out=np.full_like(upper, 0.5), where=denominator > 0)
        return validate_probabilities(np.column_stack([1.0 - q, q]), atol=probability_atol)
