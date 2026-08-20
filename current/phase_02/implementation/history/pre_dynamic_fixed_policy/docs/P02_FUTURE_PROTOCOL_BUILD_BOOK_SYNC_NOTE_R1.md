# P02 Pre-Execution Training-Policy Amendment R1

**Amendment ID:** `P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R1`  
**Status:** `OWNER_AUTHORIZED_PREEXECUTION_FREEZE`  
**Purpose:** resolve the two narrow P02 scientific-freeze blockers without reopening P00/P01, changing A0/A4 ownership, adding A14, or reducing any P02/L2 function or downstream artifact.

## 1. Why this amendment exists

The final pre-execution audit found that the implementation was technically complete but two training-policy values were intentionally left Protocol-owned: the exact EEGNet Segmentation-and-Reconstruction (S&R) challenger binding and the P02 class-weight activation policy. The existing authorities determine the method and scope but do not freeze the missing numeric/identity values. This amendment is the owner-authorized pre-run bridge and **must later be incorporated into the single cumulative Protocol v1.0 and P02 Build Book successor**.

## 2. Resolved EEGNet S&R challenger

- Condition ID: `P02-TRAIN-AUG-SR-EEGNET-FULL-R1`.
- Classification: diagnostic training-policy challenger; **not** A0/A4/A-number.
- Branch: `DNN-EEGNET` only.
- Evidence regime: `FULL_TRAIN` only.
- Datasets: PhysioNetMI, BNCI2014_001, Lee2019_MI.
- Seeds: the same five frozen EEGNet model seeds per dataset.
- Planned challenger cells: **15** (3 datasets × 5 seeds).
- Probability: **0.5** per target training trial per epoch.
- Temporal segments: **4**, contiguous, preserving segment order.
- Donors: same dataset + same legal training role + same task + same class; validation/test donors prohibited.
- Seed namespace: `IHARQ:P02:L2:EEGNET:SEGMENTATION_RECONSTRUCTION:R1`.
- Seed derivation: deterministic SHA-256 namespace derivation from dataset/model-seed/repeat/epoch.
- Hyperparameters: reuse the validation-selected primary no-augmentation EEGNet parameters for the same dataset × model seed. **No augmentation-specific retuning.**
- Validation/test: identical matched primary cell; augmentation is train-only.
- Synthetic tensors are ephemeral and never become Layer-1 `WindowRecord` objects.
- Challenger outputs are diagnostic-only, cannot replace primary A0 EEGNet, cannot enter A4 representative selection, and cannot silently become the P03 primary prediction substrate.

The official Braindecode S&R interface exposes probability, segment count, and RNG and performs label-aware segment mixing while preserving temporal segment order. IHARQ had already technically validated a four-segment same-class implementation; that earlier check was not scientific authority, so this amendment is the point at which four segments become governed for the P02 diagnostic challenger. Braindecode's S&R interface requires an explicit probability but does not prescribe a universal optimum. P02 therefore freezes 0.5 as a conservative project-specific moderate application rate that avoids a new tuning search. Braindecode's official EEG augmentation tutorial uses 0.5 for another stochastic augmentation, demonstrating that this is a conventional moderate transform probability—not S&R-specific evidence of optimality. A systematic EEG augmentation comparison likewise reports that no single augmentation strategy is best across tasks.

## 3. Resolved class-weight policy

Policy: `NEVER_WEIGHT_P02_CURRENT_FROZEN_INPUTS`.

Frozen P01 train-role counts inherited by P02:

| Dataset | left_hand | right_hand | max/min ratio | P02 action |
|---|---:|---:|---:|---|
| PhysioNetMI | 1490 | 1459 | 1.021247 | no weighting |
| BNCI2014_001 | 720 | 720 | 1.000000 | no weighting |
| Lee2019_MI | 1600 | 1600 | 1.000000 | no weighting |

Low-label budgets are frozen equal-per-class memberships and also remain unweighted. The effective class-weight vector is `[1.0, 1.0]` for every current P02 cell. This is a **phase-specific no-weight freeze**, not a new universal imbalance threshold. If the governed input/split identity or these train counts change, Stage 05 must fail closed and require a Protocol successor; the notebook may not auto-invent a threshold or weighting formula.

## 4. Minimal future document synchronization

Apply this amendment later as follows; do not rewrite unrelated historical text.

1. **Protocol v1.0 P02 annex/current cumulative authority:** add both exact policies above and the 15 challenger-cell identities; record this amendment ID/hash as the pre-execution source.
2. **P02/L2 Build Book successor:** replace the unresolved S&R numeric/identity placeholders with this freeze and add `NEVER_WEIGHT_P02_CURRENT_FROZEN_INPUTS`; keep primary neural no-augmentation, A0/A4 ownership, A14 prohibition, model portfolio and all downstream contracts unchanged.
3. **Nuts-and-Bolts:** resolve the existing `[PROTOCOL-v1.0 SYNC REQUIRED]` marker by reference to the Protocol successor; no algorithm rewrite is required.
4. **Method Selection:** no method reselection. Add only a realization note that P02 instantiated the already-selected conditional S&R challenger and determined no class weighting for the current frozen P02 inputs.
5. **Run/scientific-freeze derivatives:** preserve the 1,896 A0+A4 cells exactly; add the separate 15-cell training-policy challenger manifest.
6. **Phase Analysis:** if executed, analyze S&R evidence under a clearly diagnostic training-policy section; do not promote it into an A-number or primary A0 evidence.
7. **Layer 0 / Evidence Map / Layer 10:** consume this diagnostic evidence only under the ordinary claim/evidence governance; Layer 10 may render but not recompute.
8. **P00/P01:** no revision and no rerun.

## 5. Non-regression invariants

- A0 planned cells remain 678.
- A4 planned slots remain 1,218.
- A0+A4 total remains 1,896.
- Additional training-policy diagnostic cells = 15.
- A14 remains absent/prohibited.
- No downstream ablation ownership changes.
- Primary EEGNet remains no-augmentation.
- Test outcomes never select augmentation parameters, class weights, or challenger membership.

## 7. Supporting external-evidence record

The research/implementation rationale is preserved separately in `docs/P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R1.md`. It is supporting evidence only: future Protocol/Build-Book synchronization must copy the already-frozen amendment values exactly and must not reselect them after seeing P02 results.
