# IHARQ Phase 03 — cumulative integration guide

This directory documents how the supplied **Phase 03 GitHub-ready post-extension 64/128/256 R1** release is integrated into the cumulative P00→P03 repository. The source Phase 03 README is preserved byte-for-byte as `SOURCE_PHASE03_RELEASE_README.md`.

## Current cumulative interpretation

- **Canonical P03 evidence** is promoted into the cumulative `artifacts/.../phase_03/` families and `final_state/through_p03/`.
- **Canonical P03 runtime receipts** are retained under `current/phase_03/canonical_execution/`.
- **Accepted P03 implementation** is retained intact under `current/phase_03/implementation/` and promoted into the cumulative root `src/`, `configs/`, and `schemas/` surfaces where applicable. Functional modules are byte-identical; the root Layer 3 `__init__.py` uses a cumulative non-execution compatibility shim so import never counts as scientific execution.
- **Post-extension 64/128/256 evidence** remains scope-separated under `current/phase_03/post_extension_64_128_256/`; it is not used to overwrite canonical P03 files that share names but represent different scientific scopes.
- **P03 release metadata and external-heavy-artifact pointers** are under `current/phase_03/release_metadata/`.
- **P03→P04 handoff authority** is `artifacts/handoffs/phase_03_to_phase_04/p03_handoff_manifest.json`.

## Scientific/governance boundary

This cumulative merge performs repository integration, provenance preservation, indexing, checksum regeneration, and implementation promotion. It does **not** rerun scientific models, retune thresholds, approve candidate claims, use test data for selection, or create the future consumer-authored Protocol v1 / Phase Analysis / Layer 0 / Evidence Map / final Layer 10 outputs that the P03 release explicitly leaves to downstream governance.

## Preservation evidence

The authoritative mapping of every supplied P03 file to its cumulative destination is `artifacts/cumulative_state/p03_post_extension_merge_R1/SOURCE_TO_CUMULATIVE_PATH_MAP.csv`. Superseded P00→P02 current-path bytes are preserved under `history/p03_merge_preimages_R1/`.
