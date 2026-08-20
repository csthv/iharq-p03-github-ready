"""Authority-constrained calibrator factory; unsupported methods fail explicitly."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from ..errors import IneligibleMethod
from .base import FittedCalibrator
from .beta import BetaCalibrator
from .conditional import (
    CenteredIsotonicDiagnosticCalibrator,
    DirichletDiagnosticCalibrator,
    IsotonicDiagnosticCalibrator,
    MonotoneSplineCalibrator,
    QuadraticLogisticCalibrator,
    VennAbersDiagnosticCalibrator,
)
from .identity import IdentityCalibrator
from .platt import PlattCalibrator
from .structured import StructuredScalingCalibrator
from .temperature import TemperatureCalibrator

ACCEPTED_METHODS = {
    "identity",
    "temperature",
    "platt",
    "beta",
    "quadratic_logistic",
    "vector_scaling",
    "matrix_scaling",
    "monotone_spline",
    "isotonic_diagnostic",
    "cir_diagnostic",
    "dirichlet_diagnostic",
    "venn_abers_diagnostic",
}


def create_calibrator(profile: Mapping[str, Any], class_order: Sequence[str], score_type: str) -> FittedCalibrator:
    method = str(profile["method_id"])
    if method not in ACCEPTED_METHODS:
        raise IneligibleMethod(f"Method {method!r} is outside the accepted P03 method families")
    common = {"method_id": method, "method_family": str(profile.get("method_family", method)), "class_order": tuple(class_order), "score_type": score_type}
    if method == "identity":
        return IdentityCalibrator(**common)
    if method == "temperature":
        return TemperatureCalibrator(**common)
    if method == "platt":
        return PlattCalibrator(**common)
    if method == "beta":
        return BetaCalibrator(**common)
    if method == "quadratic_logistic":
        return QuadraticLogisticCalibrator(**common)
    if method == "vector_scaling":
        if not bool(profile.get("protocol_activated")):
            raise IneligibleMethod("Vector scaling requires explicit Protocol activation")
        return StructuredScalingCalibrator(**common, structure="vector")
    if method == "matrix_scaling":
        if not bool(profile.get("protocol_activated")):
            raise IneligibleMethod("Matrix scaling requires explicit Protocol activation")
        return StructuredScalingCalibrator(**common, structure="matrix")
    if method == "monotone_spline":
        if not bool(profile.get("protocol_activated")):
            raise IneligibleMethod("Spline calibration requires explicit Protocol activation")
        return MonotoneSplineCalibrator(**common)
    if method == "isotonic_diagnostic":
        if not bool(profile.get("diagnostic_gate")):
            raise IneligibleMethod("Isotonic is allowed only under the exact diagnostic gate")
        return IsotonicDiagnosticCalibrator(**common, diagnostic_only=True)
    if method == "cir_diagnostic":
        if not bool(profile.get("diagnostic_gate")):
            raise IneligibleMethod("CIR is allowed only under the exact diagnostic gate")
        return CenteredIsotonicDiagnosticCalibrator(**common, diagnostic_only=True)
    if method == "dirichlet_diagnostic":
        if not bool(profile.get("diagnostic_gate")):
            raise IneligibleMethod("Dirichlet calibration is allowed only under the exact diagnostic gate")
        return DirichletDiagnosticCalibrator(**common, diagnostic_only=True)
    if method == "venn_abers_diagnostic":
        if not bool(profile.get("diagnostic_gate")):
            raise IneligibleMethod("Venn–Abers is allowed only under the exact diagnostic gate")
        return VennAbersDiagnosticCalibrator(**common, diagnostic_only=True)
    raise AssertionError(method)
