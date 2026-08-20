# IHARQ BenchGuard Stretch C
# Experiment, Ablation, and Evaluation Protocol v1.0 — Phase 01 Annex

## 6.1 Document control

| Field | Frozen/actual value |
| --- | --- |
| annex_id | IHARQ-PROTOCOL-V1-P01-ANNEX-R1 |
| master_protocol_id | IHARQ-PROTOCOL-V1-MASTER-R3 |
| phase_id | P01 |
| official_phase_name | Public Data and Split Protocol |
| primary_implementation_layer | L1 |
| version | 1.0-P01-R1 |
| status | FROZEN_WITH_EXPLICIT_EXECUTION_AMENDMENTS_AND_DOWNSTREAM_REQUIREMENTS |
| registration/freeze timestamp | 2026-08-07T23:36:00+03:30 |
| source snapshot | final P01 execution bundle SHA-256 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e |
| implementation Build Book | IHARQ-IBB-R10-P01-L1-INDEPENDENT-AUDIT-REPAIRED / IHARQ-IBB-P01-L1-ANNEX-R4 |
| execution bundle | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip |
| config_id | d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| executed notebook source SHA-256 | 54b84d9cd29eb57bb22f45b7b7251e76e4947863c832528dba9c51b96189b023 |
| final runtime revision | R49-MATCHED-A4-R2-COMPLETE |
| base notebook manifest ID | P01-L1-KAGGLE-NOTEBOOK-R26 |
| scientific_freeze | P01-L1-OFFICIAL-RUN-FREEZE-R2 |
| gate decision | ACCEPTED; P01-G01..P01-G16 PASS; 0 blockers |
| evidence status | SUFFICIENT_FOR_PROTOCOL_AND_PHASE_REPORT; DATA/ENGINEERING FOUNDATION ONLY |
| external core pointer | csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473 / provider v2 / logical rev1 / dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1 |
| external A4 pointer | csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108 / provider v1 / logical family R2 / 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305 |
| supersession status | First P01 annex; inherits P00 and Master R3; A4 R2 supersedes only the failed proposed A4 R1 alternative profile |

## 6.2 Phase declaration and purpose

P01 is the governed **public-data, source-provenance, labeling, subject-group split, preprocessing, event/window materialization, quality-validation, canonical-record, external-persistence and downstream-readiness phase** for Layer 1. Its claim-bearing ceiling is data/protocol integrity and reproducible downstream readiness. P01 does **not** own decoder training, decoder superiority, calibration effectiveness, clinical efficacy, deployment safety, policy benefit, stress robustness or embodiment effectiveness.

## 6.3 Prior-state inheritance from P00

P01 reuses, without rewriting P00 history: the project authority stack; Registry-backed record/schema infrastructure; canonical hashing/canonicalization; lifecycle/lineage rules; validators/fixtures; phase/layer interfaces; global A0-A13 identities; the no-A14 lock; Protocol master inheritance; and Build Book/reproduction infrastructure. P01 extends these surfaces with actual L1 DatasetRecords, LabelMapRecords, SplitRecord, PreprocessingRecord, WindowRecords, quality records, validation reports, readiness artifacts, external Dataset pointers and P01→P02 handoffs.

P00 Annex R2 is copied byte-for-byte into this package and remains associated with Master R2 as its historical frozen context. Master R3 does not rewrite that artifact; it supplies current workflow governance for new/current annexes.

## 6.4 Pre-run Phase 1 freeze

The controlling pre-run intent was `P01-L1-OFFICIAL-RUN-FREEZE-R2`, under Build Book `IHARQ-IBB-R10-P01-L1-INDEPENDENT-AUDIT-REPAIRED` and Annex `IHARQ-IBB-P01-L1-ANNEX-R4`. It froze:

- active datasets: PhysioNetMI, BNCI2014_001, Lee2019_MI; inactive screened sources: Cho2017, GuttmannFlury2025_MI;
- official binary labels: left_hand/right_hand; exclusions: rest/no_action, feet, tongue, motor execution, technical markers and unlabeled online/test events as source-appropriate;
- `P01-L1-PREPROCESS-OFFICIAL-R2`;
- `P01-L1-SPLIT-OFFICIAL-R2`, subject grouping, 60/20/10/10, seed 20260804;
- `P01-L1-LOW-CAL-OFFICIAL-R2`, budgets 1/2/4/8/16/32 per class from calibration only, seed 20260804;
- `P01-L1-WINDOW-OFFICIAL-R2`, one +0.5..+3.5 s window/event at 160 Hz;
- `P01-L1-QUALITY-OFFICIAL-R2`, annotate-not-repair;
- original Kaggle environment intent, exact package pins, deterministic thread variables, original 60/90 GiB disk policy;
- P01-G01..P01-G16, dual persistence and P02 handoff expectations.

The Build Book itself explicitly stated that the official run was **not executed in that package**; therefore actual execution values below are taken from the final execution bundle.

## 6.5 Actual source datasets

| Dataset | Release/source revision | Scientific role | License | Access | Observed aggregate SHA-256 | Subjects | Sessions | Runs | Sampling Hz | Source event inventory count | Observed channel-set width* | Accepted core-window role counts | DatasetRecord | Semantic hash | Lifecycle | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PhysioNetMI | 1.0.0 | source/rest/provenance anchor | Open Data Commons Attribution License 1.0 (ODC-By-1.0) | MOABB_1_5_0_OFFICIAL_PHYSIONET_DOWNLOAD | 28cd2062983b6236f9a0e7fdee91fc9d8d5aad8eee3ef561cff5828ae89bf2ba | 109 | 0 | 12, 4, 8 | 128.0, 160.0 | 9509 | 65 | T 2949 / C 979 / V 495 / Test 495 | IHARQ-DATASETRECORD-20260806-66309cda68771bef | 66309cda68771bef9bd7a3aebdac819d91201cedca79ab112ea993fb61f558cf | VALIDATED | Run context is mandatory for T1/T2 semantics; Executed-movement and baseline runs are excluded from the official binary MI branch; Subject 88 rate exception must be recorded and resampled deterministically; MOABB bulk loading across subject 88 and 160 Hz subjects is prohibited; per-subject acquisition is mandatory. |
| BNCI2014_001 | 001-2014 provider file set A01T/A01E through A09T/A09E | standard four-class MI benchmark companion; official P01 binary left/right branch | Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0) | MOABB_1_5_0_OFFICIAL_BNCI_DOWNLOAD | 04a5390f8f36eaadbc0c480ec9377ce1b99caf0b7ab53bad9fda12347995bc49 | 9 | 0train, 1test | 0, 1, 2, 3, 4, 5 | 250.0 | 5184 | 26 | T 1440 / C 576 / V 288 / Test 288 | IHARQ-DATASETRECORD-20260806-42c424800627b6ee | 42c424800627b6ee0be7f47ad602ba49cf4c24a632c1fa69c8c750a4ba77e163 | VALIDATED | Feet and tongue are preserved as excluded source labels in the official binary branch; EOG channels are metadata/quality channels and not model input; CC BY-ND restrictions prohibit redistributed derived raw-signal variants |
| Lee2019_MI | GigaDB dataset DOI 10.5524/100542; MOABB 1.5.0 Lee2019_MI wrapper; labeled offline/train MI runs only | maximum-scope two-session left/right MI target companion | GNU General Public License v3.0 as documented by the maintained MOABB source card; source terms retained in DatasetCard | MOABB_1_5_0_OFFICIAL_GIGADB_DOWNLOAD | 3a07b2f302da949efd418a0712d5a9427df34dcb8b027ca553fae8e67a849f78 | 54 | 1 | 1train | 1000.0 | 5400 | 67 | T 3200 / C 1100 / V 500 / Test 600 | IHARQ-DATASETRECORD-20260806-adb91f25a65e588e | adb91f25a65e588ece06884a9598cc92bd932e91c4babc3cacb98c82901596f1 | VALIDATED | Online/test runs are excluded from supervised P01 records; High-rate source requires deterministic anti-aliased resampling; Source phase and session must remain in lineage |


*Channel-set width is the observed source record channel-set string width, including metadata/stim/EOG channels where present; the official signal tensor remains EEG-only under preprocessing. Source `event_count` is the admitted source event inventory and is not identical to the accepted left/right core denominator. Accepted core-window counts are the supervised P01 denominator after labels/exclusions and all validity rules.

## 6.6 Task, labels and exclusions

The P01 task is binary left-hand versus right-hand motor imagery. Non-target events are **excluded, not relabeled as negative**. Unknown source events fail closed. Dataset-specific mappings are:

| Dataset | Mapping | Explicit exclusions | Unknown-event behavior | LabelMapRecord | Semantic hash | Lifecycle |
| --- | --- | --- | --- | --- | --- | --- |
| PhysioNetMI | {"run_4_8_12:T1": "left_hand", "run_4_8_12:T2": "right_hand"} | run_4_8_12:T0 | BLOCK_SOURCE_EVENT_WITH_UNKNOWN_LABEL | IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9 | 4379781a3b5f5ea91f70c560e007de42d8624b4ee0e6a792921079fbd069a663 | VALIDATED |
| BNCI2014_001 | {"769": "left_hand", "770": "right_hand"} | 1023, 1072, 276, 277, 32766, 768, 771, 772, 783 | BLOCK_SOURCE_EVENT_WITH_UNKNOWN_LABEL | IHARQ-LABELMAPRECORD-20260806-587dcfff81307768 | 587dcfff813077685eaa34b9b204eae5791be7c5d25f2a500ddaff39b0348f84 | VALIDATED |
| Lee2019_MI | {"left_hand": "left_hand", "right_hand": "right_hand"} | NONE | BLOCK_SOURCE_EVENT_WITH_UNKNOWN_LABEL | IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c | b551cfd20335896c762d508e5950c8598772b7d4c75bec5d9ddee8e177bfe105 | VALIDATED |


Additional source-level exclusions include PhysioNet executed-movement/baseline runs outside MI runs 4/8/12, Lee2019 online/test/unlabeled runs, and BNCI technical/rejected/feet/tongue/ambiguous events. All excluded/unknown behavior remains traceable.

## 6.7 Split protocol and leakage contract

The final split is `P01-L1-SPLIT-OFFICIAL-R2`, canonical record `IHARQ-SPLITRECORD-20260806-e4e371d332c61e36`, semantic hash `e4e371d332c61e36699f07cb6bed6d0820e14b22d5685dc353d89c1de144c148`. The grouping unit is `(dataset_id, subject_id)`; subjects are atomic; source events/windows cannot cross roles. Ratios are train 0.60, calibration 0.20, validation 0.10, test 0.10 using deterministic SHA-256 ranking, largest remainder/minimum-one allocation and seed **20260804**.

| Dataset | Train subjects | Calibration subjects | Validation subjects | Test subjects | Train windows | Calibration windows | Validation windows | Test windows | Total windows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PhysioNetMI | 65 | 22 | 11 | 11 | 2949 | 979 | 495 | 495 | 4918 |
| BNCI2014_001 | 5 | 2 | 1 | 1 | 1440 | 576 | 288 | 288 | 2592 |
| Lee2019_MI | 32 | 11 | 5 | 6 | 3200 | 1100 | 500 | 600 | 5400 |

Global accepted core windows by role: train **7589**, calibration **2655**, validation **1283**, test **1383**. Leakage audit status: **PASS** for GROUP_DISJOINTNESS, DUPLICATE_SAMPLE, OVERLAP_GROUP, FIT_SCOPE, BUDGET_TEST_CONTAMINATION. Subject-role disjointness: **PASS**, with no intersections and no missing roles.

Fit/visibility rules: preprocessing has no learned fit requirement; future model fitting may use train; low-calibration subsets may use calibration only; validation is reserved for governed selection/checking as defined by downstream annexes; test is never visible to training, calibration, threshold selection or decision-time tuning.

## 6.8 Low-calibration budget contract

Registered budgets are **1, 2, 4, 8, 16, 32 source events per class**, calibration role only, seed **20260804**, nested deterministic SHA-256-ranked prefixes, exact class balance where feasible, and no test visibility. These are **infrastructure identities for future downstream evaluation**, not evidence that calibration experiments were executed in P01.

## 6.9 Preprocessing contract

Canonical PreprocessingRecord: `IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08`; semantic hash: `a11b59eeb3861a0801cd0540702dca2f0e96b9a55fe8d50d078ea2b3a48acb8c`. The accepted sequence is:

1. validate/normalize signal units to volts;
2. capture original source event indices/onsets before channel dropping/resampling;
3. select EEG signal channels and preserve deterministic ordering;
4. demean the continuous run;
5. apply average reference;
6. jointly resample signal and event samples to **160 Hz** with `mne.io.Raw.resample`, polyphase method, Kaiser beta **5.0**, reflect padding, `n_jobs=1`, and use the returned jointly resampled event array (independent float-time rounding prohibited);
7. apply 8–32 Hz fourth-order Butterworth SOS zero-phase filtering with `scipy.signal.sosfiltfilt`, odd padding, exact padlen **27**, minimum input samples **29**, effective forward/backward order 8;
8. cast signal output to **float32**.

Fit scope is `NOT_REQUIRED_FOR_OFFICIAL_LAYER1_PROFILE`; the generated fit-state artifact is a deterministic infrastructure/provenance surface, not held-out learned normalization. Any run violating units, event lineage, required filter length, shape or nonfinite rules fails/invalidates according to the quality/validation contracts.

## 6.10 Official core-window contract

The official core profile remains `P01-L1-WINDOW-OFFICIAL-R2`: MI cue onset +0.5 s to +3.5 s, 3.0 s duration, 160 Hz, start offset 80 samples, duration/stride 480 samples, exactly one official window per included source event, out-of-bounds **REJECT**, clipping **PROHIBITED**, parent-event overlap-group identity retained. Actual closure: **12,910 core windows / 12,910 accepted parent events, 0 invalid windows**. Signal dtype is float32.

The core profile was **not changed** by the A4 repairs.

## 6.11 Core numerical Dataset persistence

P01 uses dual persistence: compact governed records/manifests/pointers remain in the project bundle, while large lossless numerical tensors remain in a private Kaggle Dataset.

- artifact ID: `P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473`
- provider/handle: Kaggle / `csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473`
- logical immutable revision: **1**
- actual scientific provider Dataset version: **2**
- provider version 1: historical short-title shell only; provider version 2: verified scientific artifact
- manifest SHA-256: `dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1`
- format: lossless HDF5 subject shards; compression gzip-1; dtype float32
- shards: **172**; windows: **12910**
- logical float32 bytes: **1356625920** (1.263 GiB)
- actual uploaded HDF5 bytes: **1166652764** (1.087 GiB)
- local shard state: `SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD`
- creation/adoption: `ADOPTED_VERIFIED_EXISTING_DATASET`; scientific artifact recomputed = `False`; core HDF5 reuploaded = `False`.

This Protocol explicitly preserves the distinction between **logical immutable revision 1** and **Kaggle provider Dataset version 2** to avoid falsely representing the shell version as the scientific artifact.

## 6.12 Quality and validation contract

Quality profile: `P01-L1-QUALITY-OFFICIAL-R2`; policy: **ANNOTATE_NOT_REPAIR**. Hard-invalid rules include nonfinite data, incorrect tensor rank/shape, insufficient duration and missing source-event lineage. Soft diagnostics include flat/repeated signals, large voltage excursions and provider quality flags. Silent interpolation/repair is prohibited.

Observed quality closure: **489 quality summaries**, quality available for **489**, **20 soft/provider flags** represented by **20 ArtifactFlagRecords**, and **0 hard-invalid summaries**. Core invalid-window count is **0**. These are data-quality/protocol results, not decoder-performance claims.

## 6.13 A0-A13 readiness matrix

| Ablation | Official identity | Owner | Activated P01 | Scientifically executed P01 | P01 output | Downstream | Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A1 | Calibrated Decoder / Calibration Visibility | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A3 | Uncertainty and Selective Prediction | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A4 | Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls | DOWNSTREAM_AUTHORITY | False | False | A4 R2 external data substrate + registered views; Protocol synchronized here; downstream experiment still not executed in P01 | P02-P15 | READY_WITH_PROTOCOL_SYNC_REQUIRED |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A6 | IHARQ + Evidence-Quality Estimator | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A7 | IHARQ + RegimeRisk Temporal Trust | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A8 | Learning-to-defer / Deferral Comparison | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |
| A13 | Layer 9 Simulation-Only Embodiment Demo | DOWNSTREAM_AUTHORITY | False | False | Layer-1 matched-key/data foundation; no P01 effectiveness result | P02-P15 | FOUNDATION_READY |


All A0-A13 rows are **foundation/readiness** dispositions. No downstream ablation is reclassified as experimentally executed merely because L1 prepared matched keys/data.

## 6.14 A14 prohibition

`A14 = PROHIBITED / ABSENT`. Final machine evidence: selector present = false; run present = false; result present = false; claim present = false; audit status = PASS. Local identities such as A12.x remain subordinate/local and are not renamed A14.

## 6.15 A4 R2 Protocol synchronization — COMPLETE FOR FUTURE USE

The final P01 execution prepared an additive Layer-1 data substrate for A4 and explicitly marked it `DATA_READY_PROTOCOL_SYNC_REQUIRED`. This annex completes that **identity synchronization**, but does **not** convert A4 into a P01 effectiveness experiment.

Final future A4 profiles:

- family: `P01-L1-A4-WINDOW-FAMILY-FREEZE-R2`;
- longer matched profile: `A4_LONG_MATCHED_3P5S_R2`, cue +0.0 to +3.5 s, **560 samples at 160 Hz**;
- multi profile: `A4_MULTI_3X2S_UNIFORM_0P75S_R2`;
  - M1 `A4_MULTI_3X2S_M1_R2`: slice 0:320, +0.00..+2.00 s;
  - M2 `A4_MULTI_3X2S_M2_R2`: slice 120:440, +0.75..+2.75 s;
  - M3 `A4_MULTI_3X2S_M3_R2`: slice 240:560, +1.50..+3.50 s.
- one physical 560-sample tensor/event; the three 2 s members are registered immutable views; overlapping bytes are not duplicated;
- exact matched parent denominator: **12,910/12,910**; no clipping, padding or silent event drop;
- longer records: **12,910**; multi-member records: **38,730**; total A4 records: **51,640**; groups **12,910**; shards **172**;
- external handle: `csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108` provider version **1**, logical family revision **2**, manifest SHA-256 `29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305`; remote manifest verification **PASS**.

### A4 historical deviation and no-post-hoc boundary

The earlier proposed A4 R1 profile used cue +0.0..+4.0 s (640 samples). A universal denominator audit established that valid parent event `PhysioNetMI:104:0:8:event:24` has only 560 available samples after cue; 4.0 s would require **80 nonexistent samples**. Padding, clipping, fabricating or dropping the event would violate the matched-denominator contract. R2 therefore changed the **alternative A4 profile only** to +0.0..+3.5 s and uniformly registered 2 s subviews, retaining all 12,910 parents and the same +3.5 s endpoint as core.

This R1→R2 change occurred after feasibility evidence and is classified as `SCIENTIFIC_CONTRACT_CHANGE` for the **future A4 alternative profile**, not as a change to the official P01 core. It is **not described as preregistered** and P01 may not use it as retrospective confirmatory A4 effectiveness evidence. Future claim-bearing A4 execution must inherit the exact R2 identities frozen here and register the relevant downstream analysis/estimand before execution. `executed_in_p01 = false`.

## 6.16 Actual Kaggle environment

Actual accepted environment, not the original Build Book image intent:

- Python: **3.12.13**; platform `Linux-6.12.90+-x86_64-with-glibc2.35`; CPU count **4**; RAM **33659379712 bytes**; observed total disk **20957446144 bytes**; Stage-01 free disk **20336979968 bytes**;
- package versions exactly matched required execution pins: moabb=1.5.0, mne=1.12.1, numpy=2.2.6, scipy=1.15.3, pandas=2.3.1, scikit-learn=1.7.1, h5py=3.14.0, pooch=1.8.2, pyyaml=6.0.2, pydantic=2.11.7, jsonschema=4.25.0, nbformat=5.10.4; pin mismatches = **0**; required import failures = **0**;
- deterministic environment: `PYTHONHASHSEED=20260804`, OMP/MKL/OPENBLAS threads = 1;
- runtime environment amendment: `P01-L1-KAGGLE-ENV-FREEZE-R5`, compatibility/connection only; scientific values changed = none.

The earlier Build Book targeted Python >=3.11,<3.12/Kaggle image intent. The accepted run used 3.12.13 through an explicit compatibility successor. This is recorded rather than pretending the pre-run environment ran verbatim.

## 6.17 Adaptive-disk runtime amendment

Resource amendment: `P01-L1-KAGGLE-ADAPTIVE-DISK-R1`. Historical policy: minimum 60 GiB / recommended 90 GiB. Accepted runtime used an adaptive startup floor of **6.0 GiB**, calculated requirement approximately **3908544705 bytes**, observed free **18.94 GiB**, soft-warning 4.0 GiB, hard-emergency 1.5 GiB, export reserve 1.5 GiB. Read-only Kaggle inputs could not be deleted; automatic source removal was prohibited; only lawful reverified writable caches could be evicted. Scientific datasets/configs/split/labels/preprocessing/core windows were unchanged. Classification: `RESOURCE_POLICY_CHANGE`, non-scientific.

## 6.18 Executed notebook and stage matrix

The accepted stage identity is exactly **00-26 once each**. The final canonical Stage-26 state is PASS only after R54 external packaging repair; historical blocked/failure outputs are preserved separately.

| Stage | Purpose | Final status | Key outputs | Blockers | Disposition |
| --- | --- | --- | --- | --- | --- |
| 00 | Corrected bootstrap and persistent isolated worker | PASS | authority_manifest.json | 0 | FINAL_ACCEPTED |
| 01 | Environment | PASS | environment_manifest.json | 0 | FINAL_ACCEPTED |
| 02 | Project and input intake | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 03 | Authority and configuration | PASS | config_snapshot/official_run_freeze_manifest.json | 0 | FINAL_ACCEPTED |
| 04 | Phase 0 regression | PASS | reports/phase_01/tests/phase0_and_runtime_regression.json | 0 | FINAL_ACCEPTED |
| 05 | Source resolution | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 06 | Dataset registry | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 07 | Pass 1: verified source acquisition and bounded loading | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 08 | Metadata normalization | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 09 | Label mapping | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 10 | Preprocessing compilation | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 11 | Split construction and frozen fit population | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 12 | Low-calibration budgets | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 13 | Pass 2A: bounded preprocessing fit | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 14 | Adopt verified core and materialize matched A4 R2 | PASS | external_artifact_pointers/derived_windows_dataset.json, reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json | 0 | FINAL_ACCEPTED |
| 15 | Validate and commit the separate A4 R2 Dataset | PASS | external_artifact_pointers/derived_windows_dataset.json, external_artifact_pointers/a4_window_family_dataset.json | 0 | FINAL_ACCEPTED |
| 16 | Record validation | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 17 | Leakage audit | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 18 | A0–A13 readiness | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 19 | Cards | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 20 | Manifests | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 21 | Negative register | PASS | negative_and_failed_results/run_failures_and_blockers.json | 0 | FINAL_ACCEPTED |
| 22 | P02 and later compatibility | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 23 | Evidence sufficiency | PASS | reports/phase_01/preliminary_gate_evaluation.json | 0 | FINAL_ACCEPTED |
| 24 | Repair metadata | PASS | reports/phase_01/repair_reentry.json | 0 | FINAL_ACCEPTED |
| 25 | Final export preparation | PASS | No direct file / state transition | 0 | FINAL_ACCEPTED |
| 26 | Terminal decision and bundle export | PASS | /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip, /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip.sha256, /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_GitHub_Ready_Repository_d03f0a7c869d_20260807143013-663eab13.zip | 0 | FINAL_ACCEPTED |


The execution notebook source also contains material failed/recovery cells outside the 00-26 stage identity. They are historical evidence, not extra scientific stages.

## 6.19 Failure, repair, rerun and supersession ledger

| Repair | Affected stage | Class | Defect | Owner | Science changed | Data changed | Core changed | Rerun scope | Final resolution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R45 / SAME-SESSION CORE-ADOPTION NORMALIZATION | 14 | CANONICALIZATION_FIX | Existing verified core adoption blocked because date-bearing upstream record IDs changed dependent semantic hashes despite otherwise equivalent scientific records. | Implementation/Registry integration | False | False | False | fresh worker/bundle plus affected adoption path; preserved persistent checkpoints | Dependency-order full-record equivalence with exact upstream-ID mapping plus exact remote manifest hash; core Dataset not mutated/reuploaded. |
| R46 | runtime overlay | IMPLEMENTATION_BUG_FIX | Missing datetime/timezone runtime imports. | Implementation Build Book/code | False | False | False | affected runtime path only | Required imports added. |
| R47 | A4 profile canonicalization | CANONICALIZATION_FIX | Float literals in hash-bearing A4 profile could cause governed representation drift. | Registry/implementation canonicalization | False | False | False | profile serialization/validation only | Governed decimal strings used for hash-bearing seconds fields. |
| R48 | 14-15 A4 materialization/persistence | IMPLEMENTATION_BUG_FIX + PERSISTENCE_FIX | A4 child interface/set handling and storage identity/read verification gaps; resumability and exact remote manifest closure hardened. | Implementation/Nuts-and-Bolts | False | False | False | A4 child/interface and persistence path | Child interface corrected; reader/storage identity closure, synthetic E2E, resumable subject checkpoints and remote manifest verification added. |
| R49 / P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 | 14-15 A4 profile | SCIENTIFIC_CONTRACT_CHANGE (A4 ALTERNATIVE ONLY) | Original proposed A4 +0.0..+4.0 s window is impossible for one valid released parent event (PhysioNetMI:104:0:8:event:24) without 80 nonexistent samples. | Protocol/Method/Nuts-and-Bolts/Implementation for A4 alternative profile | True | True | False | A4 materialization path with exact 12,910 matched parent events | R2 freezes +0.0..+3.5 s 560-sample tensor and three registered 2 s slices; no drop/pad/clip; confirmatory use prohibited until Protocol sync and downstream execution. |
| R50 | 07 | INTEGRATION_FIX | Stale local DISPLAY_REVISION guard expected R42 while live runtime was R49; Stage 07 had not yet been submitted. | Notebook integration | False | False | False | submit Stage 07 once using live worker; no 00-06 replay | Revision guard corrected; Stage 07 PASS. |
| R51-R53 / P01-L1-R53-STAGE18-WORKER-ENV-IMPORT-PROBE-R1 | 18 | INTEGRATION_FIX | A4 readiness wrapper imported write_json from nonexistent module; two recovery-cell validation mistakes then occurred (malformed shim newline and notebook-kernel import probe outside worker PYTHONPATH). | Notebook/runtime integration | False | False | False | Stage 18 only after worker-environment import probe | Compatibility shim re-exported authoritative manifests.write_json and was probed under exact worker_env; Stage 18 PASS and readiness artifact verified. |
| P01-L1-R54-FINAL-EXPORT-SECRET-REDACTION-R1 | 26 external release closure | SECURITY/PACKAGING_FIX | Live Kaggle credential was serialized into environment_amendment and the secret scanner correctly blocked the contaminated export. | Packaging/security | False | False | False | redaction/repack/final integrity only; original worker Stage 26 not duplicated | Secret-like environment values redacted; final bundle/repository rebuilt; exact-token scan, manifests and checksums PASS; contaminated failed release is non-authoritative. |


Minor tracebacks subsumed by a governed episode are not promoted to independent scientific revisions; the material lineage remains reconstructible from notebook outputs and preserved runtime repair files.

## 6.20 Scientific versus non-scientific amendment classification

| Repair | Classification | Estimand/profile science changed | Data changed | Core changed | Denominator changed | Rerun/repair needed | Resolution |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R45 / SAME-SESSION CORE-ADOPTION NORMALIZATION | CANONICALIZATION_FIX | False | False | False | False | YES | Dependency-order full-record equivalence with exact upstream-ID mapping plus exact remote manifest hash; core Dataset not mutated/reuploaded. |
| R46 | IMPLEMENTATION_BUG_FIX | False | False | False | False | YES | Required imports added. |
| R47 | CANONICALIZATION_FIX | False | False | False | False | YES | Governed decimal strings used for hash-bearing seconds fields. |
| R48 | IMPLEMENTATION_BUG_FIX + PERSISTENCE_FIX | False | False | False | False | YES | Child interface corrected; reader/storage identity closure, synthetic E2E, resumable subject checkpoints and remote manifest verification added. |
| R49 / P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 | SCIENTIFIC_CONTRACT_CHANGE (A4 ALTERNATIVE ONLY) | True | True | False | False | YES | R2 freezes +0.0..+3.5 s 560-sample tensor and three registered 2 s slices; no drop/pad/clip; confirmatory use prohibited until Protocol sync and downstream execution. |
| R50 | INTEGRATION_FIX | False | False | False | False | YES | Revision guard corrected; Stage 07 PASS. |
| R51-R53 / P01-L1-R53-STAGE18-WORKER-ENV-IMPORT-PROBE-R1 | INTEGRATION_FIX | False | False | False | False | YES | Compatibility shim re-exported authoritative manifests.write_json and was probed under exact worker_env; Stage 18 PASS and readiness artifact verified. |
| P01-L1-R54-FINAL-EXPORT-SECRET-REDACTION-R1 | SECURITY/PACKAGING_FIX | False | False | False | False | YES | Secret-like environment values redacted; final bundle/repository rebuilt; exact-token scan, manifests and checksums PASS; contaminated failed release is non-authoritative. |


Only the A4 R1→R2 alternative profile is a scientific-contract/profile change; it neither changes the official core nor supplies an effectiveness result. All other listed repairs are execution/integration/canonicalization/persistence/security fixes with no scientific estimand, split, label, preprocessing, core-window or metric change.

## 6.21 Security/release repair history

During original Stage 26 packaging, a live Kaggle credential was inadvertently serialized into an environment artifact. The secret scanner correctly blocked the contaminated export. R54 (`P01-L1-R54-FINAL-EXPORT-SECRET-REDACTION-R1`) redacted secret-like environment values, rebuilt final packaging/integrity surfaces, and produced PASS for manifest verification, checksum verification and exact-token scanning. The secret value is **not reproduced anywhere in this Protocol package**. Science, data, split, labels, preprocessing and results were unchanged. The contaminated failed release is non-authoritative; only the R54-corrected package is accepted.

## 6.22 Gate and validation closure

| Gate | Purpose | Repair owner | Status | Failure codes | Evidence | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| P01-G01 | authority_phase0_intake | GOVERNANCE_AND_PHASE0 | PASS | 0 | manifests/phase_01/test_manifest.json; authority_manifest.json | NONBLOCKING/PASS |
| P01-G02 | source_provenance_license | METHOD_SELECTION_AND_OWNER | PASS | 0 | reports/phase_01/sources/source_version_license_report.json; inputs/source_inventory.json | NONBLOCKING/PASS |
| P01-G03 | schema_canonical_object | REGISTRY | PASS | 0 | reports/phase_01/validation/; records/ | NONBLOCKING/PASS |
| P01-G04 | metadata_completeness | L1_METADATA | PASS | 0 | reports/phase_01/metadata/metadata_completeness.json | NONBLOCKING/PASS |
| P01-G05 | label_mapping | L1_LABELS | PASS | 0 | reports/phase_01/labels/label_map_validation.json; records/labels/ | NONBLOCKING/PASS |
| P01-G06 | preprocessing_fit_scope | PROTOCOL_AND_L1_PREPROCESSING | PASS | 0 | reports/phase_01/preprocessing/fit_scope.json; records/preprocessing/ | NONBLOCKING/PASS |
| P01-G07 | split_disjointness | PROTOCOL_AND_L1_SPLITS | PASS | 0 | reports/phase_01/splits/disjointness.json; records/splits/ | NONBLOCKING/PASS |
| P01-G08 | leakage_chronology | PROTOCOL_AND_L1_LEAKAGE | PASS | 0 | reports/phase_01/leakage/leakage_contamination.json | NONBLOCKING/PASS |
| P01-G09 | low_calibration_budgets | PROTOCOL_AND_L1_BUDGETS | PASS | 0 | reports/phase_01/splits/low_calibration_budgets.csv | NONBLOCKING/PASS |
| P01-G10 | window_identity | L1_WINDOWS | PASS | 0 | reports/phase_01/windows/window_timing_overlap.json; records/windows/ | NONBLOCKING/PASS |
| P01-G11 | quality_coverage | L1_QUALITY | PASS | 0 | reports/phase_01/quality/quality_coverage.json; records/quality/ | NONBLOCKING/PASS |
| P01-G12 | matched_keys_ablation_readiness | PROTOCOL_AND_L1_READINESS | PASS | 0 | manifests/phase_01/layer1_ablation_readiness_l1_v1.json; reports/phase_01/readiness/matched_key_completeness.csv | NONBLOCKING/PASS |
| P01-G13 | cards_limitations | L0_BOUNDARY_AND_L1_CARDS | PASS | 0 | docs/cards/datasets/; docs/cards/protocols/ | NONBLOCKING/PASS |
| P01-G14 | manifest_path_hash_closure | BUILD_BOOK_AND_L1_MANIFESTS | PASS | 0 | manifests/phase_01/execution_bundle_manifest.json; checksums.sha256 | NONBLOCKING/PASS |
| P01-G15 | phase2_compatibility | BUILD_BOOK_AND_P02_CONSUMER | PASS | 0 | phase2_handoff/phase_01_to_phase_02.yaml | NONBLOCKING/PASS |
| P01-G16 | complete_artifact_closure | EXECUTION_PLAN_AND_L1_BUNDLE | PASS | 0 | manifests/phase_01/layer1_manifest.json; phase_execution_handoff.yaml | NONBLOCKING/PASS |


Additional closure: test suite **50 passed / 0 failed**; schema/canonical-record validation PASS; subject split disjointness PASS; leakage checks PASS; window timing/denominator closure PASS; external core and A4 manifest verification PASS; execution-bundle `checksums.sha256` independently reverified for **13,164/13,164 entries with 0 missing and 0 mismatches**; unresolved blocker count **0**.

## 6.23 Negative, failed, invalid and diagnostic evidence

P01 preserves distinct classes: historical failed attempts, superseded implementation defects, valid negative/diagnostic observations, invalid data items, and current blockers. The final accepted core contains **0 invalid windows**; quality contains 20 recorded soft/provider flags and 0 hard-invalid summaries. Material Stage 07/18/26 failures and repair evidence remain preserved. Current unresolved blockers: **0**. Failure history is not deleted or converted into success evidence.

## 6.24 Evidence status and claim ceiling

P01 can support factual/protocol claims about: source provenance and checksum closure; reproducible intake; exact labels/exclusions; subject-grouped split; preprocessing/window implementation; validated canonical data products; 12,910-window denominator conservation; quality/lineage/integrity; external persistence; A0-A13 foundation readiness; A14 absence; and downstream technical readiness.

P01 **cannot by itself support** decoder superiority, calibration effectiveness, clinical effectiveness, deployment safety, real-world control, downstream A4 effectiveness, policy-learning benefit, temporal-trust benefit, stress robustness or embodiment claims. Mandatory inherited limitations include `PUBLIC_EEG_ONLY`, `NON_CLINICAL`, `NO_DEPLOYMENT_CLAIM`. Layer 0 later controls claim wording/disposition.

## 6.25 External artifact registry

| Artifact | Provider/handle | Provider rev | Logical rev | Format/access | Size/count | SHA-256 identity | Producer/consumers | Local-copy state/retrieval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473 | 2 | 1 | LOSSLESS_HDF5_SUBJECT_SHARDS / PRIVATE | 172 shards; 12910 windows; 1166652764 bytes | dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1 | P01 / P02-P15 | SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD; Attach the private Kaggle Dataset at immutable version 1; load IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl (or an ordinal-prefixed suffix match); resolve the shard filename; read the declared HDF5 group and row. |
| P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108 | 1 | 2 | LOSSLESS_HDF5_MATCHED_3P5S_SUBJECT_SHARDS_WITH_REGISTERED_VIRTUAL_MULTIWINDOW_VIEWS / PRIVATE | 172 shards; 12910 materialized events; 51640 records; 1357362334 bytes | 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305 | P01 / P02 A4 and later governed consumers | A4_SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD; attach exact provider version and verify manifest SHA before use |


A handle without exact revision and checksum is insufficient for governed consumption.

## 6.26 Phase 2 handoff constraints

P02 may consume the verified core pointer, exact split/label/preprocessing/window identities, config ID and limitation tags. A4 may be consumed only under the exact R2 family/profile identities synchronized here and with a downstream Protocol/analysis cell that distinguishes it from core. Required matching keys include dataset, subject, session/run, parent event/window/group, split role, preprocessing, label map, config and profile identity as applicable. P02 may not silently rewindow, relabel, change split membership, expose test data during fitting/selection, or reinterpret Layer-1 contracts. Any such change requires a governed amendment and descendant invalidation/rerun analysis.

## 6.27 Limitations

Supported limitations only:

- project-wide: public benchmark/research evidence is not clinical or deployment validation; downstream claims remain bounded by owner layers and Layer 0;
- P01: selected public EEG portfolio and binary MI branch only; excluded source events remain out of the supervised denominator; source-specific licensing/redistribution restrictions apply;
- environment: accepted execution is tied to the recorded Kaggle/Python/package/runtime-amendment identities;
- external access: core and A4 numerical HDF5 Datasets are private Kaggle artifacts and require access plus exact revision/hash verification;
- evidence ceiling: no decoder/calibration/policy/robustness/embodiment effectiveness result was generated by P01;
- A4: R2 profile emerged from feasibility repair, is synchronized prospectively for future use, and is not retrospective confirmatory evidence;
- security: the superseded contaminated Stage-26 release is non-authoritative; credential rotation was recommended.

## 6.28 Freeze decision

**P01_PROTOCOL_V1_ANNEX_R1_FROZEN_WITH_EXPLICIT_EXECUTION_AMENDMENTS_AND_A4_R2_FUTURE_CONFIRMATORY_SYNC**

- current execution status: **ACCEPTED**;
- Protocol annex status: **FROZEN**;
- unresolved blockers: **0**;
- nonblocking limitations: `PUBLIC_EEG_ONLY`, `NON_CLINICAL`, `NO_DEPLOYMENT_CLAIM`, private external Dataset access, recorded runtime amendments, A4 retrospective-history limitation;
- A4 R2 identity synchronization: **COMPLETE** for future downstream contract use; downstream A4 effectiveness execution: **NOT PERFORMED IN P01**;
- additional P01 Kaggle execution required: **NO**;
- next lawful output: Phase 1 Evidence, Results, and Interpretation Report using this annex plus `analysis_contract.yaml` and the accepted execution bundle;
- P02 technical handoff: **READY**, subject to completion of the documentary closure chain required by Governance V6.1 before formal phase transition.

---
