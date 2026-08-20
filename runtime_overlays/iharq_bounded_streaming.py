from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Iterable
from types import MethodType, SimpleNamespace
from dataclasses import asdict, is_dataclass, replace
import ctypes
import gc
import hashlib
import importlib.metadata as importlib_metadata
import inspect
import json
import math
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
import textwrap
import uuid
import zipfile

WINDOW_SHARD_READER_SOURCE = 'from __future__ import annotations\n\n"""Read exact IHARQ P01/L1 R26 windows from an attached derived Kaggle Dataset.\n\nThe reader performs no network access. It supports Kaggle\'s optional ordinal\nfilename prefixes, verifies the manifest/index/shard identities, validates the\nHDF5 window ID at the declared row, and returns one exact NumPy array at a time.\n"""\n\nfrom dataclasses import dataclass\nfrom pathlib import Path\nfrom typing import Any, Iterable, Iterator\nimport hashlib\nimport json\nimport re\n\nMANIFEST_NAME = "IHARQ_P01_L1_DERIVED_WINDOW_DATASET_MANIFEST.json"\nLOCATION_INDEX_NAME = "IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl"\nEXPECTED_FORMAT = "LOSSLESS_HDF5_SUBJECT_SHARDS"\nEXPECTED_FREEZE = "P01-L1-OFFICIAL-RUN-FREEZE-R2"\n\n\ndef sha256_file(path: str | Path) -> str:\n    digest = hashlib.sha256()\n    with Path(path).open("rb") as stream:\n        for block in iter(lambda: stream.read(1024 * 1024), b""):\n            digest.update(block)\n    return digest.hexdigest()\n\n\ndef _canonical_leaf(name: str) -> str:\n    return Path(name).name\n\n\ndef _matches_canonical_filename(path: Path, canonical_name: str) -> bool:\n    leaf = path.name\n    canonical = _canonical_leaf(canonical_name)\n    return leaf == canonical or bool(re.fullmatch(rf"\\d+_{re.escape(canonical)}", leaf))\n\n\ndef resolve_unique_file(root: str | Path, canonical_name: str, *, expected_sha256: str | None = None) -> Path:\n    root = Path(root)\n    candidates = [p for p in root.rglob("*") if p.is_file() and _matches_canonical_filename(p, canonical_name)]\n    if expected_sha256:\n        candidates = [p for p in candidates if sha256_file(p) == expected_sha256.lower()]\n    unique = {str(p.resolve()): p.resolve() for p in candidates}\n    if len(unique) != 1:\n        raise RuntimeError(\n            "IHARQ_DERIVED_FILE_RESOLUTION_AMBIGUOUS: "\n            f"canonical={canonical_name}; matches={sorted(unique)}"\n        )\n    return next(iter(unique.values()))\n\n\ndef _iter_jsonl(path: Path) -> Iterator[dict[str, Any]]:\n    with path.open("r", encoding="utf-8") as stream:\n        for line_number, line in enumerate(stream, start=1):\n            line = line.strip()\n            if not line:\n                continue\n            try:\n                value = json.loads(line)\n            except json.JSONDecodeError as exc:\n                raise RuntimeError(f"IHARQ_JSONL_PARSE_FAILED: path={path}; line={line_number}") from exc\n            if not isinstance(value, dict):\n                raise RuntimeError(f"IHARQ_JSONL_ROW_NOT_OBJECT: path={path}; line={line_number}")\n            yield value\n\n\n@dataclass(frozen=True)\nclass WindowLocation:\n    window_id: str\n    window_record_id: str\n    shard_filename: str\n    hdf5_group: str\n    hdf5_row: int\n    shape: tuple[int, ...]\n    dtype: str\n    shard_sha256: str\n\n\nclass DerivedWindowDataset:\n    """Bounded-memory access to one attached R26 derived-window Dataset."""\n\n    def __init__(self, root: str | Path, *, verify_all_shards_at_open: bool = False):\n        self.root = Path(root).resolve()\n        if not self.root.is_dir():\n            raise FileNotFoundError(self.root)\n        self.manifest_path = resolve_unique_file(self.root, MANIFEST_NAME)\n        self.manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))\n        self._validate_manifest()\n        index_spec = self.manifest.get("window_location_index", {})\n        expected_index_hash = index_spec.get("dataset_sha256")\n        index_name = index_spec.get("dataset_filename", LOCATION_INDEX_NAME)\n        self.location_index_path = resolve_unique_file(\n            self.root,\n            str(index_name),\n            expected_sha256=str(expected_index_hash).lower() if expected_index_hash else None,\n        )\n        self._shards = {\n            str(row["filename"]): row\n            for row in self.manifest.get("shards", [])\n        }\n        if len(self._shards) != len(self.manifest.get("shards", [])):\n            raise RuntimeError("IHARQ_DERIVED_DUPLICATE_SHARD_FILENAME")\n        self._location_cache: dict[str, WindowLocation] = {}\n        self._verified_shards: set[str] = set()\n        if verify_all_shards_at_open:\n            for filename in sorted(self._shards):\n                self._resolve_and_verify_shard(filename)\n\n    @classmethod\n    def discover(cls, input_root: str | Path = "/kaggle/input", *, verify_all_shards_at_open: bool = False) -> "DerivedWindowDataset":\n        input_root = Path(input_root)\n        manifests = [p for p in input_root.rglob("*") if p.is_file() and _matches_canonical_filename(p, MANIFEST_NAME)]\n        roots = {str(p.parent.resolve()): p.parent.resolve() for p in manifests}\n        if len(roots) != 1:\n            raise RuntimeError(\n                "IHARQ_DERIVED_DATASET_DISCOVERY_REQUIRES_EXACTLY_ONE: "\n                f"observed={sorted(roots)}"\n            )\n        return cls(next(iter(roots.values())), verify_all_shards_at_open=verify_all_shards_at_open)\n\n    def _validate_manifest(self) -> None:\n        manifest = self.manifest\n        if manifest.get("scientific_freeze") != EXPECTED_FREEZE:\n            raise RuntimeError("IHARQ_DERIVED_SCIENTIFIC_FREEZE_MISMATCH")\n        if manifest.get("format") != EXPECTED_FORMAT:\n            raise RuntimeError("IHARQ_DERIVED_FORMAT_MISMATCH")\n        if manifest.get("creation_status") not in {None, "COMMITTED"}:\n            raise RuntimeError("IHARQ_DERIVED_DATASET_NOT_COMMITTED")\n        if int(manifest.get("immutable_revision", 0)) != 1:\n            raise RuntimeError("IHARQ_DERIVED_REVISION_MISMATCH")\n        if int(manifest.get("window_count", -1)) < 0:\n            raise RuntimeError("IHARQ_DERIVED_WINDOW_COUNT_INVALID")\n        if manifest.get("signal_dtype") not in {None, "float32"}:\n            raise RuntimeError("IHARQ_DERIVED_SIGNAL_DTYPE_MISMATCH")\n\n    def _resolve_and_verify_shard(self, filename: str) -> Path:\n        spec = self._shards.get(filename)\n        if spec is None:\n            raise KeyError(f"Unknown shard: {filename}")\n        path = resolve_unique_file(self.root, filename)\n        resolved_key = str(path)\n        if resolved_key not in self._verified_shards:\n            expected_bytes = int(spec["bytes"])\n            if path.stat().st_size != expected_bytes:\n                raise RuntimeError(\n                    f"IHARQ_DERIVED_SHARD_SIZE_MISMATCH: {filename}; "\n                    f"expected={expected_bytes}; observed={path.stat().st_size}"\n                )\n            observed_hash = sha256_file(path)\n            if observed_hash != str(spec["sha256"]).lower():\n                raise RuntimeError(\n                    f"IHARQ_DERIVED_SHARD_SHA256_MISMATCH: {filename}; "\n                    f"expected={spec[\'sha256\']}; observed={observed_hash}"\n                )\n            self._verified_shards.add(resolved_key)\n        return path\n\n    def iter_locations(self) -> Iterator[WindowLocation]:\n        seen: set[str] = set()\n        for row in _iter_jsonl(self.location_index_path):\n            window_id = str(row["window_id"])\n            if window_id in seen:\n                raise RuntimeError(f"IHARQ_DERIVED_DUPLICATE_WINDOW_ID: {window_id}")\n            seen.add(window_id)\n            filename = str(row["shard_filename"])\n            shard_spec = self._shards.get(filename)\n            if shard_spec is None:\n                raise RuntimeError(f"IHARQ_DERIVED_INDEX_REFERENCES_UNKNOWN_SHARD: {filename}")\n            location = WindowLocation(\n                window_id=window_id,\n                window_record_id=str(row["window_record_id"]),\n                shard_filename=filename,\n                hdf5_group=str(row["hdf5_group"]),\n                hdf5_row=int(row["hdf5_row"]),\n                shape=tuple(int(v) for v in row["shape"]),\n                dtype=str(row["dtype"]),\n                shard_sha256=str(shard_spec["sha256"]).lower(),\n            )\n            self._location_cache[window_id] = location\n            yield location\n        expected = int(self.manifest["window_count"])\n        if len(seen) != expected:\n            raise RuntimeError(\n                f"IHARQ_DERIVED_INDEX_COUNT_MISMATCH: expected={expected}; observed={len(seen)}"\n            )\n\n    def location(self, window_id: str) -> WindowLocation:\n        window_id = str(window_id)\n        cached = self._location_cache.get(window_id)\n        if cached is not None:\n            return cached\n        for location in self.iter_locations():\n            if location.window_id == window_id:\n                return location\n        raise KeyError(window_id)\n\n    def load(self, window_id: str, *, verify_window_id: bool = True):\n        import h5py\n        import numpy as np\n\n        location = self.location(window_id)\n        shard_path = self._resolve_and_verify_shard(location.shard_filename)\n        with h5py.File(shard_path, "r") as handle:\n            signals_path = f"{location.hdf5_group}/signals"\n            ids_path = f"{location.hdf5_group}/window_ids"\n            if signals_path not in handle or ids_path not in handle:\n                raise RuntimeError(f"IHARQ_DERIVED_HDF5_GROUP_MISSING: {location.hdf5_group}")\n            signals = handle[signals_path]\n            identifiers = handle[ids_path]\n            row = location.hdf5_row\n            if row < 0 or row >= int(signals.shape[0]) or row >= int(identifiers.shape[0]):\n                raise RuntimeError(f"IHARQ_DERIVED_HDF5_ROW_OUT_OF_RANGE: {window_id}; row={row}")\n            stored_id = identifiers[row]\n            if isinstance(stored_id, bytes):\n                stored_id = stored_id.decode("utf-8")\n            if verify_window_id and str(stored_id) != location.window_id:\n                raise RuntimeError(\n                    f"IHARQ_DERIVED_WINDOW_ID_MISMATCH: expected={location.window_id}; observed={stored_id}"\n                )\n            array = np.asarray(signals[row])\n        if tuple(array.shape) != location.shape:\n            raise RuntimeError(\n                f"IHARQ_DERIVED_WINDOW_SHAPE_MISMATCH: expected={location.shape}; observed={array.shape}"\n            )\n        if str(array.dtype) != location.dtype:\n            raise RuntimeError(\n                f"IHARQ_DERIVED_WINDOW_DTYPE_MISMATCH: expected={location.dtype}; observed={array.dtype}"\n            )\n        return array\n\n    def load_many(self, window_ids: Iterable[str]) -> Iterator[tuple[str, Any]]:\n        for window_id in window_ids:\n            yield str(window_id), self.load(str(window_id))\n\n\ndef _self_test() -> dict[str, Any]:\n    import tempfile\n    import h5py\n    import numpy as np\n\n    with tempfile.TemporaryDirectory() as temporary:\n        root = Path(temporary)\n        array = np.arange(24, dtype=np.float32).reshape(3, 8)\n        shard = root / "001_D_subject_001_windows.h5"\n        with h5py.File(shard, "w") as handle:\n            group = handle.require_group("window_groups/c3_t8")\n            group.create_dataset("signals", data=array[None, ...], dtype="float32")\n            group.create_dataset("window_ids", data=np.asarray(["window:test"], dtype=h5py.string_dtype("utf-8")))\n        index = root / ("002_" + LOCATION_INDEX_NAME)\n        index.write_text(json.dumps({\n            "window_id": "window:test",\n            "window_record_id": "WindowRecord:test",\n            "shard_filename": "D_subject_001_windows.h5",\n            "hdf5_group": "window_groups/c3_t8",\n            "hdf5_row": 0,\n            "shape": [3, 8],\n            "dtype": "float32",\n        }) + "\\n", encoding="utf-8")\n        manifest = {\n            "scientific_freeze": EXPECTED_FREEZE,\n            "format": EXPECTED_FORMAT,\n            "creation_status": "COMMITTED",\n            "immutable_revision": 1,\n            "window_count": 1,\n            "window_location_index": {\n                "dataset_filename": LOCATION_INDEX_NAME,\n                "dataset_sha256": sha256_file(index),\n            },\n            "shards": [{\n                "filename": "D_subject_001_windows.h5",\n                "bytes": shard.stat().st_size,\n                "sha256": sha256_file(shard),\n            }],\n        }\n        (root / ("003_" + MANIFEST_NAME)).write_text(json.dumps(manifest), encoding="utf-8")\n        dataset = DerivedWindowDataset(root)\n        restored = dataset.load("window:test")\n        return {\n            "status": "PASS" if np.array_equal(array, restored) else "FAIL",\n            "ordinal_prefix_resolution": True,\n            "lossless_roundtrip": bool(np.array_equal(array, restored)),\n            "shape": list(restored.shape),\n            "dtype": str(restored.dtype),\n        }\n\n\nif __name__ == "__main__":\n    print(json.dumps(_self_test(), indent=2))\n'

POLICY = {
    "policy_id": "P01-L1-KAGGLE-DUAL-PERSISTENCE-BOUNDED-STREAMING-R3",
    "runtime_revision": "R34",
    "policy_kind": "RESOURCE_AND_PERSISTENCE_IMPLEMENTATION_AMENDMENT_ONLY",
    "scientific_freeze_unchanged": "P01-L1-OFFICIAL-RUN-FREEZE-R2",
    "controlling_authority": "IHARQ-IBB-R10-P01-L1-INDEPENDENT-AUDIT-REPAIRED",
    "annex": "IHARQ-IBB-P01-L1-ANNEX-R4",
    "passes": {
        "pass_1": "SUBJECT_SCOPED_METADATA_EVENT_PROVENANCE_AND_RAW_FIT_STAT_SUMMARY",
        "pass_2a": "DETERMINISTIC_COMBINATION_OF_PASS1_FIT_STATISTICS",
        "pass_2b": "SUBJECT_SCOPED_TRANSFORM_QUALITY_WINDOW_MATERIALIZATION_AND_UPLOAD",
    },
    "maximum_concurrent_source_subjects": 8,
    "disposable_subject_processes": True,
    "child_rss_hard_limit_gib": 24.0,
    "minimum_disk_free_gib": 4.0,
    "progress_interval_seconds": 120,
    "derived_window_storage": "PRIVATE_KAGGLE_DATASET_LOSSLESS_HDF5_SUBJECT_SHARDS",
    "derived_kaggle_username": "csthv999z",
    "derived_dataset_slug_prefix": "iharq-p01-l1-core",
    "derived_dataset_version": 1,
    "derived_dataset_private": True,
    "local_raw_signal_retention": False,
    "local_preprocessed_signal_retention": False,
    "local_window_array_retention_after_upload": False,
    "no_scientific_scope_reduction": True,
    "active_sources_unchanged": ["PhysioNetMI", "BNCI2014_001", "Lee2019_MI"],
    "labels_splits_budgets_preprocessing_windows_unchanged": True,
    "official_joint_event_resampling_enforced": True,
    "official_window_offset_and_one_window_policy_enforced": True,
    "official_float32_window_dtype_enforced": True,
    "finalization_stage_ordering_corrected": True,
    "all_p01_gates_and_handoffs_preserved": True,
    "dual_persistence": {
        "compact_output": "GITHUB_READY_REPOSITORY_ZIP",
        "large_numerical_output": "PRIVATE_KAGGLE_DERIVED_DATASET",
        "manual_huggingface_roundtrip_required": False,
        "manual_future_kaggle_reupload_required": False,
    },
    "github_ready_repository_max_gib": 0.95,
    "github_ready_excludes_large_arrays": True,
    "storage_forecast_compression_ratio_lower": 0.55,
    "storage_forecast_compression_ratio_upper": 1.10,
    "storage_forecast_safety_multiplier": 1.25,
}

_GIB = 1024 ** 3
_CHILD_MODULE = "iharq_bounded_streaming"


class ShapeOnlySignal:
    """A non-materializable signal descriptor used after streaming Pass 1."""
    __slots__ = ("shape", "dtype", "ndim", "size", "nbytes")

    def __init__(self, shape: Iterable[int], dtype: str | Any):
        import numpy as np
        self.shape = tuple(int(x) for x in shape)
        self.dtype = np.dtype(dtype)
        self.ndim = len(self.shape)
        self.size = math.prod(self.shape)
        self.nbytes = int(self.size * self.dtype.itemsize)

    def __len__(self) -> int:
        return self.shape[0]

    def __array__(self, *args, **kwargs):
        raise RuntimeError(
            "SHAPE_ONLY_SIGNAL_MATERIALIZATION_PROHIBITED: R26 loads each subject "
            "inside a disposable child process instead of retaining all signals."
        )

    def __getitem__(self, key):
        raise RuntimeError("SHAPE_ONLY_SIGNAL_INDEXING_PROHIBITED")

    def __repr__(self) -> str:
        return f"ShapeOnlySignal(shape={self.shape!r}, dtype={str(self.dtype)!r})"


def _jsonable(value: Any) -> Any:
    import numpy as np
    if value is None or isinstance(value, (str, int, bool)):
        return value
    if isinstance(value, float):
        return value if math.isfinite(value) else str(value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, np.generic):
        return _jsonable(value.item())
    if isinstance(value, np.ndarray):
        return [_jsonable(x) for x in value.tolist()]
    if is_dataclass(value):
        return _jsonable(asdict(value))
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_jsonable(v) for v in value]
    return str(value)


def _atomic_json(path: Path, payload: Any) -> None:
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(_jsonable(payload), indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def _append_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(_jsonable(row), separators=(",", ":")) + "\n")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not Path(path).is_file():
        return []
    rows = []
    with Path(path).open("r", encoding="utf-8") as stream:
        for line in stream:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _safe(value: Any) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", str(value)).strip("_") or "unknown"


def _trim_memory() -> None:
    gc.collect()
    try:
        ctypes.CDLL("libc.so.6").malloc_trim(0)
    except Exception:
        pass


def _rss_bytes(pid: int | None = None) -> int:
    pid = int(pid or os.getpid())
    try:
        text = Path(f"/proc/{pid}/status").read_text(encoding="utf-8")
        match = re.search(r"^VmRSS:\s+(\d+)\s+kB", text, flags=re.MULTILINE)
        return int(match.group(1)) * 1024 if match else 0
    except Exception:
        return 0


def _disk_snapshot(path: Path) -> dict[str, Any]:
    usage = shutil.disk_usage(path)
    return {
        "total_bytes": usage.total,
        "used_bytes": usage.used,
        "free_bytes": usage.free,
        "free_gib": round(usage.free / _GIB, 3),
    }


def _resource_guard(work_root: Path, child_pid: int | None = None) -> None:
    disk = _disk_snapshot(work_root)
    if disk["free_bytes"] < int(POLICY["minimum_disk_free_gib"] * _GIB):
        raise RuntimeError(
            "R26_DISK_RESERVE_EXCEEDED: "
            f"free_gib={disk['free_gib']}; required_gib={POLICY['minimum_disk_free_gib']}"
        )
    if child_pid:
        rss = _rss_bytes(child_pid)
        if rss > int(POLICY["child_rss_hard_limit_gib"] * _GIB):
            raise MemoryError(
                "R26_CHILD_RSS_LIMIT_EXCEEDED: "
                f"pid={child_pid}; rss_gib={rss/_GIB:.3f}; limit_gib={POLICY['child_rss_hard_limit_gib']}"
            )


def _profile_dict(profile: Any) -> dict[str, Any]:
    return _jsonable(asdict(profile) if is_dataclass(profile) else dict(profile))


def _subject_values(profile: Any) -> list[int]:
    dataset = str(profile.dataset_id)
    raw = dict(profile.adapter_options).get("subjects")
    values: list[int] = []
    if isinstance(raw, (list, tuple, set)):
        values = [int(v) for v in raw]
    elif isinstance(raw, range):
        values = [int(v) for v in raw]
    elif raw is not None:
        try:
            values = [int(raw)]
        except Exception:
            values = []
    fallback = {
        "PhysioNetMI": list(range(1, 110)),
        "BNCI2014_001": list(range(1, 10)),
        "Lee2019_MI": list(range(1, 55)),
    }[dataset]
    if not values:
        values = fallback
    expected = set(fallback)
    if set(values) != expected:
        raise RuntimeError(
            "R26_SUBJECT_SCOPE_MISMATCH: "
            f"dataset={dataset}; expected={sorted(expected)}; observed={sorted(set(values))}"
        )
    return sorted(set(values))


def _clone_profile_for_subject(profile_dict: dict[str, Any], subject: int):
    from iharq.layer1_data_protocol.models import SourceProfile
    payload = dict(profile_dict)
    options = dict(payload.get("adapter_options", {}))
    options["subjects"] = [int(subject)]
    options["n_jobs"] = 1
    payload["adapter_options"] = options
    return SourceProfile(**payload)


def _recording_source_unit(recording: Any) -> str:
    return f"{recording.dataset_id}:{recording.subject_id}:{recording.session_id}:{recording.run_id}"


def _descriptor_from_recording(recording: Any) -> dict[str, Any]:
    return {
        "dataset_id": str(recording.dataset_id),
        "subject_id": _jsonable(recording.subject_id),
        "session_id": _jsonable(recording.session_id),
        "run_id": _jsonable(recording.run_id),
        "source_file": str(recording.source_file),
        "sampling_hz": float(recording.sampling_hz),
        "channel_names": [str(x) for x in recording.channel_names],
        "signal_shape": [int(x) for x in recording.signal.shape],
        "signal_dtype": str(recording.signal.dtype),
        "events": [
            {
                "event_id": str(event.event_id),
                "start_sample": int(event.start_sample),
                "stop_sample": int(event.stop_sample),
                "original_label": str(event.original_label),
                "metadata": _jsonable(getattr(event, "metadata", {})),
            }
            for event in recording.events
        ],
        "source_metadata": _jsonable(getattr(recording, "source_metadata", {})),
        "source_unit": _recording_source_unit(recording),
    }


def _recording_from_descriptor(row: dict[str, Any]):
    from iharq.layer1_data_protocol.models import Event, RawRecording
    events = [
        Event(
            event_id=str(event["event_id"]),
            start_sample=int(event["start_sample"]),
            stop_sample=int(event["stop_sample"]),
            original_label=str(event["original_label"]),
            metadata=dict(event.get("metadata", {})),
        )
        for event in row["events"]
    ]
    return RawRecording(
        dataset_id=str(row["dataset_id"]),
        subject_id=row["subject_id"],
        session_id=row["session_id"],
        run_id=row["run_id"],
        source_file=str(row["source_file"]),
        sampling_hz=float(row["sampling_hz"]),
        channel_names=[str(x) for x in row["channel_names"]],
        signal=ShapeOnlySignal(row["signal_shape"], row["signal_dtype"]),
        events=events,
        source_metadata=dict(row.get("source_metadata", {})),
    )


def _child_runner_stub(task: dict[str, Any]):
    report_root = Path(task["child_report_root"])
    report_root.mkdir(parents=True, exist_ok=True)
    return SimpleNamespace(
        input_root=Path(task["input_root"]),
        work_root=Path(task["child_work_root"]),
        pipeline=SimpleNamespace(bundle_root=report_root),
    )


def _load_subject_recordings(task: dict[str, Any]):
    os.environ.update({
        "OMP_NUM_THREADS": "1",
        "MKL_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1",
        "NUMEXPR_NUM_THREADS": "1",
        "IHARQ_STREAMING_CHILD": "1",
    })
    from iharq_acquisition_acceleration import install_acquisition_acceleration
    stub = _child_runner_stub(task)
    install_acquisition_acceleration(
        stub,
        child_mode=True,
        resolution_file=task["source_resolution_file"],
    )
    from iharq.layer1_data_protocol import adapters as adapters_module
    profile = _clone_profile_for_subject(task["profile"], int(task["subject"]))
    adapter_class = adapters_module.ADAPTERS.get(profile.adapter)
    if adapter_class is None:
        raise RuntimeError(f"R26_CHILD_ADAPTER_UNKNOWN: {profile.adapter}")
    cache_root = Path(task["child_work_root"]) / "source_cache" / profile.dataset_id
    adapter = adapter_class(profile, Path(task["input_root"]), cache_root)
    files = list(adapter.resolve_files())
    recordings = list(adapter.load(files))
    if not recordings:
        raise RuntimeError(
            f"R26_CHILD_NO_RECORDINGS: dataset={profile.dataset_id}; subject={task['subject']}"
        )
    expected_subject = str(task["subject"])
    observed = {str(recording.subject_id) for recording in recordings}
    # Different adapters may zero-pad or prefix subject IDs. The profile-level
    # process boundary is the authoritative subject selection; record IDs remain
    # source-native and are not rewritten here.
    return recordings, files, observed, expected_subject


def _deterministic_recording_role(recording: Any, split_profile: dict[str, Any]) -> str:
    import hashlib as _hashlib
    roles = list(split_profile["roles"]); ratios = dict(split_profile["ratios"]); keys = list(split_profile["group_keys"]); seed = split_profile["seed"]
    unit = "|".join(str(getattr(recording, key)) for key in keys)
    digest = _hashlib.sha256(f"{seed}|{unit}".encode()).hexdigest()
    value = int(digest[:16], 16) / (16**16 - 1)
    total = 0.0; selected = roles[-1]
    for role in roles:
        total += float(ratios[role])
        if value <= total:
            selected = role; break
    return selected


def _child_descriptor(task: dict[str, Any]) -> dict[str, Any]:
    recordings, files, observed, expected = _load_subject_recordings(task)
    output = Path(task["output_dir"]); output.mkdir(parents=True, exist_ok=True)
    descriptor_path = output / "descriptors.jsonl"
    fit_stats_path = output / "pass1_fit_stats.jsonl"
    for stale_path in (descriptor_path, fit_stats_path, output / "result.json"):
        stale_path.unlink(missing_ok=True)
    rows = [_descriptor_from_recording(recording) for recording in recordings]
    _append_jsonl(descriptor_path, rows)
    fit_rows = []
    if bool(task.get("collect_fit_stats")):
        import numpy as np
        # Collect exact raw per-recording summaries for every recording. Stage 13
        # later filters them by the actual frozen split assignment, which removes
        # any dependency on a pre-split approximation and avoids an extra source
        # reload. Blocks cap temporary memory while preserving float64 semantics.
        block_samples = int(task.get("fit_stat_block_samples", 262144))
        for recording in recordings:
            signal = recording.signal
            channel_count = int(signal.shape[0])
            count = 0
            mean = np.zeros(channel_count, dtype=np.float64)
            m2 = np.zeros(channel_count, dtype=np.float64)
            for start in range(0, int(signal.shape[1]), block_samples):
                stop = min(int(signal.shape[1]), start + block_samples)
                block = np.asarray(signal[:, start:stop], dtype=np.float64)
                n_b = int(block.shape[1])
                if n_b == 0:
                    continue
                mean_b = block.mean(axis=1, dtype=np.float64)
                centered_b = block - mean_b[:, None]
                m2_b = np.sum(centered_b * centered_b, axis=1, dtype=np.float64)
                if count == 0:
                    count = n_b
                    mean = mean_b.copy()
                    m2 = m2_b.copy()
                else:
                    delta = mean_b - mean
                    total = count + n_b
                    mean = mean + delta * (n_b / total)
                    m2 = m2 + m2_b + delta * delta * (count * n_b / total)
                    count = total
                del block, mean_b, centered_b, m2_b
            if count != int(signal.shape[1]):
                raise RuntimeError(
                    f"R26_PASS1_FIT_SAMPLE_COUNT_MISMATCH: "
                    f"source={_recording_source_unit(recording)}; "
                    f"expected={signal.shape[1]}; observed={count}"
                )
            fit_rows.append({
                "source_unit": _recording_source_unit(recording),
                "channel_names": [str(v) for v in recording.channel_names],
                "count": count,
                "mean": [float(v) for v in mean],
                "m2": [float(v) for v in m2],
                "shape": [int(v) for v in signal.shape],
                "candidate_role": _deterministic_recording_role(recording, dict(task["split_profile"])),
            })
            del mean, m2
            _trim_memory()
        _append_jsonl(fit_stats_path, fit_rows)
    result = {
        "action": "descriptor",
        "dataset_id": task["profile"]["dataset_id"],
        "subject": int(task["subject"]),
        "recordings": len(rows),
        "events": sum(len(row["events"]) for row in rows),
        "source_files_resolved": len(files),
        "observed_subject_ids": sorted(observed),
        "expected_profile_subject": expected,
        "descriptor_path": str(descriptor_path),
        "fit_stats_path": str(fit_stats_path),
        "fit_stat_recordings": len(fit_rows),
        "child_peak_rss_bytes": _rss_bytes(),
    }
    _atomic_json(output / "result.json", result)
    return result



def _ensure_h5_group(handle: Any, shape: tuple[int, int], dtype: str = "float32"):
    import h5py
    import numpy as np

    resolved_dtype = np.dtype(dtype)
    if resolved_dtype != np.dtype("float32"):
        raise RuntimeError(
            "R34_HDF5_WINDOW_DTYPE_MUST_BE_FLOAT32: "
            f"observed={resolved_dtype}"
        )
    key = f"c{shape[0]}_t{shape[1]}_f32"
    group = handle.require_group(f"window_groups/{key}")
    if "signals" not in group:
        group.create_dataset(
            "signals",
            shape=(0, shape[0], shape[1]),
            maxshape=(None, shape[0], shape[1]),
            dtype="float32",
            chunks=(1, shape[0], shape[1]),
            compression="gzip",
            compression_opts=1,
            shuffle=True,
            fletcher32=True,
        )
        group.create_dataset(
            "window_ids",
            shape=(0,),
            maxshape=(None,),
            dtype=h5py.string_dtype(encoding="utf-8"),
            chunks=(256,),
        )
    elif str(group["signals"].dtype) != "float32":
        raise RuntimeError(
            "R34_EXISTING_HDF5_GROUP_DTYPE_MISMATCH: "
            f"group={group.name}; dtype={group['signals'].dtype}"
        )
    return key, group




def _append_h5_window(handle: Any, array: Any, window_id: str) -> tuple[str, int]:
    import numpy as np

    resolved = np.asarray(array)
    if resolved.dtype != np.dtype("float32"):
        raise RuntimeError(
            "R34_WINDOW_ARRAY_DTYPE_MISMATCH: "
            f"expected=float32; observed={resolved.dtype}"
        )
    if resolved.ndim != 2:
        raise RuntimeError(
            "R34_WINDOW_ARRAY_RANK_MISMATCH: "
            f"expected=2; observed={resolved.ndim}"
        )
    key, group = _ensure_h5_group(
        handle,
        tuple(int(v) for v in resolved.shape),
        str(resolved.dtype),
    )
    signals = group["signals"]
    ids = group["window_ids"]
    row = int(signals.shape[0])
    signals.resize(row + 1, axis=0)
    ids.resize(row + 1, axis=0)
    signals[row] = resolved
    ids[row] = window_id
    return f"window_groups/{key}", row




def _child_materialize(task: dict[str, Any]) -> dict[str, Any]:
    import h5py
    import numpy as np
    from iharq.canonical import semantic_hash
    from iharq.layer1_data_protocol.preprocessing import FitState, transform_recording
    from iharq.layer1_data_protocol.quality import annotate
    from iharq.layer1_data_protocol.labels import map_event_label
    from iharq.layer1_data_protocol.splits import recording_role
    from iharq.layer1_data_protocol.records import make_record

    recordings, files, observed, expected = _load_subject_recordings(task)
    output = Path(task["output_dir"])
    output.mkdir(parents=True, exist_ok=True)

    fit_payload = task["fit_state"]
    mean = None if fit_payload.get("mean") is None else np.asarray(fit_payload["mean"], dtype=np.float64)
    std = None if fit_payload.get("std") is None else np.asarray(fit_payload["std"], dtype=np.float64)
    fit_state = FitState(mean, std, list(fit_payload["source_ids"]), str(fit_payload["state_hash"]))
    operations = list(task["operations"])
    assignment = dict(task["assignment"])
    split_keys = list(task["split_keys"])
    label_record = dict(task["label_record"])
    preprocessing_record = dict(task["preprocessing_record"])
    split_record = dict(task["split_record"])
    quality_profile = dict(task["quality_profile"])
    window_profile = dict(task["window_profile"])
    config_id = str(task["config_id"])
    dataset_record_id = str(task["dataset_record_id"])
    split_id = split_record["record_id"]

    required_window_contract = {
        "start_offset_samples": 80,
        "duration_samples": 480,
        "stride_samples": 480,
        "target_sampling_hz": 160,
        "last_window_policy": "ONE_WINDOW_PER_INCLUDED_SOURCE_EVENT",
        "bounds_policy": "REJECT_OUT_OF_BOUNDS",
    }
    mismatches = {
        key: {"expected": expected_value, "observed": window_profile.get(key)}
        for key, expected_value in required_window_contract.items()
        if window_profile.get(key) != expected_value
    }
    if mismatches:
        raise RuntimeError(
            "R34_FROZEN_WINDOW_CONTRACT_MISMATCH: "
            + json.dumps(mismatches, sort_keys=True)
        )

    offset = 80
    duration_samples = 480
    stride_samples = 480
    target_hz = 160.0

    shard_filename = str(task["shard_filename"])
    shard_path = output / shard_filename
    window_records_path = output / "window_records.jsonl"
    window_index_path = output / "window_index.jsonl"
    quality_records_path = output / "quality_records.jsonl"
    quality_summaries_path = output / "quality_summaries.jsonl"
    location_path = output / "window_locations.jsonl"
    invalid_windows_path = output / "invalid_windows.jsonl"
    result_path = output / "result.json"

    for stale_path in (
        shard_path,
        window_records_path,
        window_index_path,
        quality_records_path,
        quality_summaries_path,
        location_path,
        invalid_windows_path,
        result_path,
    ):
        stale_path.unlink(missing_ok=True)
    for path in (
        window_records_path,
        window_index_path,
        quality_records_path,
        quality_summaries_path,
        location_path,
        invalid_windows_path,
    ):
        path.touch()

    window_count = 0
    logical_window_bytes = 0
    event_ids: set[str] = set()
    roles: set[str] = set()
    h5_handle = None

    quality_rows_all: list[dict[str, Any]] = []
    quality_summaries: list[dict[str, Any]] = []
    invalid_windows: list[dict[str, Any]] = []
    window_records_buffer: list[dict[str, Any]] = []
    index_buffer: list[dict[str, Any]] = []
    location_buffer: list[dict[str, Any]] = []

    try:
        for source_recording in recordings:
            recording = transform_recording(
                source_recording,
                operations,
                fit_state,
            )
            if abs(float(recording.sampling_hz) - target_hz) > 1e-9:
                raise RuntimeError(
                    "R34_TRANSFORMED_SAMPLING_RATE_MISMATCH: "
                    f"source={_recording_source_unit(recording)}; "
                    f"observed={recording.sampling_hz}"
                )
            if np.asarray(recording.signal).dtype != np.dtype("float32"):
                raise RuntimeError(
                    "R34_TRANSFORMED_SIGNAL_DTYPE_MISMATCH: "
                    f"source={_recording_source_unit(recording)}; "
                    f"observed={np.asarray(recording.signal).dtype}"
                )
            if len(recording.channel_names) != int(recording.signal.shape[0]):
                raise RuntimeError(
                    "R34_TRANSFORMED_CHANNEL_GEOMETRY_MISMATCH: "
                    f"source={_recording_source_unit(recording)}"
                )

            qrows, qsummary = annotate(
                recording,
                quality_profile,
                config_id,
                dataset_record_id,
            )
            quality_rows_all.extend(qrows)
            quality_summaries.append(qsummary)

            role = recording_role(recording, assignment, split_keys)
            roles.add(role)

            for event in recording.events:
                normalized = map_event_label(event.original_label, label_record)
                if normalized is None:
                    continue

                source_sample = event.metadata.get("original_source_event_sample")
                resampled_sample = event.metadata.get("resampled_event_sample")
                if source_sample is None or resampled_sample is None:
                    invalid_windows.append(
                        {
                            "dataset_id": recording.dataset_id,
                            "subject_id": recording.subject_id,
                            "session_id": recording.session_id,
                            "run_id": recording.run_id,
                            "event_id": event.event_id,
                            "reason": "MISSING_PARENT_EVENT_SAMPLE_LINEAGE",
                        }
                    )
                    continue

                start = int(resampled_sample) + offset
                end = start + duration_samples
                if start < 0 or end > int(recording.signal.shape[1]):
                    invalid_windows.append(
                        {
                            "dataset_id": recording.dataset_id,
                            "subject_id": recording.subject_id,
                            "session_id": recording.session_id,
                            "run_id": recording.run_id,
                            "event_id": event.event_id,
                            "original_source_event_sample": int(source_sample),
                            "resampled_event_sample": int(resampled_sample),
                            "start": start,
                            "end": end,
                            "samples": int(recording.signal.shape[1]),
                            "reason": "WINDOW_OUT_OF_BOUNDS",
                        }
                    )
                    continue

                identity = {
                    "dataset": recording.dataset_id,
                    "subject": recording.subject_id,
                    "session": recording.session_id,
                    "run": recording.run_id,
                    "event": event.event_id,
                    "original_event_sample": int(source_sample),
                    "resampled_event_sample": int(resampled_sample),
                    "start": start,
                    "stop": end,
                    "split_record_id": split_id,
                    "role": role,
                    "config": config_id,
                }
                digest = semantic_hash(identity)
                wid = "window:" + digest[:20]
                if h5_handle is None:
                    h5_handle = h5py.File(shard_path, "w")
                    h5_handle.attrs["format"] = "IHARQ_P01_L1_LOSSLESS_WINDOW_SHARD_R34"
                    h5_handle.attrs["scientific_freeze"] = POLICY["scientific_freeze_unchanged"]
                    h5_handle.attrs["config_id"] = config_id
                    h5_handle.attrs["dataset_id"] = str(recording.dataset_id)
                    h5_handle.attrs["subject_profile"] = str(task["subject"])
                    h5_handle.attrs["signal_dtype"] = "float32"
                    h5_handle.attrs["window_start_offset_samples"] = offset
                    h5_handle.attrs["window_duration_samples"] = duration_samples
                    h5_handle.attrs["window_stride_samples"] = stride_samples
                    h5_handle.attrs["event_resampling"] = "MNE_POLYPHASE_JOINT_EVENTS"

                window = np.asarray(
                    recording.signal[:, start:end],
                    dtype=np.float32,
                )
                if window.shape[1] != duration_samples:
                    raise RuntimeError(
                        "R34_WINDOW_SHAPE_MISMATCH: "
                        f"window={wid}; shape={window.shape}"
                    )
                group_path, row_number = _append_h5_window(
                    h5_handle,
                    window,
                    wid,
                )
                local_pointer = (
                    "external_artifact_pointers/window_to_shard.jsonl"
                    f"#window_id={wid}"
                )
                payload = {
                    "window_id": wid,
                    "parent_event_id": event.event_id,
                    "dataset_id": recording.dataset_id,
                    "subject_id": recording.subject_id,
                    "session_id": recording.session_id,
                    "run_id": recording.run_id,
                    "split_record_id": split_id,
                    "preprocessing_record_id": preprocessing_record["record_id"],
                    "label_map_record_id": label_record["record_id"],
                    "original_source_event_sample": int(source_sample),
                    "resampled_event_sample": int(resampled_sample),
                    "start_offset_samples": offset,
                    "start_sample": start,
                    "stop_sample": end,
                    "duration_samples": duration_samples,
                    "stride_samples": stride_samples,
                    "overlap_group_id": event.event_id,
                    "normalized_label": normalized,
                    "original_label": event.original_label,
                    "role": role,
                    "signal_pointer": local_pointer,
                    "channel_mask_id": None,
                }
                source_ids = [
                    dataset_record_id,
                    split_id,
                    preprocessing_record["record_id"],
                    label_record["record_id"],
                ]
                record = make_record(
                    "WindowRecord",
                    payload,
                    config_id,
                    source_ids,
                    lifecycle_status="VALIDATED",
                )
                sample_hash = semantic_hash(
                    {
                        "shape": list(window.shape),
                        "head": [
                            str(float(value))
                            for value in window.reshape(-1)[:128]
                        ],
                    }
                )
                index_row = {
                    "window_record_id": record["record_id"],
                    "path": local_pointer,
                    "role": role,
                    "label": normalized,
                    "event_id": event.event_id,
                    "split_record_id": split_id,
                    "dataset_id": recording.dataset_id,
                    "subject_id": recording.subject_id,
                    "session_id": recording.session_id,
                    "run_id": recording.run_id,
                    "overlap_group_id": event.event_id,
                    "sample_hash": sample_hash,
                    "external_shard_filename": shard_filename,
                    "hdf5_group": group_path,
                    "hdf5_row": row_number,
                }
                location_row = {
                    "window_id": wid,
                    "window_record_id": record["record_id"],
                    "shard_filename": shard_filename,
                    "hdf5_group": group_path,
                    "hdf5_row": row_number,
                    "shape": list(window.shape),
                    "dtype": "float32",
                }
                window_records_buffer.append(record)
                index_buffer.append(index_row)
                location_buffer.append(location_row)
                window_count += 1
                logical_window_bytes += int(window.nbytes)
                event_ids.add(str(event.event_id))

                if len(window_records_buffer) >= 256:
                    _append_jsonl(window_records_path, window_records_buffer)
                    window_records_buffer.clear()
                    _append_jsonl(window_index_path, index_buffer)
                    index_buffer.clear()
                    _append_jsonl(location_path, location_buffer)
                    location_buffer.clear()
                if window_count % 256 == 0 and h5_handle is not None:
                    h5_handle.flush()

            del recording
            _trim_memory()

        if window_records_buffer:
            _append_jsonl(window_records_path, window_records_buffer)
        if index_buffer:
            _append_jsonl(window_index_path, index_buffer)
        if location_buffer:
            _append_jsonl(location_path, location_buffer)
        if quality_rows_all:
            _append_jsonl(quality_records_path, quality_rows_all)
        if quality_summaries:
            _append_jsonl(quality_summaries_path, quality_summaries)
        if invalid_windows:
            _append_jsonl(invalid_windows_path, invalid_windows)
    finally:
        if h5_handle is not None:
            h5_handle.flush()
            h5_handle.close()

    shard = None
    if shard_path.is_file():
        verified_rows = 0
        with h5py.File(shard_path, "r") as verify_handle:
            format_value = str(verify_handle.attrs.get("format", ""))
            if format_value != "IHARQ_P01_L1_LOSSLESS_WINDOW_SHARD_R34":
                raise RuntimeError(f"R34_HDF5_FORMAT_MISMATCH: {format_value}")
            if str(verify_handle.attrs.get("signal_dtype", "")) != "float32":
                raise RuntimeError("R34_HDF5_SIGNAL_DTYPE_ATTRIBUTE_MISMATCH")
            for group_name in sorted(verify_handle.get("window_groups", {})):
                group = verify_handle[f"window_groups/{group_name}"]
                signals = group["signals"]
                identifiers = group["window_ids"]
                if str(signals.dtype) != "float32":
                    raise RuntimeError(
                        f"R34_HDF5_GROUP_DTYPE_MISMATCH: group={group_name}; dtype={signals.dtype}"
                    )
                if int(signals.shape[0]) != int(identifiers.shape[0]):
                    raise RuntimeError(
                        f"R34_HDF5_SIGNAL_ID_COUNT_MISMATCH: group={group_name}; "
                        f"signals={signals.shape[0]}; ids={identifiers.shape[0]}"
                    )
                if int(signals.shape[2]) != duration_samples:
                    raise RuntimeError(
                        f"R34_HDF5_WINDOW_DURATION_MISMATCH: group={group_name}; "
                        f"observed={signals.shape[2]}"
                    )
                verified_rows += int(signals.shape[0])
        if verified_rows != window_count:
            raise RuntimeError(
                f"R34_HDF5_WINDOW_COUNT_MISMATCH: expected={window_count}; observed={verified_rows}"
            )
        shard = {
            "path": str(shard_path),
            "filename": shard_filename,
            "bytes": shard_path.stat().st_size,
            "sha256": _sha256(shard_path),
            "verified_window_rows": verified_rows,
            "logical_window_bytes": logical_window_bytes,
            "compression_ratio_to_logical": (
                shard_path.stat().st_size / logical_window_bytes
                if logical_window_bytes
                else None
            ),
            "verification_status": "PASS",
            "signal_dtype": "float32",
            "window_duration_samples": duration_samples,
        }

    result = {
        "action": "materialize",
        "dataset_id": task["profile"]["dataset_id"],
        "subject": int(task["subject"]),
        "quality_records": len(quality_rows_all),
        "quality_summaries": len(quality_summaries),
        "hard_invalid": sum(int(row.get("hard_invalid", 0)) for row in quality_summaries),
        "window_count": window_count,
        "invalid_window_count": len(invalid_windows),
        "logical_window_bytes": logical_window_bytes,
        "event_count": len(event_ids),
        "roles": sorted(roles),
        "window_records_path": str(window_records_path),
        "window_index_path": str(window_index_path),
        "quality_records_path": str(quality_records_path),
        "quality_summaries_path": str(quality_summaries_path),
        "invalid_windows_path": str(invalid_windows_path),
        "window_locations_path": str(location_path),
        "shard": shard,
        "child_peak_rss_bytes": _rss_bytes(),
    }
    _atomic_json(result_path, result)
    return result



# =====================================================================
# R49 additive A4 R2 matched-window evidence implementation
# =====================================================================

R42_A4_WINDOW_FAMILY = {
    "window_family_id": os.environ.get(
        "IHARQ_A4_WINDOW_FAMILY_ID",
        "P01-L1-A4-WINDOW-FAMILY-FREEZE-R2",
    ),
    "protocol_status": os.environ.get(
        "IHARQ_A4_PROTOCOL_STATUS",
        "DATA_READY_PROTOCOL_SYNC_REQUIRED",
    ),
    "target_sampling_hz": 160,
    "materialized_profile": {
        "profile_id": "A4_LONG_MATCHED_3P5S_R2",
        "event_anchor": "MI_CUE_ONSET",
        "start_offset_samples": 0,
        "duration_samples": 560,
        "duration_seconds": "3.5",
        "view_kind": "MATERIALIZED",
    },
    "multi_window_profile": {
        "profile_id": "A4_MULTI_3X2S_UNIFORM_0P75S_R2",
        "member_count": 3,
        "member_duration_samples": 320,
        "member_duration_seconds": "2.0",
        "member_stride_samples": 120,
        "member_stride_seconds": "0.75",
        "member_slices": [
            {
                "member_index": 1,
                "condition_id": "A4_MULTI_3X2S_M1_R2",
                "slice_start": 0,
                "slice_stop": 320,
                "start_offset_seconds": "0.0",
                "stop_offset_seconds": "2.0",
            },
            {
                "member_index": 2,
                "condition_id": "A4_MULTI_3X2S_M2_R2",
                "slice_start": 120,
                "slice_stop": 440,
                "start_offset_seconds": "0.75",
                "stop_offset_seconds": "2.75",
            },
            {
                "member_index": 3,
                "condition_id": "A4_MULTI_3X2S_M3_R2",
                "slice_start": 240,
                "slice_stop": 560,
                "start_offset_seconds": "1.5",
                "stop_offset_seconds": "3.5",
            },
        ],
        "view_kind": "REGISTERED_VIRTUAL_SLICE",
        "storage_rule": (
            "VIEWS_REFERENCE_THE_LOSSLESS_MATCHED_3P5S_EVENT_TENSOR; "
            "OVERLAPPING_NUMERICAL_BYTES_ARE_NOT_DUPLICATED"
        ),
    },
}


R42_A4_READER_SOURCE = r"""from __future__ import annotations

from pathlib import Path
import json
import h5py
import numpy as np


def read_jsonl(path: str | Path):
    with Path(path).open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(
                    f"A4 JSONL parse failure at {path}:{line_number}"
                ) from exc
            if not isinstance(row, dict):
                raise RuntimeError(
                    f"A4 JSONL row is not an object at {path}:{line_number}"
                )
            yield row


def resolve_window(
    dataset_root: str | Path,
    location_row: dict,
) -> np.ndarray:
    root = Path(dataset_root)
    shard = root / str(location_row["shard_filename"])
    if not shard.is_file():
        raise FileNotFoundError(shard)

    group_path = str(location_row["hdf5_group"])
    row = int(location_row["hdf5_row"])
    expected_storage_id = str(location_row["storage_id"])

    with h5py.File(shard, "r") as handle:
        signals_path = group_path + "/signals"
        ids_path = group_path + "/window_ids"
        if signals_path not in handle or ids_path not in handle:
            raise RuntimeError(
                f"A4 HDF5 group missing: {group_path}"
            )
        signals = handle[signals_path]
        identifiers = handle[ids_path]
        if row < 0 or row >= int(signals.shape[0]) or row >= int(identifiers.shape[0]):
            raise RuntimeError(
                f"A4 HDF5 row out of range: row={row}; group={group_path}"
            )
        stored_id = identifiers[row]
        if isinstance(stored_id, bytes):
            stored_id = stored_id.decode("utf-8")
        if str(stored_id) != expected_storage_id:
            raise RuntimeError(
                "A4 HDF5 storage identity mismatch: "
                f"expected={expected_storage_id}; observed={stored_id}"
            )
        array = np.asarray(signals[row], dtype=np.float32)

    start = int(location_row.get("slice_start", 0))
    stop = int(location_row.get("slice_stop", array.shape[1]))
    if start < 0 or stop < start or stop > int(array.shape[1]):
        raise RuntimeError(
            f"A4 slice out of range: start={start}; stop={stop}; width={array.shape[1]}"
        )
    resolved = np.asarray(array[:, start:stop], dtype=np.float32)

    expected = [int(value) for value in location_row["shape"]]
    if list(resolved.shape) != expected:
        raise RuntimeError(
            f"A4 view shape mismatch: expected={expected}; "
            f"observed={list(resolved.shape)}"
        )
    if str(resolved.dtype) != str(location_row.get("dtype", "float32")):
        raise RuntimeError(
            "A4 view dtype mismatch: "
            f"expected={location_row.get('dtype')}; observed={resolved.dtype}"
        )
    if not np.isfinite(resolved).all():
        raise RuntimeError("A4 resolved window contains non-finite values")
    return resolved
"""


def _r42_a4_config_id(base_config_id: str) -> str:
    from iharq.canonical import semantic_hash

    return semantic_hash(
        {
            "base_config_id": base_config_id,
            "a4_window_family": R42_A4_WINDOW_FAMILY,
        }
    )


def _r42_child_materialize_a4(
    task: dict[str, Any],
) -> dict[str, Any]:
    import h5py
    import numpy as np

    from iharq.canonical import semantic_hash
    from iharq.layer1_data_protocol.preprocessing import (
        FitState,
        transform_recording,
    )
    from iharq.layer1_data_protocol.quality import annotate
    from iharq.layer1_data_protocol.labels import map_event_label
    from iharq.layer1_data_protocol.splits import recording_role
    from iharq.layer1_data_protocol.records import make_record

    recordings, files, observed, expected = _load_subject_recordings(
        task
    )
    output = Path(task["output_dir"])
    output.mkdir(parents=True, exist_ok=True)

    fit_payload = task["fit_state"]
    mean = (
        None
        if fit_payload.get("mean") is None
        else np.asarray(fit_payload["mean"], dtype=np.float64)
    )
    std = (
        None
        if fit_payload.get("std") is None
        else np.asarray(fit_payload["std"], dtype=np.float64)
    )
    fit_state = FitState(
        mean,
        std,
        list(fit_payload["source_ids"]),
        str(fit_payload["state_hash"]),
    )

    operations = list(task["operations"])
    assignment = dict(task["assignment"])
    split_keys = list(task["split_keys"])
    label_record = dict(task["label_record"])
    preprocessing_record = dict(task["preprocessing_record"])
    split_record = dict(task["split_record"])
    quality_profile = dict(task["quality_profile"])
    base_config_id = str(task["base_config_id"])
    a4_config_id = str(task["a4_config_id"])
    dataset_record_id = str(task["dataset_record_id"])
    split_id = split_record["record_id"]
    family = dict(task["a4_window_family"])
    expected_core_event_ids = {
        str(value)
        for value in task.get("expected_core_event_ids", [])
    }
    if not expected_core_event_ids:
        raise RuntimeError(
            "R49_A4_EXPECTED_CORE_EVENT_SET_MISSING"
        )

    materialized = dict(family["materialized_profile"])
    multi = dict(family["multi_window_profile"])

    target_hz = float(family["target_sampling_hz"])
    full_offset = int(materialized["start_offset_samples"])
    full_duration = int(materialized["duration_samples"])

    if target_hz != 160.0:
        raise RuntimeError(
            f"R49_A4_TARGET_RATE_MISMATCH: {target_hz}"
        )
    if full_offset != 0 or full_duration != 560:
        raise RuntimeError(
            "R49_A4_FULL3P5S_CONTRACT_MISMATCH"
        )
    if int(multi["member_count"]) != 3:
        raise RuntimeError(
            "R49_A4_MULTI_MEMBER_COUNT_MUST_BE_THREE"
        )

    shard_filename = str(task["shard_filename"])
    shard_path = output / shard_filename

    records_path = output / "a4_window_records.jsonl"
    index_path = output / "a4_window_index.jsonl"
    groups_path = output / "a4_group_index.jsonl"
    locations_path = output / "a4_window_locations.jsonl"
    quality_records_path = output / "quality_records.jsonl"
    quality_summaries_path = output / "quality_summaries.jsonl"
    invalid_path = output / "a4_invalid_windows.jsonl"
    result_path = output / "result.json"

    for stale in (
        shard_path,
        records_path,
        index_path,
        groups_path,
        locations_path,
        quality_records_path,
        quality_summaries_path,
        invalid_path,
        result_path,
    ):
        stale.unlink(missing_ok=True)

    for path in (
        records_path,
        index_path,
        groups_path,
        locations_path,
        quality_records_path,
        quality_summaries_path,
        invalid_path,
    ):
        path.touch()

    record_buffer: list[dict[str, Any]] = []
    index_buffer: list[dict[str, Any]] = []
    group_buffer: list[dict[str, Any]] = []
    location_buffer: list[dict[str, Any]] = []
    quality_rows_all: list[dict[str, Any]] = []
    quality_summaries: list[dict[str, Any]] = []
    invalid_rows: list[dict[str, Any]] = []

    materialized_event_count = 0
    window_record_count = 0
    logical_stored_bytes = 0
    source_event_ids: set[str] = set()
    roles: set[str] = set()
    h5_handle = None

    try:
        for source_recording in recordings:
            recording = transform_recording(
                source_recording,
                operations,
                fit_state,
            )

            signal = np.asarray(recording.signal)
            if abs(float(recording.sampling_hz) - target_hz) > 1e-9:
                raise RuntimeError(
                    "R49_A4_TRANSFORMED_RATE_MISMATCH: "
                    f"{_recording_source_unit(recording)}"
                )
            if signal.dtype != np.dtype("float32"):
                raise RuntimeError(
                    "R49_A4_SIGNAL_DTYPE_MISMATCH: "
                    f"{signal.dtype}"
                )
            if signal.ndim != 2:
                raise RuntimeError(
                    f"R49_A4_SIGNAL_RANK_MISMATCH: {signal.ndim}"
                )
            if len(recording.channel_names) != int(signal.shape[0]):
                raise RuntimeError(
                    "R49_A4_CHANNEL_GEOMETRY_MISMATCH"
                )

            qrows, qsummary = annotate(
                recording,
                quality_profile,
                base_config_id,
                dataset_record_id,
            )
            quality_rows_all.extend(qrows)
            quality_summaries.append(qsummary)

            role = recording_role(
                recording,
                assignment,
                split_keys,
            )
            roles.add(role)

            for event in recording.events:
                normalized = map_event_label(
                    event.original_label,
                    label_record,
                )
                if normalized is None:
                    continue

                event_id = str(event.event_id)
                if event_id not in expected_core_event_ids:
                    continue

                source_sample = event.metadata.get(
                    "original_source_event_sample"
                )
                resampled_sample = event.metadata.get(
                    "resampled_event_sample"
                )
                if source_sample is None or resampled_sample is None:
                    invalid_rows.append(
                        {
                            "dataset_id": recording.dataset_id,
                            "subject_id": recording.subject_id,
                            "session_id": recording.session_id,
                            "run_id": recording.run_id,
                            "event_id": event.event_id,
                            "reason": (
                                "MISSING_PARENT_EVENT_SAMPLE_LINEAGE"
                            ),
                        }
                    )
                    continue

                full_start = int(resampled_sample) + full_offset
                full_stop = full_start + full_duration

                if (
                    full_start < 0
                    or full_stop > int(signal.shape[1])
                ):
                    invalid_rows.append(
                        {
                            "dataset_id": recording.dataset_id,
                            "subject_id": recording.subject_id,
                            "session_id": recording.session_id,
                            "run_id": recording.run_id,
                            "event_id": event.event_id,
                            "resampled_event_sample": int(
                                resampled_sample
                            ),
                            "start": full_start,
                            "stop": full_stop,
                            "available_samples": int(signal.shape[1]),
                            "reason": "A4_FULL3P5S_OUT_OF_BOUNDS",
                        }
                    )
                    continue

                full_window = np.asarray(
                    signal[:, full_start:full_stop],
                    dtype=np.float32,
                )
                if list(full_window.shape) != [
                    int(signal.shape[0]),
                    560,
                ]:
                    raise RuntimeError(
                        "R49_A4_FULL_WINDOW_SHAPE_MISMATCH: "
                        f"{list(full_window.shape)}"
                    )
                if not np.isfinite(full_window).all():
                    raise RuntimeError(
                        "R49_A4_FULL_WINDOW_NONFINITE"
                    )

                storage_identity = {
                    "window_family_id": family["window_family_id"],
                    "dataset": recording.dataset_id,
                    "subject": recording.subject_id,
                    "session": recording.session_id,
                    "run": recording.run_id,
                    "event": event.event_id,
                    "original_event_sample": int(source_sample),
                    "resampled_event_sample": int(resampled_sample),
                    "full_start": full_start,
                    "full_stop": full_stop,
                    "split_record_id": split_id,
                    "role": role,
                    "a4_config_id": a4_config_id,
                }
                storage_id = (
                    "a4-storage:"
                    + semantic_hash(storage_identity)[:20]
                )

                if h5_handle is None:
                    h5_handle = h5py.File(shard_path, "w")
                    h5_handle.attrs["format"] = (
                        "IHARQ_P01_L1_A4_FULL3P5S_SHARD_R2"
                    )
                    h5_handle.attrs["base_scientific_freeze"] = (
                        POLICY["scientific_freeze_unchanged"]
                    )
                    h5_handle.attrs["a4_window_family_id"] = (
                        family["window_family_id"]
                    )
                    h5_handle.attrs["base_config_id"] = base_config_id
                    h5_handle.attrs["a4_config_id"] = a4_config_id
                    h5_handle.attrs["dataset_id"] = str(
                        recording.dataset_id
                    )
                    h5_handle.attrs["subject_profile"] = str(
                        task["subject"]
                    )
                    h5_handle.attrs["signal_dtype"] = "float32"
                    h5_handle.attrs["materialized_duration_samples"] = 560
                    h5_handle.attrs["event_resampling"] = (
                        "MNE_POLYPHASE_JOINT_EVENTS"
                    )

                group_path, hdf5_row = _append_h5_window(
                    h5_handle,
                    full_window,
                    storage_id,
                )

                common_payload = {
                    "parent_event_id": event.event_id,
                    "dataset_id": recording.dataset_id,
                    "subject_id": recording.subject_id,
                    "session_id": recording.session_id,
                    "run_id": recording.run_id,
                    "split_record_id": split_id,
                    "preprocessing_record_id": (
                        preprocessing_record["record_id"]
                    ),
                    "label_map_record_id": (
                        label_record["record_id"]
                    ),
                    "original_source_event_sample": int(source_sample),
                    "resampled_event_sample": int(resampled_sample),
                    "normalized_label": normalized,
                    "original_label": event.original_label,
                    "role": role,
                    "overlap_group_id": event.event_id,
                    "window_family_id": family["window_family_id"],
                    "protocol_status": family["protocol_status"],
                    "a4_group_id": (
                        "a4-group:"
                        + semantic_hash(
                            {
                                "event": event.event_id,
                                "family": family["window_family_id"],
                                "config": a4_config_id,
                            }
                        )[:20]
                    ),
                }

                source_ids = [
                    dataset_record_id,
                    split_id,
                    preprocessing_record["record_id"],
                    label_record["record_id"],
                ]

                # Matched 3.5-second longer-window control.
                long_window_id = (
                    "a4-window:"
                    + semantic_hash(
                        {
                            **storage_identity,
                            "condition": materialized["profile_id"],
                        }
                    )[:20]
                )
                long_pointer = (
                    "external_artifact_pointers/"
                    "a4_window_to_shard.jsonl"
                    f"#window_id={long_window_id}"
                )
                long_payload = {
                    **common_payload,
                    "window_id": long_window_id,
                    "evidence_condition_id": (
                        materialized["profile_id"]
                    ),
                    "a4_component": "LONGER_WINDOW",
                    "view_kind": "MATERIALIZED_MATCHED_3P5S",
                    "start_offset_samples": 0,
                    "start_sample": full_start,
                    "stop_sample": full_stop,
                    "duration_samples": 560,
                    "stride_samples": 560,
                    "signal_pointer": long_pointer,
                    "channel_mask_id": None,
                    "evidence_availability_seconds": "3.5",
                }
                long_record = make_record(
                    "WindowRecord",
                    long_payload,
                    a4_config_id,
                    source_ids,
                    evidence_mode="IMPLEMENTATION",
                    lifecycle_status="VALIDATED",
                    evidence_role="DERIVED",
                    ablation_id="A4",
                    limitation_tags=[
                        "PUBLIC_EEG_ONLY",
                        "NON_CLINICAL",
                        "NO_DEPLOYMENT_CLAIM",
                        "A4_PROTOCOL_SYNC_REQUIRED",
                    ],
                )

                long_sample_hash = semantic_hash(
                    {
                        "shape": list(full_window.shape),
                        "head": [
                            str(float(value))
                            for value in full_window.reshape(-1)[:128]
                        ],
                    }
                )

                record_buffer.append(long_record)
                index_buffer.append(
                    {
                        "window_record_id": long_record["record_id"],
                        "window_id": long_window_id,
                        "event_id": event.event_id,
                        "dataset_id": recording.dataset_id,
                        "subject_id": recording.subject_id,
                        "session_id": recording.session_id,
                        "run_id": recording.run_id,
                        "role": role,
                        "label": normalized,
                        "split_record_id": split_id,
                        "a4_group_id": common_payload["a4_group_id"],
                        "a4_component": "LONGER_WINDOW",
                        "evidence_condition_id": (
                            materialized["profile_id"]
                        ),
                        "member_index": 0,
                        "sample_hash": long_sample_hash,
                        "external_shard_filename": shard_filename,
                        "hdf5_group": group_path,
                        "hdf5_row": hdf5_row,
                        "storage_id": storage_id,
                        "slice_start": 0,
                        "slice_stop": 560,
                        "view_kind": "MATERIALIZED_MATCHED_3P5S",
                    }
                )
                location_buffer.append(
                    {
                        "window_id": long_window_id,
                        "window_record_id": long_record["record_id"],
                        "shard_filename": shard_filename,
                        "hdf5_group": group_path,
                        "hdf5_row": hdf5_row,
                        "storage_id": storage_id,
                        "slice_start": 0,
                        "slice_stop": 560,
                        "shape": [int(signal.shape[0]), 560],
                        "dtype": "float32",
                        "view_kind": "MATERIALIZED_MATCHED_3P5S",
                        "a4_group_id": common_payload["a4_group_id"],
                    }
                )

                multi_record_ids: list[str] = []
                multi_window_ids: list[str] = []

                for member in multi["member_slices"]:
                    slice_start = int(member["slice_start"])
                    slice_stop = int(member["slice_stop"])
                    view = np.asarray(
                        full_window[:, slice_start:slice_stop],
                        dtype=np.float32,
                    )
                    if list(view.shape) != [
                        int(signal.shape[0]),
                        320,
                    ]:
                        raise RuntimeError(
                            "R49_A4_MULTI_VIEW_SHAPE_MISMATCH: "
                            f"{list(view.shape)}"
                        )

                    multi_window_id = (
                        "a4-window:"
                        + semantic_hash(
                            {
                                **storage_identity,
                                "condition": member["condition_id"],
                                "slice": [slice_start, slice_stop],
                            }
                        )[:20]
                    )
                    pointer = (
                        "external_artifact_pointers/"
                        "a4_window_to_shard.jsonl"
                        f"#window_id={multi_window_id}"
                    )
                    payload = {
                        **common_payload,
                        "window_id": multi_window_id,
                        "evidence_condition_id": (
                            member["condition_id"]
                        ),
                        "a4_component": "MULTI_WINDOW_MEMBER",
                        "view_kind": (
                            "REGISTERED_VIRTUAL_SLICE_OF_MATCHED_3P5S"
                        ),
                        "member_index": int(member["member_index"]),
                        "start_offset_samples": slice_start,
                        "start_sample": full_start + slice_start,
                        "stop_sample": full_start + slice_stop,
                        "duration_samples": 320,
                        "stride_samples": 120,
                        "slice_start": slice_start,
                        "slice_stop": slice_stop,
                        "signal_pointer": pointer,
                        "channel_mask_id": None,
                        "evidence_availability_seconds": (
                            str(member["stop_offset_seconds"])
                        ),
                    }
                    record = make_record(
                        "WindowRecord",
                        payload,
                        a4_config_id,
                        source_ids,
                        evidence_mode="IMPLEMENTATION",
                        lifecycle_status="VALIDATED",
                        evidence_role="DERIVED",
                        ablation_id="A4",
                        limitation_tags=[
                            "PUBLIC_EEG_ONLY",
                            "NON_CLINICAL",
                            "NO_DEPLOYMENT_CLAIM",
                            "A4_PROTOCOL_SYNC_REQUIRED",
                        ],
                    )

                    sample_hash = semantic_hash(
                        {
                            "shape": list(view.shape),
                            "head": [
                                str(float(value))
                                for value in view.reshape(-1)[:128]
                            ],
                        }
                    )

                    record_buffer.append(record)
                    index_buffer.append(
                        {
                            "window_record_id": record["record_id"],
                            "window_id": multi_window_id,
                            "event_id": event.event_id,
                            "dataset_id": recording.dataset_id,
                            "subject_id": recording.subject_id,
                            "session_id": recording.session_id,
                            "run_id": recording.run_id,
                            "role": role,
                            "label": normalized,
                            "split_record_id": split_id,
                            "a4_group_id": common_payload["a4_group_id"],
                            "a4_component": "MULTI_WINDOW_MEMBER",
                            "evidence_condition_id": (
                                member["condition_id"]
                            ),
                            "member_index": int(
                                member["member_index"]
                            ),
                            "sample_hash": sample_hash,
                            "external_shard_filename": shard_filename,
                            "hdf5_group": group_path,
                            "hdf5_row": hdf5_row,
                            "storage_id": storage_id,
                            "slice_start": slice_start,
                            "slice_stop": slice_stop,
                            "view_kind": (
                                "REGISTERED_VIRTUAL_SLICE_OF_MATCHED_3P5S"
                            ),
                        }
                    )
                    location_buffer.append(
                        {
                            "window_id": multi_window_id,
                            "window_record_id": record["record_id"],
                            "shard_filename": shard_filename,
                            "hdf5_group": group_path,
                            "hdf5_row": hdf5_row,
                            "storage_id": storage_id,
                            "slice_start": slice_start,
                            "slice_stop": slice_stop,
                            "shape": [int(signal.shape[0]), 320],
                            "dtype": "float32",
                            "view_kind": (
                                "REGISTERED_VIRTUAL_SLICE_OF_MATCHED_3P5S"
                            ),
                            "a4_group_id": common_payload["a4_group_id"],
                        }
                    )
                    multi_record_ids.append(record["record_id"])
                    multi_window_ids.append(multi_window_id)

                group_buffer.append(
                    {
                        "a4_group_id": common_payload["a4_group_id"],
                        "parent_event_id": event.event_id,
                        "dataset_id": recording.dataset_id,
                        "subject_id": recording.subject_id,
                        "session_id": recording.session_id,
                        "run_id": recording.run_id,
                        "role": role,
                        "normalized_label": normalized,
                        "split_record_id": split_id,
                        "long_window_record_id": (
                            long_record["record_id"]
                        ),
                        "long_window_id": long_window_id,
                        "storage_id": storage_id,
                        "multi_member_window_record_ids": (
                            multi_record_ids
                        ),
                        "multi_member_window_ids": multi_window_ids,
                        "expected_multi_member_count": 3,
                        "observed_multi_member_count": len(
                            multi_record_ids
                        ),
                        "complete": len(multi_record_ids) == 3,
                        "member_duration_samples": 320,
                        "member_stride_samples": 120,
                        "member_overlap_samples": 200,
                        "unique_source_event_span_samples": 560,
                        "evidence_availability_seconds": "3.5",
                        "causal_mode": (
                            "CAUSAL_AFTER_COMPLETE_3P5S_EVIDENCE"
                        ),
                        "protocol_status": family["protocol_status"],
                    }
                )

                materialized_event_count += 1
                window_record_count += 4
                logical_stored_bytes += int(full_window.nbytes)
                source_event_ids.add(str(event.event_id))

                if len(record_buffer) >= 256:
                    _append_jsonl(records_path, record_buffer)
                    record_buffer.clear()
                    _append_jsonl(index_path, index_buffer)
                    index_buffer.clear()
                    _append_jsonl(locations_path, location_buffer)
                    location_buffer.clear()

                if len(group_buffer) >= 256:
                    _append_jsonl(groups_path, group_buffer)
                    group_buffer.clear()

                if (
                    materialized_event_count % 256 == 0
                    and h5_handle is not None
                ):
                    h5_handle.flush()

            del recording
            _trim_memory()

        if record_buffer:
            _append_jsonl(records_path, record_buffer)
        if index_buffer:
            _append_jsonl(index_path, index_buffer)
        if group_buffer:
            _append_jsonl(groups_path, group_buffer)
        if location_buffer:
            _append_jsonl(locations_path, location_buffer)
        if quality_rows_all:
            _append_jsonl(
                quality_records_path,
                quality_rows_all,
            )
        if quality_summaries:
            _append_jsonl(
                quality_summaries_path,
                quality_summaries,
            )
        if invalid_rows:
            _append_jsonl(invalid_path, invalid_rows)
    finally:
        if h5_handle is not None:
            h5_handle.flush()
            h5_handle.close()

    if source_event_ids != expected_core_event_ids:
        missing = sorted(expected_core_event_ids - source_event_ids)
        unexpected = sorted(source_event_ids - expected_core_event_ids)
        raise RuntimeError(
            "R49_A4_SUBJECT_PARENT_EVENT_SET_MISMATCH: "
            f"missing={missing[:20]}; unexpected={unexpected[:20]}"
        )

    shard = None
    if shard_path.is_file():
        verified_rows = 0
        with h5py.File(shard_path, "r") as verify:
            if str(verify.attrs.get("format", "")) != (
                "IHARQ_P01_L1_A4_FULL3P5S_SHARD_R2"
            ):
                raise RuntimeError(
                    "R49_A4_HDF5_FORMAT_MISMATCH"
                )
            if str(verify.attrs.get("signal_dtype", "")) != "float32":
                raise RuntimeError(
                    "R49_A4_HDF5_DTYPE_ATTRIBUTE_MISMATCH"
                )
            for group_name in sorted(
                verify.get("window_groups", {})
            ):
                group = verify[f"window_groups/{group_name}"]
                signals = group["signals"]
                identifiers = group["window_ids"]
                if str(signals.dtype) != "float32":
                    raise RuntimeError(
                        "R49_A4_HDF5_GROUP_DTYPE_MISMATCH"
                    )
                if int(signals.shape[2]) != 560:
                    raise RuntimeError(
                        "R49_A4_HDF5_DURATION_MISMATCH"
                    )
                if int(signals.shape[0]) != int(
                    identifiers.shape[0]
                ):
                    raise RuntimeError(
                        "R49_A4_HDF5_SIGNAL_ID_COUNT_MISMATCH"
                    )
                verified_rows += int(signals.shape[0])

        if verified_rows != materialized_event_count:
            raise RuntimeError(
                "R49_A4_HDF5_EVENT_COUNT_MISMATCH: "
                f"expected={materialized_event_count}; "
                f"observed={verified_rows}"
            )

        shard = {
            "path": str(shard_path),
            "filename": shard_filename,
            "bytes": shard_path.stat().st_size,
            "sha256": _sha256(shard_path),
            "verified_materialized_event_rows": verified_rows,
            "logical_stored_bytes": logical_stored_bytes,
            "compression_ratio_to_logical": (
                shard_path.stat().st_size / logical_stored_bytes
                if logical_stored_bytes
                else None
            ),
            "verification_status": "PASS",
            "signal_dtype": "float32",
            "materialized_duration_samples": 560,
            "virtual_views_per_event": 3,
        }

    result = {
        "status": "PASS",
        "dataset_id": task["profile"]["dataset_id"],
        "subject": int(task["subject"]),
        "source_files": [str(path) for path in files],
        "source_files_resolved": len(files),
        "observed_recording_count": len(recordings),
        "observed_subject_ids": sorted(str(value) for value in observed),
        "expected_subject_id": str(expected),
        "materialized_event_count": materialized_event_count,
        "window_record_count": window_record_count,
        "a4_group_count": materialized_event_count,
        "logical_stored_bytes": logical_stored_bytes,
        "source_event_count": len(source_event_ids),
        "expected_core_event_count": len(expected_core_event_ids),
        "roles": sorted(roles),
        "shard": shard,
        "a4_window_records_path": str(records_path),
        "a4_window_index_path": str(index_path),
        "a4_group_index_path": str(groups_path),
        "a4_window_locations_path": str(locations_path),
        "quality_records_path": str(quality_records_path),
        "quality_summaries_path": str(quality_summaries_path),
        "invalid_windows_path": str(invalid_path),
        "invalid_window_count": len(invalid_rows),
        "signal_dtype": "float32",
        "a4_config_id": a4_config_id,
        "window_family_id": family["window_family_id"],
    }
    _atomic_json(result_path, result)
    return result


def _r42_download_dataset_file(
    handle: str,
    version: int,
    filename: str,
    output_root: Path,
) -> Path:
    import kagglehub

    output_root.mkdir(parents=True, exist_ok=True)
    resolved = kagglehub.dataset_download(
        f"{handle}/versions/{int(version)}",
        path=filename,
        output_dir=str(output_root),
        force_download=True,
    )
    path = Path(resolved)

    if path.is_dir():
        matches = list(path.rglob(filename))
        if len(matches) != 1:
            raise RuntimeError(
                "R42_DATASET_FILE_RESOLUTION_AMBIGUOUS: "
                f"filename={filename}; matches={len(matches)}"
            )
        path = matches[0]

    if not path.is_file():
        raise RuntimeError(
            f"R42_DATASET_FILE_MISSING: {filename}"
        )
    return path



def _r45_deep_replace_record_ids(
    value: Any,
    id_mapping: dict[str, str],
) -> Any:
    if isinstance(value, dict):
        return {
            str(key): _r45_deep_replace_record_ids(
                item,
                id_mapping,
            )
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [
            _r45_deep_replace_record_ids(
                item,
                id_mapping,
            )
            for item in value
        ]
    if isinstance(value, tuple):
        return tuple(
            _r45_deep_replace_record_ids(
                item,
                id_mapping,
            )
            for item in value
        )
    if isinstance(value, str):
        return id_mapping.get(value, value)
    return value


def _r45_normalized_record(
    record: dict[str, Any],
    id_mapping: dict[str, str],
) -> dict[str, Any]:
    normalized = _r45_deep_replace_record_ids(
        record,
        id_mapping,
    )
    normalized.pop("record_id", None)
    normalized.pop("semantic_hash", None)
    return normalized


def _r45_match_record_family(
    current: list[dict[str, Any]],
    adopted: list[dict[str, Any]],
    *,
    stable_key,
    label: str,
    id_mapping: dict[str, str],
) -> dict[str, str]:
    from iharq.canonical import semantic_hash

    current_by_key = {
        str(stable_key(row)): row
        for row in current
    }
    adopted_by_key = {
        str(stable_key(row)): row
        for row in adopted
    }

    if len(current_by_key) != len(current):
        raise RuntimeError(
            f"R45_CORE_ADOPTION_{label}_CURRENT_KEY_DUPLICATE"
        )
    if len(adopted_by_key) != len(adopted):
        raise RuntimeError(
            f"R45_CORE_ADOPTION_{label}_ADOPTED_KEY_DUPLICATE"
        )
    if set(current_by_key) != set(adopted_by_key):
        raise RuntimeError(
            f"R45_CORE_ADOPTION_{label}_KEY_SET_MISMATCH: "
            f"current={sorted(current_by_key)}; "
            f"released={sorted(adopted_by_key)}"
        )

    mapping = dict(id_mapping)

    for key in sorted(current_by_key):
        current_record = current_by_key[key]
        adopted_record = adopted_by_key[key]

        normalized_current = _r45_normalized_record(
            current_record,
            mapping,
        )
        normalized_adopted = _r45_normalized_record(
            adopted_record,
            {},
        )

        if normalized_current != normalized_adopted:
            raise RuntimeError(
                f"R45_CORE_ADOPTION_{label}_SCIENTIFIC_MISMATCH: "
                f"key={key!r}; "
                f"current_normalized_hash="
                f"{semantic_hash(normalized_current)}; "
                f"released_normalized_hash="
                f"{semantic_hash(normalized_adopted)}"
            )

        mapping[
            str(current_record["record_id"])
        ] = str(adopted_record["record_id"])

    return mapping


def _r42_adopt_existing_core_dataset(
    runner: Any,
) -> dict[str, Any]:
    pipeline = runner.pipeline

    handle = os.environ.get(
        "IHARQ_EXISTING_CORE_DATASET_HANDLE",
        "",
    ).strip()
    version = int(
        os.environ.get(
            "IHARQ_EXISTING_CORE_DATASET_VERSION",
            "0",
        )
    )
    expected_manifest_sha = os.environ.get(
        "IHARQ_EXISTING_CORE_MANIFEST_SHA256",
        "",
    ).strip().lower()

    if not handle or "/" not in handle or version < 1:
        raise RuntimeError(
            "R42_EXISTING_CORE_DATASET_CONFIGURATION_INVALID"
        )
    if not re.fullmatch(r"[0-9a-f]{64}", expected_manifest_sha):
        raise RuntimeError(
            "R42_EXISTING_CORE_MANIFEST_SHA256_INVALID"
        )

    root = (
        pipeline.work_root
        / "r42_core_adoption"
        / f"provider_version_{version}"
    )
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)

    filenames = [
        "IHARQ_P01_L1_DERIVED_WINDOW_DATASET_MANIFEST.json",
        "IHARQ_P01_L1_DERIVED_DATASET_SIDECAR.json",
        "IHARQ_P01_L1_WINDOW_RECORDS.jsonl",
        "IHARQ_P01_L1_WINDOW_INDEX.jsonl",
        "IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl",
        "IHARQ_P01_L1_DERIVED_OUTPUT_STORAGE_ACTUAL.json",
        "IHARQ_P01_L1_DERIVED_OUTPUT_STORAGE_FORECAST.json",
        "iharq_window_shard_reader.py",
    ]
    paths = {
        name: _r42_download_dataset_file(
            handle,
            version,
            name,
            root,
        )
        for name in filenames
    }

    manifest_path = paths[
        "IHARQ_P01_L1_DERIVED_WINDOW_DATASET_MANIFEST.json"
    ]
    observed_manifest_sha = _sha256(manifest_path)
    if observed_manifest_sha != expected_manifest_sha:
        raise RuntimeError(
            "R42_EXISTING_CORE_MANIFEST_SHA256_MISMATCH: "
            f"expected={expected_manifest_sha}; "
            f"observed={observed_manifest_sha}"
        )

    manifest = json.loads(
        manifest_path.read_text(encoding="utf-8")
    )
    sidecar = json.loads(
        paths[
            "IHARQ_P01_L1_DERIVED_DATASET_SIDECAR.json"
        ].read_text(encoding="utf-8")
    )
    window_records = _read_jsonl(
        paths["IHARQ_P01_L1_WINDOW_RECORDS.jsonl"]
    )
    window_index = _read_jsonl(
        paths["IHARQ_P01_L1_WINDOW_INDEX.jsonl"]
    )
    locations = _read_jsonl(
        paths["IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl"]
    )

    if manifest.get("repository_or_dataset") != handle:
        raise RuntimeError(
            "R42_EXISTING_CORE_HANDLE_MISMATCH"
        )
    if manifest.get("signal_dtype") != "float32":
        raise RuntimeError(
            "R42_EXISTING_CORE_DTYPE_MISMATCH"
        )
    if int(manifest.get("window_count", -1)) != 12_910:
        raise RuntimeError(
            "R42_EXISTING_CORE_WINDOW_COUNT_MISMATCH"
        )
    if len(manifest.get("shards", [])) != 172:
        raise RuntimeError(
            "R42_EXISTING_CORE_SHARD_COUNT_MISMATCH"
        )

    policy = manifest.get("window_policy", {})
    expected_policy = {
        "start_offset_samples": 80,
        "duration_samples": 480,
        "stride_samples": 480,
        "last_window_policy": (
            "ONE_WINDOW_PER_INCLUDED_SOURCE_EVENT"
        ),
        "bounds_policy": "REJECT_OUT_OF_BOUNDS",
    }
    for key, expected in expected_policy.items():
        if policy.get(key) != expected:
            raise RuntimeError(
                "R42_EXISTING_CORE_WINDOW_POLICY_MISMATCH: "
                f"{key}={policy.get(key)!r}"
            )

    if not (
        len(window_records)
        == len(window_index)
        == len(locations)
        == 12_910
    ):
        raise RuntimeError(
            "R42_EXISTING_CORE_INDEX_COUNT_MISMATCH: "
            f"records={len(window_records)}; "
            f"index={len(window_index)}; "
            f"locations={len(locations)}"
        )

    record_ids = {
        row["record_id"] for row in window_records
    }
    index_record_ids = {
        row["window_record_id"] for row in window_index
    }
    location_record_ids = {
        row["window_record_id"] for row in locations
    }
    if (
        len(record_ids) != 12_910
        or record_ids != index_record_ids
        or record_ids != location_record_ids
    ):
        raise RuntimeError(
            "R42_EXISTING_CORE_RECORD_ID_CLOSURE_FAILED"
        )

    event_ids = {
        row["event_id"] for row in window_index
    }
    if len(event_ids) != 12_910:
        raise RuntimeError(
            "R42_EXISTING_CORE_ONE_WINDOW_PER_EVENT_FAILED"
        )

    # Verify every compact file against the remote manifest.
    for name, row in manifest.get(
        "dataset_local_indexes",
        {},
    ).items():
        if name not in paths:
            continue
        observed = _sha256(paths[name])
        if observed != row.get("sha256"):
            raise RuntimeError(
                "R42_EXISTING_CORE_COMPACT_HASH_MISMATCH: "
                f"{name}"
            )

    # Current run must reproduce the same scientific records before the
    # existing window artifact can be adopted.
    #
    # R42 compared dependent semantic_hash values directly. That fails when
    # scientifically identical upstream record IDs differ only by execution
    # date. R45 proves full normalized-record equality in dependency order.
    current_dataset_records = list(
        pipeline.state.get("dataset_records", [])
    )
    current_label_records = list(
        pipeline.state.get("label_records", [])
    )
    current_split_records = [
        pipeline.state["split_record"]
    ]
    current_preprocessing_records = [
        pipeline.state["preprocessing_record"]
    ]

    adopted_dataset_records = list(
        sidecar["dataset_records"]
    )
    adopted_label_records = list(
        sidecar["label_records"]
    )
    adopted_split_records = [
        sidecar["split_record"]
    ]
    adopted_preprocessing_records = [
        sidecar["preprocessing_record"]
    ]

    record_id_mapping: dict[str, str] = {}

    record_id_mapping = _r45_match_record_family(
        current_dataset_records,
        adopted_dataset_records,
        stable_key=lambda row: row["payload"]["dataset_id"],
        label="DATASET_RECORDS",
        id_mapping=record_id_mapping,
    )
    record_id_mapping = _r45_match_record_family(
        current_label_records,
        adopted_label_records,
        stable_key=lambda row: row["payload"]["dataset_id"],
        label="LABEL_RECORDS",
        id_mapping=record_id_mapping,
    )
    record_id_mapping = _r45_match_record_family(
        current_split_records,
        adopted_split_records,
        stable_key=lambda row: row["payload"]["protocol_id"],
        label="SPLIT_RECORD",
        id_mapping=record_id_mapping,
    )
    record_id_mapping = _r45_match_record_family(
        current_preprocessing_records,
        adopted_preprocessing_records,
        stable_key=lambda row: row["payload"]["profile_id"],
        label="PREPROCESSING_RECORD",
        id_mapping=record_id_mapping,
    )

    pipeline.state["r45_core_record_id_mapping"] = (
        record_id_mapping
    )

    # Adopt the already released record identities so the core windows keep
    # exactly the lineage under which they were generated.
    replaced_types = {
        "DatasetRecord",
        "LabelMapRecord",
        "SplitRecord",
        "PreprocessingRecord",
        "WindowRecord",
    }
    pipeline.state["records"] = [
        row
        for row in pipeline.state.get("records", [])
        if row.get("record_type") not in replaced_types
    ]

    pipeline.state["dataset_records"] = list(
        sidecar["dataset_records"]
    )
    pipeline.state["label_records"] = list(
        sidecar["label_records"]
    )
    pipeline.state["split_record"] = dict(
        sidecar["split_record"]
    )
    pipeline.state["preprocessing_record"] = dict(
        sidecar["preprocessing_record"]
    )
    pipeline.state["window_records"] = window_records
    pipeline.state["window_index"] = window_index
    pipeline.state["quality_summaries"] = list(
        sidecar.get("quality_summaries", [])
    )
    pipeline.state["records"].extend(
        pipeline.state["dataset_records"]
        + pipeline.state["label_records"]
        + [pipeline.state["split_record"]]
        + [pipeline.state["preprocessing_record"]]
        + window_records
    )

    # Preserve compact remote evidence in the new execution bundle.
    compact_root = (
        pipeline.bundle_root
        / "external_artifact_pointers"
        / "adopted_core_dataset"
    )
    if compact_root.exists():
        shutil.rmtree(compact_root)
    compact_root.mkdir(parents=True)
    for name, path in paths.items():
        shutil.copy2(path, compact_root / name)

    pointer = {
        **manifest,
        "creation_status": "ADOPTED_VERIFIED_EXISTING_DATASET",
        "dataset_handle": handle,
        "repository_or_dataset": handle,
        "dataset_version": version,
        "provider_dataset_version": version,
        "logical_immutable_revision": 1,
        "manifest_sha256": observed_manifest_sha,
        "adoption_run_config_id": pipeline.config_id,
        "adoption_mode": (
            "DEPENDENCY_ORDER_FULL_RECORD_EQUIVALENCE_PLUS_EXACT_REMOTE_HASH"
        ),
        "scientific_artifact_recomputed": False,
        "stage14_core_reexecuted": False,
        "core_hdf5_shards_reuploaded": False,
        "provider_version_amendment": {
            "shell_provider_version": 1,
            "scientific_provider_version": 2,
            "reason": (
                "Provider version 1 is the short-title shell; "
                "provider version 2 is the verified scientific artifact."
            ),
        },
    }
    pointer_path = (
        pipeline.bundle_root
        / "external_artifact_pointers"
        / "derived_windows_dataset.json"
    )
    _atomic_json(pointer_path, pointer)

    pipeline.state["window_report"] = {
        "window_count": 12_910,
        "event_count": 12_910,
        "invalid_window_count": 0,
        "invalid_windows": [],
        "roles": sorted(
            {row["role"] for row in window_index}
        ),
        "start_offset_samples": 80,
        "duration_samples": 480,
        "stride_samples": 480,
        "duration_seconds": 3.0,
        "stride_seconds": 3.0,
        "last_window_policy": (
            "ONE_WINDOW_PER_INCLUDED_SOURCE_EVENT"
        ),
        "bounds_policy": "REJECT_OUT_OF_BOUNDS",
        "event_resampling": "MNE_POLYPHASE_JOINT_EVENTS",
        "signal_dtype": "float32",
        "overlap_group": "PARENT_EVENT",
        "storage": (
            "ADOPTED_PRIVATE_KAGGLE_DATASET_"
            "LOSSLESS_HDF5_SUBJECT_SHARDS"
        ),
        "dataset_handle": handle,
        "provider_dataset_version": version,
        "logical_immutable_revision": 1,
        "manifest_sha256": observed_manifest_sha,
    }

    pipeline.state["r42_core_adopted"] = True
    pipeline.state["r42_core_manifest"] = manifest
    pipeline.state["r42_core_pointer"] = str(
        pointer_path.relative_to(pipeline.bundle_root)
    )
    pipeline.state["r26_derived_handle"] = handle
    pipeline.state["r26_derived_pointer"] = (
        pipeline.state["r42_core_pointer"]
    )

    adoption_report = {
        "status": "PASS",
        "dataset_handle": handle,
        "provider_dataset_version": version,
        "logical_immutable_revision": 1,
        "manifest_sha256": observed_manifest_sha,
        "window_count": 12_910,
        "unique_parent_event_count": 12_910,
        "shard_count": 172,
        "signal_dtype": "float32",
        "scientific_artifact_recomputed": False,
        "core_stage14_reexecuted": False,
        "core_hdf5_shards_reuploaded": False,
        "compact_evidence_root": str(
            compact_root.relative_to(pipeline.bundle_root)
        ),
    }
    _atomic_json(
        pipeline.bundle_root
        / "reports"
        / "phase_01"
        / "storage"
        / "existing_core_dataset_adoption.json",
        adoption_report,
    )
    return adoption_report


def _r42_a4_identity(
    runner: Any,
) -> tuple[str, str]:
    attempt = os.environ.get(
        "IHARQ_EXECUTION_ATTEMPT_ID",
        datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"),
    )
    owner = os.environ.get(
        "IHARQ_KAGGLE_USERNAME",
        "csthv999z",
    ).strip()
    suffix = hashlib.sha256(
        attempt.encode("utf-8")
    ).hexdigest()[:8]
    slug = (
        f"iharq-p01-l1-a4-"
        f"{runner.pipeline.config_id[:8]}-{suffix}"
    )
    if len(slug) > 50:
        raise RuntimeError(
            f"R49_A4_SLUG_TOO_LONG: {len(slug)}"
        )
    return attempt, f"{owner}/{slug}"



def _r48_load_verified_a4_subject_checkpoint(
    task_dir: Path,
    *,
    dataset_id: str,
    subject: int,
    a4_config_id: str,
    window_family_id: str,
    expected_event_ids: set[str] | None = None,
) -> dict[str, Any] | None:
    """Return a complete prior A4 subject result only after byte-level revalidation."""
    import h5py

    result_path = Path(task_dir) / "output" / "result.json"
    if not result_path.is_file():
        return None

    try:
        result = json.loads(result_path.read_text(encoding="utf-8"))
        if result.get("status") != "PASS":
            return None
        if str(result.get("dataset_id")) != str(dataset_id):
            return None
        if int(result.get("subject")) != int(subject):
            return None
        if str(result.get("a4_config_id")) != str(a4_config_id):
            return None
        if str(result.get("window_family_id")) != str(window_family_id):
            return None
        if int(result.get("invalid_window_count", -1)) != 0:
            return None

        required_paths = [
            "a4_window_records_path",
            "a4_window_index_path",
            "a4_group_index_path",
            "a4_window_locations_path",
            "quality_records_path",
            "quality_summaries_path",
            "invalid_windows_path",
        ]
        if any(
            not Path(str(result.get(key, ""))).is_file()
            for key in required_paths
        ):
            return None

        shard = result.get("shard")
        if not isinstance(shard, dict):
            return None
        shard_path = Path(str(shard.get("path", "")))
        if not shard_path.is_file():
            return None
        if _sha256(shard_path) != str(shard.get("sha256", "")).lower():
            return None
        if int(shard.get("verified_materialized_event_rows", -1)) != int(
            result.get("materialized_event_count", -2)
        ):
            return None

        # Re-open the lossless HDF5 checkpoint, rather than trusting result.json.
        verified_rows = 0
        with h5py.File(shard_path, "r") as handle:
            if str(handle.attrs.get("format", "")) != (
                "IHARQ_P01_L1_A4_FULL3P5S_SHARD_R2"
            ):
                return None
            if str(handle.attrs.get("signal_dtype", "")) != "float32":
                return None
            if str(handle.attrs.get("a4_config_id", "")) != str(a4_config_id):
                return None
            for group_name in sorted(handle.get("window_groups", {})):
                group = handle[f"window_groups/{group_name}"]
                signals = group["signals"]
                identifiers = group["window_ids"]
                if (
                    str(signals.dtype) != "float32"
                    or int(signals.shape[2]) != 560
                    or int(signals.shape[0]) != int(identifiers.shape[0])
                ):
                    return None
                verified_rows += int(signals.shape[0])
        if verified_rows != int(result["materialized_event_count"]):
            return None

        records = _read_jsonl(Path(result["a4_window_records_path"]))
        index = _read_jsonl(Path(result["a4_window_index_path"]))
        groups = _read_jsonl(Path(result["a4_group_index_path"]))
        locations = _read_jsonl(Path(result["a4_window_locations_path"]))
        event_count = int(result["materialized_event_count"])

        if not (
            len(records) == event_count * 4
            and len(index) == event_count * 4
            and len(locations) == event_count * 4
            and len(groups) == event_count
        ):
            return None
        if any(not bool(row.get("complete")) for row in groups):
            return None
        if expected_event_ids is not None:
            observed_event_ids = {
                str(row["parent_event_id"])
                for row in groups
            }
            if observed_event_ids != {
                str(value) for value in expected_event_ids
            }:
                return None
        if len({str(row["record_id"]) for row in records}) != len(records):
            return None
        if len({str(row["window_id"]) for row in index}) != len(index):
            return None

        return result
    except Exception:
        return None


def _r42_streaming_materialize_a4(
    runner: Any,
) -> dict[str, Any]:
    pipeline = runner.pipeline
    api = _ensure_kaggle_upload_api()
    attempt, handle = _r42_a4_identity(runner)
    a4_config_id = _r42_a4_config_id(pipeline.config_id)

    plan = list(pipeline.state["r26_subject_plan"])
    profile_by_dataset = {
        profile.dataset_id: profile
        for profile in pipeline.state["profiles"]
    }
    label_by_dataset = {
        row["payload"]["dataset_id"]: row
        for row in pipeline.state["label_records"]
    }
    dataset_record_by_dataset = {
        row["payload"]["dataset_id"]: row["record_id"]
        for row in pipeline.state["dataset_records"]
    }

    expected_events_by_subject: dict[tuple[str, int], set[str]] = {}
    for row in pipeline.state["window_index"]:
        key = (
            str(row["dataset_id"]),
            int(row["subject_id"]),
        )
        expected_events_by_subject.setdefault(key, set()).add(
            str(row["event_id"])
        )

    fit_state = pipeline.state["r26_fit_state"]
    fit_payload = {
        "mean": (
            None
            if fit_state.mean is None
            else fit_state.mean.tolist()
        ),
        "std": (
            None
            if fit_state.std is None
            else fit_state.std.tolist()
        ),
        "source_ids": fit_state.source_ids,
        "state_hash": fit_state.state_hash,
    }

    root = (
        pipeline.work_root
        / "streaming_runtime"
        / "r48_a4_materialize_resume"
        / a4_config_id[:16]
    )
    root.mkdir(parents=True, exist_ok=True)

    resume_identity_path = root / "R49_A4_RESUME_IDENTITY.json"
    resume_identity = {
        "schema_version": 1,
        "base_config_id": pipeline.config_id,
        "a4_config_id": a4_config_id,
        "a4_window_family": R42_A4_WINDOW_FAMILY,
        "core_dataset_handle": os.environ[
            "IHARQ_EXISTING_CORE_DATASET_HANDLE"
        ],
        "core_provider_version": int(
            os.environ["IHARQ_EXISTING_CORE_DATASET_VERSION"]
        ),
        "core_manifest_sha256": os.environ[
            "IHARQ_EXISTING_CORE_MANIFEST_SHA256"
        ],
        "checkpoint_policy": (
            "KEEP_VERIFIED_SUBJECT_A4_HDF5_AND_COMPACT_FILES_UNTIL_DATASET_COMMIT"
        ),
    }
    if resume_identity_path.is_file():
        observed_resume_identity = json.loads(
            resume_identity_path.read_text(encoding="utf-8")
        )
        if observed_resume_identity != resume_identity:
            raise RuntimeError(
                "R49_A4_RESUME_IDENTITY_MISMATCH: "
                "existing checkpoint belongs to a different governed A4 state"
            )
    else:
        _atomic_json(resume_identity_path, resume_identity)

    pointer_root = (
        pipeline.bundle_root
        / "external_artifact_pointers"
    )
    pointer_root.mkdir(parents=True, exist_ok=True)

    location_target = pointer_root / "a4_window_to_shard.jsonl"
    records_target = pointer_root / "a4_window_records.jsonl"
    index_target = pointer_root / "a4_window_index.jsonl"
    groups_target = pointer_root / "a4_group_index.jsonl"

    for target in (
        location_target,
        records_target,
        index_target,
        groups_target,
    ):
        target.unlink(missing_ok=True)

    tokens: list[str] = []
    shard_rows: list[dict[str, Any]] = []
    a4_records: list[dict[str, Any]] = []
    a4_index: list[dict[str, Any]] = []
    a4_groups: list[dict[str, Any]] = []
    quality_records: list[dict[str, Any]] = []
    quality_summaries: list[dict[str, Any]] = []
    invalid_windows: list[dict[str, Any]] = []

    materialized_events = 0
    logical_stored_bytes = 0
    uploaded_bytes = 0
    completed = 0
    resumed_subjects = 0
    newly_materialized_subjects = 0
    started = time.monotonic()
    last_progress = 0.0
    dataset_actual: dict[str, dict[str, Any]] = {}

    for dataset, subject in plan:
        _assert_subject_scratch_capacity(
            pipeline,
            dataset,
            int(subject),
        )

        task_dir = (
            root
            / _safe(dataset)
            / f"subject_{int(subject):03d}"
        )
        shard_filename = (
            f"{_safe(dataset)}_"
            f"subject_{int(subject):03d}_a4_matched3p5s.h5"
        )
        profile = profile_by_dataset[dataset]
        label = f"R49-A4:{dataset}:subject={subject}"
        expected_core_event_ids = expected_events_by_subject.get(
            (str(dataset), int(subject)),
            set(),
        )
        if not expected_core_event_ids:
            raise RuntimeError(
                "R49_A4_EXPECTED_SUBJECT_EVENT_SET_EMPTY: "
                f"dataset={dataset}; subject={subject}"
            )

        task = {
            "action": "materialize_a4",
            "profile": _profile_dict(profile),
            "subject": int(subject),
            "input_root": str(runner.input_root),
            "child_work_root": str(task_dir / "work"),
            "child_report_root": str(task_dir / "report"),
            "output_dir": str(task_dir / "output"),
            "source_resolution_file": str(
                pipeline.state["r26_source_resolution_file"]
            ),
            "operations": pipeline.state["operations"],
            "fit_state": fit_payload,
            "assignment": pipeline.state["assignment"],
            "split_keys": list(
                pipeline.config["split"]["group_keys"]
            ),
            "label_record": label_by_dataset[dataset],
            "preprocessing_record": (
                pipeline.state["preprocessing_record"]
            ),
            "split_record": pipeline.state["split_record"],
            "quality_profile": pipeline.config.get(
                "quality",
                {},
            ),
            "base_config_id": pipeline.config_id,
            "a4_config_id": a4_config_id,
            "dataset_record_id": (
                dataset_record_by_dataset[dataset]
            ),
            "a4_window_family": R42_A4_WINDOW_FAMILY,
            "expected_core_event_ids": sorted(expected_core_event_ids),
            "shard_filename": shard_filename,
        }

        result = _r48_load_verified_a4_subject_checkpoint(
            task_dir,
            dataset_id=dataset,
            subject=int(subject),
            a4_config_id=a4_config_id,
            window_family_id=R42_A4_WINDOW_FAMILY["window_family_id"],
            expected_event_ids=expected_core_event_ids,
        )
        if result is None:
            if task_dir.exists():
                shutil.rmtree(task_dir)
            result = _run_child_task(
                task,
                pipeline.work_root,
                label,
            )
            newly_materialized_subjects += 1
        else:
            resumed_subjects += 1

        if int(result.get("expected_core_event_count", -1)) != len(
            expected_core_event_ids
        ):
            raise RuntimeError(
                "R49_A4_SUBJECT_EXPECTED_EVENT_COUNT_MISMATCH: "
                f"dataset={dataset}; subject={subject}; "
                f"expected={len(expected_core_event_ids)}; "
                f"reported={result.get('expected_core_event_count')}"
            )

        subject_records = _read_jsonl(
            Path(result["a4_window_records_path"])
        )
        subject_index = _read_jsonl(
            Path(result["a4_window_index_path"])
        )
        subject_groups = _read_jsonl(
            Path(result["a4_group_index_path"])
        )
        subject_locations = _read_jsonl(
            Path(result["a4_window_locations_path"])
        )

        a4_records.extend(subject_records)
        a4_index.extend(subject_index)
        a4_groups.extend(subject_groups)
        quality_records.extend(
            _read_jsonl(Path(result["quality_records_path"]))
        )
        quality_summaries.extend(
            _read_jsonl(Path(result["quality_summaries_path"]))
        )
        invalid_windows.extend(
            _read_jsonl(Path(result["invalid_windows_path"]))
        )

        _append_jsonl(records_target, subject_records)
        _append_jsonl(index_target, subject_index)
        _append_jsonl(groups_target, subject_groups)

        for row in subject_locations:
            row.update(
                {
                    "provider": "Kaggle",
                    "dataset_handle": handle,
                    "provider_dataset_version": 1,
                    "window_family_id": (
                        R42_A4_WINDOW_FAMILY[
                            "window_family_id"
                        ]
                    ),
                }
            )
        _append_jsonl(location_target, subject_locations)

        materialized_events += int(
            result["materialized_event_count"]
        )
        subject_logical = int(
            result["logical_stored_bytes"]
        )
        logical_stored_bytes += subject_logical

        shard = result.get("shard")
        if not shard:
            raise RuntimeError(
                f"R49_A4_SUBJECT_SHARD_MISSING: {label}"
            )

        shard_path = Path(shard["path"])
        token = _upload_blob_with_retry(api, shard_path)
        tokens.append(token)

        actual_bytes = int(shard["bytes"])
        uploaded_bytes += actual_bytes

        shard_row = {
            "filename": shard["filename"],
            "bytes": actual_bytes,
            "sha256": shard["sha256"],
            "dataset_id": dataset,
            "subject_profile": int(subject),
            "materialized_event_count": int(
                result["materialized_event_count"]
            ),
            "window_record_count": int(
                result["window_record_count"]
            ),
            "a4_group_count": int(
                result["a4_group_count"]
            ),
            "logical_stored_bytes": subject_logical,
            "compression_ratio_to_logical": (
                actual_bytes / subject_logical
                if subject_logical
                else None
            ),
            "provider": "Kaggle",
            "dataset_handle": handle,
            "format": "HDF5",
            "compression": "gzip-1-lossless",
            "signal_dtype": "float32",
            "materialized_duration_samples": 560,
            "virtual_multi_views_per_event": 3,
        }
        shard_rows.append(shard_row)

        dataset_row = dataset_actual.setdefault(
            dataset,
            {
                "dataset_id": dataset,
                "subjects": 0,
                "shards": 0,
                "materialized_events": 0,
                "window_records": 0,
                "logical_stored_bytes": 0,
                "actual_hdf5_bytes": 0,
            },
        )
        dataset_row["subjects"] += 1
        dataset_row["shards"] += 1
        dataset_row["materialized_events"] += int(
            result["materialized_event_count"]
        )
        dataset_row["window_records"] += int(
            result["window_record_count"]
        )
        dataset_row["logical_stored_bytes"] += (
            subject_logical
        )
        dataset_row["actual_hdf5_bytes"] += actual_bytes

        # R48 reliability rule: keep verified local A4 checkpoints until
        # Stage 15 has committed and remotely verified the complete Dataset.
        _trim_memory()

        completed += 1
        if (
            time.monotonic() - last_progress
            >= float(POLICY["progress_interval_seconds"])
            or completed == len(plan)
        ):
            _progress_line(
                "R49_A4_MATERIALIZE_UPLOAD_PROGRESS",
                completed,
                len(plan),
                started,
                label,
                None,
                pipeline.work_root,
                {
                    "materialized_events": materialized_events,
                    "a4_window_records": len(a4_records),
                    "a4_groups": len(a4_groups),
                    "shards_uploaded": len(shard_rows),
                    "resumed_subjects": resumed_subjects,
                    "newly_materialized_subjects": newly_materialized_subjects,
                    "uploaded_gib": round(
                        uploaded_bytes / _GIB,
                        3,
                    ),
                    "logical_stored_gib": round(
                        logical_stored_bytes / _GIB,
                        3,
                    ),
                },
            )
            last_progress = time.monotonic()

    core_event_rows = {
        str(row["event_id"]): row
        for row in pipeline.state["window_index"]
    }
    expected_events = len(core_event_rows)
    expected_records = expected_events * 4

    a4_group_rows = {
        str(row["parent_event_id"]): row
        for row in a4_groups
    }
    if len(a4_group_rows) != len(a4_groups):
        raise RuntimeError(
            "R49_A4_DUPLICATE_PARENT_EVENT_GROUP"
        )
    if set(a4_group_rows) != set(core_event_rows):
        missing = sorted(set(core_event_rows) - set(a4_group_rows))
        unexpected = sorted(set(a4_group_rows) - set(core_event_rows))
        raise RuntimeError(
            "R49_A4_PARENT_EVENT_SET_MISMATCH: "
            f"missing={missing[:20]}; unexpected={unexpected[:20]}"
        )

    for event_id, group in a4_group_rows.items():
        core = core_event_rows[event_id]
        comparisons = {
            "dataset_id": (
                str(group["dataset_id"]),
                str(core["dataset_id"]),
            ),
            "subject_id": (
                str(group["subject_id"]),
                str(core["subject_id"]),
            ),
            "session_id": (
                str(group["session_id"]),
                str(core["session_id"]),
            ),
            "run_id": (
                str(group["run_id"]),
                str(core["run_id"]),
            ),
            "role": (
                str(group["role"]),
                str(core["role"]),
            ),
            "normalized_label": (
                str(group["normalized_label"]),
                str(core["label"]),
            ),
        }
        mismatches = {
            key: {"a4": left, "core": right}
            for key, (left, right) in comparisons.items()
            if left != right
        }
        if mismatches:
            raise RuntimeError(
                "R49_A4_CORE_LINEAGE_MISMATCH: "
                f"event_id={event_id}; mismatches={mismatches}"
            )

        member_ids = list(group["multi_member_window_ids"])
        if (
            len(member_ids) != 3
            or len(set(member_ids)) != 3
            or not bool(group.get("complete"))
        ):
            raise RuntimeError(
                "R49_A4_MULTI_MEMBER_CLOSURE_FAILED: "
                f"event_id={event_id}"
            )

    component_counts = {
        "LONGER_WINDOW": sum(
            row.get("a4_component") == "LONGER_WINDOW"
            for row in a4_index
        ),
        "MULTI_WINDOW_MEMBER": sum(
            row.get("a4_component") == "MULTI_WINDOW_MEMBER"
            for row in a4_index
        ),
    }
    if component_counts != {
        "LONGER_WINDOW": expected_events,
        "MULTI_WINDOW_MEMBER": expected_events * 3,
    }:
        raise RuntimeError(
            "R49_A4_COMPONENT_COUNT_MISMATCH: "
            f"{component_counts}"
        )

    if materialized_events != expected_events:
        raise RuntimeError(
            "R49_A4_EVENT_COVERAGE_MISMATCH: "
            f"expected={expected_events}; "
            f"observed={materialized_events}"
        )
    if len(a4_groups) != expected_events:
        raise RuntimeError(
            "R49_A4_GROUP_COUNT_MISMATCH"
        )
    if len(a4_records) != expected_records:
        raise RuntimeError(
            "R49_A4_WINDOW_RECORD_COUNT_MISMATCH: "
            f"expected={expected_records}; "
            f"observed={len(a4_records)}"
        )
    if len(a4_index) != expected_records:
        raise RuntimeError(
            "R49_A4_WINDOW_INDEX_COUNT_MISMATCH"
        )
    if invalid_windows:
        invalid_path = (
            pipeline.bundle_root
            / "negative_and_failed_results"
            / "a4_invalid_windows.json"
        )
        _atomic_json(invalid_path, invalid_windows)
        raise RuntimeError(
            "R49_A4_INVALID_WINDOWS_PRESENT: "
            f"count={len(invalid_windows)}; "
            f"path={invalid_path}"
        )

    if len(quality_summaries) != 489:
        raise RuntimeError(
            "R49_A4_QUALITY_SUMMARY_COVERAGE_MISMATCH: "
            f"{len(quality_summaries)}"
        )
    hard_invalid = sum(
        int(row.get("hard_invalid", 0))
        for row in quality_summaries
    )
    if hard_invalid:
        raise RuntimeError(
            f"R49_A4_QUALITY_HARD_INVALID: {hard_invalid}"
        )

    # Use the fresh quality evidence generated during the A4 raw-source pass.
    pipeline.state["quality_records"] = quality_records
    pipeline.state["quality_summaries"] = quality_summaries
    pipeline.state["records"].extend(quality_records)

    pipeline.state["r42_a4_records"] = a4_records
    pipeline.state["r42_a4_index"] = a4_index
    pipeline.state["r42_a4_groups"] = a4_groups
    pipeline.state["r42_a4_shards"] = shard_rows
    pipeline.state["r42_a4_tokens"] = tokens
    pipeline.state["r42_a4_upload_api"] = api
    pipeline.state["r42_a4_handle"] = handle
    pipeline.state["r42_a4_attempt"] = attempt
    pipeline.state["r42_a4_config_id"] = a4_config_id
    pipeline.state["r42_a4_location_path"] = str(
        location_target.relative_to(pipeline.bundle_root)
    )
    pipeline.state["r42_a4_records_path"] = str(
        records_target.relative_to(pipeline.bundle_root)
    )
    pipeline.state["r42_a4_index_path"] = str(
        index_target.relative_to(pipeline.bundle_root)
    )
    pipeline.state["r42_a4_groups_path"] = str(
        groups_target.relative_to(pipeline.bundle_root)
    )
    pipeline.state["r48_a4_resume_root"] = str(root)

    report = {
        "artifact_id": (
            f"P01-L1-A4-STORAGE-ACTUAL-"
            f"{a4_config_id[:16]}-{attempt}"
        ),
        "status": "PRECOMMIT_ALL_A4_SHARD_TOKENS_OBTAINED",
        "base_scientific_freeze": (
            POLICY["scientific_freeze_unchanged"]
        ),
        "a4_window_family": R42_A4_WINDOW_FAMILY,
        "base_config_id": pipeline.config_id,
        "a4_config_id": a4_config_id,
        "core_dataset_handle": os.environ[
            "IHARQ_EXISTING_CORE_DATASET_HANDLE"
        ],
        "core_provider_dataset_version": int(
            os.environ["IHARQ_EXISTING_CORE_DATASET_VERSION"]
        ),
        "a4_dataset_handle": handle,
        "subject_shards": len(shard_rows),
        "resumed_subjects": resumed_subjects,
        "newly_materialized_subjects": newly_materialized_subjects,
        "resume_checkpoint_root": str(root),
        "checkpoint_cleanup_rule": "DELETE_ONLY_AFTER_REMOTE_DATASET_MANIFEST_VERIFICATION",
        "materialized_matched3p5s_events": materialized_events,
        "a4_window_records": len(a4_records),
        "a4_groups": len(a4_groups),
        "virtual_multi_views": expected_events * 3,
        "invalid_window_count": 0,
        "signal_dtype": "float32",
        "logical_materialized_float32_bytes": (
            logical_stored_bytes
        ),
        "logical_materialized_float32_gib": round(
            logical_stored_bytes / _GIB,
            3,
        ),
        "actual_hdf5_uploaded_bytes": uploaded_bytes,
        "actual_hdf5_uploaded_gib": round(
            uploaded_bytes / _GIB,
            3,
        ),
        "actual_compression_ratio": (
            uploaded_bytes / logical_stored_bytes
            if logical_stored_bytes
            else None
        ),
        "overlap_storage_policy": (
            "STORE_MATCHED_3P5S_ONCE_AND_REGISTER_3X2S_UNIFORM_0P75S_VIEWS"
        ),
        "dataset_totals": [
            {
                **row,
                "logical_stored_gib": round(
                    row["logical_stored_bytes"] / _GIB,
                    3,
                ),
                "actual_hdf5_gib": round(
                    row["actual_hdf5_bytes"] / _GIB,
                    3,
                ),
            }
            for _, row in sorted(dataset_actual.items())
        ],
    }
    report_path = (
        pipeline.bundle_root
        / "reports"
        / "phase_01"
        / "storage"
        / "a4_derived_output_storage_actual_precommit.json"
    )
    _atomic_json(report_path, report)
    pipeline.state["r42_a4_storage_report"] = report
    pipeline.state["r42_a4_storage_report_path"] = str(
        report_path.relative_to(pipeline.bundle_root)
    )
    return report


def _r42_poll_dataset_version(
    handle: str,
    minimum_version: int = 1,
) -> int:
    from kagglehub.clients import build_kaggle_client
    from kagglesdk.datasets.types.dataset_api_service import (
        ApiGetDatasetRequest,
    )

    owner, slug = handle.split("/", 1)
    observed = 0
    for _ in range(80):
        try:
            with build_kaggle_client() as client:
                request = ApiGetDatasetRequest()
                request.owner_slug = owner
                request.dataset_slug = slug
                response = (
                    client.datasets.dataset_api_client.get_dataset(
                        request
                    )
                )
                observed = int(
                    getattr(
                        response,
                        "current_version_number",
                        0,
                    )
                    or 0
                )
                if observed >= minimum_version:
                    return observed
        except Exception:
            pass
        time.sleep(5)
    raise RuntimeError(
        "R49_A4_DATASET_VERSION_NOT_VISIBLE: "
        f"handle={handle}; observed={observed}"
    )




def _r48_assert_a4_runtime_contract() -> dict[str, Any]:
    """Cheap deterministic contract checks before touching raw A4 source bytes."""
    from iharq.canonical import semantic_hash

    # Direct semantic_hash must accept the complete profile.
    config_probe = semantic_hash(
        {
            "base_config_id": "0" * 64,
            "a4_window_family": R42_A4_WINDOW_FAMILY,
        }
    )
    if not re.fullmatch(r"[0-9a-f]{64}", config_probe):
        raise RuntimeError("R49_A4_CONFIG_HASH_PREFLIGHT_FAILED")

    materialized = R42_A4_WINDOW_FAMILY["materialized_profile"]
    multi = R42_A4_WINDOW_FAMILY["multi_window_profile"]
    expected = {
        "target_sampling_hz": 160,
        "materialized_samples": 560,
        "materialized_seconds": "3.5",
        "multi_count": 3,
        "multi_samples": 320,
        "multi_seconds": "2.0",
        "multi_stride_samples": 120,
        "multi_stride_seconds": "0.75",
        "slices": [(0, 320), (120, 440), (240, 560)],
    }
    observed = {
        "target_sampling_hz": int(R42_A4_WINDOW_FAMILY["target_sampling_hz"]),
        "materialized_samples": int(materialized["duration_samples"]),
        "materialized_seconds": str(materialized["duration_seconds"]),
        "multi_count": int(multi["member_count"]),
        "multi_samples": int(multi["member_duration_samples"]),
        "multi_seconds": str(multi["member_duration_seconds"]),
        "multi_stride_samples": int(multi["member_stride_samples"]),
        "multi_stride_seconds": str(multi["member_stride_seconds"]),
        "slices": [
            (int(row["slice_start"]), int(row["slice_stop"]))
            for row in multi["member_slices"]
        ],
    }
    if observed != expected:
        raise RuntimeError(
            "R49_A4_PROFILE_CONTRACT_MISMATCH: "
            + json.dumps({"expected": expected, "observed": observed}, default=list)
        )
    return {
        "status": "PASS",
        "config_hash_probe": config_probe,
        "profile": observed,
    }




def _r49_assert_universal_matched_window_feasibility(
    runner: Any,
) -> dict[str, Any]:
    """
    Prove the R49 +0.0..+3.5 s A4 family is available for every released
    core event without consulting a new denominator or tolerating missingness.

    The released core window is +0.5..+3.5 s (80..560 samples from cue).
    Therefore every validated core record already proves that cue+560 exists.
    R49's longer window starts at cue and ends at that exact same stop sample.
    """
    pipeline = runner.pipeline
    records = list(
        pipeline.state.get(
            "window_records",
            [],
        )
    )
    if len(records) != 12_910:
        raise RuntimeError(
            "R49_A4_CORE_WINDOW_COUNT_MISMATCH: "
            f"expected=12910; observed={len(records)}"
        )

    event_ids: set[str] = set()
    source_units: set[str] = set()
    violations: list[dict[str, Any]] = []

    for record in records:
        payload = dict(
            record.get(
                "payload",
                {},
            )
        )
        event_id = str(
            payload.get(
                "parent_event_id",
                "",
            )
        )
        cue = int(
            payload.get(
                "resampled_event_sample",
                -10**12,
            )
        )
        core_start = int(
            payload.get(
                "start_sample",
                -10**12,
            )
        )
        core_stop = int(
            payload.get(
                "stop_sample",
                -10**12,
            )
        )
        core_duration = int(
            payload.get(
                "duration_samples",
                -1,
            )
        )
        core_offset = int(
            payload.get(
                "start_offset_samples",
                -1,
            )
        )

        expected_core_start = cue + 80
        expected_shared_stop = cue + 560

        if (
            not event_id
            or cue < 0
            or core_offset != 80
            or core_duration != 480
            or core_start != expected_core_start
            or core_stop != expected_shared_stop
        ):
            violations.append(
                {
                    "event_id": event_id,
                    "cue_sample": cue,
                    "core_start": core_start,
                    "core_stop": core_stop,
                    "core_offset": core_offset,
                    "core_duration": core_duration,
                    "expected_core_start": expected_core_start,
                    "expected_shared_stop": expected_shared_stop,
                }
            )
            continue

        event_ids.add(
            event_id
        )
        source_units.add(
            ":".join(
                [
                    str(payload["dataset_id"]),
                    str(payload["subject_id"]),
                    str(payload["session_id"]),
                    str(payload["run_id"]),
                ]
            )
        )

    if violations:
        raise RuntimeError(
            "R49_A4_CORE_TIMING_PROOF_FAILED: "
            + json.dumps(
                violations[:20],
                indent=2,
            )
        )
    if len(event_ids) != 12_910:
        raise RuntimeError(
            "R49_A4_CORE_EVENT_ID_UNIQUENESS_FAILED: "
            f"{len(event_ids)}"
        )
    if len(source_units) != 489:
        raise RuntimeError(
            "R49_A4_SOURCE_UNIT_COVERAGE_MISMATCH: "
            f"expected=489; observed={len(source_units)}"
        )

    return {
        "status": "PASS",
        "proof_kind": (
            "DERIVED_FROM_RELEASED_CORE_WINDOW_TIMING"
        ),
        "core_event_count": 12_910,
        "source_unit_count": 489,
        "core_profile": {
            "start_offset_samples": 80,
            "duration_samples": 480,
            "stop_offset_samples": 560,
            "start_offset_seconds": "0.5",
            "duration_seconds": "3.0",
            "stop_offset_seconds": "3.5",
        },
        "a4_matched_longer_profile": {
            "start_offset_samples": 0,
            "duration_samples": 560,
            "stop_offset_samples": 560,
            "start_offset_seconds": "0.0",
            "duration_seconds": "3.5",
            "stop_offset_seconds": "3.5",
        },
        "added_observation_samples_vs_core": 80,
        "added_observation_seconds_vs_core": "0.5",
        "added_decision_latency_seconds_vs_core": "0.0",
        "denominator_change": False,
        "missing_window_rule_required_for_primary_r49_profile": False,
        "scientific_rationale": (
            "R49 adds the cue-to-+0.5 s segment while preserving the exact "
            "core +3.5 s availability endpoint. This is the maximal "
            "universally matched cue-anchored longer window directly proven "
            "by the released 12,910-event core artifact."
        ),
    }


def _r48_a4_synthetic_end_to_end_preflight(
    runner: Any,
) -> dict[str, Any]:
    """Exercise the complete new A4 child/record/HDF5/reader contract before raw work."""
    import importlib.util
    import tempfile
    import numpy as np

    from iharq.canonical import semantic_hash
    from iharq.layer1_data_protocol.models import RawRecording, Event

    pipeline = runner.pipeline
    dataset_id = "PhysioNetMI"
    label_record = next(
        row
        for row in pipeline.state["label_records"]
        if row["payload"]["dataset_id"] == dataset_id
    )
    dataset_record = next(
        row
        for row in pipeline.state["dataset_records"]
        if row["payload"]["dataset_id"] == dataset_id
    )
    mapping_keys = sorted(label_record["payload"]["mapping"])
    if len(mapping_keys) < 2:
        raise RuntimeError(
            "R49_A4_SYNTHETIC_PREFLIGHT_LABEL_MAP_INSUFFICIENT"
        )

    sampling_hz = 160.0
    sample_count = 1_920
    timeline = np.arange(sample_count, dtype=np.float64) / sampling_hz
    signal = np.vstack(
        [
            1e-6 * np.sin(2.0 * np.pi * (10.0 + index) * timeline)
            for index in range(5)
        ]
    ).astype(np.float64)

    synthetic_subject = "999999"
    recording = RawRecording(
        dataset_id,
        synthetic_subject,
        "synthetic_session",
        "synthetic_run",
        "R48_SYNTHETIC_ONLY",
        sampling_hz,
        [f"EEG{index}" for index in range(5)],
        signal,
        [
            Event(
                "event:r48-preflight:1",
                160,
                320,
                mapping_keys[0],
                {},
            ),
            Event(
                "event:r48-preflight:2",
                960,
                1_120,
                mapping_keys[1],
                {},
            ),
        ],
        {"channel_types": ["eeg"] * 5},
    )

    split_keys = list(
        pipeline.config["split"]["group_keys"]
    )
    assignment = dict(pipeline.state["assignment"])
    synthetic_unit = "|".join(
        str(getattr(recording, key))
        for key in split_keys
    )
    assignment[synthetic_unit] = "train"

    fit_state = pipeline.state["r26_fit_state"]
    fit_payload = {
        "mean": (
            None
            if fit_state.mean is None
            else fit_state.mean.tolist()
        ),
        "std": (
            None
            if fit_state.std is None
            else fit_state.std.tolist()
        ),
        "source_ids": list(fit_state.source_ids),
        "state_hash": str(fit_state.state_hash),
    }

    a4_config_id = _r42_a4_config_id(
        pipeline.config_id
    )

    original_loader = globals()["_load_subject_recordings"]
    try:
        with tempfile.TemporaryDirectory(
            prefix="iharq-r48-a4-preflight-"
        ) as temporary:
            task_dir = Path(temporary) / "task"
            output_dir = task_dir / "output"

            def synthetic_loader(task):
                return (
                    [recording],
                    [Path(temporary) / "synthetic-source"],
                    {synthetic_subject},
                    synthetic_subject,
                )

            globals()["_load_subject_recordings"] = synthetic_loader

            task = {
                "profile": {"dataset_id": dataset_id},
                "subject": int(synthetic_subject),
                "output_dir": str(output_dir),
                "fit_state": fit_payload,
                "operations": list(pipeline.state["operations"]),
                "assignment": assignment,
                "split_keys": split_keys,
                "label_record": label_record,
                "preprocessing_record": pipeline.state[
                    "preprocessing_record"
                ],
                "split_record": pipeline.state["split_record"],
                "quality_profile": pipeline.config.get("quality", {}),
                "base_config_id": pipeline.config_id,
                "a4_config_id": a4_config_id,
                "dataset_record_id": dataset_record["record_id"],
                "a4_window_family": R42_A4_WINDOW_FAMILY,
                "expected_core_event_ids": [
                    "event:r48-preflight:1",
                    "event:r48-preflight:2",
                ],
                "shard_filename": "r49_synthetic_a4.h5",
            }

            result = _r42_child_materialize_a4(task)

            required_result = {
                "status": "PASS",
                "observed_recording_count": 1,
                "observed_subject_ids": [synthetic_subject],
                "expected_subject_id": synthetic_subject,
                "materialized_event_count": 2,
                "expected_core_event_count": 2,
                "window_record_count": 8,
                "a4_group_count": 2,
                "invalid_window_count": 0,
                "signal_dtype": "float32",
            }
            observed_result = {
                key: result.get(key)
                for key in required_result
            }
            if observed_result != required_result:
                raise RuntimeError(
                    "R49_A4_SYNTHETIC_CHILD_RESULT_CONTRACT_MISMATCH: "
                    + json.dumps(
                        {
                            "expected": required_result,
                            "observed": observed_result,
                        },
                        indent=2,
                    )
                )

            records = _read_jsonl(
                Path(result["a4_window_records_path"])
            )
            index_rows = _read_jsonl(
                Path(result["a4_window_index_path"])
            )
            group_rows = _read_jsonl(
                Path(result["a4_group_index_path"])
            )
            location_rows = _read_jsonl(
                Path(result["a4_window_locations_path"])
            )

            if not (
                len(records)
                == len(index_rows)
                == len(location_rows)
                == 8
                and len(group_rows) == 2
            ):
                raise RuntimeError(
                    "R49_A4_SYNTHETIC_CARDINALITY_MISMATCH"
                )
            if len({row["record_id"] for row in records}) != 8:
                raise RuntimeError(
                    "R49_A4_SYNTHETIC_RECORD_ID_DUPLICATE"
                )
            if len({row["window_id"] for row in index_rows}) != 8:
                raise RuntimeError(
                    "R49_A4_SYNTHETIC_WINDOW_ID_DUPLICATE"
                )
            if any(
                not row.get("storage_id")
                for row in location_rows
            ):
                raise RuntimeError(
                    "R49_A4_SYNTHETIC_STORAGE_ID_MISSING"
                )

            validation_context = (
                list(pipeline.state["dataset_records"])
                + list(pipeline.state["label_records"])
                + [pipeline.state["split_record"]]
                + [pipeline.state["preprocessing_record"]]
                + records
            )
            errors, _ = _r48_validate_records_cached(
                validation_context,
                pipeline.package_root
                / "schemas"
                / "phase_01"
                / "records",
                a4_config_id,
            )
            if errors:
                raise RuntimeError(
                    "R49_A4_SYNTHETIC_RECORD_VALIDATION_FAILED: "
                    + json.dumps(errors[:20], indent=2)
                )

            reader_path = (
                Path(temporary)
                / "iharq_a4_window_shard_reader.py"
            )
            reader_path.write_text(
                R42_A4_READER_SOURCE,
                encoding="utf-8",
            )
            spec = importlib.util.spec_from_file_location(
                "iharq_r48_a4_reader_preflight",
                reader_path,
            )
            if spec is None or spec.loader is None:
                raise RuntimeError(
                    "R49_A4_SYNTHETIC_READER_IMPORT_SPEC_FAILED"
                )
            reader = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(reader)

            expected_shapes = [
                (5, 560),
                (5, 320),
                (5, 320),
                (5, 320),
            ] * 2
            restored_shapes = []
            for row in location_rows:
                restored = reader.resolve_window(
                    output_dir,
                    row,
                )
                restored_shapes.append(
                    tuple(int(value) for value in restored.shape)
                )
            if restored_shapes != expected_shapes:
                raise RuntimeError(
                    "R49_A4_SYNTHETIC_READER_SHAPE_MISMATCH: "
                    f"{restored_shapes}"
                )

            checkpoint = _r48_load_verified_a4_subject_checkpoint(
                task_dir,
                dataset_id=dataset_id,
                subject=int(synthetic_subject),
                a4_config_id=a4_config_id,
                window_family_id=R42_A4_WINDOW_FAMILY[
                    "window_family_id"
                ],
                expected_event_ids={
                    "event:r48-preflight:1",
                    "event:r48-preflight:2",
                },
            )
            if checkpoint is None:
                raise RuntimeError(
                    "R49_A4_SYNTHETIC_CHECKPOINT_REVALIDATION_FAILED"
                )

            return {
                "status": "PASS",
                "a4_config_id": a4_config_id,
                "materialized_events": 2,
                "window_records": 8,
                "groups": 2,
                "reader_roundtrip": "PASS",
                "schema_id_lineage": "PASS",
                "checkpoint_revalidation": "PASS",
                "scientific_constants_changed": False,
            }
    finally:
        globals()["_load_subject_recordings"] = original_loader


def _r48_validate_records_cached(
    records: list[dict[str, Any]],
    schema_root: Path,
    config_id: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Equivalent P01 schema/ID/lineage validation with one validator per type."""
    from jsonschema import Draft202012Validator
    from iharq.ids import validate_id
    from iharq.lineage import missing_sources
    from iharq.layer1_data_protocol.records import make_record

    errors: list[dict[str, Any]] = []
    validators: dict[str, Any] = {}

    for record in records:
        record_type = str(record["record_type"])
        validator = validators.get(record_type)
        if validator is None:
            path = Path(schema_root) / f"{record_type}.schema.json"
            if not path.exists():
                errors.append(
                    {
                        "code": "P01_SCHEMA_MISSING",
                        "record_id": record["record_id"],
                        "schema": str(path),
                    }
                )
                validators[record_type] = False
                continue
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            validator = Draft202012Validator(schema)
            validators[record_type] = validator

        if validator is not False:
            for error in validator.iter_errors(record):
                errors.append(
                    {
                        "code": "P01_SCHEMA_INVALID",
                        "record_id": record["record_id"],
                        "path": "/".join(map(str, error.path)),
                        "message": error.message,
                    }
                )

        if not validate_id(str(record["record_id"])):
            errors.append(
                {
                    "code": "P01_RECORD_ID_INVALID",
                    "record_id": record["record_id"],
                }
            )

    missing = missing_sources(records)
    for record_id, values in missing.items():
        errors.append(
            {
                "code": "P01_LINEAGE_BROKEN",
                "record_id": record_id,
                "missing": values,
            }
        )

    payload = {
        "validation_report_id": f"validation:{config_id[:16]}",
        "target_ids": [record["record_id"] for record in records],
        "checks": [
            {
                "name": "schema_id_lineage",
                "status": "PASS" if not errors else "FAIL",
                "errors": errors,
            }
        ],
        "status": "PASS" if not errors else "FAIL",
    }
    report = make_record(
        "ValidationReport",
        payload,
        config_id,
        [record["record_id"] for record in records],
        evidence_mode="VALIDATION",
        lifecycle_status="VALIDATED" if not errors else "BLOCKED",
        evidence_role="DERIVED",
    )
    return errors, report



def _r48_verify_remote_a4_manifest(
    handle: str,
    provider_version: int,
    manifest_filename: str,
    expected_sha256: str,
    scratch: Path,
) -> dict[str, Any]:
    """Verify the exact committed compact manifest after provider promotion."""
    verify_root = Path(scratch) / "remote_manifest_verification"
    if verify_root.exists():
        shutil.rmtree(verify_root)
    verify_root.mkdir(parents=True, exist_ok=True)

    errors: list[str] = []
    for attempt in range(1, 31):
        try:
            resolved = _r42_download_dataset_file(
                handle,
                int(provider_version),
                manifest_filename,
                verify_root,
            )
            observed_sha256 = _sha256(resolved)
            if observed_sha256 != str(expected_sha256).lower():
                raise RuntimeError(
                    "R49_A4_REMOTE_MANIFEST_SHA256_MISMATCH: "
                    f"expected={expected_sha256}; observed={observed_sha256}"
                )
            return {
                "status": "PASS",
                "dataset_handle": handle,
                "provider_version": int(provider_version),
                "manifest_filename": manifest_filename,
                "manifest_sha256": observed_sha256,
                "attempt": attempt,
            }
        except Exception as exc:
            errors.append(
                f"attempt={attempt}: {type(exc).__name__}: {exc}"
            )
            if attempt < 30:
                time.sleep(5)

    raise RuntimeError(
        "R49_A4_REMOTE_MANIFEST_VERIFICATION_FAILED: "
        + json.dumps(errors[-10:], indent=2)
    )



def _r48_create_or_adopt_a4_dataset_v1(
    handle: str,
    upload_tokens: list[Any],
    manifest_filename: str,
    manifest_sha256: str,
    scratch: Path,
) -> dict[str, Any]:
    """
    Create the A4 Dataset explicitly as provider version 1.

    If creation reports an error, adopt only an already-existing provider-v1
    Dataset whose exact remote manifest hash matches this run. This makes
    Stage 15 idempotent without ever creating provider version 2.
    """
    from kagglehub.clients import build_kaggle_client
    from kagglehub.exceptions import handle_mutate_call
    from kagglehub.gcs_upload import UploadDirectoryInfo
    from kagglesdk.datasets.types.dataset_api_service import (
        ApiCreateDatasetRequest,
    )

    owner, slug = handle.split("/", 1)
    if len(slug) > 50:
        raise RuntimeError(
            f"R49_A4_DATASET_SLUG_TOO_LONG: {len(slug)}"
        )
    title = "IHARQ P01 L1 A4 Windows"
    if len(title) > 50:
        raise RuntimeError(
            f"R49_A4_DATASET_TITLE_TOO_LONG: {len(title)}"
        )

    upload_dir = UploadDirectoryInfo(
        name="",
        files=list(upload_tokens),
        directories=[],
    )
    upload_proto = upload_dir.to_proto()

    request = ApiCreateDatasetRequest()
    request.owner_slug = owner
    request.slug = slug
    request.title = title
    request.files = upload_proto.files
    request.directories = upload_proto.directories
    request.is_private = True

    created = False
    create_error: Exception | None = None
    try:
        with build_kaggle_client() as client:
            handle_mutate_call(
                lambda: client.datasets.dataset_api_client.create_dataset(
                    request
                )
            )
        created = True
    except Exception as exc:
        create_error = exc

    if not created:
        # Safe idempotent recovery: never issue a version-creation request.
        # An existing Dataset is acceptable only when provider v1 contains
        # exactly the manifest that this run intended to publish.
        try:
            verification = _r48_verify_remote_a4_manifest(
                handle,
                1,
                manifest_filename,
                manifest_sha256,
                scratch,
            )
            current_version = _r42_poll_dataset_version(
                handle,
                minimum_version=1,
            )
            if int(current_version) != 1:
                raise RuntimeError(
                    "R49_A4_EXISTING_DATASET_NOT_IMMUTABLE_V1: "
                    f"current_version={current_version}"
                )
            return {
                "status": "PASS",
                "created": False,
                "adopted_existing_exact_v1": True,
                "provider_version": 1,
                "remote_manifest_verification": verification,
                "create_error": repr(create_error),
            }
        except Exception as verify_exc:
            raise RuntimeError(
                "R49_A4_DATASET_CREATE_FAILED_AND_NO_EXACT_V1_RECOVERY: "
                f"create_error={create_error!r}; "
                f"verification_error={verify_exc!r}"
            ) from create_error

    provider_version = _r42_poll_dataset_version(
        handle,
        minimum_version=1,
    )
    if int(provider_version) != 1:
        raise RuntimeError(
            "R49_A4_PROVIDER_VERSION_UNEXPECTED_AFTER_CREATE: "
            f"expected=1; observed={provider_version}"
        )

    verification = _r48_verify_remote_a4_manifest(
        handle,
        1,
        manifest_filename,
        manifest_sha256,
        scratch,
    )
    return {
        "status": "PASS",
        "created": True,
        "adopted_existing_exact_v1": False,
        "provider_version": 1,
        "remote_manifest_verification": verification,
        "create_error": None,
    }


def _r42_finalize_a4_dataset(
    runner: Any,
) -> dict[str, Any]:
    pipeline = runner.pipeline
    api = pipeline.state["r42_a4_upload_api"]
    handle = pipeline.state["r42_a4_handle"]
    tokens = list(pipeline.state["r42_a4_tokens"])
    shards = list(pipeline.state["r42_a4_shards"])
    a4_records = list(pipeline.state["r42_a4_records"])
    a4_index = list(pipeline.state["r42_a4_index"])
    a4_groups = list(pipeline.state["r42_a4_groups"])
    a4_config_id = pipeline.state["r42_a4_config_id"]

    expected_events = 12_910

    if len(shards) != 172 or len(tokens) != 172:
        raise RuntimeError(
            "R49_A4_FINALIZE_SHARD_TOKEN_COUNT_MISMATCH: "
            f"shards={len(shards)}; tokens={len(tokens)}"
        )
    shard_names = [str(row["filename"]) for row in shards]
    if len(set(shard_names)) != len(shard_names):
        raise RuntimeError("R49_A4_FINALIZE_DUPLICATE_SHARD_FILENAME")
    if len(set(map(str, tokens))) != len(tokens):
        raise RuntimeError("R49_A4_FINALIZE_DUPLICATE_UPLOAD_TOKEN")

    if len(a4_groups) != expected_events:
        raise RuntimeError(
            "R49_A4_FINALIZE_GROUP_COUNT_MISMATCH"
        )
    if len(a4_records) != expected_events * 4:
        raise RuntimeError(
            "R49_A4_FINALIZE_RECORD_COUNT_MISMATCH"
        )
    if any(
        not bool(row.get("complete"))
        for row in a4_groups
    ):
        raise RuntimeError(
            "R49_A4_INCOMPLETE_MULTI_WINDOW_GROUP"
        )

    scratch = (
        pipeline.work_root
        / "streaming_runtime"
        / "r42_a4_dataset_commit"
    )
    if scratch.exists():
        shutil.rmtree(scratch)
    scratch.mkdir(parents=True)

    validation_context = (
        list(pipeline.state["dataset_records"])
        + list(pipeline.state["label_records"])
        + [pipeline.state["split_record"]]
        + [pipeline.state["preprocessing_record"]]
        + a4_records
    )
    a4_validation_errors, a4_validation_report = _r48_validate_records_cached(
        validation_context,
        pipeline.package_root / "schemas" / "phase_01" / "records",
        a4_config_id,
    )
    validation_path = (
        scratch
        / "IHARQ_P01_L1_A4_RECORD_VALIDATION_REPORT.json"
    )
    _atomic_json(
        validation_path,
        {
            "validation_scope": (
                "A4_WINDOW_RECORDS_WITH_REQUIRED_PARENT_CONTEXT"
            ),
            "a4_window_record_count": len(a4_records),
            "parent_context_record_count": (
                len(validation_context) - len(a4_records)
            ),
            "errors": a4_validation_errors,
            "report": a4_validation_report,
        },
    )
    if a4_validation_errors:
        raise RuntimeError(
            "R49_A4_RECORD_SCHEMA_OR_LINEAGE_VALIDATION_FAILED: "
            + json.dumps(a4_validation_errors[:20], indent=2)
        )

    source_map = {
        "IHARQ_P01_L1_A4_WINDOW_RECORDS.jsonl": (
            pipeline.bundle_root
            / pipeline.state["r42_a4_records_path"]
        ),
        "IHARQ_P01_L1_A4_WINDOW_INDEX.jsonl": (
            pipeline.bundle_root
            / pipeline.state["r42_a4_index_path"]
        ),
        "IHARQ_P01_L1_A4_GROUP_INDEX.jsonl": (
            pipeline.bundle_root
            / pipeline.state["r42_a4_groups_path"]
        ),
        "IHARQ_P01_L1_A4_WINDOW_TO_SHARD_INDEX.jsonl": (
            pipeline.bundle_root
            / pipeline.state["r42_a4_location_path"]
        ),
        "IHARQ_P01_L1_A4_OUTPUT_STORAGE_ACTUAL.json": (
            pipeline.bundle_root
            / pipeline.state["r42_a4_storage_report_path"]
        ),
    }

    compact_paths: list[Path] = [validation_path]
    for name, source in source_map.items():
        if not Path(source).is_file():
            raise RuntimeError(
                f"R49_A4_FINALIZE_COMPACT_SOURCE_MISSING: {name}: {source}"
            )
        target = scratch / name
        shutil.copy2(source, target)
        compact_paths.append(target)

    freeze_path = (
        scratch
        / "IHARQ_P01_L1_A4_WINDOW_FAMILY_FREEZE_R2.json"
    )
    _atomic_json(
        freeze_path,
        {
            "freeze_id": (
                R42_A4_WINDOW_FAMILY["window_family_id"]
            ),
            "base_scientific_freeze": (
                POLICY["scientific_freeze_unchanged"]
            ),
            "base_config_id": pipeline.config_id,
            "a4_config_id": a4_config_id,
            "authority_class": (
                "ADDITIVE_LAYER1_WINDOW_FAMILY_EXTENSION"
            ),
            "protocol_status": (
                R42_A4_WINDOW_FAMILY["protocol_status"]
            ),
            "profiles": R42_A4_WINDOW_FAMILY,
            "core_dataset_dependency": {
                "handle": os.environ[
                    "IHARQ_EXISTING_CORE_DATASET_HANDLE"
                ],
                "provider_version": int(
                    os.environ[
                        "IHARQ_EXISTING_CORE_DATASET_VERSION"
                    ]
                ),
                "manifest_sha256": os.environ[
                    "IHARQ_EXISTING_CORE_MANIFEST_SHA256"
                ],
            },
            "mutation_rule": (
                "THE_EXISTING_CORE_DATASET_IS_NOT_CHANGED"
            ),
        },
    )
    compact_paths.append(freeze_path)

    reader_path = scratch / "iharq_a4_window_shard_reader.py"
    reader_path.write_text(
        R42_A4_READER_SOURCE,
        encoding="utf-8",
    )
    compact_paths.append(reader_path)

    sidecar_path = (
        scratch
        / "IHARQ_P01_L1_A4_DERIVED_DATASET_SIDECAR.json"
    )
    _atomic_json(
        sidecar_path,
        {
            "schema_version": 1,
            "base_scientific_freeze": (
                POLICY["scientific_freeze_unchanged"]
            ),
            "window_family": R42_A4_WINDOW_FAMILY,
            "base_config_id": pipeline.config_id,
            "a4_config_id": a4_config_id,
            "dataset_records": (
                pipeline.state["dataset_records"]
            ),
            "label_records": pipeline.state["label_records"],
            "split_record": pipeline.state["split_record"],
            "preprocessing_record": (
                pipeline.state["preprocessing_record"]
            ),
            "core_dataset_pointer": (
                pipeline.state["r42_core_pointer"]
            ),
            "materialized_matched3p5s_event_count": 12_910,
            "a4_window_record_count": 51_640,
            "a4_group_count": 12_910,
            "materialized_arrays_per_event": 1,
            "registered_virtual_views_per_event": 3,
            "signal_dtype": "float32",
            "storage_efficiency_rule": (
                "OVERLAPPING_MULTI_WINDOW_BYTES_NOT_DUPLICATED"
            ),
        },
    )
    compact_paths.append(sidecar_path)

    compact_manifest = {
        path.name: {
            "sha256": _sha256(path),
            "bytes": path.stat().st_size,
            "format": (
                "JSONL"
                if path.suffix == ".jsonl"
                else "PYTHON"
                if path.suffix == ".py"
                else "JSON"
            ),
        }
        for path in compact_paths
    }

    manifest = {
        "artifact_id": (
            f"P01-L1-A4-DERIVED-WINDOWS-"
            f"{a4_config_id[:16]}-"
            f"{pipeline.state['r42_a4_attempt']}"
        ),
        "schema_version": 1,
        "provider": "Kaggle",
        "repository_or_dataset": handle,
        "access": "PRIVATE",
        "format": (
            "LOSSLESS_HDF5_MATCHED_3P5S_SUBJECT_SHARDS_"
            "WITH_REGISTERED_VIRTUAL_MULTIWINDOW_VIEWS"
        ),
        "base_scientific_freeze": (
            POLICY["scientific_freeze_unchanged"]
        ),
        "a4_window_family": R42_A4_WINDOW_FAMILY,
        "base_config_id": pipeline.config_id,
        "a4_config_id": a4_config_id,
        "core_dataset_dependency": {
            "handle": os.environ[
                "IHARQ_EXISTING_CORE_DATASET_HANDLE"
            ],
            "provider_version": int(
                os.environ[
                    "IHARQ_EXISTING_CORE_DATASET_VERSION"
                ]
            ),
            "manifest_sha256": os.environ[
                "IHARQ_EXISTING_CORE_MANIFEST_SHA256"
            ],
        },
        "source_dataset_ids": POLICY[
            "active_sources_unchanged"
        ],
        "split_record_id": (
            pipeline.state["split_record"]["record_id"]
        ),
        "preprocessing_record_id": (
            pipeline.state["preprocessing_record"]["record_id"]
        ),
        "materialized_matched3p5s_event_count": 12_910,
        "longer_window_record_count": 12_910,
        "multi_window_member_record_count": 38_730,
        "a4_window_record_count": 51_640,
        "a4_group_count": 12_910,
        "shard_count": 172,
        "signal_dtype": "float32",
        "record_schema_id_lineage_validation": "PASS",
        "core_parent_event_set_match": "PASS",
        "a4_component_counts": {
            "longer_window": 12_910,
            "multi_window_members": 38_730,
        },
        "shards": shards,
        "dataset_local_indexes": compact_manifest,
        "local_copy_status": (
            "A4_SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD"
        ),
        "reader_filename": reader_path.name,
        "consumer": "PHASE_02_LAYER_02_A4",
        "protocol_status": (
            R42_A4_WINDOW_FAMILY["protocol_status"]
        ),
        "confirmatory_use_rule": (
            "EXACT_A4_PROFILE_MUST_BE_SYNCHRONIZED_IN_PROTOCOL_V1 "
            "BEFORE_CONFIRMATORY_CLAIMS"
        ),
        "scientific_scope_changed_for_core": False,
        "core_dataset_mutated": False,
    }

    manifest_path = (
        scratch
        / "IHARQ_P01_L1_A4_DERIVED_WINDOW_DATASET_MANIFEST.json"
    )
    _atomic_json(manifest_path, manifest)
    uploaded_manifest_sha256 = _sha256(manifest_path)
    compact_paths.append(manifest_path)

    for path in compact_paths:
        tokens.append(_upload_blob_with_retry(api, path))

    create_result = _r48_create_or_adopt_a4_dataset_v1(
        handle,
        tokens,
        manifest_path.name,
        uploaded_manifest_sha256,
        scratch,
    )
    provider_version = int(create_result["provider_version"])
    remote_manifest_verification = create_result[
        "remote_manifest_verification"
    ]

    manifest["creation_status"] = "COMMITTED"
    manifest["provider_dataset_version"] = provider_version
    manifest["logical_window_family_revision"] = 2
    manifest["manifest_filename_in_dataset"] = (
        manifest_path.name
    )
    manifest["manifest_sha256"] = uploaded_manifest_sha256
    manifest["remote_manifest_verification"] = remote_manifest_verification
    manifest["provider_creation_result"] = create_result

    pointer_path = (
        pipeline.bundle_root
        / "external_artifact_pointers"
        / "a4_window_family_dataset.json"
    )
    _atomic_json(pointer_path, manifest)

    freeze_bundle_path = (
        pipeline.bundle_root
        / "config_snapshot"
        / "p01_l1_a4_window_family_freeze_R2.json"
    )
    freeze_bundle_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(freeze_path, freeze_bundle_path)

    amendment_path = (
        pipeline.bundle_root
        / "reports"
        / "phase_01"
        / "amendments"
        / "P01_L1_A4_Window_Family_Amendment_R2.md"
    )
    amendment_path.parent.mkdir(parents=True, exist_ok=True)
    amendment_path.write_text(
        textwrap.dedent(
            f"""\
            # P01/L1 A4 Window-Family Additive Amendment R2

            ## Status

            `{R42_A4_WINDOW_FAMILY["protocol_status"]}`

            ## Unchanged official core

            The verified core Dataset remains immutable:

            - Handle: `{os.environ["IHARQ_EXISTING_CORE_DATASET_HANDLE"]}`
            - Provider version: `{os.environ["IHARQ_EXISTING_CORE_DATASET_VERSION"]}`
            - Manifest SHA-256:
              `{os.environ["IHARQ_EXISTING_CORE_MANIFEST_SHA256"]}`
            - Official core window: cue +0.5 s to +3.5 s.

            ## Additive A4 data substrate

            A separate Dataset stores one lossless cue +0.0 s to +3.5 s
            tensor for every included source event. It also registers three
            exact same-event 2-second views:

            1. +0.0 s to +2.0 s
            2. +0.75 s to +2.75 s
            3. +1.5 s to +3.5 s

            The views reference slices of the matched 3.5-second tensor; their
            overlapping bytes are not duplicated.

            ## Governance boundary

            This execution makes the data substrate available to Layer 2.
            Confirmatory A4 claims require the exact profile and group
            configuration to be synchronized into Protocol v1.0 and the
            applicable Build Book. Until then, the data are valid for
            implementation readiness and diagnostic execution, not silent
            confirmatory promotion.

            ## Dataset

            - Handle: `{handle}`
            - Provider version: `{provider_version}`
            - A4 config ID: `{a4_config_id}`
            """
        ),
        encoding="utf-8",
    )

    pipeline.state["r42_a4_pointer"] = str(
        pointer_path.relative_to(pipeline.bundle_root)
    )
    pipeline.state["r42_a4_manifest"] = manifest
    pipeline.state["r42_a4_provider_version"] = (
        provider_version
    )
    pipeline.state["r42_a4_committed"] = True

    # Clear only upload tokens and compact scratch.
    pipeline.state.pop("r42_a4_tokens", None)
    pipeline.state.pop("r42_a4_upload_api", None)
    shutil.rmtree(scratch, ignore_errors=True)
    resume_root = pipeline.state.get("r48_a4_resume_root")
    if resume_root:
        shutil.rmtree(Path(resume_root), ignore_errors=True)
        pipeline.state["r48_a4_resume_checkpoint_cleanup"] = "PASS"

    return {
        "status": "PASS",
        "pointer": pipeline.state["r42_a4_pointer"],
        "dataset_handle": handle,
        "provider_dataset_version": provider_version,
        "a4_config_id": a4_config_id,
        "materialized_matched3p5s_events": 12_910,
        "a4_window_records": 51_640,
        "a4_groups": 12_910,
        "core_dataset_reused": True,
        "core_hdf5_shards_reuploaded": False,
    }

def _child_main(request_path: str) -> int:
    try:
        task = json.loads(Path(request_path).read_text(encoding="utf-8"))
        action = str(task["action"])
        if action == "descriptor": result = _child_descriptor(task)
        elif action == "materialize": result = _child_materialize(task)
        elif action == "materialize_a4": result = _r42_child_materialize_a4(task)
        else: raise RuntimeError(f"R26_CHILD_ACTION_UNKNOWN: {action}")
        print("__IHARQ_R26_CHILD_RESULT__" + json.dumps(_jsonable(result), separators=(",", ":")), flush=True)
        return 0
    except Exception as exc:
        print("__IHARQ_R26_CHILD_ERROR__" + json.dumps({"error": repr(exc), "traceback": traceback.format_exc()}), flush=True)
        return 1


def _progress_line(event: str, completed: int, total: int, started: float, current: str, child_pid: int | None, work_root: Path, extra: dict[str, Any] | None = None) -> dict[str, Any]:
    elapsed = max(0.001, time.monotonic() - started)
    rate = completed / elapsed if completed else 0.0
    remaining = max(0, total - completed)
    eta = remaining / rate if rate > 0 else None
    payload = {
        "event": event,
        "completed": completed,
        "total": total,
        "percent": round(100.0 * completed / total, 2) if total else 100.0,
        "elapsed_seconds": round(elapsed, 1),
        "eta_seconds": None if eta is None else round(eta, 1),
        "current": current,
        "parent_rss_gib": round(_rss_bytes() / _GIB, 3),
        "child_pid": child_pid,
        "child_rss_gib": round(_rss_bytes(child_pid) / _GIB, 3) if child_pid else 0.0,
        "disk": _disk_snapshot(work_root),
    }
    if extra: payload.update(_jsonable(extra))
    print("[R26 PROGRESS] " + json.dumps(payload, separators=(",", ":")), flush=True)
    return payload


def _run_child_task(task: dict[str, Any], work_root: Path, label: str, retries: int = 2) -> dict[str, Any]:
    """Run one disposable subject worker while measuring its true peak RSS.

    The measured peak is returned to the parent and is used after the real-loader
    preflight to choose the fastest memory-safe parallelism. Scientific work and
    retry semantics are unchanged.
    """
    task_root = Path(task["output_dir"])
    task_root.mkdir(parents=True, exist_ok=True)
    request_path = task_root / "request.json"
    _atomic_json(request_path, task)
    errors = []
    for attempt in range(1, retries + 1):
        output_log = task_root / f"child_attempt_{attempt}.log"
        env = os.environ.copy()
        env["IHARQ_STREAMING_CHILD"] = "1"
        env.setdefault("PYTHONHASHSEED", "0")
        command = [sys.executable, "-u", "-m", _CHILD_MODULE, "--child", str(request_path)]
        peak_rss_bytes = 0
        with output_log.open("w", encoding="utf-8", buffering=1) as log_stream:
            process = subprocess.Popen(command, env=env, stdout=log_stream, stderr=subprocess.STDOUT, text=True)
            started = time.monotonic(); last = 0.0
            try:
                while process.poll() is None:
                    time.sleep(1.0)
                    observed_rss = _rss_bytes(process.pid)
                    peak_rss_bytes = max(peak_rss_bytes, observed_rss)
                    _resource_guard(work_root, process.pid)
                    if time.monotonic() - last >= float(POLICY["progress_interval_seconds"]):
                        _progress_line(
                            "SUBJECT_CHILD_HEARTBEAT", 0, 1, started, label,
                            process.pid, work_root,
                            {"attempt": attempt, "measured_peak_rss_bytes": peak_rss_bytes},
                        )
                        last = time.monotonic()
            except Exception as exc:
                process.kill(); process.wait(timeout=30)
                errors.append({
                    "attempt": attempt,
                    "error": repr(exc),
                    "log": str(output_log),
                    "measured_peak_rss_bytes": peak_rss_bytes,
                })
            else:
                peak_rss_bytes = max(peak_rss_bytes, _rss_bytes(process.pid))
                returncode = process.wait()
                if returncode == 0 and (task_root / "result.json").is_file():
                    result = json.loads((task_root / "result.json").read_text(encoding="utf-8"))
                    result["child_peak_rss_bytes"] = max(
                        int(result.get("child_peak_rss_bytes", 0)),
                        int(peak_rss_bytes),
                    )
                    result["child_runtime_seconds"] = round(time.monotonic() - started, 3)
                    return result
                errors.append({
                    "attempt": attempt,
                    "returncode": returncode,
                    "log": str(output_log),
                    "tail": output_log.read_text(encoding="utf-8", errors="replace")[-6000:],
                    "measured_peak_rss_bytes": peak_rss_bytes,
                })
        _trim_memory()
    raise RuntimeError(f"R27_SUBJECT_TASK_FAILED: label={label}; errors={json.dumps(errors, indent=2)}")


def _combine_fit_rows(rows: list[dict[str, Any]], legal_source_ids: set[str]):
    import numpy as np
    from iharq.canonical import semantic_hash
    from iharq.layer1_data_protocol.preprocessing import FitState
    found: set[str] = set(); count = 0; mean = None; m2 = None; channel_names = None
    duplicates: set[str] = set()
    for row in rows:
        source_unit = str(row["source_unit"])
        if source_unit not in legal_source_ids:
            continue
        if source_unit in found:
            duplicates.add(source_unit)
            continue
        found.add(source_unit)
        n_b = int(row["count"]); mean_b = np.asarray(row["mean"], dtype=np.float64); m2_b = np.asarray(row["m2"], dtype=np.float64)
        names = [str(x) for x in row["channel_names"]]
        if channel_names is None:
            channel_names = names; mean = np.zeros_like(mean_b); m2 = np.zeros_like(m2_b)
        if names != channel_names:
            raise RuntimeError(f"R26_FIT_CHANNEL_ORDER_MISMATCH: source={source_unit}")
        if mean_b.shape != mean.shape:
            raise RuntimeError(f"R26_FIT_CHANNEL_COUNT_MISMATCH: source={source_unit}")
        if count == 0:
            count = n_b; mean = mean_b.copy(); m2 = m2_b.copy(); continue
        delta = mean_b - mean; total = count + n_b
        mean = mean + delta * (n_b / total)
        m2 = m2 + m2_b + delta * delta * (count * n_b / total)
        count = total
    if duplicates:
        raise RuntimeError(
            f"R26_FIT_SOURCE_DUPLICATED: count={len(duplicates)}; "
            f"sample={sorted(duplicates)[:20]}"
        )
    missing = sorted(set(legal_source_ids) - found)
    if missing:
        raise RuntimeError(f"R26_FIT_SOURCE_UNOBSERVED: count={len(missing)}; sample={missing[:20]}")
    if count <= 0 or mean is None or m2 is None:
        raise RuntimeError("R26_LEGAL_FIT_POPULATION_EMPTY")
    std = np.sqrt(m2 / count); std = np.where(std < 1e-12, 1.0, std)
    mean2 = mean[:, None]; std2 = std[:, None]
    state_hash = semantic_hash({
        "mean": [str(float(x)) for x in mean2[:, 0]],
        "std": [str(float(x)) for x in std2[:, 0]],
        "sources": sorted(legal_source_ids),
    })
    return FitState(mean2, std2, sorted(legal_source_ids), state_hash), {"sample_count": count, "channel_names": channel_names, "observed_fit_sources": len(found)}


def _ensure_kaggle_upload_api() -> dict[str, Any]:
    expected = {"kagglehub": "1.0.2", "kagglesdk": "0.1.23"}
    observed = {}
    for package, version in expected.items():
        try: observed[package] = importlib_metadata.version(package)
        except importlib_metadata.PackageNotFoundError: observed[package] = "MISSING"
    if observed != expected:
        raise RuntimeError(f"R26_KAGGLE_UPLOAD_STACK_MISMATCH: expected={expected}; observed={observed}")
    for name in list(sys.modules):
        if name == "kagglehub" or name.startswith("kagglehub.") or name == "kagglesdk" or name.startswith("kagglesdk."):
            sys.modules.pop(name, None)
    if not os.environ.get("KAGGLE_API_TOKEN"):
        try:
            from kaggle_secrets import UserSecretsClient
            token = UserSecretsClient().get_secret("KAGGLE_API_TOKEN")
        except Exception as exc:
            raise RuntimeError("R26_KAGGLE_API_TOKEN_SECRET_UNAVAILABLE") from exc
        if not token: raise RuntimeError("R26_KAGGLE_API_TOKEN_SECRET_EMPTY")
        os.environ["KAGGLE_API_TOKEN"] = token
    import functools
    import kagglehub.gcs_upload as gcs_upload_module
    if not getattr(gcs_upload_module.tqdm, "_iharq_r26_silent", False):
        silent = functools.partial(gcs_upload_module.tqdm, disable=True); silent._iharq_r26_silent = True; gcs_upload_module.tqdm = silent
    from kagglesdk.kaggle_env import get_web_endpoint
    from kagglehub.datasets_helpers import create_dataset_or_version
    from kagglehub.gcs_upload import UploadDirectoryInfo, _upload_blob
    from kagglehub.handle import parse_dataset_handle
    from kagglesdk.blobs.types.blob_api_service import ApiBlobType
    if not callable(get_web_endpoint): raise RuntimeError("R26_KAGGLESDK_ENDPOINT_API_UNAVAILABLE")
    return {
        "create_dataset_or_version": create_dataset_or_version,
        "UploadDirectoryInfo": UploadDirectoryInfo,
        "_upload_blob": _upload_blob,
        "parse_dataset_handle": parse_dataset_handle,
        "ApiBlobType": ApiBlobType,
        "versions": expected,
    }


def _upload_blob_with_retry(api: dict[str, Any], path: Path, retries: int = 3):
    errors = []
    for attempt in range(1, retries + 1):
        try:
            return api["_upload_blob"](str(path), api["ApiBlobType"].DATASET)
        except Exception as exc:
            errors.append({"attempt": attempt, "error": repr(exc)})
            if attempt < retries: time.sleep(min(30, 2 ** attempt))
    raise RuntimeError(f"R26_DERIVED_SHARD_UPLOAD_FAILED: path={path}; errors={errors}")


def _derived_identity(runner: Any) -> tuple[str, str]:
    attempt = os.environ.get("IHARQ_EXECUTION_ATTEMPT_ID")
    if not attempt:
        attempt = time.strftime("%Y%m%d%H%M%S", time.gmtime()) + "-" + uuid.uuid4().hex[:8]
        os.environ["IHARQ_EXECUTION_ATTEMPT_ID"] = attempt
    suffix = re.sub(r"[^a-z0-9-]+", "-", attempt.lower()).strip("-")[-24:]
    slug = f"{POLICY['derived_dataset_slug_prefix']}-{runner.pipeline.config_id[:12]}-{suffix}"[:100].strip("-")
    return attempt, f"{POLICY['derived_kaggle_username']}/{slug}"




def _post_preprocessing_geometry(
    recording: Any,
    operations: list[dict[str, Any]],
) -> tuple[int, int, float]:
    """Infer the exact frozen output geometry without materializing a signal."""
    names = [operation.get("name") for operation in operations]
    official = [
        "validate_units",
        "capture_events",
        "select_eeg",
        "demean",
        "rereference_average",
        "resample_polyphase_with_events",
        "bandpass_sos_zero_phase",
        "cast",
    ]
    if names != official:
        raise RuntimeError(
            "R34_STORAGE_FORECAST_PREPROCESSING_GRAPH_MISMATCH: "
            f"observed={names}"
        )

    channel_types = list(
        recording.source_metadata.get("channel_types", [])
    )
    if len(channel_types) != len(recording.channel_names):
        raise RuntimeError(
            "R34_STORAGE_FORECAST_CHANNEL_METADATA_MISMATCH: "
            f"source={_recording_source_unit(recording)}; "
            f"channels={len(recording.channel_names)}; types={len(channel_types)}"
        )
    channels = sum(str(value).lower() == "eeg" for value in channel_types)
    if channels <= 0:
        raise RuntimeError(
            "R34_STORAGE_FORECAST_NO_EEG_CHANNELS: "
            f"source={_recording_source_unit(recording)}"
        )

    input_samples = int(recording.signal.shape[1])
    input_hz = float(recording.sampling_hz)
    output_hz = 160.0
    output_samples = max(1, int(round(input_samples * output_hz / input_hz)))
    return channels, output_samples, output_hz




def _count_windows_for_event(
    *,
    event: Any,
    signal_samples: int,
    input_sampling_hz: float,
    output_sampling_hz: float,
    start_offset_samples: int,
    duration_samples: int,
) -> tuple[int, dict[str, Any] | None]:
    """Forecast the official one-window-per-event contract and invalid evidence."""
    ratio = float(output_sampling_hz) / float(input_sampling_hz)
    resampled_sample = min(
        int(round(int(event.start_sample) * ratio)),
        max(0, int(signal_samples) - 1),
    )
    start = resampled_sample + int(start_offset_samples)
    end = start + int(duration_samples)
    if start < 0 or end > int(signal_samples):
        return 0, {
            "event_id": str(event.event_id),
            "original_source_event_sample": int(event.start_sample),
            "resampled_event_sample": resampled_sample,
            "start": start,
            "end": end,
            "samples": int(signal_samples),
            "reason": "WINDOW_OUT_OF_BOUNDS",
        }
    return 1, None




def _estimate_derived_storage(pipeline: Any) -> dict[str, Any]:
    """Forecast exact logical float32 window bytes under the official freeze."""
    from iharq.layer1_data_protocol.labels import map_event_label

    operations = list(pipeline.state["operations"])
    window_profile = dict(pipeline.config.get("windows", {}))
    required = {
        "start_offset_samples": 80,
        "duration_samples": 480,
        "stride_samples": 480,
        "target_sampling_hz": 160,
        "last_window_policy": "ONE_WINDOW_PER_INCLUDED_SOURCE_EVENT",
        "bounds_policy": "REJECT_OUT_OF_BOUNDS",
    }
    mismatches = {
        key: {"expected": expected, "observed": window_profile.get(key)}
        for key, expected in required.items()
        if window_profile.get(key) != expected
    }
    if mismatches:
        raise RuntimeError(
            "R34_STORAGE_FORECAST_WINDOW_CONTRACT_MISMATCH: "
            + json.dumps(mismatches, sort_keys=True)
        )

    label_by_dataset = {
        row["payload"]["dataset_id"]: row
        for row in pipeline.state["label_records"]
    }
    rows: list[dict[str, Any]] = []
    dataset_totals: dict[str, dict[str, Any]] = {}
    subject_totals: dict[str, int] = {}
    forecast_invalid: list[dict[str, Any]] = []
    total_windows = 0
    total_logical_bytes = 0

    for recording in pipeline.state["recordings"]:
        channels, signal_samples, output_hz = _post_preprocessing_geometry(
            recording,
            operations,
        )
        accepted_events = 0
        recording_windows = 0
        recording_invalid = 0
        for event in recording.events:
            normalized = map_event_label(
                event.original_label,
                label_by_dataset[recording.dataset_id],
            )
            if normalized is None:
                continue
            accepted_events += 1
            count, invalid = _count_windows_for_event(
                event=event,
                signal_samples=signal_samples,
                input_sampling_hz=float(recording.sampling_hz),
                output_sampling_hz=output_hz,
                start_offset_samples=80,
                duration_samples=480,
            )
            recording_windows += count
            if invalid is not None:
                recording_invalid += 1
                forecast_invalid.append(
                    {
                        "dataset_id": recording.dataset_id,
                        "subject_id": recording.subject_id,
                        "session_id": recording.session_id,
                        "run_id": recording.run_id,
                        **invalid,
                    }
                )

        logical_bytes = recording_windows * channels * 480 * 4
        source_unit = _recording_source_unit(recording)
        subject_key = f"{recording.dataset_id}:subject={recording.subject_id}"
        subject_totals[subject_key] = subject_totals.get(subject_key, 0) + logical_bytes
        dataset_row = dataset_totals.setdefault(
            recording.dataset_id,
            {
                "dataset_id": recording.dataset_id,
                "recordings": 0,
                "accepted_events": 0,
                "planned_windows": 0,
                "forecast_invalid_windows": 0,
                "logical_signal_bytes": 0,
            },
        )
        dataset_row["recordings"] += 1
        dataset_row["accepted_events"] += accepted_events
        dataset_row["planned_windows"] += recording_windows
        dataset_row["forecast_invalid_windows"] += recording_invalid
        dataset_row["logical_signal_bytes"] += logical_bytes
        rows.append(
            {
                "source_unit": source_unit,
                "dataset_id": recording.dataset_id,
                "subject_id": recording.subject_id,
                "session_id": recording.session_id,
                "run_id": recording.run_id,
                "input_sampling_hz": float(recording.sampling_hz),
                "output_sampling_hz": output_hz,
                "eeg_channels": channels,
                "output_signal_samples": signal_samples,
                "start_offset_samples": 80,
                "duration_samples": 480,
                "stride_samples": 480,
                "accepted_events": accepted_events,
                "planned_windows": recording_windows,
                "forecast_invalid_windows": recording_invalid,
                "signal_dtype": "float32",
                "logical_signal_bytes": logical_bytes,
            }
        )
        total_windows += recording_windows
        total_logical_bytes += logical_bytes

    metadata_bytes_estimate = total_windows * 2048 + len(subject_totals) * 1024 * 1024
    ratio_lower = float(POLICY["storage_forecast_compression_ratio_lower"])
    ratio_upper = float(POLICY["storage_forecast_compression_ratio_upper"])
    lower_bytes = int(total_logical_bytes * ratio_lower + metadata_bytes_estimate)
    upper_bytes = int(total_logical_bytes * ratio_upper + metadata_bytes_estimate)
    recommended_capacity = int(upper_bytes * float(POLICY["storage_forecast_safety_multiplier"]))
    largest_subject_bytes = max(subject_totals.values(), default=0)
    recommended_local_scratch = int(
        largest_subject_bytes * 1.15
        + float(POLICY["minimum_disk_free_gib"]) * _GIB
    )

    report = {
        "artifact_id": f"P01-L1-DERIVED-STORAGE-FORECAST-{pipeline.config_id[:16]}",
        "policy_id": POLICY["policy_id"],
        "scientific_freeze": POLICY["scientific_freeze_unchanged"],
        "calculation_status": "EXACT_LOGICAL_FLOAT32_BYTES_PLANNING_ENVELOPE_FOR_COMPRESSION",
        "config_id": pipeline.config_id,
        "window_profile": window_profile,
        "preprocessing_operations": operations,
        "event_resampling": "MNE_POLYPHASE_JOINT_EVENTS_EQUIVALENT_INDEX_FORECAST",
        "planned_recordings": len(rows),
        "planned_subject_profiles": len(subject_totals),
        "planned_windows": total_windows,
        "forecast_invalid_window_count": len(forecast_invalid),
        "forecast_invalid_windows": forecast_invalid,
        "signal_dtype": "float32",
        "logical_float32_signal_bytes": total_logical_bytes,
        "logical_float32_signal_gib": round(total_logical_bytes / _GIB, 3),
        "estimated_index_and_hdf5_metadata_bytes": metadata_bytes_estimate,
        "lossless_hdf5_planning_envelope": {
            "lower_bytes": lower_bytes,
            "lower_gib": round(lower_bytes / _GIB, 3),
            "upper_bytes": upper_bytes,
            "upper_gib": round(upper_bytes / _GIB, 3),
            "compression_ratio_range": [ratio_lower, ratio_upper],
            "warning": "Compression ratio is planning-only; Stage 14 records exact uploaded bytes.",
        },
        "recommended_private_kaggle_capacity": {
            "bytes": recommended_capacity,
            "gib": round(recommended_capacity / _GIB, 3),
            "safety_multiplier": float(POLICY["storage_forecast_safety_multiplier"]),
        },
        "recommended_local_scratch": {
            "bytes": recommended_local_scratch,
            "gib": round(recommended_local_scratch / _GIB, 3),
            "largest_subject_logical_bytes": largest_subject_bytes,
        },
        "dataset_totals": [
            {
                **row,
                "logical_signal_gib": round(row["logical_signal_bytes"] / _GIB, 3),
            }
            for _, row in sorted(dataset_totals.items())
        ],
        "recording_rows": rows,
    }
    report_path = (
        pipeline.bundle_root
        / "reports"
        / "phase_01"
        / "storage"
        / "derived_output_storage_forecast.json"
    )
    _atomic_json(report_path, report)
    pipeline.state["r26_storage_forecast"] = report
    pipeline.state["r26_storage_forecast_path"] = str(
        report_path.relative_to(pipeline.bundle_root)
    )
    return report



def _subject_forecast_bytes(
    pipeline: Any,
    dataset_id: str,
    subject: int,
) -> int:
    forecast = pipeline.state.get(
        "r26_storage_forecast",
        {},
    )
    rows = forecast.get("recording_rows", [])
    return sum(
        int(row.get("logical_signal_bytes", 0))
        for row in rows
        if (
            str(row.get("dataset_id")) == str(dataset_id)
            and str(row.get("subject_id")) == str(subject)
        )
    )


def _assert_subject_scratch_capacity(
    pipeline: Any,
    dataset_id: str,
    subject: int,
) -> None:
    expected = _subject_forecast_bytes(
        pipeline,
        dataset_id,
        subject,
    )
    fixed_reserve = int(
        float(POLICY["minimum_disk_free_gib"]) * _GIB
    )
    required = int(expected * 1.15) + fixed_reserve
    disk = _disk_snapshot(pipeline.work_root)

    if disk["free_bytes"] < required:
        raise RuntimeError(
            "R26_SUBJECT_SHARD_SCRATCH_CAPACITY_INSUFFICIENT: "
            f"dataset={dataset_id}; subject={subject}; "
            f"expected_subject_logical_gib={expected/_GIB:.3f}; "
            f"required_free_gib={required/_GIB:.3f}; "
            f"observed_free_gib={disk['free_gib']}"
        )


def _copy_compact_path(
    source: Path,
    destination: Path,
) -> None:
    source = Path(source)
    destination = Path(destination)

    if not source.exists():
        return

    disallowed_suffixes = {
        ".h5",
        ".hdf5",
        ".mat",
        ".edf",
        ".gdf",
        ".fif",
    }

    if source.is_file():
        if source.suffix.lower() in disallowed_suffixes:
            return
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        return

    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in disallowed_suffixes:
            continue
        relative = path.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def _write_deterministic_zip(
    source_root: Path,
    zip_path: Path,
) -> None:
    source_root = Path(source_root)
    zip_path = Path(zip_path)
    zip_path.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(
        zip_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in sorted(source_root.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(
                source_root.parent
            ).as_posix()
            info = zipfile.ZipInfo(relative)
            info.date_time = (1980, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(
                info,
                path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )


def _create_github_ready_repository(
    runner: Any,
) -> dict[str, Any]:
    """
    Create a compact repository package with no raw or derived EEG arrays.

    This package is ready for later Git initialization/push, but the notebook
    deliberately does not require GitHub credentials or publish automatically.
    """
    pipeline = runner.pipeline
    attempt = pipeline.state["r26_execution_attempt_id"]
    repository_name = (
        "IHARQ_P01_L1_GitHub_Ready_Repository_"
        f"{pipeline.config_id[:12]}_"
        f"{_safe(attempt)}"
    )
    release_root = (
        pipeline.work_root
        / "github_ready_release"
    )
    repository_root = release_root / repository_name
    shutil.rmtree(repository_root, ignore_errors=True)
    repository_root.mkdir(parents=True)

    # Reusable implementation and configuration.
    _copy_compact_path(
        pipeline.package_root / "src",
        repository_root / "src",
    )
    _copy_compact_path(
        pipeline.package_root / "configs",
        repository_root / "configs",
    )
    for name in [
        "requirements-lock.txt",
        "pyproject.toml",
        "README.md",
    ]:
        _copy_compact_path(
            pipeline.package_root / name,
            repository_root / name,
        )

    runtime_dir = repository_root / "runtime_overlays"
    runtime_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        Path(__file__),
        runtime_dir / "iharq_bounded_streaming.py",
    )
    try:
        import iharq_acquisition_acceleration
        acquisition_path = Path(
            inspect.getsourcefile(
                iharq_acquisition_acceleration
            )
            or ""
        )
        if acquisition_path.is_file():
            shutil.copy2(
                acquisition_path,
                runtime_dir
                / "iharq_acquisition_acceleration.py",
            )
    except Exception:
        pass

    (
        runtime_dir
        / "iharq_window_shard_reader.py"
    ).write_text(
        WINDOW_SHARD_READER_SOURCE,
        encoding="utf-8",
    )

    # Compact scientific artifacts and evidence.
    compact_bundle_paths = [
        "authority_manifest.json",
        "environment_manifest.json",
        "notebook_manifest.json",
        "environment_amendment.json",
        "phase_execution_handoff.yaml",
        "gate_decision.json",
        "integration_patch_manifest.yaml",
        "checksums.sha256",
        "records",
        "reports/phase_01",
        "docs/cards",
        "manifests/phase_01",
        "derived_outputs/preprocessing_fit_state",
        "analysis_inputs",
        "protocol_v1_handoff",
        "layer0_handoff",
        "evidence_map_handoff",
        "layer10_source_bundle",
        "phase2_handoff",
        "handoffs",
        "external_artifact_pointers",
        "negative_and_failed_results",
        "figure_source_data",
        "table_source_data",
    ]

    for relative in compact_bundle_paths:
        _copy_compact_path(
            pipeline.bundle_root / relative,
            repository_root / "artifacts" / relative,
        )

    (repository_root / ".gitignore").write_text(
        "\n".join(
            [
                "__pycache__/",
                "*.py[cod]",
                ".pytest_cache/",
                ".mypy_cache/",
                ".venv/",
                "venv/",
                ".env",
                "*.token",
                "*.secret",
                "*.h5",
                "*.hdf5",
                "*.mat",
                "*.edf",
                "*.gdf",
                "*.fif",
                "data/raw/",
                "data/derived/",
                "source_cache/",
                "streaming_runtime/",
                "",
            ]
        ),
        encoding="utf-8",
    )

    data_dir = repository_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "README.md").write_text(
        textwrap.dedent(
            f"""\
            # Data access

            Large numerical arrays are intentionally not stored in this
            GitHub-ready repository.

            Attach the private Kaggle Dataset identified by:

            `artifacts/external_artifact_pointers/derived_windows_dataset.json`

            The original raw sources remain in the three source Kaggle
            Datasets. The derived Dataset contains lossless HDF5 subject
            shards, indexes, manifest, sidecar, storage reports, and the
            future-phase reader.

            Scientific freeze: {POLICY["scientific_freeze_unchanged"]}
            Runtime policy: {POLICY["policy_id"]}
            """
        ),
        encoding="utf-8",
    )

    (repository_root / "README.md").write_text(
        textwrap.dedent(
            f"""\
            # IHARQ Phase 01 / Layer 01

            This repository is the compact code, configuration, governance,
            records, evidence, cards, manifests, gates, and handoff companion
            to the private Kaggle derived-window Dataset.

            It contains no duplicate raw EEG files and no HDF5 window shards.

            - Config ID: `{pipeline.config_id}`
            - Execution attempt: `{attempt}`
            - Scientific freeze: `{POLICY["scientific_freeze_unchanged"]}`
            - Runtime policy: `{POLICY["policy_id"]}`
            - Derived Dataset handle:
              `{pipeline.state.get("r26_derived_handle")}`

            ## Reproduction

            1. Attach the original source Kaggle Datasets when raw-source
               regeneration is required.
            2. Attach the private derived-window Dataset for future phases.
            3. Use `runtime_overlays/iharq_window_shard_reader.py` to resolve
               window IDs to immutable HDF5 shard rows.
            4. Verify manifests and SHA-256 values before use.

            No later-phase model training is executed in Layer 1.
            """
        ),
        encoding="utf-8",
    )

    (repository_root / "SECURITY.md").write_text(
        (
            "# Security\n\n"
            "No Kaggle token or secret is stored here. Keep the derived "
            "Dataset private unless a separate license and redistribution "
            "review authorizes publication.\n"
        ),
        encoding="utf-8",
    )

    (repository_root / "DATA_LICENSE_NOTICE.md").write_text(
        (
            "# Data and license notice\n\n"
            "This compact repository does not redistribute the raw EEG "
            "sources or derived numerical shards. Dataset-specific licenses "
            "and redistribution constraints remain recorded in DatasetRecord "
            "and card artifacts. The Kaggle derived Dataset inherits those "
            "constraints and is private by default.\n"
        ),
        encoding="utf-8",
    )

    # Validate exclusions and scan for obvious secret leakage.
    files = [
        path
        for path in repository_root.rglob("*")
        if path.is_file()
    ]
    forbidden = [
        path
        for path in files
        if path.suffix.lower()
        in {".h5", ".hdf5", ".mat", ".edf", ".gdf", ".fif"}
    ]
    if forbidden:
        raise RuntimeError(
            "R26_GITHUB_READY_LARGE_ARRAY_EXCLUSION_FAILED: "
            f"{forbidden[:5]}"
        )

    # Reject actual credential files or the exact live secret value. Merely
    # mentioning the environment-variable name in code/documentation is safe.
    credential_files = [
        path
        for path in files
        if path.name.lower() in {
            "kaggle.json",
            ".env",
            "credentials.json",
        }
    ]
    if credential_files:
        raise RuntimeError(
            "R26_GITHUB_READY_SECRET_SCAN_FAILED: "
            f"credential_files={credential_files[:5]}"
        )

    live_token = os.environ.get("KAGGLE_API_TOKEN", "")
    if live_token:
        token_hits: list[str] = []
        for path in files:
            if path.stat().st_size > 5 * 1024 * 1024:
                continue
            try:
                content = path.read_bytes()
            except Exception:
                continue
            if live_token.encode("utf-8") in content:
                token_hits.append(
                    path.relative_to(
                        repository_root
                    ).as_posix()
                )
        if token_hits:
            raise RuntimeError(
                "R26_GITHUB_READY_SECRET_SCAN_FAILED: "
                f"live_token_serialized_in={token_hits[:5]}"
            )

    manifest_rows = []
    for path in sorted(files):
        manifest_rows.append(
            {
                "path": path.relative_to(
                    repository_root
                ).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
            }
        )

    repository_manifest = {
        "artifact_id": (
            f"P01-L1-GITHUB-READY-"
            f"{pipeline.config_id[:16]}-{attempt}"
        ),
        "schema_version": 1,
        "scientific_freeze": (
            POLICY["scientific_freeze_unchanged"]
        ),
        "policy_id": POLICY["policy_id"],
        "repository_name": repository_name,
        "derived_dataset_handle": (
            pipeline.state.get("r26_derived_handle")
        ),
        "file_count": len(manifest_rows),
        "files": manifest_rows,
        "excluded_large_arrays": True,
        "excluded_raw_sources": True,
        "automatic_github_publish": False,
        "reason": (
            "GitHub credentials and repository ownership are not runtime "
            "dependencies; this ZIP can be initialized/pushed later."
        ),
    }
    manifest_path = (
        repository_root
        / "GITHUB_READY_REPOSITORY_MANIFEST.json"
    )
    _atomic_json(manifest_path, repository_manifest)

    total_bytes = sum(
        path.stat().st_size
        for path in repository_root.rglob("*")
        if path.is_file()
    )
    maximum = int(
        float(POLICY["github_ready_repository_max_gib"])
        * _GIB
    )
    if total_bytes > maximum:
        raise RuntimeError(
            "R26_GITHUB_READY_REPOSITORY_TOO_LARGE: "
            f"bytes={total_bytes}; maximum={maximum}"
        )

    zip_path = (
        pipeline.work_root
        / f"{repository_name}.zip"
    )
    _write_deterministic_zip(
        repository_root,
        zip_path,
    )
    zip_hash = _sha256(zip_path)
    sidecar_path = zip_path.with_suffix(
        zip_path.suffix + ".sha256"
    )
    sidecar_path.write_text(
        f"{zip_hash}  {zip_path.name}\n",
        encoding="utf-8",
    )

    pointer = {
        "artifact_id": repository_manifest["artifact_id"],
        "format": "GITHUB_READY_REPOSITORY_ZIP",
        "path": str(zip_path),
        "sha256": zip_hash,
        "bytes": zip_path.stat().st_size,
        "repository_uncompressed_bytes": total_bytes,
        "repository_file_count": len(manifest_rows),
        "contains_large_arrays": False,
        "derived_dataset_pointer": (
            "external_artifact_pointers/"
            "derived_windows_dataset.json"
        ),
        "publication_status": (
            "READY_FOR_OWNER_CONTROLLED_GITHUB_PUSH"
        ),
    }

    pointer["detached_hash_boundary"] = (
        "THE REPOSITORY ZIP IS CREATED AFTER THE EXECUTION BUNDLE FREEZE; "
        "ITS ACTUAL SHA-256 IS RECORDED OUTSIDE BOTH SELF-REFERENTIAL ZIP FILES."
    )
    pointer_path = (
        pipeline.work_root
        / "github_ready_repository_pointer.json"
    )
    _atomic_json(pointer_path, pointer)
    release_manifest_path = (
        pipeline.work_root
        / "github_ready_repository_manifest.json"
    )
    _atomic_json(release_manifest_path, repository_manifest)
    pointer["external_pointer_path"] = str(pointer_path)
    pointer["external_manifest_path"] = str(release_manifest_path)

    pipeline.state["r26_github_ready"] = pointer
    return pointer

def _streaming_load_sources(
    self,
    input_root: Path,
):
    from concurrent.futures import (
        ThreadPoolExecutor,
        as_completed,
    )
    from iharq.layer1_data_protocol import (
        adapters as adapters_module,
    )

    recordings = []
    inventories = {}
    plan = []
    pass1_fit_rows: list[
        dict[str, Any]
    ] = []

    bundle = self.bundle_root
    descriptor_index_path = (
        bundle
        / "inputs"
        / "streaming_descriptor_index.jsonl"
    )
    fit_index_path = (
        bundle
        / "inputs"
        / "streaming_pass1_fit_stats.jsonl"
    )

    for aggregate_path in [
        descriptor_index_path,
        fit_index_path,
    ]:
        aggregate_path.unlink(
            missing_ok=True
        )

    source_resolution_file = Path(
        self.state[
            "r26_source_resolution_file"
        ]
    )
    source_resolution_sha256 = _sha256(
        source_resolution_file
    )

    profiles = list(
        self.state.get("profiles", [])
    )

    collect_fit_stats = any(
        operation.get("name")
        == "standardize_train_fit"
        for operation in (
            self.config.get(
                "preprocessing",
                {},
            ).get(
                "operations",
                [],
            )
        )
    )

    plan_by_dataset = {}

    for profile in profiles:
        adapter_class = (
            adapters_module.ADAPTERS.get(
                profile.adapter
            )
        )

        if adapter_class is None:
            self.blockers.append(
                {
                    "code": "P01_ADAPTER_UNKNOWN",
                    "dataset_id": (
                        profile.dataset_id
                    ),
                    "adapter": profile.adapter,
                    "owner": "BUILD_BOOK",
                }
            )
            continue

        adapter = adapter_class(
            profile,
            input_root,
            (
                self.work_root
                / "source_cache"
                / profile.dataset_id
            ),
        )

        try:
            files = adapter.resolve_files()
            inventory = adapter.verify_files(
                files
            )
            inventories[
                profile.dataset_id
            ] = inventory
        except Exception as exc:
            self.blockers.append(
                {
                    "code": (
                        "P01_SOURCE_LOAD_FAILED"
                    ),
                    "dataset_id": (
                        profile.dataset_id
                    ),
                    "message": str(exc),
                    "owner": "OWNER_OR_ADAPTER",
                }
            )
            continue

        subjects = _subject_values(
            profile
        )

        for subject in subjects:
            plan.append(
                (profile, int(subject))
            )

        plan_by_dataset[
            str(profile.dataset_id)
        ] = (
            profile,
            [int(value) for value in subjects],
        )

    if self.blockers:
        raise RuntimeError(
            "R26_PASS1_SOURCE_INTAKE_BLOCKED: "
            + json.dumps(
                self.blockers,
                indent=2,
            )
        )

    checkpoint_root = (
        self.work_root
        / "streaming_runtime"
        / "pass1_subject_checkpoints"
        / _safe(self.config_id)
    )
    checkpoint_root.mkdir(
        parents=True,
        exist_ok=True,
    )

    child_root = (
        self.work_root
        / "streaming_runtime"
        / "pass1_descriptors"
    )

    cpu_count = max(
        1,
        int(os.cpu_count() or 1),
    )

    # Upper bounds only. The final worker count is resolved *after* a real
    # conversion preflight using measured peak RSS and currently available RAM.
    parallelism_upper_bounds = {
        "PhysioNetMI": min(8, cpu_count),
        "BNCI2014_001": min(6, cpu_count),
        "Lee2019_MI": min(4, cpu_count),
    }
    configured_parallelism = dict(parallelism_upper_bounds)
    resolved_parallelism: dict[str, int] = {}
    parallelism_evidence: dict[str, dict[str, Any]] = {}

    def available_memory_bytes() -> int:
        try:
            import psutil
            return int(psutil.virtual_memory().available)
        except Exception:
            try:
                return int(os.sysconf("SC_AVPHYS_PAGES")) * int(os.sysconf("SC_PAGE_SIZE"))
            except Exception:
                # Conservative fallback for environments without either API.
                return 8 * _GIB

    def resolve_parallelism(dataset_id: str, preflight_result: dict[str, Any]) -> int:
        available = max(1, available_memory_bytes())
        measured_peak = max(
            int(preflight_result.get("child_peak_rss_bytes", 0)),
            512 * 1024 * 1024,
        )
        # Keep a large parent/filesystem reserve and inflate the measured worker
        # footprint. This makes acceleration adaptive without risking OOM-driven
        # corruption or repeated subject failures.
        reserve = max(4 * _GIB, int(available * 0.20))
        usable = max(measured_peak, available - reserve)
        guarded_per_worker = max(1 * _GIB, int(measured_peak * 1.60))
        memory_cap = max(1, int(usable // guarded_per_worker))
        upper = max(1, int(parallelism_upper_bounds.get(dataset_id, 1)))
        selected = max(1, min(cpu_count, upper, memory_cap))
        resolved_parallelism[dataset_id] = selected
        parallelism_evidence[dataset_id] = {
            "selected_workers": selected,
            "cpu_count": cpu_count,
            "dataset_upper_bound": upper,
            "available_memory_bytes": available,
            "reserved_memory_bytes": reserve,
            "measured_preflight_peak_rss_bytes": measured_peak,
            "guarded_per_worker_bytes": guarded_per_worker,
            "memory_worker_cap": memory_cap,
            "safety_multiplier": 1.60,
            "scientific_scope_changed": False,
        }
        return selected

    result_by_key: dict[
        tuple[str, int],
        tuple[
            list[dict[str, Any]],
            list[dict[str, Any]],
        ],
    ] = {}

    started = time.monotonic()
    last_progress = 0.0
    completed = 0
    completed_recordings = 0
    reused_checkpoints = 0
    generated_checkpoints = 0
    total_subjects = len(plan)

    def profile_sha256(
        profile,
    ) -> str:
        payload = json.dumps(
            _jsonable(
                _profile_dict(profile)
            ),
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        return hashlib.sha256(
            payload
        ).hexdigest()

    def checkpoint_paths(
        dataset_id: str,
        subject: int,
    ) -> tuple[Path, Path, Path]:
        root = (
            checkpoint_root
            / _safe(dataset_id)
            / f"subject_{subject:03d}"
        )
        root.mkdir(
            parents=True,
            exist_ok=True,
        )
        return (
            root / "descriptors.jsonl",
            root / "fit_stats.jsonl",
            root / "checkpoint_manifest.json",
        )

    def load_checkpoint(
        profile,
        subject: int,
    ):
        dataset_id = str(
            profile.dataset_id
        )
        descriptor_path, fit_path, manifest_path = (
            checkpoint_paths(
                dataset_id,
                subject,
            )
        )

        if not (
            descriptor_path.is_file()
            and fit_path.is_file()
            and manifest_path.is_file()
        ):
            return None

        try:
            manifest = json.loads(
                manifest_path.read_text(
                    encoding="utf-8"
                )
            )

            expected_inventory = str(
                inventories[
                    dataset_id
                ].get(
                    "observed_checksum",
                    inventories[
                        dataset_id
                    ].get(
                        "aggregate_sha256",
                        "",
                    ),
                )
            )

            required = {
                "checkpoint_policy_id": (
                    "P01-L1-R26-PASS1-"
                    "SUBJECT-CHECKPOINT-R1"
                ),
                "config_id": (
                    str(self.config_id)
                ),
                "dataset_id": dataset_id,
                "subject": int(subject),
                "source_resolution_sha256": (
                    source_resolution_sha256
                ),
                "profile_sha256": (
                    profile_sha256(profile)
                ),
                "source_inventory_sha256": (
                    expected_inventory
                ),
                "collect_fit_stats": bool(
                    collect_fit_stats
                ),
            }

            for key, expected in (
                required.items()
            ):
                if (
                    manifest.get(key)
                    != expected
                ):
                    raise RuntimeError(
                        "CHECKPOINT_FIELD_MISMATCH: "
                        f"{key}; "
                        f"expected={expected!r}; "
                        f"observed="
                        f"{manifest.get(key)!r}"
                    )

            if (
                _sha256(descriptor_path)
                != manifest.get(
                    "descriptor_sha256"
                )
            ):
                raise RuntimeError(
                    "CHECKPOINT_DESCRIPTOR_SHA256_"
                    "MISMATCH"
                )

            if (
                _sha256(fit_path)
                != manifest.get(
                    "fit_stats_sha256"
                )
            ):
                raise RuntimeError(
                    "CHECKPOINT_FIT_SHA256_MISMATCH"
                )

            rows = _read_jsonl(
                descriptor_path
            )
            fit_rows = _read_jsonl(
                fit_path
            )

            if not rows:
                raise RuntimeError(
                    "CHECKPOINT_EMPTY_DESCRIPTORS"
                )

            if any(
                str(row.get("dataset_id"))
                != dataset_id
                or str(row.get("subject_id"))
                != str(subject)
                for row in rows
            ):
                raise RuntimeError(
                    "CHECKPOINT_SUBJECT_SCOPE_"
                    "MISMATCH"
                )

            if (
                collect_fit_stats
                and len(fit_rows)
                != len(rows)
            ):
                raise RuntimeError(
                    "CHECKPOINT_FIT_ROW_COUNT_"
                    "MISMATCH"
                )

            return rows, fit_rows

        except Exception as exc:
            rejection_path = (
                manifest_path.parent
                / "checkpoint_rejection.json"
            )
            _atomic_json(
                rejection_path,
                {
                    "event": (
                        "PASS1_CHECKPOINT_REJECTED"
                    ),
                    "dataset_id": dataset_id,
                    "subject": int(subject),
                    "reason": repr(exc),
                    "recorded_unix": time.time(),
                },
            )

            for path in [
                descriptor_path,
                fit_path,
                manifest_path,
            ]:
                path.unlink(
                    missing_ok=True
                )

            return None

    def commit_checkpoint(
        profile,
        subject: int,
        rows,
        fit_rows,
    ):
        dataset_id = str(
            profile.dataset_id
        )
        descriptor_path, fit_path, manifest_path = (
            checkpoint_paths(
                dataset_id,
                subject,
            )
        )

        descriptor_temp = (
            descriptor_path
            .with_suffix(
                ".jsonl.tmp"
            )
        )
        fit_temp = (
            fit_path
            .with_suffix(
                ".jsonl.tmp"
            )
        )

        for path in [
            descriptor_temp,
            fit_temp,
        ]:
            path.unlink(
                missing_ok=True
            )

        _append_jsonl(
            descriptor_temp,
            rows,
        )
        _append_jsonl(
            fit_temp,
            fit_rows,
        )

        descriptor_temp.replace(
            descriptor_path
        )
        fit_temp.replace(
            fit_path
        )

        inventory_sha256 = str(
            inventories[
                dataset_id
            ].get(
                "observed_checksum",
                inventories[
                    dataset_id
                ].get(
                    "aggregate_sha256",
                    "",
                ),
            )
        )

        _atomic_json(
            manifest_path,
            {
                "checkpoint_policy_id": (
                    "P01-L1-R26-PASS1-"
                    "SUBJECT-CHECKPOINT-R1"
                ),
                "scientific_freeze": (
                    POLICY[
                        "scientific_freeze_"
                        "unchanged"
                    ]
                ),
                "config_id": (
                    str(self.config_id)
                ),
                "dataset_id": dataset_id,
                "subject": int(subject),
                "source_resolution_sha256": (
                    source_resolution_sha256
                ),
                "profile_sha256": (
                    profile_sha256(profile)
                ),
                "source_inventory_sha256": (
                    inventory_sha256
                ),
                "collect_fit_stats": bool(
                    collect_fit_stats
                ),
                "descriptor_rows": len(rows),
                "fit_stat_rows": len(
                    fit_rows
                ),
                "descriptor_sha256": (
                    _sha256(descriptor_path)
                ),
                "fit_stats_sha256": (
                    _sha256(fit_path)
                ),
                "status": (
                    "ATOMICALLY_COMMITTED"
                ),
                "created_unix": time.time(),
            },
        )

    def make_task(
        profile,
        subject: int,
    ):
        dataset_id = str(
            profile.dataset_id
        )
        task_dir = (
            child_root
            / _safe(dataset_id)
            / f"subject_{subject:03d}"
        )

        task = {
            "action": "descriptor",
            "profile": (
                _profile_dict(profile)
            ),
            "subject": int(subject),
            "input_root": str(input_root),
            "child_work_root": str(
                task_dir / "work"
            ),
            "child_report_root": str(
                task_dir / "report"
            ),
            "output_dir": str(
                task_dir / "output"
            ),
            "source_resolution_file": str(
                source_resolution_file
            ),
            "collect_fit_stats": (
                collect_fit_stats
            ),
            "split_profile": (
                self.config.get(
                    "split",
                    {},
                )
            ),
            "fit_roles": (
                self.config.get(
                    "preprocessing",
                    {},
                ).get(
                    "fit_roles",
                    ["train"],
                )
            ),
        }

        return task_dir, task

    def record_progress(
        current: str,
        active_workers: int,
    ):
        nonlocal last_progress

        now = time.monotonic()
        if (
            now - last_progress
            >= float(
                POLICY[
                    "progress_interval_seconds"
                ]
            )
            or completed == total_subjects
        ):
            _progress_line(
                "PASS1_DESCRIPTOR_PROGRESS",
                completed,
                total_subjects,
                started,
                current,
                None,
                self.work_root,
                {
                    "recordings": (
                        completed_recordings
                    ),
                    "reused_checkpoints": (
                        reused_checkpoints
                    ),
                    "generated_checkpoints": (
                        generated_checkpoints
                    ),
                    "active_parallel_workers": (
                        active_workers
                    ),
                    "parallelism_policy": (
                        configured_parallelism
                    ),
                },
            )
            last_progress = now

    def consume_child_result(
        profile,
        dataset_id: str,
        subject: int,
        result: dict[str, Any],
    ) -> None:
        nonlocal generated_checkpoints
        nonlocal completed_recordings

        rows = _read_jsonl(
            Path(result["descriptor_path"])
        )
        fit_rows = _read_jsonl(
            Path(result["fit_stats_path"])
        )

        if not rows:
            raise RuntimeError(
                "R26_EMPTY_DESCRIPTOR_RESULT: "
                f"{dataset_id}:subject={subject}"
            )

        if (
            collect_fit_stats
            and len(fit_rows) != len(rows)
        ):
            raise RuntimeError(
                "R26_PASS1_FIT_ROW_COUNT_MISMATCH: "
                f"{dataset_id}:subject={subject}; "
                f"descriptors={len(rows)}; "
                f"fit_rows={len(fit_rows)}"
            )

        commit_checkpoint(
            profile,
            subject,
            rows,
            fit_rows,
        )
        result_by_key[(dataset_id, subject)] = (
            rows,
            fit_rows,
        )
        generated_checkpoints += 1
        completed_recordings += len(rows)

    def failure_row(
        dataset_id: str,
        subject: int,
        exc: BaseException,
        phase: str,
    ) -> dict[str, Any]:
        return {
            "dataset_id": dataset_id,
            "subject": int(subject),
            "phase": phase,
            "error_type": type(exc).__name__,
            "error": repr(exc),
            "traceback": traceback.format_exc(),
        }

    def write_dataset_failure(
        dataset_id: str,
        errors: list[dict[str, Any]],
    ) -> Path:
        failure_path = (
            bundle
            / "negative_and_failed_results"
            / (
                "pass1_dataset_failures_"
                + _safe(dataset_id)
                + ".json"
            )
        )
        _atomic_json(
            failure_path,
            {
                "dataset_id": dataset_id,
                "errors": errors,
                "successful_subject_checkpoints": sum(
                    1
                    for current_dataset, _
                    in result_by_key
                    if current_dataset == dataset_id
                ),
                "checkpoint_root": str(
                    checkpoint_root
                ),
                "failure_policy": (
                    "REAL_LOADER_PREFLIGHT_THEN_"
                    "BOUNDED_PARALLEL_EXECUTION"
                ),
            },
        )
        return failure_path

    for dataset_id, (
        profile,
        subjects,
    ) in plan_by_dataset.items():
        # Stay serial until the real-loader preflight measures this dataset's
        # actual memory footprint. Parallelism is then raised to the fastest
        # guarded value for the remaining subjects.
        max_workers = 1

        subjects_to_run: list[int] = []
        dataset_errors: list[dict[str, Any]] = []

        # Resolve valid checkpoints before creating any process. A clean run
        # has no checkpoints; a resumed run skips completed subjects exactly.
        for subject in subjects:
            checkpoint = load_checkpoint(
                profile,
                subject,
            )
            if checkpoint is None:
                subjects_to_run.append(subject)
                continue

            rows, fit_rows = checkpoint
            result_by_key[(dataset_id, subject)] = (
                rows,
                fit_rows,
            )
            reused_checkpoints += 1
            completed += 1
            completed_recordings += len(rows)
            record_progress(
                (
                    "CHECKPOINT_REUSED:"
                    f"{dataset_id}:subject={subject}"
                ),
                max_workers,
            )

        # Real conversion preflight: not merely a filename/path probe. This
        # catches downloader leakage, MAT incompatibility, MOABB API drift,
        # event/channel errors, and adapter errors before mass submission.
        if subjects_to_run:
            preflight_subject = subjects_to_run.pop(0)
            task_dir, task = make_task(
                profile,
                preflight_subject,
            )
            try:
                preflight_result = _run_child_task(
                    task,
                    self.work_root,
                    (
                        f"PREFLIGHT:{dataset_id}:"
                        f"subject={preflight_subject}"
                    ),
                )
                consume_child_result(
                    profile,
                    dataset_id,
                    preflight_subject,
                    preflight_result,
                )
                max_workers = resolve_parallelism(
                    dataset_id,
                    preflight_result,
                )
            except Exception as exc:
                row = failure_row(
                    dataset_id,
                    preflight_subject,
                    exc,
                    "REAL_LOADER_PREFLIGHT",
                )
                dataset_errors.append(row)
                failure_path = write_dataset_failure(
                    dataset_id,
                    dataset_errors,
                )
                raise RuntimeError(
                    "R26_PASS1_REAL_LOADER_PREFLIGHT_FAILED: "
                    f"dataset={dataset_id}; "
                    f"subject={preflight_subject}; "
                    f"error={repr(exc)}; "
                    f"evidence={failure_path}"
                ) from exc
            finally:
                completed += 1
                record_progress(
                    (
                        f"PREFLIGHT:{dataset_id}:"
                        f"subject={preflight_subject}"
                    ),
                    1,
                )
                shutil.rmtree(
                    task_dir,
                    ignore_errors=True,
                )
                _trim_memory()

        # Only subjects that passed the dataset-level real-loader preflight
        # reach bounded parallel execution. A fully checkpoint-reused dataset
        # performs no new child work.
        if dataset_id not in resolved_parallelism:
            resolved_parallelism[dataset_id] = 1
            parallelism_evidence[dataset_id] = {
                "selected_workers": 1,
                "reason": "NO_PENDING_SUBJECTS_AFTER_CHECKPOINT_VALIDATION",
                "scientific_scope_changed": False,
            }
        pending = {}
        with ThreadPoolExecutor(
            max_workers=max_workers,
            thread_name_prefix=(
                "iharq-pass1-"
                + _safe(dataset_id)
            ),
        ) as executor:
            for subject in subjects_to_run:
                task_dir, task = make_task(
                    profile,
                    subject,
                )
                future = executor.submit(
                    _run_child_task,
                    task,
                    self.work_root,
                    (
                        f"PASS1:{dataset_id}:"
                        f"subject={subject}"
                    ),
                )
                pending[future] = (
                    subject,
                    task_dir,
                )

            for future in as_completed(pending):
                subject, task_dir = pending[future]
                try:
                    consume_child_result(
                        profile,
                        dataset_id,
                        subject,
                        future.result(),
                    )
                except Exception as exc:
                    dataset_errors.append(
                        failure_row(
                            dataset_id,
                            subject,
                            exc,
                            "BOUNDED_PARALLEL_SUBJECT",
                        )
                    )
                finally:
                    completed += 1
                    record_progress(
                        (
                            f"PASS1:{dataset_id}:"
                            f"subject={subject}"
                        ),
                        max_workers,
                    )
                    shutil.rmtree(
                        task_dir,
                        ignore_errors=True,
                    )
                    _trim_memory()

        if dataset_errors:
            failure_path = write_dataset_failure(
                dataset_id,
                dataset_errors,
            )
            sample = [
                {
                    "subject": row["subject"],
                    "error_type": row["error_type"],
                    "error": row["error"],
                }
                for row in dataset_errors[:2]
            ]
            raise RuntimeError(
                "R26_PASS1_DATASET_SUBJECT_FAILURES: "
                f"dataset={dataset_id}; "
                f"failed={len(dataset_errors)}; "
                f"sample={json.dumps(sample, default=str)}; "
                f"evidence={failure_path}"
            )

    aggregate_descriptor_rows = []
    aggregate_fit_rows = []

    for profile, subject in plan:
        key = (
            str(profile.dataset_id),
            int(subject),
        )

        if key not in result_by_key:
            raise RuntimeError(
                "R26_PASS1_RESULT_MISSING: "
                f"{key}"
            )

        rows, fit_rows = (
            result_by_key[key]
        )

        recordings.extend(
            _recording_from_descriptor(row)
            for row in rows
        )
        pass1_fit_rows.extend(
            fit_rows
        )
        aggregate_descriptor_rows.extend(
            rows
        )
        aggregate_fit_rows.extend(
            fit_rows
        )

    descriptor_temp = (
        descriptor_index_path
        .with_suffix(
            ".jsonl.tmp"
        )
    )
    fit_temp = (
        fit_index_path
        .with_suffix(
            ".jsonl.tmp"
        )
    )

    for path in [
        descriptor_temp,
        fit_temp,
    ]:
        path.unlink(
            missing_ok=True
        )

    _append_jsonl(
        descriptor_temp,
        aggregate_descriptor_rows,
    )
    _append_jsonl(
        fit_temp,
        aggregate_fit_rows,
    )

    descriptor_index_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    descriptor_temp.replace(
        descriptor_index_path
    )
    fit_temp.replace(
        fit_index_path
    )

    self.state[
        "recordings"
    ] = recordings
    self.state[
        "inventories"
    ] = inventories
    self.state[
        "r26_subject_plan"
    ] = [
        (
            profile.dataset_id,
            subject,
        )
        for profile, subject in plan
    ]
    self.state[
        "r26_pass1_fit_rows"
    ] = pass1_fit_rows
    self.state[
        "r26_descriptor_index_path"
    ] = str(
        descriptor_index_path.relative_to(
            bundle
        )
    )
    self.state[
        "r26_pass1_fit_index_path"
    ] = str(
        fit_index_path.relative_to(
            bundle
        )
    )

    _atomic_json(
        (
            bundle
            / "reports"
            / "phase_01"
            / "runtime"
            / "bounded_streaming"
            / "pass1_summary.json"
        ),
        {
            "policy_id": (
                POLICY["policy_id"]
            ),
            "checkpoint_policy_id": (
                "P01-L1-R26-PASS1-"
                "SUBJECT-CHECKPOINT-R1"
            ),
            "subjects_processed": (
                len(plan)
            ),
            "recordings": (
                len(recordings)
            ),
            "descriptor_index": (
                self.state[
                    "r26_descriptor_index_path"
                ]
            ),
            "fit_stats_index": (
                self.state[
                    "r26_pass1_fit_index_path"
                ]
            ),
            "pass1_fit_stat_rows": (
                len(pass1_fit_rows)
            ),
            "signals_retained_in_parent": (
                False
            ),
            "reused_checkpoints": (
                reused_checkpoints
            ),
            "generated_checkpoints": (
                generated_checkpoints
            ),
            "checkpoint_hash_validation": (
                True
            ),
            "parallelism_upper_bounds": (
                configured_parallelism
            ),
            "resolved_parallelism": (
                resolved_parallelism
            ),
            "parallelism_evidence": (
                parallelism_evidence
            ),
            "cpu_count": cpu_count,
        },
    )

    return recordings




def _split_budget_without_signal_fit(self):
    """Construct the frozen split/budget/preprocessing plan without loading signals.

    This is the accelerated equivalent of the planning half of authoritative
    R6 ``Layer1Pipeline.split_budget_preprocess``.  Event rows intentionally
    use the exact authoritative schema consumed by ``budgets.allocate`` and
    later lineage surfaces.
    """
    from iharq.layer1_data_protocol.splits import (
        construct,
        recording_role,
        validate_disjointness,
        validate_role_coverage,
    )
    from iharq.layer1_data_protocol.budgets import allocate
    from iharq.layer1_data_protocol.preprocessing import compile_operations
    from iharq.layer1_data_protocol.labels import map_event_label

    split_profile = self.config.get("split", {})
    dataset_record_ids = [
        row["record_id"]
        for row in self.state["dataset_records"]
    ]
    assignment, split_record = construct(
        self.state["recordings"],
        split_profile,
        self.config_id,
        dataset_record_ids,
    )
    self.state["assignment"] = assignment
    self.state["split_record"] = split_record
    self.state["records"].append(split_record)

    group_keys = list(split_profile["group_keys"])
    required_roles = list(split_profile["roles"])
    self.state["split_disjointness"] = validate_disjointness(
        self.state["recordings"],
        assignment,
        group_keys,
    )
    self.state["split_role_coverage"] = validate_role_coverage(
        assignment,
        required_roles,
    )

    label_by_dataset = {
        row["payload"]["dataset_id"]: row
        for row in self.state["label_records"]
    }
    event_rows: list[dict[str, Any]] = []
    for recording in self.state["recordings"]:
        dataset_id = recording.dataset_id
        if dataset_id not in label_by_dataset:
            raise RuntimeError(
                "R35_STAGE11_LABEL_RECORD_MISSING: "
                f"dataset_id={dataset_id!r}"
            )
        role = recording_role(
            recording,
            assignment,
            group_keys,
        )
        label_record = label_by_dataset[dataset_id]
        source_unit = _recording_source_unit(recording)
        for event in recording.events:
            # Exact authoritative R6 row contract.  These identity fields are
            # required by deterministic low-calibration budget allocation.
            event_rows.append(
                {
                    "event_id": event.event_id,
                    "dataset_id": recording.dataset_id,
                    "subject_id": recording.subject_id,
                    "session_id": recording.session_id,
                    "run_id": recording.run_id,
                    "role": role,
                    "normalized_label": map_event_label(
                        event.original_label,
                        label_record,
                    ),
                    "source_unit": source_unit,
                }
            )

    required_event_fields = {
        "event_id",
        "dataset_id",
        "subject_id",
        "session_id",
        "run_id",
        "role",
        "normalized_label",
        "source_unit",
    }
    malformed = [
        {
            "index": index,
            "missing": sorted(
                required_event_fields.difference(row)
            ),
        }
        for index, row in enumerate(event_rows)
        if required_event_fields.difference(row)
    ]
    if malformed:
        raise RuntimeError(
            "R35_STAGE11_EVENT_ROW_SCHEMA_INVALID: "
            + json.dumps(malformed[:20], indent=2)
        )
    if not event_rows:
        raise RuntimeError("R35_STAGE11_EVENT_ROWS_EMPTY")

    self.state["event_rows"] = event_rows
    budgets, budget_report = allocate(
        event_rows,
        self.config.get("budgets", {}),
    )
    self.state["budgets"] = budgets
    self.state["budget_report"] = budget_report
    split_record["payload"]["budget_ids"] = [
        row["budget_id"]
        for row in budgets
    ]
    split_record["payload"]["source_event_ids"] = sorted(
        row["event_id"]
        for row in event_rows
    )

    operations = compile_operations(
        self.config.get("preprocessing", {})
    )
    self.state["operations"] = operations
    fit_roles = set(
        self.config["preprocessing"].get(
            "fit_roles",
            ["train"],
        )
    )
    legal = {
        row["source_unit"]
        for row in event_rows
        if row["role"] in fit_roles
    }
    if not legal:
        raise RuntimeError("R26_LEGAL_FIT_POPULATION_EMPTY")
    self.state["r26_legal_fit_source_ids"] = sorted(legal)

    _atomic_json(
        self.bundle_root
        / "reports"
        / "phase_01"
        / "runtime"
        / "bounded_streaming"
        / "split_budget_fit_plan.json",
        {
            "policy_id": POLICY["policy_id"],
            "repair_id": (
                "P01-L1-R35-STAGE11-"
                "AUTHORITATIVE-EVENT-ROW-CONTRACT-R1"
            ),
            "split_record_id": split_record["record_id"],
            "event_row_count": len(event_rows),
            "event_row_required_fields": sorted(
                required_event_fields
            ),
            "event_row_contract": (
                "AUTHORITATIVE_R6_DATASET_SUBJECT_"
                "SESSION_RUN_EVENT_ROLE_LABEL_SOURCE_UNIT"
            ),
            "budget_status": budget_report.get("status"),
            "budget_allocation_count": len(budgets),
            "legal_fit_sources": sorted(legal),
            "operations": operations,
            "signal_arrays_loaded": False,
            "scientific_scope_changed": False,
        },
    )




def _streaming_fit(runner: Any) -> dict[str, Any]:
    import numpy as np
    from iharq.canonical import semantic_hash
    from iharq.layer1_data_protocol.preprocessing import FitState, build_preprocessing_record
    pipeline = runner.pipeline; operations = list(pipeline.state["operations"]); legal = set(pipeline.state["r26_legal_fit_source_ids"])
    need = any(op["name"] == "standardize_train_fit" for op in operations)
    fit_rows: list[dict[str, Any]] = list(pipeline.state.get("r26_pass1_fit_rows", []))
    if need:
        fit_state, detail = _combine_fit_rows(fit_rows, legal)
        detail["fit_stats_collected_during_pass1"] = True
        detail["additional_source_reload_for_fit"] = False
    else:
        fit_state = FitState(None, None, sorted(legal), semantic_hash({"fit": "not-required", "sources": sorted(legal)})); detail = {"fit_required": False}
    fit_dir = pipeline.bundle_root / "derived_outputs" / "preprocessing_fit_state"; fit_dir.mkdir(parents=True, exist_ok=True)
    npz_path = fit_dir / "fit_state.npz"
    np.savez_compressed(npz_path, mean=np.asarray([]) if fit_state.mean is None else fit_state.mean, std=np.asarray([]) if fit_state.std is None else fit_state.std, source_ids=np.asarray(fit_state.source_ids), state_hash=np.asarray(fit_state.state_hash))
    fit_manifest = {
        "policy_id": POLICY["policy_id"], "state_hash": fit_state.state_hash, "source_ids": fit_state.source_ids, "mean_shape": None if fit_state.mean is None else list(fit_state.mean.shape), "std_shape": None if fit_state.std is None else list(fit_state.std.shape),
        "npz_path": str(npz_path.relative_to(pipeline.bundle_root)), "npz_sha256": _sha256(npz_path), "npz_bytes": npz_path.stat().st_size, "reduction": "DETERMINISTIC_FLOAT64_CHAN_PARALLEL_VARIANCE_IN_FROZEN_SUBJECT_ORDER", **detail,
    }
    _atomic_json(fit_dir / "fit_state_manifest.json", fit_manifest)
    source_ids = [r["record_id"] for r in pipeline.state["dataset_records"]] + [pipeline.state["split_record"]["record_id"]]
    preproc = build_preprocessing_record(pipeline.config["preprocessing"], operations, fit_state, source_ids, pipeline.config_id, "external_artifact_pointers/derived_windows_dataset.json")
    preproc["payload"]["split_record_id"] = pipeline.state["split_record"]["record_id"]
    preproc["payload"]["fit_state_pointer"] = str((fit_dir / "fit_state_manifest.json").relative_to(pipeline.bundle_root))
    pipeline.state["preprocessing_record"] = preproc; pipeline.state["records"].append(preproc); pipeline.state["fit_source_ids"] = fit_state.source_ids; pipeline.state["r26_fit_state"] = fit_state
    storage_forecast = _estimate_derived_storage(pipeline)
    return {
        "preprocessing_record": preproc["record_id"],
        "fit_state": fit_manifest,
        "storage_forecast": {
            "planned_windows": storage_forecast["planned_windows"],
            "logical_float32_signal_gib": storage_forecast[
                "logical_float32_signal_gib"
            ],
            "planning_lower_gib": storage_forecast[
                "lossless_hdf5_planning_envelope"
            ]["lower_gib"],
            "planning_upper_gib": storage_forecast[
                "lossless_hdf5_planning_envelope"
            ]["upper_gib"],
            "recommended_private_kaggle_capacity_gib": storage_forecast[
                "recommended_private_kaggle_capacity"
            ]["gib"],
            "report_path": pipeline.state[
                "r26_storage_forecast_path"
            ],
        },
    }



def _streaming_materialize(runner: Any) -> dict[str, Any]:
    pipeline = runner.pipeline
    api = _ensure_kaggle_upload_api()
    attempt, handle = _derived_identity(runner)

    plan = list(pipeline.state["r26_subject_plan"])
    profile_by_dataset = {
        profile.dataset_id: profile
        for profile in pipeline.state["profiles"]
    }
    label_by_dataset = {
        row["payload"]["dataset_id"]: row
        for row in pipeline.state["label_records"]
    }
    dataset_record_by_dataset = {
        row["payload"]["dataset_id"]: row["record_id"]
        for row in pipeline.state["dataset_records"]
    }

    fit_state = pipeline.state["r26_fit_state"]
    fit_payload = {
        "mean": (
            None
            if fit_state.mean is None
            else fit_state.mean.tolist()
        ),
        "std": (
            None
            if fit_state.std is None
            else fit_state.std.tolist()
        ),
        "source_ids": fit_state.source_ids,
        "state_hash": fit_state.state_hash,
    }

    root = (
        pipeline.work_root
        / "streaming_runtime"
        / "pass2b_materialize"
    )
    location_target = (
        pipeline.bundle_root
        / "external_artifact_pointers"
        / "window_to_shard.jsonl"
    )
    if location_target.exists():
        location_target.unlink()

    tokens: list[str] = []
    shard_rows: list[dict[str, Any]] = []
    window_records: list[dict[str, Any]] = []
    window_index: list[dict[str, Any]] = []
    quality_records: list[dict[str, Any]] = []
    quality_summaries: list[dict[str, Any]] = []
    invalid_windows: list[dict[str, Any]] = []

    started = time.monotonic()
    last_progress = 0.0
    completed = 0
    uploaded_bytes = 0
    logical_window_bytes = 0
    dataset_actual: dict[str, dict[str, Any]] = {}

    for dataset, subject in plan:
        _assert_subject_scratch_capacity(
            pipeline,
            dataset,
            int(subject),
        )

        label = f"PASS2B:{dataset}:subject={subject}"
        task_dir = (
            root
            / _safe(dataset)
            / f"subject_{int(subject):03d}"
        )
        shard_filename = (
            f"{_safe(dataset)}_"
            f"subject_{int(subject):03d}_windows.h5"
        )
        profile = profile_by_dataset[dataset]

        task = {
            "action": "materialize",
            "profile": _profile_dict(profile),
            "subject": int(subject),
            "input_root": str(runner.input_root),
            "child_work_root": str(task_dir / "work"),
            "child_report_root": str(task_dir / "report"),
            "output_dir": str(task_dir / "output"),
            "source_resolution_file": str(
                pipeline.state[
                    "r26_source_resolution_file"
                ]
            ),
            "operations": pipeline.state["operations"],
            "fit_state": fit_payload,
            "assignment": pipeline.state["assignment"],
            "split_keys": list(
                pipeline.config["split"]["group_keys"]
            ),
            "label_record": label_by_dataset[dataset],
            "preprocessing_record": (
                pipeline.state["preprocessing_record"]
            ),
            "split_record": pipeline.state["split_record"],
            "quality_profile": pipeline.config.get(
                "quality",
                {},
            ),
            "window_profile": pipeline.config.get(
                "windows",
                {},
            ),
            "config_id": pipeline.config_id,
            "dataset_record_id": (
                dataset_record_by_dataset[dataset]
            ),
            "shard_filename": shard_filename,
        }

        result = _run_child_task(
            task,
            pipeline.work_root,
            label,
        )

        subject_logical = int(
            result.get("logical_window_bytes", 0)
        )
        logical_window_bytes += subject_logical

        quality_records.extend(
            _read_jsonl(
                Path(result["quality_records_path"])
            )
        )
        quality_summaries.extend(
            _read_jsonl(
                Path(result["quality_summaries_path"])
            )
        )
        invalid_windows.extend(
            _read_jsonl(
                Path(result["invalid_windows_path"])
            )
        )
        window_records.extend(
            _read_jsonl(
                Path(result["window_records_path"])
            )
        )
        window_index.extend(
            _read_jsonl(
                Path(result["window_index_path"])
            )
        )

        locations = _read_jsonl(
            Path(result["window_locations_path"])
        )
        for row in locations:
            row.update(
                {
                    "provider": "Kaggle",
                    "dataset_handle": handle,
                    "immutable_revision": 1,
                }
            )
        _append_jsonl(location_target, locations)

        shard = result.get("shard")
        if shard:
            shard_path = Path(shard["path"])
            _resource_guard(pipeline.work_root)
            token = _upload_blob_with_retry(
                api,
                shard_path,
            )
            tokens.append(token)

            actual_bytes = int(shard["bytes"])
            uploaded_bytes += actual_bytes

            if shard.get("signal_dtype") != "float32":
                raise RuntimeError(
                    "R34_UPLOADED_SHARD_DTYPE_MISMATCH: "
                    f"subject={subject}; observed={shard.get('signal_dtype')}"
                )
            shard_row = {
                "filename": shard["filename"],
                "bytes": actual_bytes,
                "sha256": shard["sha256"],
                "dataset_id": dataset,
                "subject_profile": int(subject),
                "window_count": int(
                    result["window_count"]
                ),
                "logical_window_bytes": (
                    subject_logical
                ),
                "compression_ratio_to_logical": (
                    actual_bytes / subject_logical
                    if subject_logical
                    else None
                ),
                "provider": "Kaggle",
                "dataset_handle": handle,
                "immutable_revision": 1,
                "format": "HDF5",
                "compression": "gzip-1-lossless",
                "signal_dtype": "float32",
                "window_duration_samples": 480,
            }
            shard_rows.append(shard_row)

            dataset_row = dataset_actual.setdefault(
                dataset,
                {
                    "dataset_id": dataset,
                    "subjects": 0,
                    "shards": 0,
                    "windows": 0,
                    "logical_window_bytes": 0,
                    "actual_hdf5_bytes": 0,
                },
            )
            dataset_row["subjects"] += 1
            dataset_row["shards"] += 1
            dataset_row["windows"] += int(
                result["window_count"]
            )
            dataset_row["logical_window_bytes"] += (
                subject_logical
            )
            dataset_row["actual_hdf5_bytes"] += (
                actual_bytes
            )

            # No local large-array retention after verified token.
            shard_path.unlink(missing_ok=True)

        completed += 1
        if (
            time.monotonic() - last_progress
            >= float(POLICY["progress_interval_seconds"])
            or completed == len(plan)
        ):
            _progress_line(
                "PASS2B_MATERIALIZE_UPLOAD_PROGRESS",
                completed,
                len(plan),
                started,
                label,
                None,
                pipeline.work_root,
                {
                    "windows": len(window_records),
                    "shards_uploaded": len(shard_rows),
                    "uploaded_gib": round(
                        uploaded_bytes / _GIB,
                        3,
                    ),
                    "logical_window_gib": round(
                        logical_window_bytes / _GIB,
                        3,
                    ),
                },
            )
            last_progress = time.monotonic()

        shutil.rmtree(task_dir, ignore_errors=True)
        _trim_memory()

    pipeline.state["quality_records"] = quality_records
    pipeline.state["quality_summaries"] = quality_summaries
    pipeline.state["invalid_windows"] = invalid_windows
    pipeline.state["records"].extend(quality_records)
    invalid_path = (
        pipeline.bundle_root
        / "negative_and_failed_results"
        / "invalid_windows_streaming.json"
    )
    _atomic_json(invalid_path, invalid_windows)
    pipeline.state["r34_invalid_windows_path"] = str(
        invalid_path.relative_to(pipeline.bundle_root)
    )
    pipeline.state["r26_pending_window_records"] = (
        window_records
    )
    pipeline.state["r26_pending_window_index"] = (
        window_index
    )
    pipeline.state["r26_derived_tokens"] = tokens
    pipeline.state["r26_derived_shards"] = shard_rows
    pipeline.state["r26_derived_handle"] = handle
    pipeline.state["r26_execution_attempt_id"] = attempt
    pipeline.state["r26_upload_api"] = api

    actual_report = {
        "artifact_id": (
            f"P01-L1-DERIVED-STORAGE-ACTUAL-"
            f"{pipeline.config_id[:16]}-{attempt}"
        ),
        "policy_id": POLICY["policy_id"],
        "scientific_freeze": (
            POLICY["scientific_freeze_unchanged"]
        ),
        "status": "PRECOMMIT_ALL_SHARD_TOKENS_OBTAINED",
        "quality_records": len(quality_records),
        "quality_summaries": len(quality_summaries),
        "windows_materialized": len(window_records),
        "invalid_window_count": len(invalid_windows),
        "invalid_windows_path": pipeline.state["r34_invalid_windows_path"],
        "signal_dtype": "float32",
        "shards_uploaded": len(shard_rows),
        "logical_float32_window_bytes": (
            logical_window_bytes
        ),
        "logical_float32_window_gib": round(
            logical_window_bytes / _GIB,
            3,
        ),
        "actual_hdf5_uploaded_bytes": uploaded_bytes,
        "actual_hdf5_uploaded_gib": round(
            uploaded_bytes / _GIB,
            3,
        ),
        "actual_compression_ratio": (
            uploaded_bytes / logical_window_bytes
            if logical_window_bytes
            else None
        ),
        "derived_dataset_handle": handle,
        "execution_attempt_id": attempt,
        "forecast_report": pipeline.state.get(
            "r26_storage_forecast_path"
        ),
        "dataset_totals": [
            {
                **row,
                "logical_window_gib": round(
                    row["logical_window_bytes"]
                    / _GIB,
                    3,
                ),
                "actual_hdf5_gib": round(
                    row["actual_hdf5_bytes"]
                    / _GIB,
                    3,
                ),
                "compression_ratio": (
                    row["actual_hdf5_bytes"]
                    / row["logical_window_bytes"]
                    if row["logical_window_bytes"]
                    else None
                ),
            }
            for _, row in sorted(dataset_actual.items())
        ],
    }
    actual_path = (
        pipeline.bundle_root
        / "reports"
        / "phase_01"
        / "storage"
        / "derived_output_storage_actual_precommit.json"
    )
    _atomic_json(actual_path, actual_report)
    pipeline.state["r26_storage_actual"] = actual_report
    pipeline.state["r26_storage_actual_path"] = str(
        actual_path.relative_to(pipeline.bundle_root)
    )

    summary = {
        "quality_records": len(quality_records),
        "quality_summaries": len(quality_summaries),
        "windows_materialized": len(window_records),
        "invalid_window_count": len(invalid_windows),
        "invalid_windows_path": pipeline.state["r34_invalid_windows_path"],
        "signal_dtype": "float32",
        "shards_uploaded": len(shard_rows),
        "logical_window_bytes": logical_window_bytes,
        "uploaded_bytes": uploaded_bytes,
        "actual_compression_ratio": (
            uploaded_bytes / logical_window_bytes
            if logical_window_bytes
            else None
        ),
        "derived_dataset_handle": handle,
        "execution_attempt_id": attempt,
        "storage_actual_report": (
            pipeline.state["r26_storage_actual_path"]
        ),
    }
    _atomic_json(
        pipeline.bundle_root
        / "reports"
        / "phase_01"
        / "runtime"
        / "bounded_streaming"
        / "pass2b_summary_precommit.json",
        summary,
    )
    return summary



def _finalize_derived_dataset(runner: Any) -> dict[str, Any]:
    pipeline = runner.pipeline
    invalid_windows = list(pipeline.state.get("invalid_windows", []))
    if invalid_windows:
        raise RuntimeError(
            "R34_DERIVED_DATASET_COMMIT_REFUSED_INVALID_WINDOWS: "
            f"count={len(invalid_windows)}; "
            f"evidence={pipeline.state.get('r34_invalid_windows_path')}"
        )
    api = pipeline.state["r26_upload_api"]
    handle = pipeline.state["r26_derived_handle"]
    shards = list(pipeline.state["r26_derived_shards"])
    tokens = list(pipeline.state["r26_derived_tokens"])
    pending_records = list(pipeline.state["r26_pending_window_records"])
    pending_index = list(pipeline.state["r26_pending_window_index"])
    if not pending_records or len(pending_records) != len(pending_index):
        raise RuntimeError(
            "R34_DERIVED_WINDOW_RECORD_INDEX_COUNT_MISMATCH: "
            f"records={len(pending_records)}; index={len(pending_index)}"
        )
    record_ids = [row["record_id"] for row in pending_records]
    index_ids = [row["window_record_id"] for row in pending_index]
    if len(record_ids) != len(set(record_ids)) or set(record_ids) != set(index_ids):
        raise RuntimeError("R34_DERIVED_WINDOW_RECORD_ID_CLOSURE_FAILED")
    if sum(int(row.get("window_count", 0)) for row in shards) != len(pending_records):
        raise RuntimeError("R34_DERIVED_SHARD_WINDOW_COUNT_CLOSURE_FAILED")
    locations_path = pipeline.bundle_root / "external_artifact_pointers" / "window_to_shard.jsonl"
    location_hash = _sha256(locations_path); location_bytes = locations_path.stat().st_size
    manifest = {
        "artifact_id": f"P01-L1-DERIVED-WINDOWS-{pipeline.config_id[:16]}-{pipeline.state['r26_execution_attempt_id']}",
        "schema_version": 1,
        "policy_id": POLICY["policy_id"],
        "scientific_freeze": POLICY["scientific_freeze_unchanged"],
        "provider": "Kaggle",
        "repository_or_dataset": handle,
        "immutable_revision": 1,
        "access": "PRIVATE",
        "format": "LOSSLESS_HDF5_SUBJECT_SHARDS",
        "signal_dtype": "float32",
        "event_resampling": "MNE_POLYPHASE_JOINT_EVENTS",
        "window_policy": {
            "start_offset_samples": 80,
            "duration_samples": 480,
            "stride_samples": 480,
            "last_window_policy": "ONE_WINDOW_PER_INCLUDED_SOURCE_EVENT",
            "bounds_policy": "REJECT_OUT_OF_BOUNDS",
        },
        "source_dataset_ids": POLICY["active_sources_unchanged"],
        "source_inventory_record_ids": [r["record_id"] for r in pipeline.state["dataset_records"]],
        "split_record_id": pipeline.state["split_record"]["record_id"],
        "preprocessing_record_id": pipeline.state["preprocessing_record"]["record_id"],
        "window_count": len(
            pipeline.state["r26_pending_window_records"]
        ),
        "storage_forecast": pipeline.state.get(
            "r26_storage_forecast_path"
        ),
        "storage_actual": pipeline.state.get(
            "r26_storage_actual_path"
        ),
        "dual_persistence": POLICY["dual_persistence"],
        "shards": shards,
        "window_location_index": {"bundle_path": str(locations_path.relative_to(pipeline.bundle_root)), "sha256": location_hash, "bytes": location_bytes},
        "local_copy_status": "SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD",
        "retrieval_instructions": "Attach the private Kaggle Dataset at immutable version 1; load IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl (or an ordinal-prefixed suffix match); resolve the shard filename; read the declared HDF5 group and row.",
        "license": "INHERIT_EACH_SOURCE_LICENSE_AND_REDISTRIBUTION_CONSTRAINT_FROM_DATASET_RECORDS",
        "consumer_phases": [f"P{i:02d}" for i in range(2, 16)],
    }
    scratch = pipeline.work_root / "streaming_runtime" / "derived_dataset_commit"
    if scratch.exists(): shutil.rmtree(scratch)
    scratch.mkdir(parents=True, exist_ok=True)

    # Persist the compact scientific indexes inside the derived Dataset itself,
    # so later phases can attach one immutable Dataset and do not need to
    # manually download/re-upload local shard metadata.
    location_dataset_name = "IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl"
    location_dataset_path = scratch / location_dataset_name
    shutil.copy2(locations_path, location_dataset_path)

    window_records_name = "IHARQ_P01_L1_WINDOW_RECORDS.jsonl"
    window_records_path = scratch / window_records_name
    _append_jsonl(window_records_path, pipeline.state["r26_pending_window_records"])

    window_index_name = "IHARQ_P01_L1_WINDOW_INDEX.jsonl"
    window_index_path = scratch / window_index_name
    _append_jsonl(window_index_path, pipeline.state["r26_pending_window_index"])

    sidecar_name = "IHARQ_P01_L1_DERIVED_DATASET_SIDECAR.json"
    sidecar_path = scratch / sidecar_name
    _atomic_json(sidecar_path, {
        "schema_version": 1,
        "policy_id": POLICY["policy_id"],
        "scientific_freeze": POLICY["scientific_freeze_unchanged"],
        "config_id": pipeline.config_id,
        "dataset_records": pipeline.state["dataset_records"],
        "label_records": pipeline.state["label_records"],
        "split_record": pipeline.state["split_record"],
        "preprocessing_record": pipeline.state["preprocessing_record"],
        "quality_summaries": pipeline.state.get("quality_summaries", []),
        "window_count": len(pipeline.state["r26_pending_window_records"]),
        "invalid_window_count": 0,
        "signal_dtype": "float32",
        "event_resampling": "MNE_POLYPHASE_JOINT_EVENTS",
        "window_contract": {
            "start_offset_samples": 80,
            "duration_samples": 480,
            "stride_samples": 480,
            "one_window_per_included_event": True,
        },
        "shard_count": len(shards),
    })

    reader_name = "iharq_window_shard_reader.py"
    reader_path = scratch / reader_name
    reader_path.write_text(
        WINDOW_SHARD_READER_SOURCE,
        encoding="utf-8",
    )

    forecast_name = (
        "IHARQ_P01_L1_DERIVED_OUTPUT_STORAGE_FORECAST.json"
    )
    forecast_path = scratch / forecast_name
    shutil.copy2(
        pipeline.bundle_root
        / pipeline.state["r26_storage_forecast_path"],
        forecast_path,
    )

    actual_name = (
        "IHARQ_P01_L1_DERIVED_OUTPUT_STORAGE_ACTUAL.json"
    )
    actual_path = scratch / actual_name
    shutil.copy2(
        pipeline.bundle_root
        / pipeline.state["r26_storage_actual_path"],
        actual_path,
    )

    compact_files = [
        location_dataset_path,
        window_records_path,
        window_index_path,
        sidecar_path,
        reader_path,
        forecast_path,
        actual_path,
    ]
    manifest["dataset_local_indexes"] = {
        path.name: {
            "sha256": _sha256(path),
            "bytes": path.stat().st_size,
            "format": "JSONL" if path.suffix == ".jsonl" else "JSON",
        }
        for path in compact_files
    }
    manifest["window_location_index"].update({
        "dataset_filename": location_dataset_name,
        "dataset_sha256": _sha256(location_dataset_path),
        "dataset_bytes": location_dataset_path.stat().st_size,
    })
    manifest["window_records_filename"] = window_records_name
    manifest["window_index_filename"] = window_index_name
    manifest["derived_dataset_sidecar_filename"] = sidecar_name
    manifest["future_phase_reader_filename"] = reader_name
    manifest["storage_forecast_filename"] = forecast_name
    manifest["storage_actual_filename"] = actual_name

    for compact_path in compact_files:
        tokens.append(_upload_blob_with_retry(api, compact_path))

    manifest_name = "IHARQ_P01_L1_DERIVED_WINDOW_DATASET_MANIFEST.json"
    manifest_path = scratch / manifest_name; _atomic_json(manifest_path, manifest)
    manifest_token = _upload_blob_with_retry(api, manifest_path); tokens.append(manifest_token)
    expected_token_count = len(shards) + len(compact_files) + 1
    if len(tokens) != expected_token_count:
        raise RuntimeError(
            f"R26_DERIVED_DATASET_TOKEN_COUNT_MISMATCH: "
            f"expected={expected_token_count}; observed={len(tokens)}"
        )
    upload_dir = api["UploadDirectoryInfo"](name="", files=tokens, directories=[])
    response = api["create_dataset_or_version"](
        api["parse_dataset_handle"](handle), upload_dir,
        f"IHARQ P01/L1 exact derived windows for {POLICY['scientific_freeze_unchanged']} under {POLICY['policy_id']}",
    )
    pointer_path = pipeline.bundle_root / "external_artifact_pointers" / "derived_windows_dataset.json"
    manifest["creation_status"] = "COMMITTED"
    actual_report = dict(
        pipeline.state.get("r26_storage_actual", {})
    )
    actual_report["status"] = "COMMITTED"
    actual_report["dataset_handle"] = handle
    actual_report["dataset_version"] = 1
    _atomic_json(
        pipeline.bundle_root
        / pipeline.state["r26_storage_actual_path"],
        actual_report,
    )
    pipeline.state["r26_storage_actual"] = actual_report
    manifest["creation_response_type"] = type(response).__name__
    manifest["dataset_version"] = 1
    manifest["manifest_filename_in_dataset"] = manifest_name
    _atomic_json(pointer_path, manifest)
    pipeline.state["preprocessing_record"]["payload"]["output_pointer"] = str(pointer_path.relative_to(pipeline.bundle_root))
    window_records = pipeline.state.pop("r26_pending_window_records"); window_index = pipeline.state.pop("r26_pending_window_index")
    pipeline.state["window_records"] = window_records; pipeline.state["window_index"] = window_index; pipeline.state["records"].extend(window_records)
    pipeline.state["window_report"] = {
        "window_count": len(window_records),
        "event_count": len({row["event_id"] for row in window_index}),
        "invalid_window_count": 0,
        "invalid_windows": [],
        "roles": sorted({row["role"] for row in window_index}),
        "start_offset_samples": 80,
        "duration_samples": 480,
        "stride_samples": 480,
        "duration_seconds": pipeline.config.get("windows", {}).get("duration_seconds"),
        "stride_seconds": pipeline.config.get("windows", {}).get("stride_seconds"),
        "last_window_policy": "ONE_WINDOW_PER_INCLUDED_SOURCE_EVENT",
        "bounds_policy": "REJECT_OUT_OF_BOUNDS",
        "event_resampling": "MNE_POLYPHASE_JOINT_EVENTS",
        "signal_dtype": "float32",
        "overlap_group": "PARENT_EVENT",
        "storage": "PRIVATE_KAGGLE_DATASET_LOSSLESS_HDF5_SUBJECT_SHARDS",
        "dataset_handle": handle,
        "immutable_revision": 1,
    }
    pipeline.state["r26_derived_pointer"] = str(pointer_path.relative_to(pipeline.bundle_root))
    pipeline.state.pop("r26_derived_tokens", None); pipeline.state.pop("r26_upload_api", None)
    shutil.rmtree(scratch, ignore_errors=True)
    return {"window_report": pipeline.state["window_report"], "pointer": pipeline.state["r26_derived_pointer"], "shards": len(shards)}





def install_bounded_streaming(
    runner: Any,
    *,
    source_resolution_file: str | Path,
) -> dict[str, Any]:
    pipeline = runner.pipeline
    pipeline.state["r26_source_resolution_file"] = str(source_resolution_file)
    attempt, handle = _derived_identity(runner)
    pipeline.state["r26_execution_attempt_id"] = attempt
    pipeline.state["r26_derived_handle"] = handle
    pipeline.load_sources = MethodType(_streaming_load_sources, pipeline)
    pipeline.split_budget_preprocess = MethodType(_split_budget_without_signal_fit, pipeline)

    def _sync_stage_result(self, result: Any) -> None:
        rows = self.pipeline.state.get("stage_results", [])
        for index in range(len(rows) - 1, -1, -1):
            if rows[index].get("stage") == result.stage:
                rows[index] = dict(result.__dict__)
                break
        status_path = self.work_root / "stage_status" / f"{result.stage}.json"
        status_path.parent.mkdir(parents=True, exist_ok=True)
        status_path.write_text(
            json.dumps(result.__dict__, indent=2, default=str),
            encoding="utf-8",
        )

    def stage_13(self):
        if not self.pipeline.state.get("r26_legal_fit_source_ids"):
            return self._record("13", "BLOCKED", blockers=self.pipeline.blockers)
        try:
            observations = _streaming_fit(self)
            return self._record("13", "PASS", observations=observations)
        except Exception as exc:
            blocker = {
                "code": "P01_STREAMING_FIT_FAILED",
                "message": str(exc),
                "owner": "L1_PREPROCESSING_RUNTIME",
            }
            self.pipeline.blockers.append(blocker)
            return self._record(
                "13",
                "BLOCKED",
                blockers=self.pipeline.blockers,
                observations={"traceback": traceback.format_exc()},
            )

    def stage_14(self):
        if not self.pipeline.state.get("preprocessing_record"):
            return self._record("14", "BLOCKED", blockers=self.pipeline.blockers)
        try:
            observations = _streaming_materialize(self)
            hard_invalid = sum(
                int(row.get("hard_invalid", 0))
                for row in self.pipeline.state.get("quality_summaries", [])
            )
            blockers = []
            if hard_invalid:
                blocker = {
                    "code": "P01_QUALITY_HARD_INVALID",
                    "hard_invalid": hard_invalid,
                    "owner": "L1_QUALITY_OR_SOURCE_BYTES",
                }
                self.pipeline.blockers.append(blocker)
                blockers.append(blocker)
            status = "PASS" if not blockers else "FAIL"
            return self._record(
                "14",
                status,
                observations={
                    "quality_records": observations["quality_records"],
                    "quality_summaries": observations["quality_summaries"],
                    "hard_invalid": hard_invalid,
                    "coverage": self.pipeline.state.get("quality_summaries", []),
                    "streaming_window_candidates": observations["windows_materialized"],
                    "invalid_window_count": observations["invalid_window_count"],
                    "invalid_windows_path": observations["invalid_windows_path"],
                    "signal_dtype": observations["signal_dtype"],
                    "shards_uploaded_precommit": observations["shards_uploaded"],
                    "logical_window_gib": round(observations["logical_window_bytes"] / _GIB, 3),
                    "uploaded_hdf5_gib": round(observations["uploaded_bytes"] / _GIB, 3),
                    "actual_compression_ratio": observations["actual_compression_ratio"],
                    "storage_actual_report": observations["storage_actual_report"],
                },
                blockers=blockers,
            )
        except Exception as exc:
            blocker = {
                "code": "P01_STREAMING_MATERIALIZATION_FAILED",
                "message": str(exc),
                "owner": "L1_QUALITY_WINDOW_RUNTIME",
            }
            self.pipeline.blockers.append(blocker)
            return self._record(
                "14",
                "BLOCKED",
                blockers=self.pipeline.blockers,
                observations={"traceback": traceback.format_exc()},
            )

    def stage_15(self):
        if "r26_derived_tokens" not in self.pipeline.state:
            return self._record("15", "BLOCKED", blockers=self.pipeline.blockers)
        invalid_windows = list(self.pipeline.state.get("invalid_windows", []))
        if invalid_windows:
            blocker = {
                "code": "P01_WINDOW_INVALID_OR_MISSING",
                "invalid_window_count": len(invalid_windows),
                "evidence": self.pipeline.state.get("r34_invalid_windows_path"),
                "owner": "L1_WINDOWS_OR_SOURCE_BYTES",
            }
            self.pipeline.blockers.append(blocker)
            return self._record(
                "15",
                "FAIL",
                observations={
                    "invalid_window_count": len(invalid_windows),
                    "invalid_windows_path": self.pipeline.state.get("r34_invalid_windows_path"),
                },
                blockers=[blocker],
            )
        try:
            observations = _finalize_derived_dataset(self)
            window_report = self.pipeline.state.get("window_report", {})
            valid = (
                bool(self.pipeline.state.get("window_records"))
                and int(window_report.get("invalid_window_count", -1)) == 0
                and window_report.get("signal_dtype") == "float32"
                and int(window_report.get("start_offset_samples", -1)) == 80
                and int(window_report.get("duration_samples", -1)) == 480
                and int(window_report.get("stride_samples", -1)) == 480
            )
            blockers = [] if valid else [{
                "code": "P01_WINDOW_COMMIT_CONTRACT_MISMATCH",
                "window_report": window_report,
                "owner": "L1_WINDOWS_OR_PERSISTENCE",
            }]
            if blockers:
                self.pipeline.blockers.extend(blockers)
            return self._record(
                "15",
                "PASS" if valid else "FAIL",
                outputs=[observations["pointer"]],
                observations={
                    **window_report,
                    "storage_forecast": self.pipeline.state.get("r26_storage_forecast_path"),
                    "storage_actual": self.pipeline.state.get("r26_storage_actual_path"),
                    "future_phase_reader_in_dataset": "iharq_window_shard_reader.py",
                },
                blockers=blockers,
            )
        except Exception as exc:
            blocker = {
                "code": "P01_DERIVED_WINDOW_DATASET_COMMIT_FAILED",
                "message": str(exc),
                "owner": "KAGGLE_ARTIFACT_PERSISTENCE",
            }
            self.pipeline.blockers.append(blocker)
            return self._record(
                "15",
                "BLOCKED",
                blockers=self.pipeline.blockers,
                observations={"traceback": traceback.format_exc()},
            )

    def stage_26(self):
        expected_zip = self.work_root / f"{self.pipeline.bundle_root.name}.zip"
        expected_sha = Path(str(expected_zip) + ".sha256")
        repository_name = (
            "IHARQ_P01_L1_GitHub_Ready_Repository_"
            f"{self.pipeline.config_id[:12]}_"
            f"{_safe(self.pipeline.state['r26_execution_attempt_id'])}"
        )
        expected_repo_zip = self.work_root / f"{repository_name}.zip"
        expected_repo_sha = expected_repo_zip.with_suffix(
            expected_repo_zip.suffix + ".sha256"
        )
        release_plan_rel = "reports/phase_01/repository_release_plan.json"
        release_plan = {
            "artifact_type": "GITHUB_READY_REPOSITORY_ZIP",
            "expected_path": str(expected_repo_zip),
            "expected_detached_sha256_path": str(expected_repo_sha),
            "creation_order": "AFTER_EXECUTION_BUNDLE_FINAL_FREEZE",
            "actual_hash_location": "EXTERNAL_DETACHED_VERIFICATION",
            "circularity_rule": (
                "THE ACTUAL REPOSITORY ZIP HASH MUST NOT BE WRITTEN BACK INTO "
                "THE FROZEN EXECUTION BUNDLE OR INTO THE REPOSITORY ZIP ITSELF."
            ),
        }
        _atomic_json(
            self.pipeline.bundle_root / release_plan_rel,
            release_plan,
        )
        pre = {
            "phase": "P01",
            "layer": "L1",
            "notebook_revision": "R42",
            "config_id": self.pipeline.config_id,
            "pre_package_decision": self.pipeline.state.get(
                "preliminary_decision", {}
            ).get("status", "BLOCKED"),
            "blockers": self.pipeline.blockers,
            "bundle_target": str(expected_zip),
            "detached_checksum_target": str(expected_sha),
            "github_ready_repository_target": str(expected_repo_zip),
            "github_ready_repository_detached_checksum_target": str(
                expected_repo_sha
            ),
            "repository_release_plan": release_plan_rel,
            "external_hash_boundary": (
                "BOTH ZIP SHA-256 VALUES ARE DETACHED EXTERNAL VERIFICATION "
                "SURFACES AND ARE NOT EMBEDDED INTO THEIR OWN FROZEN BYTES."
            ),
            "next_step": (
                "Create Protocol v1.0 P01 annex"
                if self.pipeline.state.get("preliminary_decision", {}).get(
                    "status"
                ) == "ACCEPTED"
                else "Preserve failed bundle; repair the exact governed defect and rerun"
            ),
        }
        result = self._record(
            "26",
            "PASS",
            outputs=[
                str(expected_zip),
                str(expected_sha),
                str(expected_repo_zip),
                str(expected_repo_sha),
                release_plan_rel,
            ],
            observations=pre,
        )
        try:
            # Stage 26 already exists, so the exact 00-26 identity is frozen once.
            # No file inside the bundle is modified after this call.
            final_decision = self.pipeline.prepare_final_artifacts()
            repository = _create_github_ready_repository(self)
            package = self.pipeline.package_bundle()
            final = {
                **pre,
                "decision": final_decision["status"],
                "final_manifest_closure": self.pipeline.state.get(
                    "final_manifest_closure"
                ),
                "compact_phase_execution_bundle": package,
                "github_ready_repository": repository,
                "private_derived_windows_dataset": {
                    "handle": self.pipeline.state.get("r26_derived_handle"),
                    "version": 1,
                    "pointer": self.pipeline.state.get("r26_derived_pointer"),
                    "storage_forecast": self.pipeline.state.get(
                        "r26_storage_forecast_path"
                    ),
                    "storage_actual": self.pipeline.state.get(
                        "r26_storage_actual_path"
                    ),
                    "signal_dtype": "float32",
                    "window_contract": (
                        "OFFSET_80_DURATION_480_ONE_PER_INCLUDED_EVENT"
                    ),
                },
                "future_phase_retrieval": (
                    "Attach the private derived Dataset directly; use the included "
                    "shard reader and verify manifest/shard hashes."
                ),
                "next_step": (
                    "Create Protocol v1.0 Phase 1 annex"
                    if final_decision["status"] == "ACCEPTED"
                    else "Resolve blockers and rerun"
                ),
            }
            # The internal Stage 26 record remains the frozen pre-export contract.
            # Actual external ZIP hashes are emitted only outside the bundle.
            result.observations = final
            result.outputs = [
                package["zip"],
                package["sha256_file"],
                repository["path"],
                repository["path"] + ".sha256",
                repository["external_pointer_path"],
                repository["external_manifest_path"],
                "external_artifact_pointers/derived_windows_dataset.json",
            ]
            status_path = self.work_root / "stage_status" / "26.json"
            status_path.parent.mkdir(parents=True, exist_ok=True)
            status_path.write_text(
                json.dumps(result.__dict__, indent=2, default=str),
                encoding="utf-8",
            )
            external = self.work_root / "final_external_package_verification.json"
            external.write_text(
                json.dumps(
                    {
                        "stage": "26",
                        "package": package,
                        "github_ready_repository": repository,
                        "decision": final_decision["status"],
                        "bundle_internal_stage_evidence": (
                            "reports/phase_01/tests/stage_results.json"
                        ),
                        "bundle_frozen_before_external_zip_creation": True,
                        "self_hash_boundary": (
                            "ZIP SHA-256 VALUES ARE DETACHED AND CANNOT BE "
                            "EMBEDDED INSIDE THE SAME FROZEN ZIP BYTES."
                        ),
                    },
                    indent=2,
                    default=str,
                ),
                encoding="utf-8",
            )
            print(json.dumps(final, indent=2, default=str))
            return result
        except Exception as exc:
            blocker = {
                "code": "P01_FINAL_EXPORT_OR_DUAL_PERSISTENCE_FAILED",
                "message": str(exc),
                "owner": "L1_PACKAGING_OR_EXTERNAL_PERSISTENCE",
            }
            if blocker not in self.pipeline.blockers:
                self.pipeline.blockers.append(blocker)
            result.status = "BLOCKED"
            result.blockers = [blocker]
            result.observations = {
                **pre,
                "error": repr(exc),
                "traceback": traceback.format_exc(),
            }
            _sync_stage_result(self, result)
            try:
                failed_decision = self.pipeline.prepare_final_artifacts()
                failed_package = self.pipeline.package_bundle()
                result.outputs = [
                    failed_package["zip"],
                    failed_package["sha256_file"],
                ]
                result.observations["failed_bundle_package"] = failed_package
                result.observations["failed_final_decision"] = failed_decision[
                    "status"
                ]
            except Exception as preserve_exc:
                result.observations["failed_bundle_preservation_error"] = repr(
                    preserve_exc
                )
            status_path = self.work_root / "stage_status" / "26.json"
            status_path.parent.mkdir(parents=True, exist_ok=True)
            status_path.write_text(
                json.dumps(result.__dict__, indent=2, default=str),
                encoding="utf-8",
            )
            return result

    runner.stage_13 = MethodType(stage_13, runner)
    runner.stage_14 = MethodType(stage_14, runner)
    runner.stage_15 = MethodType(stage_15, runner)
    # Stages 24 and 25 intentionally retain the authoritative R6 ordering.
    # Repository creation and final manifest freezing occur only in Stage 26.
    runner.stage_26 = MethodType(stage_26, runner)

    installation = {
        "policy": POLICY,
        "installed_at_unix": time.time(),
        "execution_attempt_id": attempt,
        "derived_dataset_handle": handle,
        "source_resolution_file": str(source_resolution_file),
        "patched_surfaces": [
            "Layer1Pipeline.load_sources",
            "Layer1Pipeline.split_budget_preprocess:R35_AUTHORITATIVE_EVENT_ROW_SCHEMA",
            "StageRunner.stage_13",
            "StageRunner.stage_14",
            "StageRunner.stage_15",
            "StageRunner.stage_26",
        ],
        "authoritative_stage_order_retained": ["24", "25"],
        "downstream_contract_closure": {
            "joint_event_resampling": True,
            "eeg_only_channel_selection": True,
            "float32_output_dtype": True,
            "window_start_offset_samples": 80,
            "window_duration_samples": 480,
            "window_stride_samples": 480,
            "one_window_per_included_event": True,
            "invalid_windows_preserved_and_block_commit": True,
            "quality_hard_invalid_blocks_stage14": True,
            "stage24_no_premature_finalization": True,
            "stage26_complete_identity_before_finalization": True,
            "compact_bundle_packaged": True,
            "github_ready_repository_packaged": True,
        },
        "preservation": {
            "all_three_sources": True,
            "all_subjects_sessions_runs": True,
            "all_labels": True,
            "split_budget_profiles": True,
            "stage11_authoritative_event_row_contract": True,
            "preprocessing_operations": True,
            "quality_annotation": True,
            "window_identity_and_sample_hash": True,
            "canonical_records": True,
            "validation_and_leakage": True,
            "cards_manifests_readiness": True,
            "p01_gates": True,
            "phase2_and_later_handoffs": True,
            "negative_evidence": True,
            "final_bundle": True,
        },
        "resource_properties": {
            "parent_retains_signal_arrays": False,
            "maximum_subject_processes": 8,
            "subject_process_disposable": True,
            "stage07_parallelism": "REAL_PREFLIGHT_MEASURED_RSS_ADAPTIVE",
            "temporary_shard_deleted_after_blob_upload": True,
            "exact_float32_storage_forecast_before_materialization": True,
            "actual_storage_report_after_upload": True,
        },
        "persistence_outputs": {
            "compact_github_ready_repository": True,
            "large_private_kaggle_dataset": True,
            "future_phase_reader_in_dataset": True,
        },
    }
    _atomic_json(
        pipeline.bundle_root
        / "reports"
        / "phase_01"
        / "runtime"
        / "bounded_streaming"
        / "installation.json",
        installation,
    )
    return installation




# =====================================================================
# R42 runner/pipeline integration
# =====================================================================

_R42_BASE_INSTALL_BOUNDED_STREAMING = install_bounded_streaming


def install_bounded_streaming(
    runner: Any,
    *,
    source_resolution_file: str | Path,
) -> dict[str, Any]:
    installation = _R42_BASE_INSTALL_BOUNDED_STREAMING(
        runner,
        source_resolution_file=source_resolution_file,
    )

    pipeline = runner.pipeline
    base_readiness_cards_manifests = (
        pipeline.readiness_cards_manifests
    )
    base_p02_handoff = pipeline.p02_handoff
    base_write_downstream_handoffs = (
        pipeline.write_downstream_handoffs
    )

    def r42_readiness_cards_manifests(self):
        result = base_readiness_cards_manifests()

        a4_pointer = self.state.get("r42_a4_pointer")
        if not a4_pointer:
            raise RuntimeError(
                "R49_A4_POINTER_MISSING_AT_READINESS"
            )

        for row in self.state.get("readiness", []):
            if row.get("ablation_id") != "A4":
                continue
            row["status"] = "FOUNDATION_READY"
            row["foundation_ready"] = True
            row["data_substrate_status"] = (
                "READY_WITH_PROTOCOL_SYNC_REQUIRED"
            )
            row["a4_components"] = {
                "ordinary_cross_model_ensemble": {
                    "status": (
                        "DOWNSTREAM_MODEL_PREDICTIONS_REQUIRED"
                    ),
                    "data_ready": True,
                },
                "longer_window_matched3p5s": {
                    "status": (
                        "DATA_READY_PROTOCOL_SYNC_REQUIRED"
                    ),
                    "window_profile_id": (
                        "A4_LONG_MATCHED_3P5S_R2"
                    ),
                    "pointer": a4_pointer,
                },
                "same_event_multi_window_3x2s": {
                    "status": (
                        "DATA_READY_PROTOCOL_SYNC_REQUIRED"
                    ),
                    "window_profile_id": (
                        "A4_MULTI_3X2S_UNIFORM_0P75S_R2"
                    ),
                    "member_count": 3,
                    "pointer": a4_pointer,
                },
            }
            row["confirmatory_use_rule"] = (
                "PROTOCOL_V1_EXACT_PROFILE_SYNC_REQUIRED"
            )
            row["activated_in_p01"] = False
            row["executed_in_p01"] = False

        from iharq.layer1_data_protocol.manifests import write_json

        write_json(
            self.bundle_root
            / "manifests"
            / "phase_01"
            / "layer1_ablation_readiness_l1_v1.json",
            {
                "rows": self.state["readiness"],
                "a14_absence": self.state["a14"],
                "a4_window_family_pointer": a4_pointer,
                "a4_window_family": R42_A4_WINDOW_FAMILY,
                "core_dataset_pointer": (
                    self.state["r42_core_pointer"]
                ),
            },
        )

        for row in self.state.get("matched_key_rows", []):
            if row.get("ablation_id") == "A4":
                row["keys_complete"] = True
                row["status"] = "FOUNDATION_READY"
                row["required_keys"] += (
                    "|a4_group_id|evidence_condition_id"
                )
        return result

    def r42_p02_handoff(self):
        ready = base_p02_handoff()
        path = (
            self.bundle_root
            / "handoffs"
            / "phase_01_to_phase_02.yaml"
        )
        import yaml

        payload = yaml.safe_load(
            path.read_text(encoding="utf-8")
        )
        payload["core_dataset_pointer"] = (
            self.state["r42_core_pointer"]
        )
        payload["a4_window_family_pointer"] = (
            self.state["r42_a4_pointer"]
        )
        payload["a4_data_readiness"] = {
            "ordinary_ensemble": (
                "DOWNSTREAM_MODEL_PREDICTIONS_REQUIRED"
            ),
            "longer_window_matched3p5s": (
                "DATA_READY_PROTOCOL_SYNC_REQUIRED"
            ),
            "same_event_multi_window_3x2s": (
                "DATA_READY_PROTOCOL_SYNC_REQUIRED"
            ),
            "confirmatory_use_rule": (
                "SYNC_EXACT_A4_PROFILE_IN_PROTOCOL_V1"
            ),
        }
        payload["limitations"] = sorted(
            set(
                list(payload.get("limitations", []))
                + ["A4_EXACT_PROFILE_PROTOCOL_SYNC_REQUIRED"]
            )
        )
        data = yaml.safe_dump(payload, sort_keys=False)
        path.write_text(data, encoding="utf-8")
        (
            self.bundle_root
            / "phase2_handoff"
            / "phase_01_to_phase_02.yaml"
        ).write_text(data, encoding="utf-8")
        self.state["p02_handoff"] = payload
        return ready

    def r42_write_downstream_handoffs(self):
        result = base_write_downstream_handoffs()
        import yaml

        for path in (
            self.bundle_root
            / "handoffs"
        ).rglob("*.yaml"):
            try:
                payload = yaml.safe_load(
                    path.read_text(encoding="utf-8")
                )
            except Exception:
                continue
            if not isinstance(payload, dict):
                continue
            payload["core_dataset_pointer"] = (
                self.state["r42_core_pointer"]
            )
            payload["a4_window_family_pointer"] = (
                self.state["r42_a4_pointer"]
            )
            payload["a4_protocol_status"] = (
                R42_A4_WINDOW_FAMILY["protocol_status"]
            )
            path.write_text(
                yaml.safe_dump(payload, sort_keys=False),
                encoding="utf-8",
            )
        return result

    pipeline.readiness_cards_manifests = MethodType(
        r42_readiness_cards_manifests,
        pipeline,
    )
    pipeline.p02_handoff = MethodType(
        r42_p02_handoff,
        pipeline,
    )
    pipeline.write_downstream_handoffs = MethodType(
        r42_write_downstream_handoffs,
        pipeline,
    )

    def r42_stage_14(self):
        try:
            a4_contract = _r48_assert_a4_runtime_contract()
            a4_synthetic_preflight = _r48_a4_synthetic_end_to_end_preflight(self)
            core = _r42_adopt_existing_core_dataset(self)
            a4_universal_feasibility = (
                _r49_assert_universal_matched_window_feasibility(self)
            )
            a4 = _r42_streaming_materialize_a4(self)
            observations = {
                "a4_runtime_contract": a4_contract,
                "a4_synthetic_preflight": a4_synthetic_preflight,
                "a4_universal_feasibility": a4_universal_feasibility,
                "core_adoption": core,
                "a4_precommit": a4,
                "quality_records": len(
                    self.pipeline.state.get(
                        "quality_records",
                        [],
                    )
                ),
                "quality_summaries": len(
                    self.pipeline.state.get(
                        "quality_summaries",
                        [],
                    )
                ),
                "hard_invalid": 0,
                "core_stage14_reexecuted": False,
                "core_hdf5_shards_reuploaded": False,
                "a4_materialization_executed": True,
            }
            return self._record(
                "14",
                "PASS",
                outputs=[
                    self.pipeline.state["r42_core_pointer"],
                    self.pipeline.state[
                        "r42_a4_storage_report_path"
                    ],
                ],
                observations=observations,
            )
        except Exception as exc:
            blocker = {
                "code": (
                    "P01_R42_CORE_ADOPTION_OR_A4_"
                    "MATERIALIZATION_FAILED"
                ),
                "message": str(exc),
                "owner": (
                    "L1_A4_WINDOW_EXTENSION_OR_EXTERNAL_BYTES"
                ),
            }
            self.pipeline.blockers.append(blocker)
            return self._record(
                "14",
                "BLOCKED",
                blockers=self.pipeline.blockers,
                observations={
                    "traceback": traceback.format_exc(),
                    "core_stage14_reexecuted": False,
                },
            )

    def r42_stage_15(self):
        if not self.pipeline.state.get("r42_core_adopted"):
            return self._record(
                "15",
                "BLOCKED",
                blockers=self.pipeline.blockers,
            )
        if "r42_a4_tokens" not in self.pipeline.state:
            return self._record(
                "15",
                "BLOCKED",
                blockers=self.pipeline.blockers,
            )
        try:
            a4 = _r42_finalize_a4_dataset(self)
            valid = (
                bool(
                    self.pipeline.state.get("window_records")
                )
                and len(
                    self.pipeline.state.get(
                        "window_records",
                        [],
                    )
                )
                == 12_910
                and bool(
                    self.pipeline.state.get(
                        "r42_a4_committed"
                    )
                )
                and len(
                    self.pipeline.state.get(
                        "r42_a4_groups",
                        [],
                    )
                )
                == 12_910
            )
            blockers = []
            if not valid:
                blockers = [
                    {
                        "code": (
                            "P01_R42_CORE_A4_POINTER_"
                            "CLOSURE_FAILED"
                        ),
                        "owner": "L1_PERSISTENCE",
                    }
                ]
                self.pipeline.blockers.extend(blockers)

            return self._record(
                "15",
                "PASS" if valid else "FAIL",
                outputs=[
                    self.pipeline.state["r42_core_pointer"],
                    self.pipeline.state["r42_a4_pointer"],
                ],
                observations={
                    "core_dataset": (
                        self.pipeline.state["window_report"]
                    ),
                    "a4_dataset": a4,
                    "core_recomputed": False,
                    "core_hdf5_shards_reuploaded": False,
                    "a4_matched3p5s_materialized": True,
                    "a4_multiwindow_views_registered": True,
                    "a4_protocol_status": (
                        R42_A4_WINDOW_FAMILY[
                            "protocol_status"
                        ]
                    ),
                },
                blockers=blockers,
            )
        except Exception as exc:
            blocker = {
                "code": "P01_R49_A4_DATASET_COMMIT_FAILED",
                "message": str(exc),
                "owner": "KAGGLE_ARTIFACT_PERSISTENCE",
            }
            self.pipeline.blockers.append(blocker)
            return self._record(
                "15",
                "BLOCKED",
                blockers=self.pipeline.blockers,
                observations={"traceback": traceback.format_exc()},
            )

    runner.stage_14 = MethodType(r42_stage_14, runner)
    runner.stage_15 = MethodType(r42_stage_15, runner)

    installation["r42_core_mode"] = (
        "ADOPT_EXISTING_VERIFIED_DATASET"
    )
    installation["r42_a4_window_family"] = (
        R42_A4_WINDOW_FAMILY
    )
    installation["r42_core_hdf5_reupload"] = False

    _atomic_json(
        pipeline.bundle_root
        / "reports"
        / "phase_01"
        / "runtime"
        / "r49_core_reuse_a4_r2_extension_installation.json",
        installation,
    )
    return installation

def _synthetic_self_test() -> dict[str, Any]:
    import numpy as np
    import h5py
    import types
    from dataclasses import dataclass
    from tempfile import TemporaryDirectory
    # The test can run before the R6 base package is attached. Minimal private
    # stubs exercise only the exact contracts consumed by _combine_fit_rows.
    inserted_modules: list[str] = []
    try:
        from iharq.canonical import semantic_hash as _probe_semantic_hash
        from iharq.layer1_data_protocol.preprocessing import FitState as _probe_fit_state
    except Exception:
        iharq_mod = types.ModuleType("iharq")
        canonical_mod = types.ModuleType("iharq.canonical")
        layer1_mod = types.ModuleType("iharq.layer1_data_protocol")
        prep_mod = types.ModuleType("iharq.layer1_data_protocol.preprocessing")
        def semantic_hash(value):
            raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
            return hashlib.sha256(raw).hexdigest()
        @dataclass
        class FitState:
            mean: Any
            std: Any
            source_ids: list[str]
            state_hash: str
        canonical_mod.semantic_hash = semantic_hash
        prep_mod.FitState = FitState
        iharq_mod.canonical = canonical_mod
        iharq_mod.layer1_data_protocol = layer1_mod
        layer1_mod.preprocessing = prep_mod
        for name, module in {
            "iharq": iharq_mod,
            "iharq.canonical": canonical_mod,
            "iharq.layer1_data_protocol": layer1_mod,
            "iharq.layer1_data_protocol.preprocessing": prep_mod,
        }.items():
            if name not in sys.modules:
                sys.modules[name] = module
                inserted_modules.append(name)
    rng = np.random.default_rng(20260806)
    arrays = [rng.normal(size=(4, n)).astype(np.float64) for n in (37, 53, 29)]
    rows = []
    for i, x in enumerate(arrays):
        mean = x.mean(axis=1); centered = x - mean[:, None]
        rows.append({"source_unit": f"D:{i}:S:R", "channel_names": [f"C{k}" for k in range(4)], "count": x.shape[1], "mean": mean.tolist(), "m2": np.sum(centered*centered, axis=1).tolist()})
    state, detail = _combine_fit_rows(rows, {row["source_unit"] for row in rows})
    cat = np.concatenate(arrays, axis=1)
    fit_ok = np.allclose(state.mean[:, 0], cat.mean(axis=1), rtol=1e-13, atol=1e-13) and np.allclose(state.std[:, 0], cat.std(axis=1), rtol=1e-12, atol=1e-12)
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "test.h5"; window = rng.normal(size=(4, 64)).astype(np.float32)
        with h5py.File(path, "w") as handle: group, row = _append_h5_window(handle, window, "window:test")
        with h5py.File(path, "r") as handle: restored = handle[group + "/signals"][row]
        h5_ok = np.array_equal(window, restored)
    import ast as _ast
    no_h5_proxy = not any(isinstance(node, _ast.ClassDef) and node.name == "H5Signal" for node in _ast.walk(_ast.parse(Path(__file__).read_text(encoding="utf-8"))))
    for name in reversed(inserted_modules):
        sys.modules.pop(name, None)
    return {"status": "PASS" if fit_ok and h5_ok and no_h5_proxy and str(restored.dtype) == "float32" else "FAIL", "streaming_fit_matches_concatenate": fit_ok, "lossless_hdf5_roundtrip": h5_ok, "no_whole_array_h5_proxy": no_h5_proxy, "detail": detail}


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--child":
        raise SystemExit(_child_main(sys.argv[2]))
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        print(json.dumps(_synthetic_self_test(), indent=2)); raise SystemExit(0)
    raise SystemExit("Use --child <request.json> or --self-test")
