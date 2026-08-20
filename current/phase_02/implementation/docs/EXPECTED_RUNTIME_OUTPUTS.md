# Expected runtime outputs

When the notebook is later executed on real governed P01 data, it creates one `IHARQ_P02_L2_Phase_Execution_Bundle_<RUN_ID>/`-style governed bundle containing:

- authority/source/environment/notebook/config/input/run-cell/checkpoint/record/artifact/failure/external-pointer/bundle manifests;
- accepted PredictionRecords and other frozen P02 record families;
- A0 terminal evidence and participant-level analysis sources;
- low-label curves and subject/session profile sources;
- A4 C0–C5 terminal evidence;
- the 15-cell EEGNet FULL_TRAIN diagnostic Segmentation-and-Reconstruction challenger terminal evidence, dataset-level validation-only S&R probability selection, recorded auto-resolved segment count, matched-primary comparisons where both cells succeed, and explicit negative/failure states otherwise;
- governed per-run class-weight decision evidence: fit-role counts, standard balanced vector when applicable, uniform-vs-weighted validation metrics, selected policy and explicit no-test-selection provenance;
- `protocol_change_required/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml`, `protocol_change_required/P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md`, and the supporting R2 external-evidence note, so the accepted run bundle carries the exact future Protocol/Build-Book update obligation;
- matched C1/C2/C3-vs-C0 evidence;
- C4/C5 ensemble-vs-validation-selected-strongest-constituent participant-level evidence;
- failures, blocked branches, negative/null and diagnostic-only evidence;
- figure-source and table-source data;
- Protocol v1, Phase Analysis, Layer 0, Evidence Map, Layer 10 and P03 handoffs;
- stage/gate ledgers, persistent logs, heartbeats and resource evidence;
- SHA-256 checksums and a validated archive.

A partial/blocked future execution exports only lawful partial evidence and explicitly identifies unexecuted descendants/blockers. It never marks a partial phase as complete.

This authoring package contains no real P02 runtime result bundle.
