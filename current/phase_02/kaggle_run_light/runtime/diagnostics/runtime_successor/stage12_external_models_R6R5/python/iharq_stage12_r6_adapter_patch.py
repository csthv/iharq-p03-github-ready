from __future__ import annotations
import numpy as np
import iharq_stage12_external_adapters as _base

class IHARQCBraModR6ScaledAdapter(_base.IHARQCBraModGovernedAdapter):
    resolved_variant = "CBraMod-HF-Braindecode-GovernedP02-R6Scale1e4"

    def _prepare(self, X):
        out = super()._prepare(X)
        scale = float(self.config.get("input_scale", 1.0))
        if scale == 1.0:
            return out
        # New array is deliberate: never mutate P01/core data or a shared cache.
        return np.asarray(out, dtype=np.float32) * np.float32(scale)


def build_cbramod_r6(checkpoint_path, config):
    cfg = dict(config or {})
    cfg["input_scale"] = float(cfg.get("input_scale", 10000.0))
    cfg["preparation_cache_max_gib"] = float(cfg.get("preparation_cache_max_gib", 0.0))
    return IHARQCBraModR6ScaledAdapter(checkpoint_path, cfg)
