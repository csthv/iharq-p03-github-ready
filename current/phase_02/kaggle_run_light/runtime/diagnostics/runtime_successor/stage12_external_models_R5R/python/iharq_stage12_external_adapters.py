from __future__ import annotations

import gc
import hashlib
import importlib.util
import io
import math
import random
import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np


_PREP_CACHE = {}
_PREP_CACHE_BYTES = 0
_SOURCE_MODULE_CACHE = {}


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def _require_file(path, expected_sha=None):
    p = Path(path)
    if not p.is_file():
        raise RuntimeError(f"CHECKPOINT_BLOCKED:REQUIRED_FILE_MISSING:{p}")
    if expected_sha:
        observed = _sha256(p)
        if observed != str(expected_sha):
            raise RuntimeError(
                f"CHECKPOINT_BLOCKED:FILE_SHA256_MISMATCH:{p}:{observed}:{expected_sha}"
            )
    return p


def _load_source_module(module_name, path, expected_sha):
    key = (str(module_name), str(Path(path).resolve()), str(expected_sha))
    if key in _SOURCE_MODULE_CACHE:
        return _SOURCE_MODULE_CACHE[key]
    p = _require_file(path, expected_sha)
    spec = importlib.util.spec_from_file_location(str(module_name), str(p))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"DEPENDENCY_BLOCKED:SOURCE_IMPORT_SPEC_FAILED:{p}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[str(module_name)] = mod
    try:
        spec.loader.exec_module(mod)
    except Exception:
        sys.modules.pop(str(module_name), None)
        raise
    _SOURCE_MODULE_CACHE[key] = mod
    return mod


def _seed_everything(seed):
    import torch

    seed = int(seed)
    random.seed(seed)
    np.random.seed(seed % (2**32 - 1))
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    # Match the governed deterministic stance without enabling new global
    # deterministic-algorithm restrictions or changing TF32/AMP policy.
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def _is_oom(exc):
    text = str(exc).lower()
    return (
        "out of memory" in text
        or "cuda error: out of memory" in text
        or "cuda out of memory" in text
    )


def _array_token(x, prefix):
    a = np.asarray(x)
    flat = a.reshape(-1)
    if flat.size == 0:
        sample = b""
    else:
        n = min(96, int(flat.size))
        idx = np.linspace(0, flat.size - 1, n, dtype=np.int64)
        sample = np.ascontiguousarray(flat[idx]).tobytes()
    h = hashlib.sha256()
    h.update(str(tuple(a.shape)).encode())
    h.update(str(a.dtype).encode())
    h.update(sample)
    return (str(prefix), tuple(a.shape), str(a.dtype), h.hexdigest())


def _cache_get(token):
    return _PREP_CACHE.get(token)


def _cache_put(token, value, max_gib):
    global _PREP_CACHE_BYTES
    arr = np.asarray(value)
    size = int(arr.nbytes)
    limit = int(float(max_gib) * (1024**3))
    if size <= 0 or size > limit:
        return value
    if token in _PREP_CACHE:
        return _PREP_CACHE[token]
    if _PREP_CACHE_BYTES + size > limit:
        return value
    _PREP_CACHE[token] = arr
    _PREP_CACHE_BYTES += size
    return arr


def preparation_cache_state():
    return {
        "entries": len(_PREP_CACHE),
        "bytes": int(_PREP_CACHE_BYTES),
        "gib": float(_PREP_CACHE_BYTES / (1024**3)),
    }


class _GovernedTorchExternalAdapter:
    score_type = "SOFTMAX_PROBABILITY"
    resolved_variant = "UNRESOLVED_EXTERNAL"
    supports_class_weights = True

    def __init__(self, checkpoint_path, config):
        self.checkpoint_path = None if checkpoint_path is None else str(checkpoint_path)
        self.config = dict(config or {})
        self.seed = int(self.config.get("iharq_seed", self.config.get("seed", 0)))
        self.model = None
        self.device = "cpu"
        self.actual_batch_size = None
        self.gradient_accumulation = None
        self.raw_shape = None
        self.prepared_shape = None
        self.training_epochs_completed = 0
        self.best_validation_bacc = None
        self.resource_events = []

    def _prepare(self, X):
        raise NotImplementedError

    def _build_model(self, n_chans, n_times):
        raise NotImplementedError

    def _forward_logits(self, xb):
        z = self.model(xb)
        if isinstance(z, (tuple, list)):
            z = z[-1]
        return z

    def _prepare_and_validate(self, X):
        a = np.asarray(X, dtype=np.float32)
        if a.ndim != 3:
            raise RuntimeError(f"INPUT_INCOMPATIBLE:EXPECTED_BCT:{a.shape}")
        if not np.all(np.isfinite(a)):
            raise RuntimeError("INPUT_INCOMPATIBLE:NONFINITE_INPUT")
        expected_c = self.config.get("expected_n_chans")
        expected_t = self.config.get("expected_n_times")
        if expected_c is not None and int(a.shape[1]) != int(expected_c):
            raise RuntimeError(
                f"INPUT_INCOMPATIBLE:CHANNEL_COUNT:{a.shape[1]}!={expected_c}"
            )
        if expected_t is not None and int(a.shape[2]) != int(expected_t):
            raise RuntimeError(
                f"INPUT_INCOMPATIBLE:TIME_SAMPLES:{a.shape[2]}!={expected_t}"
            )
        out = np.asarray(self._prepare(a), dtype=np.float32)
        if not np.all(np.isfinite(out)):
            raise RuntimeError("INPUT_INCOMPATIBLE:NONFINITE_PREPARED_INPUT")
        return out

    def _predict_scores_prepared(self, Xp, device=None):
        import torch

        if self.model is None:
            raise RuntimeError("MODEL_NOT_FIT")
        d = str(device or self.device)
        self.model.eval()
        bs = int(self.actual_batch_size or self.config.get("inference_batch_size", 64))
        bs = max(1, bs)
        outputs = []
        with torch.no_grad():
            for start in range(0, len(Xp), bs):
                xb = torch.as_tensor(
                    Xp[start : start + bs], dtype=torch.float32, device=d
                )
                z = self._forward_logits(xb)
                if z.ndim != 2 or int(z.shape[1]) != 2:
                    raise RuntimeError(
                        f"INPUT_INCOMPATIBLE:OUTPUT_SHAPE:{tuple(z.shape)}"
                    )
                p = torch.softmax(z, dim=1)
                outputs.append(p.detach().cpu().numpy())
        if not outputs:
            return np.empty((0, 2), dtype=np.float32)
        out = np.concatenate(outputs, axis=0).astype(np.float32, copy=False)
        if not np.all(np.isfinite(out)):
            raise RuntimeError("NONFINITE_MODEL_SCORES")
        return out

    def fit(
        self,
        X,
        y,
        epochs=100,
        lr=1e-3,
        weight_decay=0.0,
        batch_size=64,
        effective_batch_target=64,
        device="cpu",
        X_val=None,
        y_val=None,
        patience=12,
        min_delta=0.0,
        restore_best=True,
        class_weights=None,
        **kw,
    ):
        import torch
        from sklearn.metrics import balanced_accuracy_score
        from torch.utils.data import DataLoader, TensorDataset

        batch_size = int(batch_size)
        if batch_size not in {64, 32, 16}:
            raise ValueError("BATCH_SIZE_NOT_IN_FROZEN_LADDER")
        _seed_everything(self.seed)

        Xraw = np.asarray(X, dtype=np.float32)
        y = np.asarray(y, dtype=np.int64)
        if len(Xraw) != len(y):
            raise RuntimeError("INPUT_INCOMPATIBLE:X_Y_LENGTH_MISMATCH")
        if set(np.unique(y).tolist()) - {0, 1}:
            raise RuntimeError("INPUT_INCOMPATIBLE:LABEL_DOMAIN_NOT_BINARY_0_1")

        self.raw_shape = (int(Xraw.shape[1]), int(Xraw.shape[2]))
        Xp = self._prepare_and_validate(Xraw)
        Xvp = None
        if X_val is not None:
            Xvp = self._prepare_and_validate(np.asarray(X_val, dtype=np.float32))
            if y_val is None or len(Xvp) != len(y_val):
                raise RuntimeError("INPUT_INCOMPATIBLE:VALIDATION_LENGTH_MISMATCH")

        self.prepared_shape = tuple(int(v) for v in Xp.shape[1:])
        self.model = self._build_model(*self.raw_shape).to(device)
        self.device = str(device)

        # R5R resource-only acceleration: use all allowed GPUs in the
        # current Kaggle session for a single governed cell when the
        # training set is large enough. The scientific batch size,
        # optimizer, grid, epoch/early-stop policy, labels and metrics are
        # unchanged; DataParallel only shards the existing total batch.
        use_dp = (
            bool(self.config.get("use_data_parallel", False))
            and torch.cuda.is_available()
            and torch.cuda.device_count() >= 2
            and str(device).startswith("cuda")
            and len(Xp) >= int(self.config.get("data_parallel_min_samples", 256))
        )
        if use_dp:
            max_gpus = max(2, int(self.config.get("data_parallel_max_gpus", torch.cuda.device_count())))
            device_ids = list(range(min(torch.cuda.device_count(), max_gpus)))
            self.model = torch.nn.DataParallel(self.model, device_ids=device_ids)
            self.resource_events.append(
                {
                    "type": "DATA_PARALLEL",
                    "device_ids": device_ids,
                    "total_batch_size": batch_size,
                    "scientific_hyperparameters_changed": False,
                    "resource_execution_changed": True,
                    "numerical_execution_path_changed": True,
                }
            )

        self.actual_batch_size = batch_size
        self.gradient_accumulation = max(
            1, int(math.ceil(int(effective_batch_target) / batch_size))
        )

        cw = None
        if class_weights is not None:
            if len(class_weights) != 2:
                raise RuntimeError("INPUT_INCOMPATIBLE:CLASS_WEIGHT_LENGTH_NOT_2")
            cw = torch.tensor(class_weights, dtype=torch.float32, device=device)

        loss_fn = torch.nn.CrossEntropyLoss(weight=cw)
        opt = torch.optim.AdamW(
            self.model.parameters(), lr=float(lr), weight_decay=float(weight_decay)
        )
        y_tensor = torch.as_tensor(y, dtype=torch.long)
        data_tensor = torch.as_tensor(Xp, dtype=torch.float32)

        best = -np.inf
        best_state = None
        bad = 0
        self.training_epochs_completed = 0

        try:
            for epoch in range(int(epochs)):
                gen = torch.Generator()
                gen.manual_seed(int(self.seed) + int(epoch))
                loader = DataLoader(
                    TensorDataset(data_tensor, y_tensor),
                    batch_size=batch_size,
                    shuffle=True,
                    generator=gen,
                )
                self.model.train()
                opt.zero_grad(set_to_none=True)
                pending = 0
                for xb, yb in loader:
                    xb = xb.to(device, non_blocking=False)
                    yb = yb.to(device, non_blocking=False)
                    z = self._forward_logits(xb)
                    loss = loss_fn(z, yb) / self.gradient_accumulation
                    loss.backward()
                    pending += 1
                    if pending % self.gradient_accumulation == 0:
                        opt.step()
                        opt.zero_grad(set_to_none=True)
                if pending % self.gradient_accumulation:
                    opt.step()
                    opt.zero_grad(set_to_none=True)

                self.training_epochs_completed += 1

                if Xvp is not None:
                    pv = np.argmax(
                        self._predict_scores_prepared(Xvp, device=device), axis=1
                    )
                    bacc = float(
                        balanced_accuracy_score(np.asarray(y_val, dtype=int), pv)
                    )
                    if bacc > best + float(min_delta):
                        best = bacc
                        bad = 0
                        best_state = {
                            k: v.detach().cpu().clone()
                            for k, v in self.model.state_dict().items()
                        }
                    else:
                        bad += 1
                    if bad >= int(patience):
                        break
        except RuntimeError as exc:
            if _is_oom(exc):
                self.resource_events.append(
                    {
                        "type": "CUDA_OOM",
                        "batch_size": batch_size,
                        "message": str(exc)[:240],
                    }
                )
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                raise ResourceWarning(
                    f"CUDA_OOM_AT_FROZEN_BATCH:{batch_size}"
                ) from exc
            raise

        if restore_best and best_state is not None:
            self.model.load_state_dict(best_state, strict=True)

        # Checkpoint the underlying single model, not the DataParallel
        # transport wrapper. This keeps checkpoint identity independent of
        # the number of visible GPUs.
        if isinstance(self.model, torch.nn.DataParallel):
            self.model = self.model.module

        self.best_validation_bacc = None if best == -np.inf else float(best)
        return self

    def predict_scores(self, X, device=None, **kw):
        Xp = self._prepare_and_validate(np.asarray(X, dtype=np.float32))
        return self._predict_scores_prepared(Xp, device=device)

    def predict(self, X, device=None, **kw):
        return np.argmax(self.predict_scores(X, device=device, **kw), axis=1)

    def _checkpoint_metadata(self):
        return {
            "resolved_variant": self.resolved_variant,
            "seed": int(self.seed),
            "raw_shape": list(self.raw_shape) if self.raw_shape is not None else None,
            "prepared_shape": list(self.prepared_shape)
            if self.prepared_shape is not None
            else None,
            "config": self.config,
            "resource_events": list(self.resource_events),
        }

    def export_iharq_checkpoint_bytes(self):
        import torch

        if self.model is None or self.raw_shape is None:
            raise RuntimeError("MODEL_NOT_FIT")
        payload = {
            "state_dict": {
                k: v.detach().cpu() for k, v in self.model.state_dict().items()
            },
            "metadata": self._checkpoint_metadata(),
        }
        bio = io.BytesIO()
        torch.save(payload, bio)
        return bio.getvalue()

    def reload_iharq_checkpoint_bytes(self, payload):
        import torch

        try:
            d = torch.load(io.BytesIO(payload), map_location="cpu", weights_only=True)
        except TypeError:
            d = torch.load(io.BytesIO(payload), map_location="cpu")
        meta = d["metadata"]
        q = self.__class__(self.checkpoint_path, dict(meta["config"]))
        q.seed = int(meta["seed"])
        q.raw_shape = tuple(int(v) for v in meta["raw_shape"])
        q.prepared_shape = tuple(int(v) for v in meta["prepared_shape"])
        _seed_everything(q.seed)
        q.model = q._build_model(*q.raw_shape).cpu()
        q.model.load_state_dict(d["state_dict"], strict=True)
        q.model.eval()
        q.device = "cpu"
        q.actual_batch_size = int(self.actual_batch_size or 64)
        q.gradient_accumulation = int(self.gradient_accumulation or 1)
        return q


class IHARQFBCNetOriginalAuthorAdapter(_GovernedTorchExternalAdapter):
    score_type = "SOFTMAX_PROBABILITY"
    resolved_variant = "FBCNet-OriginalAuthor-P01ConstrainedFilterBank"

    def __init__(self, checkpoint_path, config):
        super().__init__(checkpoint_path, config)
        self.network_source_path = str(self.config["network_source_path"])
        self.network_source_sha256 = str(self.config["network_source_sha256"])
        self.transform_source_path = str(self.config["transform_source_path"])
        self.transform_source_sha256 = str(self.config["transform_source_sha256"])
        self.fs = float(self.config.get("source_sampling_hz", 160))
        self.bands = [tuple(map(float, x)) for x in self.config["bands_hz"]]
        self.filt_allowance = float(self.config.get("filt_allowance_hz", 2.0))
        self.filt_type = str(self.config.get("filt_type", "filter"))
        self.cache_max_gib = float(self.config.get("preparation_cache_max_gib", 10.0))
        if len(self.bands) != int(self.config.get("n_bands", len(self.bands))):
            raise RuntimeError("INPUT_INCOMPATIBLE:FBCNET_NBANDS_CONFIG_MISMATCH")
        _require_file(self.network_source_path, self.network_source_sha256)
        _require_file(self.transform_source_path, self.transform_source_sha256)

    def _prepare(self, X):
        token = _array_token(X, "FBCNET_FILTERBANK_V1")
        cached = _cache_get(token)
        if cached is not None:
            return cached
        transforms_mod = _load_source_module(
            "_iharq_fbcnet_original_transforms_" + self.transform_source_sha256[:12],
            self.transform_source_path,
            self.transform_source_sha256,
        )
        fb = transforms_mod.filterBank(
            self.bands,
            self.fs,
            filtAllowance=self.filt_allowance,
            axis=-1,
            filtType=self.filt_type,
        )
        X = np.asarray(X, dtype=np.float32)
        out = np.empty((*X.shape, len(self.bands)), dtype=np.float32)
        chunk = int(self.config.get("filter_chunk_trials", 128))
        for start in range(0, len(X), chunk):
            stop = min(len(X), start + chunk)
            block = X[start:stop]
            for band_index, band in enumerate(self.bands):
                filtered = fb.bandpassFilter(
                    block,
                    list(band),
                    self.fs,
                    self.filt_allowance,
                    axis=-1,
                    filtType=self.filt_type,
                )
                out[start:stop, :, :, band_index] = np.asarray(
                    filtered, dtype=np.float32
                )
        # Original FBCNet contract: batch x 1 x channel x time x filterBand.
        out = out[:, None, :, :, :]
        return _cache_put(token, out, self.cache_max_gib)

    def _build_model(self, n_chans, n_times):
        if int(n_times) % int(self.config.get("stride_factor", 4)) != 0:
            raise RuntimeError(
                f"INPUT_INCOMPATIBLE:FBCNET_STRIDE_FACTOR:{n_times}"
            )
        mod = _load_source_module(
            "_iharq_fbcnet_original_networks_" + self.network_source_sha256[:12],
            self.network_source_path,
            self.network_source_sha256,
        )
        _seed_everything(self.seed)
        model = mod.FBCNet(
            nChan=int(n_chans),
            nTime=int(n_times),
            nClass=2,
            nBands=len(self.bands),
            m=int(self.config.get("m", 32)),
            temporalLayer=str(self.config.get("temporal_layer", "LogVarLayer")),
            strideFactor=int(self.config.get("stride_factor", 4)),
            doWeightNorm=bool(self.config.get("do_weight_norm", True)),
        )
        return model


class IHARQDBConformerOriginalAuthorAdapter(_GovernedTorchExternalAdapter):
    score_type = "SOFTMAX_PROBABILITY"
    resolved_variant = "DBConformer-OriginalAuthor-P01CompatibilityPatched"

    def __init__(self, checkpoint_path, config):
        super().__init__(checkpoint_path, config)
        self.source_path = str(self.config["patched_source_path"])
        self.source_sha256 = str(self.config["patched_source_sha256"])
        _require_file(self.source_path, self.source_sha256)

    def _prepare(self, X):
        # Official model forward contract is B x 1 x C x T.
        return np.asarray(X, dtype=np.float32)[:, None, :, :]

    def _build_model(self, n_chans, n_times):
        mod = _load_source_module(
            "_iharq_dbconformer_p01_compat_" + self.source_sha256[:12],
            self.source_path,
            self.source_sha256,
        )
        _seed_everything(self.seed)
        args = SimpleNamespace(
            data_name="IHARQ_P01_CORE_CANONICAL_480_NO_ENDPOINT_TRIM",
            chn=int(n_chans),
            class_num=2,
            time_sample_num=int(n_times),
            patch_size=int(self.config.get("patch_size", 125)),
            spa_dim=int(self.config.get("spa_dim", 16)),
            gate_flag=bool(self.config.get("gate_flag", False)),
            posemb_flag=bool(self.config.get("posemb_flag", True)),
            branch=str(self.config.get("branch", "all")),
            chn_atten_flag=bool(self.config.get("chn_atten_flag", True)),
        )
        model = mod.DBConformer(
            args,
            emb_size=int(self.config.get("emb_size", 40)),
            tem_depth=int(self.config.get("transformer_depth_tem", 2)),
            chn_depth=int(self.config.get("transformer_depth_chn", 2)),
            chn=int(n_chans),
            n_classes=2,
        )
        return model

    def _forward_logits(self, xb):
        z = self.model(xb)
        if not isinstance(z, (tuple, list)) or len(z) < 2:
            raise RuntimeError("INPUT_INCOMPATIBLE:DBCONFORMER_FORWARD_CONTRACT")
        return z[1]


class IHARQCBraModGovernedAdapter(_GovernedTorchExternalAdapter):
    score_type = "SOFTMAX_PROBABILITY"
    resolved_variant = "CBraMod-HF-Braindecode-GovernedP02"

    def __init__(self, checkpoint_path, config):
        super().__init__(checkpoint_path, config)
        self.src_hz = int(self.config.get("source_sampling_hz", 160))
        self.dst_hz = int(self.config.get("target_sampling_hz", 200))
        self.patch_size = int(self.config.get("patch_size", 200))
        self.cache_max_gib = float(self.config.get("preparation_cache_max_gib", 10.0))
        if self.checkpoint_path is None:
            raise RuntimeError("CHECKPOINT_BLOCKED:CBRAMOD_CHECKPOINT_PATH_MISSING")
        expected = self.config.get("checkpoint_sha256")
        _require_file(self.checkpoint_path, expected)
        local = self.config.get("pretrained_local_dir")
        if not local or not Path(local).is_dir():
            raise RuntimeError("CHECKPOINT_BLOCKED:CBRAMOD_LOCAL_SNAPSHOT_MISSING")

    def _prepare(self, X):
        from scipy.signal import resample_poly

        token = _array_token(X, "CBRAMOD_RESAMPLE_160_200_V1")
        cached = _cache_get(token)
        if cached is not None:
            return cached
        X = np.asarray(X, dtype=np.float32)
        if self.src_hz == self.dst_hz:
            out = X
        else:
            g = math.gcd(self.src_hz, self.dst_hz)
            out = resample_poly(
                X,
                self.dst_hz // g,
                self.src_hz // g,
                axis=-1,
            ).astype(np.float32)
        if bool(self.config.get("strict_patch_alignment", True)):
            if int(out.shape[-1]) % self.patch_size != 0:
                raise RuntimeError(
                    f"INPUT_INCOMPATIBLE:CBRAMOD_PATCH_ALIGNMENT:"
                    f"{out.shape[-1]}%{self.patch_size}"
                )
        return _cache_put(token, out, self.cache_max_gib)

    def _build_model(self, n_chans, n_times):
        from braindecode.models import CBraMod

        _seed_everything(self.seed)
        resampled_times = int(round(int(n_times) * self.dst_hz / self.src_hz))
        if resampled_times % self.patch_size != 0:
            raise RuntimeError(
                f"INPUT_INCOMPATIBLE:CBRAMOD_PATCH_ALIGNMENT:"
                f"{resampled_times}%{self.patch_size}"
            )
        local = str(self.config["pretrained_local_dir"])
        try:
            return CBraMod.from_pretrained(
                local,
                n_outputs=2,
                n_chans=int(n_chans),
                n_times=resampled_times,
                sfreq=float(self.dst_hz),
            )
        except Exception as exc:
            raise RuntimeError(
                f"CHECKPOINT_BLOCKED:CBRAMOD_PRETRAINED_LOAD:"
                f"{type(exc).__name__}:{str(exc)[:180]}"
            ) from exc

    def _forward_logits(self, xb):
        z = self.model(xb)
        if isinstance(z, (tuple, list)):
            z = z[0]
        return z


def build_iharq_adapter(branch_id, checkpoint_path, config):
    config = dict(config or {})
    kind = str(config.get("adapter_kind", ""))

    if branch_id == "DNN-FBCNET" or kind == "FBCNET_ORIGINAL_AUTHOR_P01":
        return IHARQFBCNetOriginalAuthorAdapter(checkpoint_path, config)

    if branch_id == "DNN-SEQ" or kind == "DBCONFORMER_ORIGINAL_AUTHOR_P01":
        return IHARQDBConformerOriginalAuthorAdapter(checkpoint_path, config)

    if branch_id == "SSL-CBRAMOD" or kind == "CBRAMOD_GOVERNED_P02":
        return IHARQCBraModGovernedAdapter(checkpoint_path, config)

    raise RuntimeError(f"ADAPTER_BRANCH_MISMATCH:{branch_id}:{kind}")
