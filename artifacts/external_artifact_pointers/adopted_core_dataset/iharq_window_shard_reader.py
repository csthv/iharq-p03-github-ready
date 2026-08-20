from __future__ import annotations

"""Read exact IHARQ P01/L1 R26 windows from an attached derived Kaggle Dataset.

The reader performs no network access. It supports Kaggle's optional ordinal
filename prefixes, verifies the manifest/index/shard identities, validates the
HDF5 window ID at the declared row, and returns one exact NumPy array at a time.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator
import hashlib
import json
import re

MANIFEST_NAME = "IHARQ_P01_L1_DERIVED_WINDOW_DATASET_MANIFEST.json"
LOCATION_INDEX_NAME = "IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl"
EXPECTED_FORMAT = "LOSSLESS_HDF5_SUBJECT_SHARDS"
EXPECTED_FREEZE = "P01-L1-OFFICIAL-RUN-FREEZE-R2"


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _canonical_leaf(name: str) -> str:
    return Path(name).name


def _matches_canonical_filename(path: Path, canonical_name: str) -> bool:
    leaf = path.name
    canonical = _canonical_leaf(canonical_name)
    return leaf == canonical or bool(re.fullmatch(rf"\d+_{re.escape(canonical)}", leaf))


def resolve_unique_file(root: str | Path, canonical_name: str, *, expected_sha256: str | None = None) -> Path:
    root = Path(root)
    candidates = [p for p in root.rglob("*") if p.is_file() and _matches_canonical_filename(p, canonical_name)]
    if expected_sha256:
        candidates = [p for p in candidates if sha256_file(p) == expected_sha256.lower()]
    unique = {str(p.resolve()): p.resolve() for p in candidates}
    if len(unique) != 1:
        raise RuntimeError(
            "IHARQ_DERIVED_FILE_RESOLUTION_AMBIGUOUS: "
            f"canonical={canonical_name}; matches={sorted(unique)}"
        )
    return next(iter(unique.values()))


def _iter_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"IHARQ_JSONL_PARSE_FAILED: path={path}; line={line_number}") from exc
            if not isinstance(value, dict):
                raise RuntimeError(f"IHARQ_JSONL_ROW_NOT_OBJECT: path={path}; line={line_number}")
            yield value


@dataclass(frozen=True)
class WindowLocation:
    window_id: str
    window_record_id: str
    shard_filename: str
    hdf5_group: str
    hdf5_row: int
    shape: tuple[int, ...]
    dtype: str
    shard_sha256: str


class DerivedWindowDataset:
    """Bounded-memory access to one attached R26 derived-window Dataset."""

    def __init__(self, root: str | Path, *, verify_all_shards_at_open: bool = False):
        self.root = Path(root).resolve()
        if not self.root.is_dir():
            raise FileNotFoundError(self.root)
        self.manifest_path = resolve_unique_file(self.root, MANIFEST_NAME)
        self.manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        self._validate_manifest()
        index_spec = self.manifest.get("window_location_index", {})
        expected_index_hash = index_spec.get("dataset_sha256")
        index_name = index_spec.get("dataset_filename", LOCATION_INDEX_NAME)
        self.location_index_path = resolve_unique_file(
            self.root,
            str(index_name),
            expected_sha256=str(expected_index_hash).lower() if expected_index_hash else None,
        )
        self._shards = {
            str(row["filename"]): row
            for row in self.manifest.get("shards", [])
        }
        if len(self._shards) != len(self.manifest.get("shards", [])):
            raise RuntimeError("IHARQ_DERIVED_DUPLICATE_SHARD_FILENAME")
        self._location_cache: dict[str, WindowLocation] = {}
        self._verified_shards: set[str] = set()
        if verify_all_shards_at_open:
            for filename in sorted(self._shards):
                self._resolve_and_verify_shard(filename)

    @classmethod
    def discover(cls, input_root: str | Path = "/kaggle/input", *, verify_all_shards_at_open: bool = False) -> "DerivedWindowDataset":
        input_root = Path(input_root)
        manifests = [p for p in input_root.rglob("*") if p.is_file() and _matches_canonical_filename(p, MANIFEST_NAME)]
        roots = {str(p.parent.resolve()): p.parent.resolve() for p in manifests}
        if len(roots) != 1:
            raise RuntimeError(
                "IHARQ_DERIVED_DATASET_DISCOVERY_REQUIRES_EXACTLY_ONE: "
                f"observed={sorted(roots)}"
            )
        return cls(next(iter(roots.values())), verify_all_shards_at_open=verify_all_shards_at_open)

    def _validate_manifest(self) -> None:
        manifest = self.manifest
        if manifest.get("scientific_freeze") != EXPECTED_FREEZE:
            raise RuntimeError("IHARQ_DERIVED_SCIENTIFIC_FREEZE_MISMATCH")
        if manifest.get("format") != EXPECTED_FORMAT:
            raise RuntimeError("IHARQ_DERIVED_FORMAT_MISMATCH")
        if manifest.get("creation_status") not in {None, "COMMITTED"}:
            raise RuntimeError("IHARQ_DERIVED_DATASET_NOT_COMMITTED")
        if int(manifest.get("immutable_revision", 0)) != 1:
            raise RuntimeError("IHARQ_DERIVED_REVISION_MISMATCH")
        if int(manifest.get("window_count", -1)) < 0:
            raise RuntimeError("IHARQ_DERIVED_WINDOW_COUNT_INVALID")
        if manifest.get("signal_dtype") not in {None, "float32"}:
            raise RuntimeError("IHARQ_DERIVED_SIGNAL_DTYPE_MISMATCH")

    def _resolve_and_verify_shard(self, filename: str) -> Path:
        spec = self._shards.get(filename)
        if spec is None:
            raise KeyError(f"Unknown shard: {filename}")
        path = resolve_unique_file(self.root, filename)
        resolved_key = str(path)
        if resolved_key not in self._verified_shards:
            expected_bytes = int(spec["bytes"])
            if path.stat().st_size != expected_bytes:
                raise RuntimeError(
                    f"IHARQ_DERIVED_SHARD_SIZE_MISMATCH: {filename}; "
                    f"expected={expected_bytes}; observed={path.stat().st_size}"
                )
            observed_hash = sha256_file(path)
            if observed_hash != str(spec["sha256"]).lower():
                raise RuntimeError(
                    f"IHARQ_DERIVED_SHARD_SHA256_MISMATCH: {filename}; "
                    f"expected={spec['sha256']}; observed={observed_hash}"
                )
            self._verified_shards.add(resolved_key)
        return path

    def iter_locations(self) -> Iterator[WindowLocation]:
        seen: set[str] = set()
        for row in _iter_jsonl(self.location_index_path):
            window_id = str(row["window_id"])
            if window_id in seen:
                raise RuntimeError(f"IHARQ_DERIVED_DUPLICATE_WINDOW_ID: {window_id}")
            seen.add(window_id)
            filename = str(row["shard_filename"])
            shard_spec = self._shards.get(filename)
            if shard_spec is None:
                raise RuntimeError(f"IHARQ_DERIVED_INDEX_REFERENCES_UNKNOWN_SHARD: {filename}")
            location = WindowLocation(
                window_id=window_id,
                window_record_id=str(row["window_record_id"]),
                shard_filename=filename,
                hdf5_group=str(row["hdf5_group"]),
                hdf5_row=int(row["hdf5_row"]),
                shape=tuple(int(v) for v in row["shape"]),
                dtype=str(row["dtype"]),
                shard_sha256=str(shard_spec["sha256"]).lower(),
            )
            self._location_cache[window_id] = location
            yield location
        expected = int(self.manifest["window_count"])
        if len(seen) != expected:
            raise RuntimeError(
                f"IHARQ_DERIVED_INDEX_COUNT_MISMATCH: expected={expected}; observed={len(seen)}"
            )

    def location(self, window_id: str) -> WindowLocation:
        window_id = str(window_id)
        cached = self._location_cache.get(window_id)
        if cached is not None:
            return cached
        for location in self.iter_locations():
            if location.window_id == window_id:
                return location
        raise KeyError(window_id)

    def load(self, window_id: str, *, verify_window_id: bool = True):
        import h5py
        import numpy as np

        location = self.location(window_id)
        shard_path = self._resolve_and_verify_shard(location.shard_filename)
        with h5py.File(shard_path, "r") as handle:
            signals_path = f"{location.hdf5_group}/signals"
            ids_path = f"{location.hdf5_group}/window_ids"
            if signals_path not in handle or ids_path not in handle:
                raise RuntimeError(f"IHARQ_DERIVED_HDF5_GROUP_MISSING: {location.hdf5_group}")
            signals = handle[signals_path]
            identifiers = handle[ids_path]
            row = location.hdf5_row
            if row < 0 or row >= int(signals.shape[0]) or row >= int(identifiers.shape[0]):
                raise RuntimeError(f"IHARQ_DERIVED_HDF5_ROW_OUT_OF_RANGE: {window_id}; row={row}")
            stored_id = identifiers[row]
            if isinstance(stored_id, bytes):
                stored_id = stored_id.decode("utf-8")
            if verify_window_id and str(stored_id) != location.window_id:
                raise RuntimeError(
                    f"IHARQ_DERIVED_WINDOW_ID_MISMATCH: expected={location.window_id}; observed={stored_id}"
                )
            array = np.asarray(signals[row])
        if tuple(array.shape) != location.shape:
            raise RuntimeError(
                f"IHARQ_DERIVED_WINDOW_SHAPE_MISMATCH: expected={location.shape}; observed={array.shape}"
            )
        if str(array.dtype) != location.dtype:
            raise RuntimeError(
                f"IHARQ_DERIVED_WINDOW_DTYPE_MISMATCH: expected={location.dtype}; observed={array.dtype}"
            )
        return array

    def load_many(self, window_ids: Iterable[str]) -> Iterator[tuple[str, Any]]:
        for window_id in window_ids:
            yield str(window_id), self.load(str(window_id))


def _self_test() -> dict[str, Any]:
    import tempfile
    import h5py
    import numpy as np

    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        array = np.arange(24, dtype=np.float32).reshape(3, 8)
        shard = root / "001_D_subject_001_windows.h5"
        with h5py.File(shard, "w") as handle:
            group = handle.require_group("window_groups/c3_t8")
            group.create_dataset("signals", data=array[None, ...], dtype="float32")
            group.create_dataset("window_ids", data=np.asarray(["window:test"], dtype=h5py.string_dtype("utf-8")))
        index = root / ("002_" + LOCATION_INDEX_NAME)
        index.write_text(json.dumps({
            "window_id": "window:test",
            "window_record_id": "WindowRecord:test",
            "shard_filename": "D_subject_001_windows.h5",
            "hdf5_group": "window_groups/c3_t8",
            "hdf5_row": 0,
            "shape": [3, 8],
            "dtype": "float32",
        }) + "\n", encoding="utf-8")
        manifest = {
            "scientific_freeze": EXPECTED_FREEZE,
            "format": EXPECTED_FORMAT,
            "creation_status": "COMMITTED",
            "immutable_revision": 1,
            "window_count": 1,
            "window_location_index": {
                "dataset_filename": LOCATION_INDEX_NAME,
                "dataset_sha256": sha256_file(index),
            },
            "shards": [{
                "filename": "D_subject_001_windows.h5",
                "bytes": shard.stat().st_size,
                "sha256": sha256_file(shard),
            }],
        }
        (root / ("003_" + MANIFEST_NAME)).write_text(json.dumps(manifest), encoding="utf-8")
        dataset = DerivedWindowDataset(root)
        restored = dataset.load("window:test")
        return {
            "status": "PASS" if np.array_equal(array, restored) else "FAIL",
            "ordinal_prefix_resolution": True,
            "lossless_roundtrip": bool(np.array_equal(array, restored)),
            "shape": list(restored.shape),
            "dtype": str(restored.dtype),
        }


if __name__ == "__main__":
    print(json.dumps(_self_test(), indent=2))
