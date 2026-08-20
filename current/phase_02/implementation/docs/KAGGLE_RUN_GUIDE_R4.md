# IHARQ Phase 02 — Final Kaggle Run Guide R4

## What you should run

Use **one notebook only**:

`IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb`

Use the matching implementation input package:

`IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R4.zip`

Do **not** edit the notebook's model, S&R, class-weight, A0, A4, seed, metric, statistical, or artifact settings before execution. The two former training-policy blockers are now resolved by governed code:

- S&R probability is selected per dataset from the frozen validation-only grid `{0.25, 0.50, 0.75}` before test inference; `n_segments` is resolved by pinned Braindecode with `n_segments=None` and recorded.
- Equal fit-role class counts use uniform training. Unequal counts compute standard training-label-only balanced weights and compare weighted vs uniform with the same selected hyperparameters/seed on validation only. Only natively/explicitly supported classifiers participate.

No test result is allowed to choose either policy.

---

# Step-by-step Kaggle procedure

## 1. Create the Kaggle notebook

1. Open Kaggle Notebooks.
2. Import/upload `IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb`.
3. Do not modify its cells.

## 2. Configure the runtime

Before starting the scientific run:

1. Select a **GPU accelerator**. A GPU with at least 12 GiB VRAM is preferred; the notebook also has governed behavior for 8–12 GiB, <8 GiB, and CPU-only cases.
2. Turn **Internet ON** for the bootstrap unless you already know the exact frozen Python package versions are present. The first cell installs the exact pinned requirements only when the environment does not already match them.
3. Do not manually substitute package versions if installation fails. Stage 01 is the environment gate; an exact-pin failure should be repaired as an environment problem, not by changing scientific methods.

## 3. Attach the P02 implementation package

Attach a Kaggle Dataset/input containing exactly:

`IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R4.zip`

The notebook discovers that exact filename under `/kaggle/input`, extracts it to `/kaggle/working`, and verifies its internal `checksums.sha256` **before importing project code**.

Do not attach two copies/versions of the implementation package at the same time; the bootstrap deliberately fails on ambiguous package resolution.

## 4. Attach the cumulative P00+P01 repository ZIP

Attach the canonical cumulative repository file:

`IHARQ_Cumulative_GitHub_Ready_Through_P01_R1.zip`

Required SHA-256:

`dc2708ab70e7746499ae09760456825b54efcf587cae3db3410e6f72b0024542`

If your local copy is named with a suffix such as `(2)`, rename the file to the canonical filename **without altering its bytes** before putting it in the Kaggle input Dataset.

## 5. Attach the immutable P01 core Dataset

Add this Kaggle Dataset as an input:

`csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473`

The notebook expects:

- provider version: `2`
- logical immutable revision: `1`
- manifest: `IHARQ_P01_L1_DERIVED_WINDOW_DATASET_MANIFEST.json`
- manifest SHA-256: `dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1`
- HDF5 bytes: `1,166,652,764`
- core windows: `12,910`

This input is read-only.

## 6. Attach the immutable P01 A4 R2 Dataset

Add this Kaggle Dataset as an input:

`csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108`

Expected contract:

- provider version: `1`
- logical revision: `2`
- manifest: `IHARQ_P01_L1_A4_DERIVED_WINDOW_DATASET_MANIFEST.json`
- manifest SHA-256: `29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305`
- matched parents: `12,910 / 12,910`
- A4 WindowRecord rows: `51,640`

The notebook must consume this frozen R2 A4 substrate; it must not reconstruct or regenerate it.

## 7. Conditional model/checkpoint inputs

If you possess the exact immutable assets required for a conditional deep/SSL branch, attach them before the run. They must pass the branch's checksum, license, corpus-overlap, input-compatibility and resource gates.

If you do not have such an asset, do **not** invent one or download an unknown mutable checkpoint during a scientific stage. The branch will receive its governed blocked/skipped terminal status and remain visible in evidence. The mandatory P02 baseline floor continues according to the frozen gates.

## 8. Secrets

No Kaggle API token is required for the core scientific computation when all required inputs are already attached through Kaggle.

Do not paste credentials into notebook cells. If a future conditional asset genuinely needs authentication, use Kaggle Secrets. The package records only credential availability/source type, never the secret value.

## 9. Start the actual governed run

After all inputs and settings are correct, execute the notebook **top to bottom exactly once**.

For a long run, prefer creating the actual Kaggle version with **Save Version / Save & Run All** after the inputs and accelerator are configured. This gives you a clean top-to-bottom batch execution and persistent version logs/output rather than relying only on the browser's interactive session.

Do not start a second concurrent copy of the same run.

## 10. What the first cells do

The bootstrap will:

1. resolve exactly one R4 implementation package;
2. verify internal package checksums;
3. verify `P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R4.json` is PASS with zero blockers;
4. verify the R2 training-policy amendment is present;
5. compare the current Python environment with the frozen requirements;
6. install exact pins only when required;
7. import the P02 package;
8. compute source/config/stage-plan/R5-freeze fingerprints;
9. create the single production `NotebookSession`.

If bootstrap fails, **do not manually skip the cell**. Fix the named input/environment problem first.

## 11. Preflight stages 00–07

These stages verify authority identity, environment/resources, cumulative-repository integrity, external P01 pointers, immutable P01 contract, R5/R2 scientific-policy freeze, schemas/imports and the data-role firewall.

An error here happens before expensive official scientific execution. Preserve the exact error/log and repair the input/environment issue rather than changing scientific settings.

## 12. How the former blockers are resolved automatically

You do not enter any values manually.

### Class weighting

For each eligible selected classifier/loss:

- equal legal fit-role counts → uniform training, no extra weighted fit;
- unequal counts → compute `n / (K * n_c)` weights from fit labels only;
- compare uniform vs balanced using the same selected hyperparameters and seed on the legal validation role;
- select by validation BACC → validation macro-F1 → uniform tie-break;
- freeze the selected policy before test inference;
- store counts, weights, validation metrics and selected policy in runtime evidence.

Algorithms without native/verified class-weight support are not silently rewritten.

### EEGNet Segmentation/Reconstruction

The primary EEGNet remains unaugmented.

For the separate FULL_TRAIN diagnostic challenger:

- evaluate probabilities `0.25`, `0.50`, `0.75` on validation only;
- use all five frozen EEGNet model seeds in the real run;
- aggregate by median validation BACC → median validation macro-F1;
- deterministic tie-break: proximity to `0.50`, then lower probability;
- Braindecode resolves `n_segments` with `n_segments=None` and the resolved value is recorded;
- only after selection are the final 15 dataset×seed challenger cells evaluated on test.

Those calibration fits are internal model selection, not new A-numbers and not additions to the official 1,896 A0/A4 cells.

## 13. Scientific stages

The notebook then runs the governed sequence:

- Stage 08 sanity/negative controls
- Stage 09 classical anchors
- Stage 10 Riemannian anchors
- Stage 11 compact neural + training-policy challenger
- Stage 12 conditional deep/SSL branches
- Stage 13 checkpoint/model-registry closure
- Stage 14 PredictionRecord closure
- Stage 15 A0 + training-policy closure
- Stage 16 low-label curves
- Stage 17 participant/session profiles
- Stage 18 A4 C0–C5 + C4/C5 strongest-constituent inference
- Stage 18U additional-ablation authority check
- Stages 19–24 failure evidence, readiness, figure/table sources, downstream handoffs, evidence sufficiency and final export

Do not manually rerun an expensive scientific cell simply because a later stage reports a problem. Use the stage ledger and the named blocker to determine the lawful repair scope.

## 14. Final output

On successful Stage 24, the notebook prints the final runtime bundle path and also copies the ZIP to the top-level Kaggle working/output area:

`/kaggle/working/IHARQ_P02_L2_Phase_Execution_Bundle_<RUN_ID>.zip`

The bundle includes runtime records, metrics, PredictionRecords, checkpoints/pointers, A0/A4 evidence, training-policy selection evidence, failures/negative results, figure/table sources, logs, stage/gate ledgers, Protocol/Phase-Analysis/Layer0/EvidenceMap/Layer10/P03 handoffs, the future Protocol-change files and SHA-256 checksums.

## 15. After the run succeeds

Preserve/download:

1. the final `IHARQ_P02_L2_Phase_Execution_Bundle_<RUN_ID>.zip`;
2. the completed Kaggle notebook version/output/logs;
3. any separately attached conditional-asset identities used during the run.

Do not edit the emitted training-policy selections after seeing test results.

The runtime bundle contains a `protocol_change_required/` directory with:

- `P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml`
- `P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md`
- `P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R2.md`

Use those later to synchronize the cumulative Protocol v1.0 / P02 Build-Book successor and record the **realized accepted-run bindings**. The later documentary update must not retrospectively retune them.

## 16. If the notebook blocks

Do not compromise the project by bypassing a gate.

Capture and preserve:

- exact stage ID;
- blocker/status code;
- full traceback/log;
- stage ledger JSON;
- partial bundle path if one was emitted;
- Kaggle accelerator/resource information.

A mandatory-input, environment or code defect should be repaired at that layer. A conditional external-model resource/license/checkpoint failure remains its governed terminal evidence unless the exact admissible asset can be supplied. Never solve a runtime problem by changing A0/A4 membership, using the test set for selection, replacing immutable P01 windows, weakening checksums, or inventing a new execution mode.
