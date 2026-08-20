"""Compatibility shim for the already-running Stage-18 worker.

The authoritative implementation is layer1_data_protocol.manifests.write_json.
"""
from .manifests import write_json

__all__ = ["write_json"]
