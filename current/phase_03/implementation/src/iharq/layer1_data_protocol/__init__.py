"""IHARQ Phase 1 / Layer 1 public-data and split-protocol runtime."""
SCIENTIFIC_EXECUTION = False
from .pipeline import Layer1Pipeline
from .kaggle_adapter import StageRunner
__all__ = ["Layer1Pipeline", "StageRunner", "SCIENTIFIC_EXECUTION"]
