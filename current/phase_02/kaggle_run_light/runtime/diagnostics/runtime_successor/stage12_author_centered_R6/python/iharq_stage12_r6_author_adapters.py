
from __future__ import annotations

import gc
import math
import numpy as np

import iharq_stage12_external_adapters as base


class _R6AuthorTrainingMixin:
    supports_class_weights = True

    def _r6_recipe(self):
        r = dict(self.config.get("r6_recipe") or {})
        if not r:
            raise RuntimeError("R6_RECIPE_MISSING")
        return r

    def _checkpoint_metadata(self):
        d = super()._checkpoint_metadata()
        d["r6_author_centered"] = {
            "recipe": self._r6_recipe(),
            "max_epochs_policy": int(self.config.get("r6_max_epochs", 150)),
            "patience_policy": int(self.config.get("r6_patience", 40)),
            "min_delta_policy": float(self.config.get("r6_min_delta", 0.0)),
            "best_epoch": getattr(self, "best_epoch", None),
            "training_epochs_completed": int(getattr(self, "training_epochs_completed", 0)),
            "best_validation_bacc": getattr(self, "best_validation_bacc", None),
            "training_history": list(getattr(self, "training_history", [])),
        }
        return d

    def _build_optimizer(self, model, recipe, total_steps):
        import torch

        name = str(recipe["optimizer"])
        scheduler = None

        if name == "Adam":
            opt = torch.optim.Adam(
                model.parameters(),
                lr=float(recipe["lr"]),
                weight_decay=float(recipe.get("weight_decay", 0.0)),
            )

        elif name == "AdamW":
            if "body_lr" in recipe and "head_lr" in recipe:
                body, head = [], []
                for n, p in model.named_parameters():
                    if not p.requires_grad:
                        continue
                    nl = str(n).lower()
                    is_head = (
                        "final_layer" in nl
                        or "classifier" in nl
                        or nl.endswith(".head.weight")
                        or nl.endswith(".head.bias")
                        or ".head." in nl
                    )
                    (head if is_head else body).append(p)
                if not body or not head:
                    raise RuntimeError(
                        f"R6_CBRAMOD_PARAMETER_GROUP_RESOLUTION_FAILED:"
                        f"body={len(body)}:head={len(head)}"
                    )
                opt = torch.optim.AdamW(
                    [
                        {"params": body, "lr": float(recipe["body_lr"])},
                        {"params": head, "lr": float(recipe["head_lr"])},
                    ],
                    weight_decay=float(recipe.get("weight_decay", 0.0)),
                )
            else:
                opt = torch.optim.AdamW(
                    model.parameters(),
                    lr=float(recipe["lr"]),
                    weight_decay=float(recipe.get("weight_decay", 0.0)),
                )
        else:
            raise RuntimeError(f"R6_UNSUPPORTED_OPTIMIZER:{name}")

        if str(recipe.get("scheduler", "constant")) == "cosine":
            scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                opt,
                T_max=max(1, int(total_steps)),
                eta_min=float(recipe.get("eta_min", 1e-6)),
            )
        elif str(recipe.get("scheduler", "constant")) != "constant":
            raise RuntimeError(
                f"R6_UNSUPPORTED_SCHEDULER:{recipe.get('scheduler')}"
            )
        return opt, scheduler

    def fit(
        self,
        X,
        y,
        epochs=150,
        lr=1e-3,
        weight_decay=0.0,
        batch_size=64,
        effective_batch_target=64,
        device="cpu",
        X_val=None,
        y_val=None,
        patience=40,
        min_delta=0.0,
        restore_best=True,
        class_weights=None,
        augmentation_policy=None,
        augmentation_context=None,
        **kw,
    ):
        import torch
        from sklearn.metrics import balanced_accuracy_score
        from torch.utils.data import DataLoader, TensorDataset

        recipe = self._r6_recipe()
        smoke = bool(self.config.get("r6_smoke_mode", False))

        if not smoke:
            # Production Stage12 must exactly use the R6 policy. The generic
            # dispatcher values are checked rather than silently ignored.
            if int(epochs) != int(self.config.get("r6_max_epochs", 150)):
                raise RuntimeError(
                    f"R6_MAX_EPOCH_POLICY_MISMATCH:{epochs}:"
                    f"{self.config.get('r6_max_epochs')}"
                )
            if int(patience) != int(self.config.get("r6_patience", 40)):
                raise RuntimeError(
                    f"R6_PATIENCE_POLICY_MISMATCH:{patience}:"
                    f"{self.config.get('r6_patience')}"
                )
            if float(min_delta) != float(self.config.get("r6_min_delta", 0.0)):
                raise RuntimeError("R6_MIN_DELTA_POLICY_MISMATCH")
            if restore_best is not True:
                raise RuntimeError("R6_RESTORE_BEST_REQUIRED")

        # Source-author recipe is authoritative for these branch-local choices.
        scientific_batch = int(recipe["batch_size"])
        scientific_epochs = int(epochs)
        scientific_patience = int(patience)

        if class_weights is not None:
            cw = np.asarray(class_weights, dtype=float).reshape(-1)
            if cw.shape != (2,) or not np.allclose(cw, np.ones(2), atol=1e-12):
                raise RuntimeError(
                    "R6_AUTHOR_RECIPE_REQUIRES_UNIFORM_CLASS_WEIGHTS"
                )
        if augmentation_policy not in (None, {}, "NONE"):
            raise RuntimeError("R6_PRIMARY_AUGMENTATION_MUST_REMAIN_NONE")
        # An inert augmentation_context may be carried as provenance by the
        # dispatcher; it is not applied when augmentation_policy is NONE.

        base._seed_everything(self.seed)
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        Xraw = np.asarray(X, dtype=np.float32)
        y = np.asarray(y, dtype=np.int64)
        if Xraw.ndim != 3 or len(Xraw) != len(y):
            raise RuntimeError("INPUT_INCOMPATIBLE:R6_X_Y_SHAPE")
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
        self.actual_batch_size = scientific_batch
        self.gradient_accumulation = 1

        use_dp = (
            bool(recipe.get("use_data_parallel", False))
            and torch.cuda.is_available()
            and torch.cuda.device_count() >= 2
            and str(device).startswith("cuda")
            and len(Xp) >= int(recipe.get("data_parallel_min_samples", 256))
        )
        if use_dp:
            max_gpus = min(
                int(recipe.get("data_parallel_max_gpus", 2)),
                torch.cuda.device_count(),
            )
            device_ids = list(range(max_gpus))
            self.model = torch.nn.DataParallel(self.model, device_ids=device_ids)
            self.resource_events.append({
                "type": "R6_DATA_PARALLEL_SAME_GLOBAL_BATCH",
                "device_ids": device_ids,
                "global_batch_size": scientific_batch,
                "scientific_batch_changed": False,
                "numerical_execution_path_changed": True,
            })

        loss_fn = torch.nn.CrossEntropyLoss(
            label_smoothing=float(recipe.get("label_smoothing", 0.0))
        )

        data_tensor = torch.from_numpy(np.asarray(Xp, dtype=np.float32))
        y_tensor = torch.from_numpy(y.astype(np.int64, copy=False))
        loader_steps = max(1, int(math.ceil(len(y_tensor) / scientific_batch)))
        total_steps = max(1, scientific_epochs * loader_steps)
        opt, scheduler = self._build_optimizer(self.model, recipe, total_steps)

        best = -np.inf
        best_epoch = 0
        best_state = None
        bad = 0
        self.training_epochs_completed = 0
        self.training_history = []

        try:
            for epoch in range(scientific_epochs):
                gen = torch.Generator()
                gen.manual_seed(int(self.seed) + int(epoch))
                loader = DataLoader(
                    TensorDataset(data_tensor, y_tensor),
                    batch_size=scientific_batch,
                    shuffle=True,
                    generator=gen,
                    num_workers=0,
                    pin_memory=bool(torch.cuda.is_available()),
                    drop_last=False,
                )

                self.model.train()
                epoch_loss = 0.0
                epoch_n = 0

                for xb, yb in loader:
                    xb = xb.to(device, non_blocking=bool(torch.cuda.is_available()))
                    yb = yb.to(device, non_blocking=bool(torch.cuda.is_available()))
                    opt.zero_grad(set_to_none=True)
                    logits = self._forward_logits(xb)
                    loss = loss_fn(logits, yb)
                    if not torch.isfinite(loss):
                        raise RuntimeError("R6_NONFINITE_TRAINING_LOSS")
                    loss.backward()

                    clip = recipe.get("grad_clip")
                    if clip is not None:
                        torch.nn.utils.clip_grad_norm_(
                            self.model.parameters(), float(clip)
                        )
                    opt.step()
                    if scheduler is not None:
                        scheduler.step()

                    bs = int(yb.shape[0])
                    epoch_loss += float(loss.detach().cpu().item()) * bs
                    epoch_n += bs

                self.training_epochs_completed += 1

                val_bacc = None
                if Xvp is not None:
                    scores = self._predict_scores_prepared(Xvp, device=device)
                    pred = np.argmax(scores, axis=1)
                    val_bacc = float(
                        balanced_accuracy_score(
                            np.asarray(y_val, dtype=np.int64), pred
                        )
                    )

                    if val_bacc > best + float(min_delta):
                        best = val_bacc
                        best_epoch = epoch + 1
                        bad = 0
                        best_state = {
                            k: v.detach().cpu().clone()
                            for k, v in self.model.state_dict().items()
                        }
                    else:
                        bad += 1

                self.training_history.append({
                    "epoch": epoch + 1,
                    "train_loss": float(epoch_loss / max(1, epoch_n)),
                    "validation_BACC": val_bacc,
                    "bad_epochs": int(bad),
                    "lr_groups": [float(pg["lr"]) for pg in opt.param_groups],
                })

                if Xvp is not None and bad >= scientific_patience:
                    break

        except RuntimeError as exc:
            if base._is_oom(exc):
                self.resource_events.append({
                    "type": "CUDA_OOM",
                    "scientific_batch_size": scientific_batch,
                    "message": str(exc)[:240],
                })
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                raise ResourceWarning(
                    f"CUDA_OOM_AT_R6_AUTHOR_BATCH:{scientific_batch}"
                ) from exc
            raise

        if restore_best and best_state is not None:
            self.model.load_state_dict(best_state, strict=True)

        if isinstance(self.model, torch.nn.DataParallel):
            self.model = self.model.module

        self.model.eval()
        self.best_validation_bacc = None if best == -np.inf else float(best)
        self.best_epoch = int(best_epoch)
        self.resource_events.append({
            "type": "R6_AUTHOR_CENTERED_TRAINING",
            "recipe_id": recipe.get("recipe_id"),
            "epochs_completed": int(self.training_epochs_completed),
            "best_epoch": int(self.best_epoch),
            "best_validation_BACC": self.best_validation_bacc,
            "patience": scientific_patience,
            "max_epochs": scientific_epochs,
            "global_batch_size": scientific_batch,
            "gradient_accumulation": 1,
            "class_weights": None,
            "augmentation": "NONE",
        })
        return self


class R6FBCNetAdapter(
    _R6AuthorTrainingMixin,
    base.IHARQFBCNetOriginalAuthorAdapter,
):
    resolved_variant = (
        "FBCNet-OriginalAuthor-P01ConstrainedFilterBank-R6AuthorCentered"
    )


class R6DBConformerAdapter(
    _R6AuthorTrainingMixin,
    base.IHARQDBConformerOriginalAuthorAdapter,
):
    resolved_variant = (
        "DBConformer-OriginalAuthor-P01CompatibilityPatched-R6AuthorCentered"
    )


class R6CBraModAdapter(
    _R6AuthorTrainingMixin,
    base.IHARQCBraModGovernedAdapter,
):
    resolved_variant = (
        "CBraMod-HF-Braindecode-GovernedP02-R6Scale1e4AuthorCentered"
    )

    def _prepare(self, X):
        from scipy.signal import resample_poly

        scale = float(self.config.get("r6_input_scale", 1e4))
        token = base._array_token(
            X,
            f"CBRAMOD_R6_SCALE_{scale:g}_RESAMPLE_{self.src_hz}_{self.dst_hz}_V1",
        )
        cached = base._cache_get(token)
        if cached is not None:
            return cached

        # P01 remains bytes-in-volts. Scaling is model-local only.
        a = np.asarray(X, dtype=np.float32)
        out = (a * np.float32(scale)).astype(np.float32, copy=False)

        if self.src_hz != self.dst_hz:
            g = math.gcd(self.src_hz, self.dst_hz)
            out = resample_poly(
                out,
                self.dst_hz // g,
                self.src_hz // g,
                axis=-1,
            ).astype(np.float32)

        if bool(self.config.get("strict_patch_alignment", True)):
            if int(out.shape[-1]) % int(self.patch_size) != 0:
                raise RuntimeError(
                    f"INPUT_INCOMPATIBLE:CBRAMOD_PATCH_ALIGNMENT:"
                    f"{out.shape[-1]}%{self.patch_size}"
                )

        return base._cache_put(token, out, self.cache_max_gib)


def build_r6_adapter(branch_id, checkpoint_path, config):
    cfg = dict(config or {})
    if branch_id == "DNN-FBCNET":
        return R6FBCNetAdapter(checkpoint_path, cfg)
    if branch_id == "DNN-SEQ":
        return R6DBConformerAdapter(checkpoint_path, cfg)
    if branch_id == "SSL-CBRAMOD":
        return R6CBraModAdapter(checkpoint_path, cfg)
    raise RuntimeError(f"R6_ADAPTER_BRANCH_MISMATCH:{branch_id}")
