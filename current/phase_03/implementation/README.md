# IHARQ BenchGuard Stretch C — Cumulative GitHub-Ready Repository Through Phase 02

**Current cumulative state:** `P00_P01_P02_MERGED_VALIDATED_READY_FOR_P03_INTAKE`

This is the canonical GitHub-ready cumulative repository state after formal Phase 02 / Layer 2 closure. It preserves the complete Phase 00 + Phase 01 GitHub-ready state, the accepted Phase 02 implementation/execution/replay state, and the finalized post-execution Protocol → Phase Analysis → Layer 0 → Evidence Map → Layer 10 → downstream-handoff lifecycle.

## What was merged

- The Phase 01 cumulative source archive is fully preserved by content: all 13,802 predecessor files are present in the supplied P02 tree; 13,799 are byte-identical and the three changed root-state files are explicitly retained under `history/predecessor_phase_01_cumulative_root_state_R1/`.
- The Stage24-replayed P02 GitHub-ready tree is the repository-content base and remains preserved under its existing paths.
- The accepted Layer 2 implementation is promoted to `src/iharq/layer2_decoders/` for cumulative import/reuse with only a root compatibility non-execution flag added to `__init__.py`; its original package remains unchanged at `current/phase_02/implementation/`.
- The finalized cumulative scientific/governance state is preserved exactly under `final_state/through_p02/`.
- The P02→P03 consumer-facing handoff is projected to `artifacts/handoffs/phase_02_to_phase_03/`.

## Current scientific/project state

- **P00:** preserved governed engineering, identity, validation, evidence, and reproducibility foundation.
- **P01 / L1:** accepted frozen public-EEG data/split/preprocessing/window and low-label substrate.
- **P02 / L2:** execution complete; A0/A4 evidence, model/checkpoint/prediction records, failures, diagnostics, statistics, finalized Protocol/Analysis/Layer 0/Evidence Map/Layer 10, and P03 handoff are available.
- **P03:** **not executed**. The next lawful step is P03 intake, reuse/invalidation review, environment/config/Protocol freeze, then governed execution.
- **A14:** `ABSENT_PROHIBITED`.
- Scientific evidence remains public-benchmark/non-clinical and carries the explicit A4, Stage18S, low-label, participant-scope, and external-access limitations recorded in the final handoff.

## Canonical navigation

- Core project authorities: `docs/authorities/current/`
- Final cumulative post-execution state through P02: `final_state/through_p02/`
- Final cumulative Protocol: `final_state/through_p02/authorities/protocol_v1/`
- Final cumulative Phase Analysis: `final_state/through_p02/analysis/`
- Final cumulative Layer 0: `final_state/through_p02/layer0/`
- Final cumulative Evidence Map: `final_state/through_p02/evidence_map/`
- Final cumulative Layer 10: `final_state/through_p02/layer10/`
- P02 Stage24 replay/current execution evidence: `current/phase_02/`
- P02 original accepted implementation package: `current/phase_02/implementation/`
- P02 promoted Layer 2 code: `src/iharq/layer2_decoders/`
- P02 environment: `environments/phase_02/`
- P02→P03 handoff: `artifacts/handoffs/phase_02_to_phase_03/`
- Heavy P02 artifact pointers: `external_artifact_pointer_manifest.yaml`
- Merge audit: `artifacts/cumulative_state/p02_final_merge_R2/`

## P03 intake

Start with:

1. `CURRENT_PROJECT_STATUS.json`
2. `artifacts/handoffs/phase_02_to_phase_03/P03_fresh_session_intake_checklist.md`
3. `artifacts/handoffs/phase_02_to_phase_03/downstream_readiness.yaml`
4. `artifacts/handoffs/phase_02_to_phase_03/producer_consumer_matrix.yaml`
5. `final_state/through_p02/authorities/protocol_v1/`
6. `final_state/through_p02/evidence_map/`
7. `external_artifact_pointer_manifest.yaml`

Do not infer P03 results from this repository. P03 must perform its own intake, authority/config/environment/Protocol freeze, reuse decisions, execution, analysis, Layer 0, Evidence Map, Layer 10, and handoff lifecycle.

## Verification

```bash
python scripts/verify_cumulative_release.py
python -m compileall -q src
python -m pytest -q -p no:cacheprovider
```

The nested P02 implementation/replay package has its own validation assets and remains independently auditable under `current/phase_02/implementation/` and `current/phase_02/kaggle_run_light/`.
