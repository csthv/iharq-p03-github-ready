# IHARQ Phase 01 / Layer 01

This repository is the compact code, configuration, governance,
records, evidence, cards, manifests, gates, and handoff companion
to the private Kaggle derived-window Dataset.

It contains no duplicate raw EEG files and no HDF5 window shards.

- Config ID: `d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f`
- Execution attempt: `20260807143013-663eab13`
- Scientific freeze: `P01-L1-OFFICIAL-RUN-FREEZE-R2`
- Runtime policy: `P01-L1-KAGGLE-DUAL-PERSISTENCE-BOUNDED-STREAMING-R3`
- Derived Dataset handle:
  `csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473`

## Reproduction

1. Attach the original source Kaggle Datasets when raw-source
   regeneration is required.
2. Attach the private derived-window Dataset for future phases.
3. Use `runtime_overlays/iharq_window_shard_reader.py` to resolve
   window IDs to immutable HDF5 shard rows.
4. Verify manifests and SHA-256 values before use.

No later-phase model training is executed in Layer 1.
