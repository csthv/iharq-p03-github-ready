"""IHARQ Phase 03 / Layer 03 calibration, uncertainty, and selective prediction.

This package is an additive P03 overlay for the finalized cumulative repository
through P02.  Scientific execution is enabled only through a validated immutable
P03 execution freeze; importing the package never starts computation.
"""

from .constants import LAYER_ID, PHASE_ID, PACKAGE_VERSION

SCIENTIFIC_EXECUTION = True

__all__ = ["LAYER_ID", "PHASE_ID", "PACKAGE_VERSION", "SCIENTIFIC_EXECUTION"]

