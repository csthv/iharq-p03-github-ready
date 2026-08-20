"""P03-owned CALIBRATION/VALIDATION score materialization from accepted P02 checkpoints.

This module implements the governed P03 correction required because accepted P02
PredictionRecord partitions are final-test-only.  It never retrains or mutates P02.
It replays accepted P02 checkpoints on frozen P01 CALIBRATION and VALIDATION windows,
excludes exact low-label training memberships from calibrator-fit populations, and
returns label-free score artifacts plus protected truth-join metadata for Stage 07.
"""
from __future__ import annotations

import gc
import hashlib
import importlib.util
import io
import json
import pickle
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

import numpy as np

from .identity import sha256_file, sha256_json

LOW_BUDGET_RE = re.compile(r":(1|2|4|8|16|32)_PER_CLASS$")
ELIGIBLE_REPLAY_SCORE_TYPES = {"NATIVE_PROBABILITY", "SOFTMAX_PROBABILITY"}
SEMANTIC_DIAGNOSTIC_TYPES = {"TRAIN_PRIOR_PROBABILITY", "DISTANCE_DERIVED_SIMPLEX", "HARD_LABEL_ONLY"}
_EEGNET_STATS_CACHE: dict[tuple[str, str], dict[str, Any]] = {}
_SNAPSHOT_MANIFEST_CACHE: dict[str, tuple[dict[str, dict[str, Any]], dict[str, list[dict[str, Any]]]]] = {}
_EXTERNAL_ADAPTER_CACHE: dict[str, Any] = {}


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _dataset_budget_from_registry_path(path: Path) -> tuple[str, str]:
    dataset = next((part.split("=", 1)[1] for part in path.parts if part.startswith("dataset=")), None)
    budget = next((part.split("=", 1)[1] for part in path.parts if part.startswith("budget=")), None)
    if not dataset or not budget:
        raise RuntimeError(f"P02_MODEL_REGISTRY_PARTITION_KEYS_MISSING:{path}")
    return dataset, budget


def eligible_replay_models(
    runtime_root: str | Path,
    *,
    expected_config_sha256: str,
    expected_count: int,
    expected_population_sha256: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Return the exact claim-bearing A0 replay population and verify its frozen fingerprint."""
    runtime_root = Path(runtime_root)
    diagnostic_rows = _read_jsonl(runtime_root / "records/DiagnosticOnlyFlag/diagnostics.jsonl")
    diagnostic_ids = {
        str(source_id)
        for row in diagnostic_rows
        for source_id in row.get("source_ids", [])
    }
    models: list[dict[str, Any]] = []
    terminal_counts: Counter[str] = Counter()
    score_counts: Counter[str] = Counter()
    family_counts: Counter[str] = Counter()
    for path in sorted((runtime_root / "records/ModelRegistryRecord").rglob("*.jsonl")):
        dataset_id, budget_id = _dataset_budget_from_registry_path(path)
        for row in _read_jsonl(path):
            source_ids = [str(value) for value in row.get("source_ids", [])]
            run_cell_id = source_ids[0] if source_ids else ""
            if not run_cell_id.startswith("P02-A0-"):
                continue
            terminal_counts[str(row.get("terminal_status"))] += 1
            if row.get("terminal_status") != "SUCCESS" or row.get("admission_status") != "SUCCESS":
                continue
            if row.get("config_sha256") != expected_config_sha256 or row.get("evidence_class") != "P02_EXECUTION_EVIDENCE":
                raise RuntimeError(f"P02_REPLAY_MODEL_IDENTITY_MISMATCH:{row.get('record_id')}")
            score_type = str(row.get("score_type"))
            if run_cell_id in diagnostic_ids or score_type in SEMANTIC_DIAGNOSTIC_TYPES:
                continue
            if score_type not in ELIGIBLE_REPLAY_SCORE_TYPES:
                raise RuntimeError(f"P02_REPLAY_UNMAPPED_SCORE_TYPE:{run_cell_id}:{score_type}")
            class_order = list(row.get("class_order") or [])
            if class_order != ["left_hand", "right_hand"]:
                raise RuntimeError(f"P02_REPLAY_CLASS_ORDER_MISMATCH:{run_cell_id}:{class_order}")
            item = dict(row)
            item.update({
                "p03_dataset_id": dataset_id,
                "p03_budget_id": budget_id,
                "p03_run_cell_id": run_cell_id,
            })
            models.append(item)
            score_counts[score_type] += 1
            family_counts[str(row.get("family_role"))] += 1
    models.sort(key=lambda row: row["p03_run_cell_id"])
    normalized = [
        {
            "run_cell_id": row["p03_run_cell_id"],
            "dataset_id": row["p03_dataset_id"],
            "budget_id": row["p03_budget_id"],
            "model_id": str(row["model_id"]),
            "checkpoint_sha256": str(row["checkpoint_sha256"]),
            "score_type": str(row["score_type"]),
            "class_order": list(row["class_order"]),
            "family_role": str(row["family_role"]),
        }
        for row in models
    ]
    population_sha = hashlib.sha256(
        json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    if len(models) != int(expected_count):
        raise RuntimeError(f"P02_REPLAY_POPULATION_COUNT_MISMATCH:expected={expected_count}:observed={len(models)}")
    if population_sha != str(expected_population_sha256):
        raise RuntimeError(f"P02_REPLAY_POPULATION_HASH_MISMATCH:expected={expected_population_sha256}:observed={population_sha}")
    if len({str(row["checkpoint_sha256"]) for row in models}) != len(models):
        raise RuntimeError("P02_REPLAY_CHECKPOINT_UNIQUENESS_FAILED")
    return models, {
        "expected_count": int(expected_count),
        "observed_count": len(models),
        "population_sha256": population_sha,
        "score_type_counts": dict(sorted(score_counts.items())),
        "family_counts": dict(sorted(family_counts.items())),
        "diagnostic_source_id_count": len(diagnostic_ids),
        "a0_terminal_counts": dict(sorted(terminal_counts.items())),
    }


def select_replay_snapshot_rows(
    manifest_rows: Sequence[Mapping[str, Any]],
    models: Sequence[Mapping[str, Any]],
    replay_config: Mapping[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Select exact P01 core, run-cell, checkpoint, and accepted external-source objects."""
    by_path = {str(row["path"]): dict(row) for row in manifest_rows}
    checkpoint_prefix = str(replay_config["checkpoint_prefix"])
    run_cell_prefix = str(replay_config["run_cell_prefix"])
    p01_prefix = str(replay_config["p01_core_prefix"])
    external_prefix = str(replay_config["external_source_prefix"])
    cbramod_prefix = str(replay_config["cbramod_asset_prefix"])
    cbramod_patch_prefix = str(replay_config["cbramod_adapter_patch_prefix"])

    p01_rows = [row for path, row in by_path.items() if path.startswith(p01_prefix)]
    external_rows = [row for path, row in by_path.items() if path.startswith(external_prefix)]
    cbramod_rows = [row for path, row in by_path.items() if path.startswith(cbramod_prefix)]
    cbramod_patch_rows = [
        row for path, row in by_path.items()
        if path.startswith(cbramod_patch_prefix)
        and str(row["sha256"]) == str(replay_config["cbramod_adapter_patch_sha256"])
    ]
    if len(p01_rows) != int(replay_config["p01_core_file_count"]):
        raise RuntimeError(f"P03_REPLAY_P01_CORE_CARDINALITY:expected={replay_config['p01_core_file_count']}:observed={len(p01_rows)}")
    if len(external_rows) != int(replay_config["external_source_file_count"]):
        raise RuntimeError(f"P03_REPLAY_EXTERNAL_SOURCE_CARDINALITY:expected={replay_config['external_source_file_count']}:observed={len(external_rows)}")
    if len(cbramod_rows) != int(replay_config["cbramod_asset_file_count"]):
        raise RuntimeError(f"P03_REPLAY_CBRAMOD_ASSET_CARDINALITY:expected={replay_config['cbramod_asset_file_count']}:observed={len(cbramod_rows)}")
    if len(cbramod_patch_rows) != int(replay_config["cbramod_adapter_patch_file_count"]):
        raise RuntimeError(
            f"P03_REPLAY_CBRAMOD_ADAPTER_PATCH_CARDINALITY:"
            f"expected={replay_config['cbramod_adapter_patch_file_count']}:"
            f"observed={len(cbramod_patch_rows)}"
        )

    checkpoint_by_sha: dict[str, list[dict[str, Any]]] = {}
    for path, row in by_path.items():
        if path.startswith(checkpoint_prefix):
            checkpoint_by_sha.setdefault(str(row["sha256"]), []).append(row)

    selected: dict[str, dict[str, Any]] = {}
    for row in p01_rows + external_rows + cbramod_rows + cbramod_patch_rows:
        selected[str(row["path"])] = row
    for model in models:
        run_cell_id = str(model["p03_run_cell_id"])
        run_path = f"{run_cell_prefix}{run_cell_id}.json"
        if run_path not in by_path:
            raise RuntimeError(f"P03_REPLAY_RUN_CELL_NOT_IN_SNAPSHOT:{run_cell_id}")
        selected[run_path] = by_path[run_path]
        checkpoint_sha = str(model["checkpoint_sha256"])
        matches = checkpoint_by_sha.get(checkpoint_sha, [])
        if len(matches) != 1:
            raise RuntimeError(f"P03_REPLAY_CHECKPOINT_RESOLUTION:{run_cell_id}:matches={len(matches)}")
        selected[str(matches[0]["path"])] = matches[0]

    adapter_matches = [row for row in external_rows if str(row["path"]).endswith("iharq_stage12_external_adapters.py")]
    if len(adapter_matches) != 1 or str(adapter_matches[0]["sha256"]) != str(replay_config["external_adapter_sha256"]):
        raise RuntimeError("P03_REPLAY_EXTERNAL_ADAPTER_IDENTITY_MISMATCH")
    cbramod_matches = [row for row in cbramod_rows if str(row["path"]).endswith("model.safetensors")]
    if len(cbramod_matches) != 1 or str(cbramod_matches[0]["sha256"]) != str(replay_config["cbramod_asset_sha256"]):
        raise RuntimeError("P03_REPLAY_CBRAMOD_ASSET_IDENTITY_MISMATCH")
    if (
        len(cbramod_patch_rows) != 1
        or str(cbramod_patch_rows[0]["sha256"]) != str(replay_config["cbramod_adapter_patch_sha256"])
    ):
        raise RuntimeError("P03_REPLAY_CBRAMOD_ADAPTER_PATCH_IDENTITY_MISMATCH")

    rows = [selected[path] for path in sorted(selected)]
    return rows, {
        "selected_object_count": len(rows),
        "selected_bytes": sum(int(row["bytes"]) for row in rows),
        "p01_core_file_count": len(p01_rows),
        "run_cell_count": len(models),
        "checkpoint_count": len({str(row["checkpoint_sha256"]) for row in models}),
        "external_source_file_count": len(external_rows),
        "cbramod_asset_file_count": len(cbramod_rows),
        "cbramod_adapter_patch_file_count": len(cbramod_patch_rows),
        "cbramod_adapter_patch_sha256": str(replay_config["cbramod_adapter_patch_sha256"]),
    }


def _snapshot_manifest(snapshot_root: Path, manifest_path: str) -> tuple[dict[str, dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    key = f"{snapshot_root.resolve()}::{manifest_path}"
    cached = _SNAPSHOT_MANIFEST_CACHE.get(key)
    if cached is not None:
        return cached
    by_path: dict[str, dict[str, Any]] = {}
    by_sha: dict[str, list[dict[str, Any]]] = {}
    path = snapshot_root / manifest_path
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            row = {"path": str(row["path"]), "bytes": int(row["bytes"]), "sha256": str(row["sha256"])}
            by_path[row["path"]] = row
            by_sha.setdefault(row["sha256"], []).append(row)
    _SNAPSHOT_MANIFEST_CACHE[key] = (by_path, by_sha)
    return by_path, by_sha


def _resolve_by_sha(snapshot_root: Path, manifest_path: str, sha256: str, *, prefer_prefix: str | None = None) -> Path:
    _, by_sha = _snapshot_manifest(snapshot_root, manifest_path)
    rows = list(by_sha.get(str(sha256), []))
    if prefer_prefix:
        preferred = [row for row in rows if str(row["path"]).startswith(prefer_prefix)]
        if preferred:
            rows = preferred
    existing = []
    for row in rows:
        p = snapshot_root / str(row["path"])
        if p.is_file():
            existing.append((p, row))
    if len(existing) != 1:
        raise RuntimeError(f"P03_REPLAY_SHA_RESOLUTION_FAILED:{sha256}:matches={len(existing)}")
    p, row = existing[0]
    if p.stat().st_size != int(row["bytes"]) or sha256_file(p) != str(row["sha256"]):
        raise RuntimeError(f"P03_REPLAY_SHA_INTEGRITY_FAILED:{p}")
    return p


def _run_cell(snapshot_root: Path, runtime_root_rel: str, run_cell_id: str) -> dict[str, Any]:
    path = snapshot_root / runtime_root_rel / "run_cells" / f"{run_cell_id}.json"
    if not path.is_file():
        raise RuntimeError(f"P02_RUN_CELL_NOT_FOUND:{run_cell_id}")
    row = json.loads(path.read_text(encoding="utf-8"))
    if str(row.get("run_cell_id")) != run_cell_id:
        raise RuntimeError(f"P02_RUN_CELL_IDENTITY_MISMATCH:{run_cell_id}")
    return row


def parse_budget_n(budget_id: str) -> int | None:
    if budget_id == "FULL_TRAIN":
        return None
    match = LOW_BUDGET_RE.search(str(budget_id))
    if not match:
        raise RuntimeError(f"UNKNOWN_BUDGET_ID:{budget_id}")
    return int(match.group(1))


def low_label_training_event_ids(core: Any, dataset_id: str, budget_id: str, seed: int = 20260804) -> set[str]:
    from iharq.layer2_decoders.data import frozen_budget_memberships
    n = parse_budget_n(budget_id)
    if n is None:
        return set()
    key = f"{dataset_id}:budget-{n}-seed-{seed}"
    return set(frozen_budget_memberships(core, [n], seed)[key])


def calibration_rows(core: Any, dataset_id: str, budget_id: str, seed: int = 20260804) -> tuple[list[dict[str, Any]], set[str]]:
    rows = list(core.rows(dataset_id=dataset_id, role="calibration"))
    excluded = low_label_training_event_ids(core, dataset_id, budget_id, seed)
    kept = [row for row in rows if str(row.get("event_id")) not in excluded]
    if not kept:
        raise RuntimeError(f"P03_CALIBRATION_POOL_EMPTY:{dataset_id}:{budget_id}")
    return kept, excluded


def validation_rows(core: Any, dataset_id: str) -> list[dict[str, Any]]:
    rows = list(core.rows(dataset_id=dataset_id, role="validation"))
    if not rows:
        raise RuntimeError(f"P03_VALIDATION_POOL_EMPTY:{dataset_id}")
    return rows


def _load_torch_weights(path: Path) -> Any:
    import torch
    raw = Path(path).read_bytes()
    try:
        return torch.load(io.BytesIO(raw), map_location="cpu", weights_only=True)
    except TypeError:
        return torch.load(io.BytesIO(raw), map_location="cpu")


class _P02EEGNetP01InputWrapper:
    """Factory namespace for the exact accepted P02 EEGNet wrapper contract.

    The accepted P02 checkpoint is a state_dict of a wrapper, not the bare
    Braindecode EEGNet.  The wrapper owns the fitted model-local normalization
    buffers, so P03 must restore those exact checkpointed buffers instead of
    recomputing them from P01.
    """

    @staticmethod
    def build(base_model: Any, n_chans: int, *, unit_multiplier: float = 1.0e6, eps_uv: float = 1.0e-6):
        import torch

        class _Wrapper(torch.nn.Module):
            def __init__(self):
                super().__init__()
                self.base_model = base_model
                self.n_chans = int(n_chans)
                self.eps_uv = float(eps_uv)
                self.register_buffer(
                    "iharq_unit_multiplier",
                    torch.tensor(float(unit_multiplier), dtype=torch.float32),
                )
                self.register_buffer(
                    "iharq_channel_mean_uv",
                    torch.zeros(1, self.n_chans, 1, dtype=torch.float32),
                )
                self.register_buffer(
                    "iharq_channel_std_uv",
                    torch.ones(1, self.n_chans, 1, dtype=torch.float32),
                )

            def forward(self, x):
                x = x * self.iharq_unit_multiplier
                x = (x - self.iharq_channel_mean_uv) / self.iharq_channel_std_uv
                return self.base_model(x)

        return _Wrapper()


def _build_eegnet(model_row: Mapping[str, Any], run_cell: Mapping[str, Any], n_chans: int, n_times: int):
    import inspect
    import torch
    from braindecode.models import EEGNet

    params = dict(run_cell.get("selected_params") or {})
    kwargs = {
        "n_chans": int(n_chans),
        "n_outputs": 2,
        "n_times": int(n_times),
        "sfreq": 160.0,
        "F1": 8,
        "D": 2,
        "F2": 16,
        "kernel_length": int(params.get("kernel_length", 40)),
        "depthwise_kernel_length": int(params.get("depthwise_kernel_length", 20)),
        "pool1_kernel_size": int(params.get("pool1_kernel_size", 5)),
        "pool2_kernel_size": int(params.get("pool2_kernel_size", 10)),
        "pool_mode": "mean",
        "drop_prob": float(params.get("dropout", 0.5)),
        "conv_spatial_max_norm": 1.0,
        "final_layer_with_constraint": True,
        "norm_rate": 0.25,
    }
    signature = inspect.signature(EEGNet)
    kwargs = {key: value for key, value in kwargs.items() if key in signature.parameters}
    torch.manual_seed(int(model_row["model_seed"]))
    base = EEGNet(**kwargs).cpu()
    return _P02EEGNetP01InputWrapper.build(base, int(n_chans), unit_multiplier=1.0e6, eps_uv=1.0e-6).cpu()


def recompute_eegnet_normalization(core: Any, dataset_id: str, budget_id: str, seed: int = 20260804) -> dict[str, Any]:
    key = (dataset_id, budget_id)
    if key in _EEGNET_STATS_CACHE:
        return _EEGNET_STATS_CACHE[key]
    if budget_id == "FULL_TRAIN":
        train_rows = list(core.rows(dataset_id=dataset_id, role="train"))
        fit_role = "train"
    else:
        train_ids = low_label_training_event_ids(core, dataset_id, budget_id, seed)
        train_rows = [row for row in core.rows(dataset_id=dataset_id, role="calibration") if str(row.get("event_id")) in train_ids]
        fit_role = "frozen_low_label_training_membership"
    if not train_rows:
        raise RuntimeError(f"P03_EEGNET_NORMALIZATION_POPULATION_EMPTY:{dataset_id}:{budget_id}")
    X, _, _ = core.load_rows(train_rows)
    X = np.asarray(X, np.float32) * 1_000_000.0
    mean = X.mean(axis=(0, 2), keepdims=True)
    std = np.maximum(X.std(axis=(0, 2), keepdims=True), 1e-6)
    stats = {
        "mean": mean, "std": std, "fit_samples": len(train_rows),
        "source_unit": "V", "unit_multiplier": 1_000_000.0, "fit_role": fit_role,
    }
    _EEGNET_STATS_CACHE[key] = stats
    del X
    gc.collect()
    return stats


def _rebind_snapshot_locator(value: str, snapshot_root: Path) -> str:
    """Rebase a P02 machine-local absolute locator onto the immutable P03 snapshot.

    This changes only the runtime locator.  It does not alter checkpoint state,
    scientific configuration, model parameters, or source bytes.
    """
    text = str(value)
    marker = "/kaggle/working/iharq_p02_run/"
    if marker not in text:
        return text
    suffix = text.split(marker, 1)[1]
    candidate = snapshot_root / "iharq_p02_run" / suffix
    if candidate.exists():
        return str(candidate)
    return text


def _rebind_paths_by_sha(obj: Any, snapshot_root: Path, manifest_path: str, stage12_prefix: str) -> Any:
    if isinstance(obj, dict):
        out = dict(obj)
        # First, use exact content hashes whenever a path/hash pair exists.
        for key, value in list(obj.items()):
            if key.endswith("_sha256") and isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value):
                stem = key[:-7]
                path_keys = [
                    stem + "path",
                    stem + "_path",
                    stem + "_file",
                    stem + "_dir",
                    stem + "_manifest",
                ]
                for pkey in path_keys:
                    if pkey in out:
                        try:
                            p = _resolve_by_sha(snapshot_root, manifest_path, value, prefer_prefix=stage12_prefix)
                        except RuntimeError:
                            p = _resolve_by_sha(snapshot_root, manifest_path, value)
                        out[pkey] = str(p)
                        break
        # Then rebase any remaining absolute P02 working-directory locators onto
        # the immutable materialized snapshot when the exact relative object exists.
        for key, value in list(out.items()):
            if isinstance(value, str):
                out[key] = _rebind_snapshot_locator(value, snapshot_root)
            else:
                out[key] = _rebind_paths_by_sha(value, snapshot_root, manifest_path, stage12_prefix)
        return out
    if isinstance(obj, list):
        return [_rebind_paths_by_sha(item, snapshot_root, manifest_path, stage12_prefix) for item in obj]
    if isinstance(obj, str):
        return _rebind_snapshot_locator(obj, snapshot_root)
    return obj


_EXTERNAL_TRANSPORT_LOCATOR_KEYS = {
    "checkpoint_path",
    "pretrained_local_dir",
    "network_source_path",
    "transform_source_path",
    "original_source_path",
    "patched_source_path",
    "compatibility_patch_manifest",
    "r6_adapter_patch_file",
}


def _external_checkpoint_bytes_with_rebound_config(
    payload: Mapping[str, Any],
    rebound_config: Mapping[str, Any],
) -> tuple[bytes, dict[str, Any]]:
    """Create an in-memory transport copy with machine-local locators rebound only.

    This function does not change model tensors or accepted checkpoint bytes on
    disk.  It explicitly compares every checkpoint config field and permits
    differences only in the closed locator vocabulary above.
    """
    import torch

    if not isinstance(payload, Mapping) or "state_dict" not in payload or "metadata" not in payload:
        raise RuntimeError("P03_EXTERNAL_CHECKPOINT_PAYLOAD_CONTRACT_INVALID")
    metadata = dict(payload.get("metadata") or {})
    original_config = dict(metadata.get("config") or {})
    rebound = dict(rebound_config)

    changed = {}
    for key in sorted(set(original_config) | set(rebound)):
        before = original_config.get(key, "__P03_MISSING__")
        after = rebound.get(key, "__P03_MISSING__")
        if before != after:
            changed[str(key)] = {"before": before, "after": after}

    illegal = sorted(set(changed) - _EXTERNAL_TRANSPORT_LOCATOR_KEYS)
    if illegal:
        detail = {key: changed[key] for key in illegal}
        raise RuntimeError(
            "P03_EXTERNAL_CHECKPOINT_NONLOCATOR_CONFIG_MUTATION_PROHIBITED:"
            + json.dumps(detail, sort_keys=True, default=str)
        )

    # A changed locator must actually move away from the stale P02 working-tree
    # locator (or add the derived checkpoint_path) rather than silently preserve
    # an unresolved absolute path.
    unresolved = {}
    stale_marker = "/kaggle/working/iharq_p02_run/"
    for key, diff in changed.items():
        after = diff["after"]
        if (
            key != "checkpoint_path"
            and isinstance(after, str)
            and stale_marker in after
        ):
            unresolved[key] = diff
    if unresolved:
        raise RuntimeError(
            "P03_EXTERNAL_CHECKPOINT_LOCATOR_REBIND_INCOMPLETE:"
            + json.dumps(unresolved, sort_keys=True, default=str)
        )

    metadata["config"] = rebound
    transport = dict(payload)
    transport["metadata"] = metadata
    bio = io.BytesIO()
    torch.save(transport, bio)
    return bio.getvalue(), {
        "changed_locator_fields": sorted(changed),
        "changed_locator_count": len(changed),
        "nonlocator_fields_changed": [],
    }


def _load_external_adapter(snapshot_root: Path, manifest_path: str, replay_config: Mapping[str, Any]):
    expected_sha = str(replay_config["external_adapter_sha256"])
    cache_key = "BASE:" + expected_sha
    if cache_key in _EXTERNAL_ADAPTER_CACHE:
        return _EXTERNAL_ADAPTER_CACHE[cache_key]
    p = _resolve_by_sha(
        snapshot_root, manifest_path, expected_sha,
        prefer_prefix=str(replay_config["external_source_prefix"]),
    )
    # The accepted R6 CBraMod patch imports this exact historical module name.
    # Register the exact-hash R5R base under that canonical transport name before
    # importing the R6 patch.
    module_name = "iharq_stage12_external_adapters"
    spec = importlib.util.spec_from_file_location(module_name, p)
    if spec is None or spec.loader is None:
        raise RuntimeError("P03_EXTERNAL_ADAPTER_IMPORT_SPEC_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    if not hasattr(module, "build_iharq_adapter"):
        raise RuntimeError("P03_EXTERNAL_ADAPTER_ENTRYPOINT_MISSING")
    if sha256_file(Path(module.__file__).resolve()) != expected_sha:
        raise RuntimeError("P03_EXTERNAL_ADAPTER_IMPORTED_SHA_MISMATCH")
    _EXTERNAL_ADAPTER_CACHE[cache_key] = module
    return module


def _load_cbramod_r6_adapter_patch(
    snapshot_root: Path,
    manifest_path: str,
    replay_config: Mapping[str, Any],
    base_module: Any,
):
    expected_sha = str(replay_config["cbramod_adapter_patch_sha256"])
    cache_key = "CBR6:" + expected_sha
    if cache_key in _EXTERNAL_ADAPTER_CACHE:
        return _EXTERNAL_ADAPTER_CACHE[cache_key]
    # Ensure the exact accepted R5R base is the object imported by the R6 patch.
    sys.modules["iharq_stage12_external_adapters"] = base_module
    p = _resolve_by_sha(
        snapshot_root, manifest_path, expected_sha,
        prefer_prefix=str(replay_config["cbramod_adapter_patch_prefix"]),
    )
    module_name = "iharq_stage12_r6_adapter_patch"
    spec = importlib.util.spec_from_file_location(module_name, p)
    if spec is None or spec.loader is None:
        raise RuntimeError("P03_CBRAMOD_R6_PATCH_IMPORT_SPEC_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    if sha256_file(Path(module.__file__).resolve()) != expected_sha:
        raise RuntimeError("P03_CBRAMOD_R6_PATCH_IMPORTED_SHA_MISMATCH")
    cls = getattr(module, "IHARQCBraModR6ScaledAdapter", None)
    builder = getattr(module, "build_cbramod_r6", None)
    if cls is None or not callable(builder):
        raise RuntimeError("P03_CBRAMOD_R6_PATCH_CONTRACT_MISSING")
    for method in ("export_iharq_checkpoint_bytes", "reload_iharq_checkpoint_bytes"):
        if not callable(getattr(cls, method, None)):
            raise RuntimeError("P03_CBRAMOD_R6_PATCH_CHECKPOINT_SURFACE_MISSING:" + method)
    _EXTERNAL_ADAPTER_CACHE[cache_key] = module
    return module


def _gpu_policy(replay_config: Mapping[str, Any]) -> dict[str, Any]:
    return dict(replay_config.get("gpu_inference") or {})


def _require_gpu_runtime(replay_config: Mapping[str, Any]) -> dict[str, Any]:
    policy = _gpu_policy(replay_config)
    if not bool(policy.get("enabled", False)):
        return {"enabled": False, "device": "cpu", "device_count": 0, "device_ids": []}
    import torch
    available = bool(torch.cuda.is_available())
    count = int(torch.cuda.device_count()) if available else 0
    minimum = int(policy.get("minimum_gpu_count", 1))
    if bool(policy.get("required", False)) and (not available or count < minimum):
        raise RuntimeError(f"P03_GPU_REQUIRED_BUT_UNAVAILABLE:available={available}:count={count}:minimum={minimum}")
    if not available:
        return {"enabled": False, "device": "cpu", "device_count": 0, "device_ids": []}
    torch.cuda.set_device(0)
    # Preserve the governed deterministic/numerical stance.  AMP and TF32 are
    # deliberately disabled; inference remains float32, with P03's existing
    # float64 probability closure at the score boundary.
    torch.backends.cudnn.benchmark = bool(policy.get("cudnn_benchmark", False))
    torch.backends.cudnn.deterministic = bool(policy.get("cudnn_deterministic", True))
    if hasattr(torch.backends, "cuda") and hasattr(torch.backends.cuda, "matmul"):
        torch.backends.cuda.matmul.allow_tf32 = bool(policy.get("tf32", False))
    if hasattr(torch.backends, "cudnn"):
        torch.backends.cudnn.allow_tf32 = bool(policy.get("tf32", False))
    if bool(policy.get("automatic_mixed_precision", False)):
        raise RuntimeError("P03_GPU_AMP_PROHIBITED_BY_C7_POLICY")
    device_ids = list(range(count)) if bool(policy.get("use_all_visible_gpus", True)) else [0]
    return {
        "enabled": True,
        "device": "cuda:0",
        "device_count": count,
        "device_ids": device_ids,
        "device_names": [str(torch.cuda.get_device_name(i)) for i in device_ids],
        "torch_cuda": torch.version.cuda,
        "cudnn": int(torch.backends.cudnn.version() or 0),
        "tf32": bool(policy.get("tf32", False)),
        "automatic_mixed_precision": bool(policy.get("automatic_mixed_precision", False)),
        "cudnn_benchmark": bool(policy.get("cudnn_benchmark", False)),
        "cudnn_deterministic": bool(policy.get("cudnn_deterministic", True)),
    }


def _family_gpu_batch_size(replay_config: Mapping[str, Any], family: str) -> int:
    policy = _gpu_policy(replay_config)
    table = dict(policy.get("family_inference_batch_size") or {})
    return max(1, int(table.get(str(family), replay_config.get("score_load_batch_size", 128))))


def _configure_torch_network_for_gpu(network: Any, family: str, replay_config: Mapping[str, Any]) -> tuple[Any, dict[str, Any]]:
    runtime = _require_gpu_runtime(replay_config)
    if not runtime["enabled"]:
        return network, {**runtime, "family": family, "data_parallel": False}
    import torch
    device = torch.device(runtime["device"])
    network = network.to(device)
    use_dp = (
        bool(_gpu_policy(replay_config).get("data_parallel_if_multiple_gpus", True))
        and len(runtime["device_ids"]) >= 2
    )
    if use_dp:
        network = torch.nn.DataParallel(network, device_ids=runtime["device_ids"], output_device=0)
    network.eval()
    return network, {
        **runtime,
        "family": family,
        "data_parallel": bool(use_dp),
        "inference_batch_size": _family_gpu_batch_size(replay_config, family),
        "scientific_hyperparameters_changed": False,
        "checkpoint_bytes_mutated": False,
        "model_retrained": False,
        "numerical_execution_path_changed": True,
    }


def restore_accepted_model(
    model_row: Mapping[str, Any], run_cell: Mapping[str, Any], snapshot_root: Path,
    manifest_path: str, replay_config: Mapping[str, Any], core: Any,
) -> tuple[Any, dict[str, Any]]:
    checkpoint_sha = str(model_row["checkpoint_sha256"])
    checkpoint = _resolve_by_sha(snapshot_root, manifest_path, checkpoint_sha, prefer_prefix=str(replay_config["checkpoint_prefix"]))
    family = str(model_row["family_role"])
    dataset_id = str(model_row["p03_dataset_id"])
    budget_id = str(model_row["p03_budget_id"])
    if checkpoint.name.endswith(".pkl"):
        model = pickle.loads(checkpoint.read_bytes())
        return model, {
            "checkpoint_path": str(checkpoint), "checkpoint_sha256": checkpoint_sha,
            "checkpoint_format": "TRUSTED_PROJECT_PICKLE_PINNED_ENVIRONMENT", "budget_id": budget_id,
        }
    if checkpoint.name.endswith(".state_dict.pt"):
        sample_rows = validation_rows(core, dataset_id)[:1]
        X, _, _ = core.load_rows(sample_rows)
        model = _build_eegnet(model_row, run_cell, X.shape[1], X.shape[2])
        state = _load_torch_weights(checkpoint)
        if not isinstance(state, Mapping):
            raise RuntimeError("P03_EEGNET_STATE_DICT_PAYLOAD_INVALID")
        expected_keys = set(model.state_dict())
        observed_keys = set(state)
        if expected_keys != observed_keys:
            raise RuntimeError(
                "P03_EEGNET_WRAPPER_STATE_DICT_KEY_MISMATCH:"
                f"missing={sorted(expected_keys-observed_keys)}:unexpected={sorted(observed_keys-expected_keys)}"
            )
        model.load_state_dict(state, strict=True)
        model.eval()
        with __import__("torch").no_grad():
            unit = float(model.iharq_unit_multiplier.item())
            mean = model.iharq_channel_mean_uv.detach().cpu().numpy()
            std = model.iharq_channel_std_uv.detach().cpu().numpy()
        if not np.isclose(unit, 1_000_000.0, rtol=0.0, atol=1e-3):
            raise RuntimeError(f"P03_EEGNET_CHECKPOINT_UNIT_MULTIPLIER_INVALID:{unit}")
        if mean.shape != (1, X.shape[1], 1) or std.shape != (1, X.shape[1], 1):
            raise RuntimeError(f"P03_EEGNET_CHECKPOINT_NORMALIZATION_SHAPE_INVALID:{mean.shape}:{std.shape}")
        if not np.all(np.isfinite(mean)) or not np.all(np.isfinite(std)) or np.any(std <= 0):
            raise RuntimeError("P03_EEGNET_CHECKPOINT_NORMALIZATION_INVALID")
        del X
        model, gpu_audit = _configure_torch_network_for_gpu(model, family, replay_config)
        return ("EEGNET_P02_WRAPPED", model), {
            "checkpoint_path": str(checkpoint), "checkpoint_sha256": checkpoint_sha,
            "checkpoint_format": "PYTORCH_WRAPPER_STATE_DICT_WEIGHTS_ONLY_STRICT", "budget_id": budget_id,
            "normalization_source": "EXACT_CHECKPOINTED_P02_WRAPPER_BUFFERS",
            "unit_multiplier": unit,
            "checkpoint_state_key_count": len(observed_keys),
            "gpu_execution": gpu_audit,
        }
    if checkpoint.name.endswith(".external.chk"):
        module = _load_external_adapter(snapshot_root, manifest_path, replay_config)
        payload = _load_torch_weights(checkpoint)
        metadata = dict(payload.get("metadata") or {}) if isinstance(payload, Mapping) else {}
        original_config = dict(metadata.get("config") or {})
        config = _rebind_paths_by_sha(
            original_config, snapshot_root, manifest_path, str(replay_config["external_source_prefix"])
        )
        if config.get("checkpoint_sha256"):
            pretrained = _resolve_by_sha(snapshot_root, manifest_path, str(config["checkpoint_sha256"]))
            config["checkpoint_path"] = str(pretrained)
            config["pretrained_local_dir"] = str(pretrained.parent)

        if family == "SSL-CBRAMOD":
            checkpoint_patch_sha = str(original_config.get("r6_adapter_patch_sha256") or "")
            expected_patch_sha = str(replay_config["cbramod_adapter_patch_sha256"])
            if checkpoint_patch_sha != expected_patch_sha:
                raise RuntimeError(
                    "P03_CBRAMOD_R6_PATCH_IDENTITY_MISMATCH:"
                    f"checkpoint={checkpoint_patch_sha}:expected={expected_patch_sha}"
                )
            r6_module = _load_cbramod_r6_adapter_patch(
                snapshot_root, manifest_path, replay_config, module
            )
            base = r6_module.build_cbramod_r6(
                checkpoint_path=config.get("checkpoint_path"),
                config=config,
            )
            adapter_variant = "CBRAMOD_R6_SCALED_ACCEPTED_CLASS"
        else:
            base = module.build_iharq_adapter(
                branch_id=family,
                checkpoint_path=config.get("checkpoint_path"),
                config=config,
            )
            adapter_variant = "R5R_ACCEPTED_EXTERNAL_CLASS"

        rebound_bytes, transport_audit = _external_checkpoint_bytes_with_rebound_config(payload, config)
        restored = base.reload_iharq_checkpoint_bytes(rebound_bytes)
        gpu_runtime = _require_gpu_runtime(replay_config)
        gpu_audit = {**gpu_runtime, "family": family, "data_parallel": False}
        if gpu_runtime["enabled"]:
            configured_model, model_gpu_audit = _configure_torch_network_for_gpu(restored.model, family, replay_config)
            restored.model = configured_model
            restored.device = gpu_runtime["device"]
            restored.actual_batch_size = _family_gpu_batch_size(replay_config, family)
            gpu_audit = model_gpu_audit
        return restored, {
            "checkpoint_path": str(checkpoint), "checkpoint_sha256": checkpoint_sha,
            "checkpoint_format": "EXTERNAL_GOVERNED_INTERFACE", "budget_id": budget_id,
            "adapter_source_sha256": str(replay_config["external_adapter_sha256"]),
            "cbramod_adapter_patch_sha256": (
                str(replay_config["cbramod_adapter_patch_sha256"])
                if family == "SSL-CBRAMOD" else None
            ),
            "adapter_variant": adapter_variant,
            "accepted_checkpoint_bytes_mutated": False,
            "in_memory_transport_rebind": "EXPLICIT_MACHINE_LOCAL_LOCATOR_FIELDS_ONLY",
            "transport_audit": transport_audit,
            "external_state_dict_preserved": True,
            "gpu_execution": gpu_audit,
        }
    raise RuntimeError(f"UNSUPPORTED_ACCEPTED_CHECKPOINT_FORMAT:{checkpoint.name}")


P03_SOURCE_FLOAT_PROBABILITY_ATOL = 1e-5


def _validate_probability_matrix(probabilities: np.ndarray, *, atol: float = 1e-8) -> np.ndarray:
    """Validate and numerically close a probability matrix without calibration.

    Accepted P02 neural score producers emit float32 probabilities and their own
    governed score check permits row-sum error up to 1e-5.  P03 keeps its
    stricter 1e-8 canonical simplex contract by:
      1) rejecting nonfinite/out-of-range values;
      2) requiring the incoming row sum to be within the inherited 1e-5
         floating-point tolerance;
      3) performing deterministic float64 row renormalization only;
      4) re-validating the canonical result at the P03 1e-8 tolerance.

    This is numerical closure only: no temperature, calibration, thresholding,
    class reordering, logit transformation, or learned parameter is introduced.
    """
    p = np.asarray(probabilities, dtype=np.float64)
    if p.ndim != 2 or p.shape[1] != 2 or not np.all(np.isfinite(p)):
        raise RuntimeError(f"P03_REPLAY_INVALID_PROBABILITY_SHAPE_OR_FINITE:{p.shape}")
    if np.any(p < -atol) or np.any(p > 1.0 + atol):
        raise RuntimeError("P03_REPLAY_INVALID_PROBABILITY_BOUNDS")

    p = np.clip(p, 0.0, 1.0)
    row_sum = p.sum(axis=1, dtype=np.float64)
    if np.any(~np.isfinite(row_sum)) or np.any(row_sum <= 0.0):
        raise RuntimeError("P03_REPLAY_INVALID_PROBABILITY_ROW_SUM")
    max_source_deviation = float(np.max(np.abs(row_sum - 1.0))) if len(row_sum) else 0.0
    if max_source_deviation > P03_SOURCE_FLOAT_PROBABILITY_ATOL:
        raise RuntimeError(
            "P03_REPLAY_INVALID_PROBABILITY_SIMPLEX_SOURCE:"
            f"max_deviation={max_source_deviation}:"
            f"allowed={P03_SOURCE_FLOAT_PROBABILITY_ATOL}"
        )

    # Deterministic arithmetic closure of source float probabilities.
    p = p / row_sum[:, None]
    final_sum = p.sum(axis=1, dtype=np.float64)
    if not np.allclose(final_sum, 1.0, atol=atol, rtol=0.0):
        raise RuntimeError(
            "P03_REPLAY_INVALID_PROBABILITY_SIMPLEX_AFTER_NUMERIC_CLOSURE:"
            f"max_deviation={float(np.max(np.abs(final_sum - 1.0)))}"
        )
    return p


def _is_cuda_oom(exc: BaseException) -> bool:
    text = str(exc).lower()
    return "out of memory" in text and "cuda" in text


def score_model(model: Any, X: np.ndarray, *, batch_size: int = 128, replay_config: Mapping[str, Any] | None = None, family: str | None = None) -> np.ndarray:
    replay_config = dict(replay_config or {})
    family = str(family or "UNKNOWN")
    policy = _gpu_policy(replay_config)
    minimum_bs = max(1, int(policy.get("minimum_oom_backoff_batch_size", 16)))
    backoff = max(2, int(policy.get("oom_backoff_factor", 2)))

    if isinstance(model, tuple) and model[0] == "EEGNET_P02_WRAPPED":
        import torch
        _, network = model
        raw = np.asarray(X, np.float32)
        try:
            device = next(network.parameters()).device
        except Exception:
            device = torch.device("cpu")
        current_bs = max(1, int(batch_size))
        while True:
            try:
                outputs = []
                network.eval()
                with torch.inference_mode():
                    for start in range(0, len(raw), current_bs):
                        xb = torch.as_tensor(raw[start:start + current_bs], dtype=torch.float32, device=device)
                        # Network inference remains exactly float32. Softmax is
                        # float64 only at the 2-class score boundary, as in C6.
                        logits = network(xb)
                        outputs.append(torch.softmax(logits.to(torch.float64), 1).cpu().numpy())
                return _validate_probability_matrix(np.concatenate(outputs, axis=0) if outputs else np.empty((0, 2)))
            except RuntimeError as exc:
                if device.type == "cuda" and _is_cuda_oom(exc) and current_bs > minimum_bs:
                    current_bs = max(minimum_bs, current_bs // backoff)
                    torch.cuda.empty_cache()
                    continue
                raise

    if hasattr(model, "scores"):
        probabilities = model.scores(X)
    elif hasattr(model, "predict_scores"):
        # Accepted external adapters expose governed device-aware inference.
        # Retry only CUDA OOM by reducing operational inference batch size; this
        # does not alter model parameters, data, role membership or predictions'
        # mathematical definition.
        if hasattr(model, "actual_batch_size") and str(getattr(model, "device", "cpu")).startswith("cuda"):
            current_bs = max(1, int(getattr(model, "actual_batch_size") or batch_size))
            while True:
                try:
                    model.actual_batch_size = current_bs
                    probabilities = model.predict_scores(X)
                    break
                except RuntimeError as exc:
                    if _is_cuda_oom(exc) and current_bs > minimum_bs:
                        current_bs = max(minimum_bs, current_bs // backoff)
                        try:
                            import torch
                            torch.cuda.empty_cache()
                        except Exception:
                            pass
                        continue
                    raise
        else:
            probabilities = model.predict_scores(X)
    else:
        probabilities = None
    if probabilities is None:
        raise RuntimeError("MODEL_HAS_NO_LAWFUL_SCORE_OUTPUT")
    return _validate_probability_matrix(probabilities)


def score_core_rows(
    core: Any,
    rows: Sequence[Mapping[str, Any]],
    model: Any,
    *,
    load_batch_size: int = 128,
    replay_config: Mapping[str, Any] | None = None,
    family: str | None = None,
) -> np.ndarray:
    outputs: list[np.ndarray] = []
    rows = list(rows)
    replay_config = dict(replay_config or {})
    family = str(family or "UNKNOWN")
    outer = max(1, int(load_batch_size))
    for start in range(0, len(rows), outer):
        X, _, _ = core.load_rows(rows[start:start + outer])
        outputs.append(
            score_model(
                model,
                X,
                batch_size=_family_gpu_batch_size(replay_config, family),
                replay_config=replay_config,
                family=family,
            )
        )
        del X
    if not outputs:
        return np.empty((0, 2), dtype=float)
    return _validate_probability_matrix(np.concatenate(outputs, axis=0))


def canonical_truth_row(core: Any, row: Mapping[str, Any]) -> dict[str, Any]:
    location = core.locations[str(row["window_record_id"])]
    return {
        **dict(row),
        "window_id": str(location["window_id"]),
        "event_order": int(location["hdf5_row"]),
    }


def _cache_paths(cache_root: Path, run_cell_id: str) -> tuple[Path, Path]:
    safe = hashlib.sha256(run_cell_id.encode("utf-8")).hexdigest()[:24]
    return cache_root / f"{safe}.npz", cache_root / f"{safe}.json"


def _load_replay_cache(cache_root: Path, model_row: Mapping[str, Any], context_fingerprint: str) -> dict[str, Any] | None:
    npz_path, meta_path = _cache_paths(cache_root, str(model_row["p03_run_cell_id"]))
    if not npz_path.is_file() or not meta_path.is_file():
        return None
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    if (
        meta.get("context_fingerprint") != context_fingerprint
        or meta.get("run_cell_id") != model_row["p03_run_cell_id"]
        or meta.get("checkpoint_sha256") != model_row["checkpoint_sha256"]
        or meta.get("status") != "SUCCESS"
        or meta.get("npz_sha256") != sha256_file(npz_path)
    ):
        return None
    arrays = np.load(npz_path, allow_pickle=False)
    return {"meta": meta, "calibration_scores": arrays["calibration_scores"], "validation_scores": arrays["validation_scores"]}


def replay_one_model(
    *,
    model_row: Mapping[str, Any], core: Any, snapshot_root: Path, runtime_root_rel: str,
    manifest_path: str, replay_config: Mapping[str, Any], cache_root: Path, context_fingerprint: str,
) -> dict[str, Any]:
    cached = _load_replay_cache(cache_root, model_row, context_fingerprint)
    if cached is not None:
        return {**cached, "resume_action": "REUSED_EXACT_REPLAY_CACHE"}
    run_cell_id = str(model_row["p03_run_cell_id"])
    run_cell = _run_cell(snapshot_root, runtime_root_rel, run_cell_id)
    if str(run_cell.get("checkpoint_sha256")) != str(model_row["checkpoint_sha256"]):
        raise RuntimeError(f"P03_REPLAY_RUN_CELL_CHECKPOINT_MISMATCH:{run_cell_id}")
    model, provenance = restore_accepted_model(model_row, run_cell, snapshot_root, manifest_path, replay_config, core)
    cal_rows, excluded = calibration_rows(core, str(model_row["p03_dataset_id"]), str(model_row["p03_budget_id"]))
    val_rows = validation_rows(core, str(model_row["p03_dataset_id"]))
    family = str(model_row.get("family_role"))
    gpu_policy = _gpu_policy(replay_config)
    load_batch_size = int(gpu_policy.get("outer_load_batch_size", replay_config.get("score_load_batch_size", 128)))
    cal_scores = score_core_rows(
        core, cal_rows, model, load_batch_size=load_batch_size, replay_config=replay_config, family=family
    )
    val_scores = score_core_rows(
        core, val_rows, model, load_batch_size=load_batch_size, replay_config=replay_config, family=family
    )
    if len(cal_scores) != len(cal_rows) or len(val_scores) != len(val_rows):
        raise RuntimeError(f"P03_REPLAY_SCORE_CARDINALITY_MISMATCH:{run_cell_id}")
    cache_root.mkdir(parents=True, exist_ok=True)
    npz_path, meta_path = _cache_paths(cache_root, run_cell_id)
    np.savez_compressed(npz_path, calibration_scores=cal_scores, validation_scores=val_scores)
    metadata = {
        "status": "SUCCESS", "context_fingerprint": context_fingerprint,
        "run_cell_id": run_cell_id, "model_registry_record_id": model_row.get("record_id"),
        "model_id": model_row.get("model_id"), "dataset_id": model_row["p03_dataset_id"],
        "budget_id": model_row["p03_budget_id"], "family_role": model_row.get("family_role"),
        "checkpoint_sha256": model_row["checkpoint_sha256"], "score_type": model_row["score_type"],
        "class_order": list(model_row["class_order"]), "excluded_low_label_training_event_count": len(excluded),
        "calibration_row_count": len(cal_rows), "validation_row_count": len(val_rows),
        "calibration_window_record_ids_sha256": hashlib.sha256("\n".join(str(row["window_record_id"]) for row in cal_rows).encode()).hexdigest(),
        "validation_window_record_ids_sha256": hashlib.sha256("\n".join(str(row["window_record_id"]) for row in val_rows).encode()).hexdigest(),
        "restore_provenance": provenance,
        "gpu_inference_policy": {
            "policy_id": str(gpu_policy.get("policy_id") or "DISABLED"),
            "enabled": bool(gpu_policy.get("enabled", False)),
            "required": bool(gpu_policy.get("required", False)),
            "strategy": str(gpu_policy.get("strategy") or "CPU"),
            "outer_load_batch_size": load_batch_size,
            "family_inference_batch_size": _family_gpu_batch_size(replay_config, family),
            "automatic_mixed_precision": bool(gpu_policy.get("automatic_mixed_precision", False)),
            "tf32": bool(gpu_policy.get("tf32", False)),
        },
        "probability_numeric_policy": {
            "policy_id": "P03-C6-NUMERIC-SIMPLEX-CLOSURE-R1",
            "source_probability_atol": P03_SOURCE_FLOAT_PROBABILITY_ATOL,
            "canonical_probability_atol": 1e-8,
            "operation": "FLOAT64_SOFTMAX_WHERE_LOGITS_AVAILABLE_ELSE_FLOAT64_ROW_RENORMALIZATION",
            "learned_or_calibration_transformation": False,
        },
    }
    metadata["npz_sha256"] = sha256_file(npz_path)
    meta_path.write_text(json.dumps(metadata, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    del model
    gc.collect()
    try:
        import torch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except Exception:
        pass
    return {"meta": metadata, "calibration_scores": cal_scores, "validation_scores": val_scores, "resume_action": "EXECUTED"}


def load_test_partition(
    *,
    snapshot_root: Path, runtime_root_rel: str, run_cell_id: str, expected_config_sha256: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    run_cell = _run_cell(snapshot_root, runtime_root_rel, run_cell_id)
    relative = str(run_cell.get("prediction_partition"))
    if not relative:
        raise RuntimeError(f"P03_REPLAY_P02_TEST_PARTITION_MISSING_IN_RUN_CELL:{run_cell_id}")
    path = (snapshot_root / runtime_root_rel / relative).resolve()
    runtime_root = (snapshot_root / runtime_root_rel).resolve()
    if runtime_root not in path.parents or not path.is_file():
        raise RuntimeError(f"P03_REPLAY_P02_TEST_PARTITION_RESOLUTION_FAILED:{run_cell_id}:{relative}")
    rows = _read_jsonl(path)
    if any(row.get("config_sha256") != expected_config_sha256 for row in rows):
        raise RuntimeError(f"P03_REPLAY_TEST_CONFIG_MISMATCH:{run_cell_id}")
    if any(str(row.get("split_role")) != "test" for row in rows):
        raise RuntimeError(f"P03_REPLAY_NONTEST_P02_PREDICTION:{run_cell_id}")
    return rows, run_cell


def build_selection_score_record(
    *,
    model_row: Mapping[str, Any], truth: Mapping[str, Any], score_vector: Sequence[float], role: str, row_index: int,
) -> dict[str, Any]:
    if role not in {"calibration", "validation"}:
        raise ValueError(role)
    return {
        "record_family": "P03SelectionScoreRecord", "phase_id": "P03", "layer_id": "L3",
        "purpose_role": "calibration_fit" if role == "calibration" else "threshold_validation_selection",
        "source_canonical_role": role, "source_window_record_id": truth["window_record_id"],
        "window_id": truth["window_id"], "event_id": truth.get("event_id"),
        "dataset_id": model_row["p03_dataset_id"], "model_id": model_row["model_id"],
        "parent_model_registry_record_id": model_row["record_id"], "parent_p02_run_cell_id": model_row["p03_run_cell_id"],
        "checkpoint_sha256": model_row["checkpoint_sha256"], "score_type": model_row["score_type"],
        "class_order": list(model_row["class_order"]), "score_vector": [float(value) for value in score_vector],
        "truth_join_contract": "PROTECTED_P01_WINDOWRECORD_JOIN_BY_WINDOW_ID__NOT_STORED_IN_SCORE_RECORD",
        "budget_id": model_row["p03_budget_id"], "row_index": int(row_index),
    }


def context_fingerprint(context: Mapping[str, Any]) -> str:
    return sha256_json(dict(context))
