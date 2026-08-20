# P03 Fresh-Session Intake Checklist

This checklist is a consumer-facing projection of the governed P02 handoff. It does not execute P03 science.

1. Load `downstream_readiness.yaml` and verify accepted P02 run `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d` and config `9e181d2e935d2e9674ca6e05572f49520ad0306a3761362b770f8bee8c78ce13`.
2. Validate `execution/implementation/contracts/record_schema_freeze.yaml`.
3. Load the `Layer2ReadinessReport`; require `compatibility_status: PASS`, `missing_fields: []`, and `blocking_reasons: []`.
4. Resolve PredictionRecord partitions through the local partition manifests and the preferred immutable P02 workspace source in `external_artifact_retrieval.yaml`.
5. Preserve recorded `class_order`, `score_type`, and `score_semantics`; do not reinterpret scores.
6. Load ModelRegistryRecord lineage and checkpoint hashes. Retrieve checkpoint bytes only when the P03 method actually requires them.
7. Preserve P01 dataset/split/preprocessing/window identities; do not mutate upstream records in place.
8. Carry `persistent_limitations.yaml` into P03 planning.
9. P03 may calibrate, threshold, and evaluate selective/uncertainty behavior; P02 did not establish those scientific results.
10. Resolve `IHARQ_HF_TOKEN_PRE_P02` and `IHARQ_HF_TOKEN_P02` independently where required. Never hardcode literal credential values.
