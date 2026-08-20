# IHARQ P02/L2 Cumulative Pre-Execution Audit Report R3 — TRAINING-POLICY RESOLVED / READY

## Controlling decision

```text
P02_KAGGLE_PREEXECUTION_AUDIT: PASS
READY_FOR_GOVERNED_KAGGLE_EXECUTION: YES
P02_SCIENTIFIC_EXECUTION_STARTED: NO
FREEZE_CRITICAL_BLOCKERS: 0
```

This R3 successor supersedes the R2 BLOCKED result for current pre-execution readiness while preserving R2 as historical audit evidence. R2 was correct to block: the project had selected the S&R challenger method/scope and conditional class-weight policy, but two exact Protocol-owned bindings were still absent. The owner subsequently authorized a minimal, research-grounded P02-only pre-execution amendment. No P00/P01 authority or accepted execution is changed.

## Source-exhaustion result before making new choices

The complete authority stack was rechecked before resolution. Method Selection freezes primary no-augmentation, a separate conditionally selected training-only S&R challenger, and class weighting only when needed, while deliberately delegating exact S&R segment/probability values and the class-weight trigger/formula downstream. Nuts-and-Bolts defines the S&R algorithm, leakage boundary, provenance and failure behavior but marks its probability/segment/seed/cell bindings Protocol-sync required. Build Book R4 fixes the challenger to EEGNet FULL_TRAIN with the same five model seeds but does not supply the missing numeric bindings. The cumulative Protocol through P01 does not own P02 exact values. Phase Analysis, Layer 0, Evidence Map and Layer 10 are consumers/governors and cannot invent new P02 training constants.

The targeted same-class gap scan found no third required-but-numerically-unfrozen P02 execution policy. Historical delegated Layer-2 issues are either concretized by Build Book R4/current implementation, lawful runtime gates for conditional external assets/environment, or downstream-owner responsibilities.

## Resolution 1 — EEGNet Segmentation-and-Reconstruction diagnostic challenger

Frozen by `P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R1`:

- condition: `P02-TRAIN-AUG-SR-EEGNET-FULL-R1`;
- diagnostic training-policy condition, not an A-number;
- EEGNet only, FULL_TRAIN only;
- PhysioNetMI, BNCI2014_001 and Lee2019_MI;
- same five primary EEGNet model seeds;
- exactly 15 separate diagnostic run cells;
- probability `0.5`;
- `n_segments=4`;
- deterministic namespace `IHARQ:P02:L2:EEGNET:SEGMENTATION_RECONSTRUCTION:R1`;
- same dataset / legal training role / task / class donors; validation/test donors forbidden;
- primary validation-selected EEGNet hyperparameters reused; no augmentation-specific tuning;
- validation/test protocol unchanged;
- augmented tensors ephemeral; no Layer-1 `WindowRecord` creation/overwrite;
- excluded from A4 role selection and primary P03 substrate.

Four segments are promoted here because they were the only IHARQ-bounded S&R configuration already technically validated and divide the 480-sample CORE window exactly into four contiguous 120-sample segments. The 0.5 probability is a conservative project-specific fixed strength chosen before scientific execution to avoid creating another tuning dimension. It is not claimed to be a universal or S&R-optimal value.

## Resolution 2 — current P02 class weighting

Frozen policy: `NEVER_WEIGHT_P02_CURRENT_FROZEN_INPUTS`, effective vector `[1.0, 1.0]`.

Exact inherited full-train counts are:

| dataset | left_hand | right_hand | action |
|---|---:|---:|---|
| PhysioNetMI | 1490 | 1459 | unweighted |
| BNCI2014_001 | 720 | 720 | unweighted |
| Lee2019_MI | 1600 | 1600 | unweighted |

P01 low-label budgets are equal-per-class and are also unweighted. This amendment intentionally defines no universal imbalance threshold. If the immutable input/split identity or the verified train counts change, Stage 05 fails closed and requires a new Protocol successor rather than auto-activating weights.

## Scope/non-regression

The official ablation plan remains exactly **678 A0 + 1,218 A4 = 1,896** cells. The 15 S&R cells are separate diagnostic training-policy cells. A14 remains absent/prohibited. Primary EEGNet remains no-augmentation. No P00/P01 regeneration is required. No future Phase Analysis, Layer 0, Evidence Map, Layer 10 or P03 artifact is removed or weakened.

## Runtime implementation

The resolved values are not notebook-local magic constants. They live in governed YAML/config surfaces, are checked by Stage 05, are consumed by the production neural fit path, receive deterministic augmentation provenance, are closed by Stage 15, are handed forward at Stage 22, and are copied into the final runtime bundle under `protocol_change_required/`. The notebook contains a dedicated pre-Stage-05 governance cell that records the amendment and future document synchronization obligation.

## Validation

- authoring/golden/negative/regression tests: **72/72 PASS**;
- strengthened static/package validator: **84/84 PASS**;
- real production-dispatch fixture: **26/26 PASS**;
- fixture runtime bundle: **298/298 internal checksum targets PASS; CRC PASS**;
- P00+P01 cumulative verifier: **40/40 PASS**;
- P01 finalized verifier: **24/24 PASS**;
- accepted P01 execution bundle: **13,164/13,164 internal checksum targets PASS; CRC PASS**;
- Sections 1–274: **274/274 re-audited**;
- Sections 275–323: **49/49 mapped and re-audited**;
- freeze-critical blockers remaining: **0**.

The small synthetic authoring suite is run with BLAS/OpenMP threads constrained to one to avoid local test-harness oversubscription. This is only a deterministic authoring-validation setting and does not alter the governed Kaggle scientific resource policy.

## Future Protocol / Build-Book synchronization

After the actual P02 execution bundle is accepted, the single cumulative Protocol v1.0 and P02 Build Book successor must incorporate the exact pre-execution amendment values and chronology. This is synchronization of a decision made **before** P02 scientific results, not an opportunity to retune or choose new values after seeing results. The exact instructions are in `docs/P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R1.md` and the machine-readable handoff template.

## Final boundary

P02 scientific execution has not been performed by this authoring/audit process. The package is ready to begin governed Kaggle execution subject only to normal runtime gates already represented in the design (immutable input verification, exact environment materialization, resource checks and conditional external-asset/license/checkpoint gates). Those gates do not represent unresolved P02 scientific-policy choices.


### Supporting external-evidence record

`docs/P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R1.md` preserves the literature/official-implementation rationale separately from project authority. It is non-superseding and cannot be used for post-result reselection.

- code-owned scientific bindings for the two resolved policies: **0** (`P02_TRAINING_POLICY_CODE_OWNERSHIP_AUDIT_R1.json`).
