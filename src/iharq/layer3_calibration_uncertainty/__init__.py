"""IHARQ cumulative Layer 3 import boundary.

The accepted P03 implementation is retained unchanged under
``current/phase_03/implementation/src/iharq/layer3_calibration_uncertainty``.
The cumulative root package exposes the same Layer 3 modules while preserving
the repository-wide contract that importing a layer never constitutes or
starts scientific execution.
"""
from .constants import LAYER_ID, PHASE_ID, PACKAGE_VERSION

SCIENTIFIC_EXECUTION_ON_IMPORT = False
SCIENTIFIC_EXECUTION = False

__all__ = [
    "LAYER_ID",
    "PHASE_ID",
    "PACKAGE_VERSION",
    "SCIENTIFIC_EXECUTION_ON_IMPORT",
    "SCIENTIFIC_EXECUTION",
]
