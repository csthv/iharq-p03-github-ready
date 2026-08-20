---
title: "IHARQ Experiment, Ablation, Evaluation, Execution, and Analysis Protocol v1.0 — Phase 02 / Layer 2 Annex"
document_id: "IHARQ-PROTOCOL-V1-P02-ANNEX-R2"
version: "1.0-P02-R2"
status: "FROZEN_WITH_EXPLICIT_SCIENTIFIC_RUNTIME_AMENDMENTS_RESOURCE_CONSTRAINED_A4_POST_HOC_SENSITIVITY_AND_DUAL_HF_HANDOFF"
phase_id: "P02"
primary_layer: "L2"
primary_layer_name: "Decoder and Baseline Measurement Spine"
parent_cumulative_protocol: "IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1"
future_merge_target: "SAME_CUMULATIVE_PROTOCOL_AUTHORITY"
generation_timestamp: "2026-08-14T18:20:00+03:30"
execution_status: "ACCEPTED_FOR_PROTOCOL_AND_PHASE_ANALYSIS"
evidence_status: "SUFFICIENT_FOR_PROTOCOL_AND_PHASE_REPORT_WITH_EXPLICIT_RESOURCE_CONSTRAINED_A4_LIMITS"
---

# IHARQ BenchGuard Stretch C
# Experiment, Ablation, Evaluation, Execution, and Analysis Protocol v1.0
## Phase 02 / Layer 2 — Decoder and Baseline Measurement Spine — Standalone Annex R2

**Protocol annex authority:** `IHARQ-PROTOCOL-V1-P02-ANNEX-R2`  
**Parent Protocol:** `IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1`  
**Phase / primary layer:** `P02 / L2`  
**Accepted run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`  
**Evidence decision:** **SUFFICIENT**, with explicit A4 scope limitations  
**Current blockers:** **0**  

> **Standalone-now / cumulative-later rule.** This file is the canonical Phase 02 annex for the present task. It deliberately does not rewrite or merge the existing cumulative P00–P01 Protocol. When the cumulative Protocol is next consolidated, this annex is designed to be inserted after the P01 annex as the Phase 02 execution-and-analysis record, with only global de-duplication and index updates; its scientific history, deviation classifications, exact run identities, and limitations must not be semantically rewritten.

> **Actual-history rule.** Protocol v1.0 is post-execution truth. The P02 Build Book is the pre-execution implementation authority; the accepted execution bundle is the authority for what actually ran. Stage 11 and Stage 12 author-informed successors, the Stage 18 resource-constrained A4 deviation, Stage 18S post-hoc sensitivity supplement, and Stage 24 release repairs are therefore recorded as historical amendments/deviations/supplements rather than retroactively described as original pre-registration.

---

# PART III-A — PHASE 02 PROTOCOL ANNEX

## 7.1 Document control

| Field | Frozen / actual value |
| --- | --- |
| annex_id | `IHARQ-PROTOCOL-V1-P02-ANNEX-R2` |
| supersedes | `IHARQ-PROTOCOL-V1-P02-ANNEX-R1` for documentary/machine-readable corrections only; no scientific result changed |
| parent cumulative Protocol | `IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1` |
| future merge behavior | extend the same cumulative Protocol authority; no competing master |
| phase_id | `P02` |
| official phase role | Baseline decoders / decoder measurement spine |
| primary layer | `L2 — Decoder and Baseline Measurement Spine` |
| version | `1.0-P02-R2` |
| status | `FROZEN_WITH_EXPLICIT_SCIENTIFIC_RUNTIME_AMENDMENTS_RESOURCE_CONSTRAINED_A4_POST_HOC_SENSITIVITY_DUAL_HF_HANDOFF_AND_AUDIT_CLOSURE` |
| accepted run_id | `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d` |
| run configuration SHA-256 | `9e181d2e935d2e9674ca6e05572f49520ad0306a3761362b770f8bee8c78ce13` |
| scientific freeze | `P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5` |
| scientific freeze SHA-256 | `7449216c988eec14191ba85300d720547f06fbc6ac7020e9e142bf12a4b0a598` |
| notebook logical identity | `IHARQ-P02-COMPLETE-EXECUTION-AND-ANALYSIS-R4` |
| runtime-revision `source_sha256` fingerprint | `a54bfa816acc6763c1d1042b8c65cf54ae04ec774c57ec50de86014a6730c5fa` |
| runtime-revision config SHA-256 | `d82334535e397c681d6172694da96d3fff0143ffb1b63a18876ee1f7778f60a1` |
| stage-plan SHA-256 | `043eb30e008af910d37c563e8be8c719ef881cf009aec3e34687dc97bdc34aad` |
| owner-supplied final post-restart continuation notebook SHA-256 | `498b837ffaabc945160cd2b8482528c17ed85e978501119a19c88073d72b543a` |
| packaged implementation notebook SHA-256 | `4c36e340721156de2f58e03b1568f7b1072db3d31145aaba566b283305e7fecf` |
| G23 evidence sufficiency | PASS; `missing=[]` |
| G24 bundle/finalization gate | PASS; blockers `[]` |
| unresolved blockers | 0 |
| execution status | `ACCEPTED_FOR_PROTOCOL_AND_PHASE_ANALYSIS` |
| evidence status | `SUFFICIENT_FOR_PROTOCOL_AND_PHASE_REPORT_WITH_EXPLICIT_RESOURCE_CONSTRAINED_A4_LIMITS` |
| canonical human-readable artifact | this Markdown file |
| presentation derivatives | DOCX and PDF generated from this canonical R2 source |
| machine-readable companions | `P02_run_matrix.yaml`, `P02_analysis_contract.yaml`, `P02_external_artifact_access_contract.yaml` |

### 7.1.1 Hash and notebook-identity nomenclature guard

The accepted P02 state exposes several distinct identities. They are **not interchangeable**:

- `run_config_hash = 9e181d2e935d2e9674ca6e05572f49520ad0306a3761362b770f8bee8c78ce13` identifies the accepted scientific/runtime run configuration exposed by Stage 06 and the Protocol handoff;
- `scientific_freeze_sha256 = 7449216c988eec14191ba85300d720547f06fbc6ac7020e9e142bf12a4b0a598` identifies the frozen pre-execution scientific plan state;
- `runtime_revision_config_sha256 = d82334535e397c681d6172694da96d3fff0143ffb1b63a18876ee1f7778f60a1` is the serialized runtime/config revision fingerprint carried by the stage ledger;
- `runtime_revision_source_sha256 = a54bfa816acc6763c1d1042b8c65cf54ae04ec774c57ec50de86014a6730c5fa` is the stage-ledger **runtime-revision source fingerprint field**. It is retained exactly as recorded, but R2 no longer labels it as the physical SHA-256 of the owner-supplied notebook file;
- `stage_plan_sha256 = 043eb30e008af910d37c563e8be8c719ef881cf009aec3e34687dc97bdc34aad` identifies the executed stage-plan revision;
- the owner-supplied `notebook110a2128e2 (18).ipynb` is the final **post-restart continuation notebook**, SHA-256 `498b837ffaabc945160cd2b8482528c17ed85e978501119a19c88073d72b543a`; its executed cells intentionally begin from the survived canonical Stage-18 state and continue through Stage18S/18U/19–24 rather than replaying Stages 00–18;
- the packaged implementation notebook `IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb` has physical SHA-256 `4c36e340721156de2f58e03b1568f7b1072db3d31145aaba566b283305e7fecf` and represents the integrated implementation notebook source distributed in the cumulative project state.

The runtime stage ledger, accepted stage artifacts, and post-restart continuation together reconstruct the actual execution history. No single physical notebook SHA is substituted for a different fingerprint class.

## 7.2 Phase declaration, Layer 2 role, record surface, and claim boundary

Phase 02 converts the frozen P01 public-data, split, preprocessing, label, and window substrate into the project's first governed **decoder and baseline measurement spine**. Layer 2 is a measurement layer: it trains/qualifies plural decoder families, records native prediction/score evidence, measures raw accept-all performance, constructs low-label and participant/session evidence, executes ordinary A4 longer/multi-window/ensemble controls, preserves model/run provenance and failures, and emits a fail-closed downstream readiness handoff.

The Architecture fixes eight official Layer-2 modules: **Baseline trainer; Prediction logger; Low-calibration curve builder; Subject difficulty profiler; Model-family registry; Ensemble comparison builder; Compact SSL adapter; Downstream readiness validator.** P02 executed or dispositioned each of these responsibilities through its stage/record/handoff surfaces.

Layer 2 does **not** own calibration, uncertainty estimation, thresholding, abstention, selective prediction, readiness policy, clinical interpretation, deployment safety, temporal trust, stress robustness, closed-loop simulation, or embodiment claims. Those remain downstream responsibilities. P02 supplies the prediction substrate and baseline evidence against which later layers operate; it does not convert decoder performance into a safety or deployment decision.

The Registry-backed P02 record surface includes `PredictionRecord`, `ModelRegistryRecord`, `BaselineMetricRecord`, `LowCalibrationCurveRecord`, `SubjectProfileRecord`, `EnsembleControlRecord`, `FailureCaseIndex`, `Layer2ReadinessReport`, `NegativeResultNote`, and `DiagnosticOnlyFlag`, with owner-routed `LeakageWarningRecord` and `MatchedComparisonReport` where applicable. The accepted runtime contains record partitions/instances for the relevant P02 families and preserves prediction partitions separately through the prediction manifest surface.

Status axes remain separate: method role, run terminal state, record validation state, lifecycle state, consumer-readiness state, diagnostic/negative-evidence classification, and claim limitation are not collapsed into one generic “success” label.

## 7.3 Authority intake and source-utilization reconciliation

R2 was produced only after a source-complete audit of the supplied project state. Governance, all seven authorities, the P00/P01 project state and cumulative documentary products, the P02 Build Book/implementation package, the owner-supplied final continuation notebook, the accepted P02 cumulative execution state, and the R1 Protocol package were independently inventoried and reconciled. Archive duplicates/cumulative copies were dispositioned as duplicate evidence rather than counted as independent scientific results.

| Source authority / evidence surface | Protocol use |
| --- | --- |
| Governance V6.1 | workflow, Protocol-after-execution role, no-post-hoc rewriting, evidence sufficiency/repair loop, external-pointer requirements |
| Architecture | Layer 2 purpose, eight-module scope, interfaces and downstream boundaries |
| Canonical Registry R44 | record/status/identity/interface vocabulary and lifecycle rules |
| Execution & Evidence Plan | P02 required outputs/evidence/gates/handoffs and closure criteria |
| Protocol v0.1 R42 | exact A0–A13 identities, A14 prohibition, fairness/leakage/matching/statistical discipline |
| Phase Execution Playbook R41 | operational phase ordering, validation and closure behavior |
| Method Selection R2 | selected datasets/model/method/platform families and rationale |
| Nuts-and-Bolts R2 | accepted Layer-2 internals, matching, metrics, fail-closed behavior and interfaces |
| P00/P01 state + cumulative Protocol | inherited scientific identities and cross-phase documentary precedent |
| P02 Build Book R4 | pre-execution P02 implementation/run intent and the 89-row responsibility traceability matrix |
| P02 runtime/notebook/evidence | actual execution, amendments, successors, terminal states, gates, analysis inputs and release history |
| R1 Protocol package | documentary target audited line-by-line and superseded by R2 where corrections were required |

### 7.3.1 Supplied top-level source snapshot identities

| Source | File / package | SHA-256 |
| --- | --- | --- |
| Governance V6.1 | `00_IHARQ_Document_Stack_Governance_and_Creation_Guide_V6_1_Single_Track_Full_Depth_Consolidated_Notebook(8).md` | `c811373c19a7c2c3f6d72cf2aed984e02ffcb07bb448cfc3bdbdf26a35a4f1d9` |
| Seven-authority package | `IHARQ_Clean_Final_Seven_Documents_Layers0_to_10_R1_20260801_COMPLETE(20260814-122103).zip` | `beb00f47e4a790242d62405dcca799647d849c8dc2ff043c5196cee372607128` |
| Phase 00 final whole-stack package | `IHARQ_Phase_0_Final_Whole_Stack_Advanced_Internal_Repository_COMPLETE_R1(5).zip` | `2c554eb57602bb8286338a682ff4172a6768480e126edbee9b35077603277bf7` |
| P01 final download package | `IHARQ_FINAL_DOWNLOAD_PACKAGE.zip` | `9226cb780710b7e7b84b35ea960a98a0c08c4a67288281fb36a7a9f63b9abc72` |
| P01 executed notebook | `Phase_01_Notebook(2).ipynb` | `54b84d9cd29eb57bb22f45b7b7251e76e4947863c832528dba9c51b96189b023` |
| Prior cumulative Protocol through P01 | `IHARQ_Protocol_v1_0_Final_Through_Phase_01(3).zip` | `fef708febf6b0cad18b6c3e82767c31b27da4794587432ace799c3995b9075eb` |
| Cumulative Phase Analysis through P01 | `IHARQ_Cumulative_Phase_Analysis_Through_P01_Final(3).zip` | `bb0cdaffe9ea813611e731e7ae907f419a2b7a90b198bb44151aa5adc9162227` |
| Layer-0-embedded Phase Analysis through P01 | `IHARQ_Cumulative_Phase_Analysis_Embedded_Layer0_Through_P01_Final(3).zip` | `2c95e96d961d820a3cb0db1661f315498c825eb59f849b0756fba90892e29eda` |
| Cumulative Evidence Map through P01 | `IHARQ_Cumulative_Evidence_Map_Through_P01_Final(2).zip` | `f5d435a4429fb0a376cca6958c66924208cea0a4fbbd09c281e6aa3c173221aa` |
| Cumulative Layer 10 through P01 | `IHARQ_Cumulative_Layer10_Through_P01_Final(2).zip` | `02377e2e67ea553efe6bb3e43b95c9351d32b3efe5283674807b47549f65f632` |
| Cumulative GitHub-ready through P01 | `IHARQ_Cumulative_GitHub_Ready_Through_P01_R1(20260814-123111).zip` | `dc2708ab70e7746499ae09760456825b54efcf587cae3db3410e6f72b0024542` |
| P02 Build Book package R4 | `IHARQ_P02_L2_Implementation_Build_Book_Package_R4(20260814-123109).zip` | `2d19167370b70772fe9533e627f85ef83f1e1b68ae33f878955eef1348c9f31e` |
| Owner-supplied final P02 continuation notebook | `notebook110a2128e2 (18).ipynb` | `498b837ffaabc945160cd2b8482528c17ed85e978501119a19c88073d72b543a` |
| P02 cumulative GitHub-ready execution state | `IHARQ_Cumulative_GitHub_Ready_Through_P02_Stage24Replay_R1.zip` | `4e779859fc5ab2c07cb1cdb079f1e9d08cfe41641142d51e093f6c3936bfec81` |
| Protocol package under audit | `IHARQ_Protocol_v1_0_Phase_02_Layer_02_Final_R1.zip` | `7bab07e7f662182ea5681366e0d8a5bf8c245aae0edec31c7036832007350575` |

The final execution evidence controls over stale planning text when the Build Book and actual runtime differ, within authority ownership. Earlier failed/superseded attempts remain provenance evidence. The complete source-coverage ledger and archive/parse validation are carried in `audit/` and `validation/`.

## 7.4 Prior-state inheritance from P00/P01

P02 inherits without mutation the project authority stack, canonical hashing/lineage infrastructure, A0–A13 ladder, no-A14 lock, and the P01 scientific data substrate. Specifically, the accepted P01 handoff fixes:

- datasets: `PhysioNetMI`, `BNCI2014_001`, `Lee2019_MI`;
- binary task: `left_hand` versus `right_hand`, with source-specific non-target events excluded rather than relabeled;
- split: `P01-L1-SPLIT-OFFICIAL-R2`, grouped by dataset/subject and preserving train/calibration/validation/test roles;
- core window: `P01-L1-WINDOW-OFFICIAL-R2`, `+0.5..+3.5 s`, 3.0 s, 480 samples at 160 Hz;
- 12,910 governed core windows;
- low-label profile: `P01-L1-LOW-CAL-OFFICIAL-R2`, exact inherited per-class subsets at 1/2/4/8/16/32, seed `20260804`, with no new membership generation;
- A4 family: `P01-L1-A4-WINDOW-FAMILY-FREEZE-R2`, long profile `A4_LONG_MATCHED_3P5S_R2` and three virtual views `[0:320, 120:440, 240:560]`, with 12,910/12,910 matched parents;
- inherited limitations: public benchmark/research scope, non-clinical evidence, and no deployment claim.

P02 may train new models and generate new Layer 2 records, but it may not silently relabel, resplit, rewindow, alter P01 membership, or use test data for model/hyperparameter/policy selection.

## 7.5 Pre-run scientific freeze and actual change boundary

The controlling scientific freeze was `P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5` with SHA-256 `7449216c988eec14191ba85300d720547f06fbc6ac7020e9e142bf12a4b0a598`. It froze A0 and A4 as the two P02 full-execution ablations; prohibited result-dependent additional-ablation unlock; declared A1–A3 and A5–A13 as downstream confirmatory execution; and retained A14 as absent/prohibited.

The initial freeze also fixed the principal metric/statistical framework, seed derivation, low-label membership, candidate caps, and model-family implementation plan. A separate owner-authorized pre-test amendment, `P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2`, resolved the EEGNet segmentation/reconstruction diagnostic challenger and class-weight policy before test evaluation.

The accepted runtime later contains additional **post-observation scientific amendments** at Stages 11 and 12 and one **resource-constrained A4 protocol deviation** at Stage 18. The Protocol does not backdate those changes. Each is classified below with its trigger, changed surface, unchanged fairness boundaries, superseded evidence, and claim consequence.

## 7.6 Actual inherited source data, task, split, preprocessing, windows, and evaluation roles

P02 reused the validated P01 scientific substrate **without mutation**. The inherited source identities below are therefore part of the P02 Protocol because P02 model evidence is conditional on them.

### 7.6.1 Dataset identities

| Dataset | Release/source | License/source terms recorded by P01 | Access route | Observed aggregate SHA-256 | Subjects | P01 accepted core windows T/C/V/Test | DatasetRecord / semantic hash |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| PhysioNetMI | release 1.0.0 | ODC-By-1.0 | `MOABB_1_5_0_OFFICIAL_PHYSIONET_DOWNLOAD` | `28cd2062983b6236f9a0e7fdee91fc9d8d5aad8eee3ef561cff5828ae89bf2ba` | 109 | 2949 / 979 / 495 / 495 | `IHARQ-DATASETRECORD-20260806-66309cda68771bef` / `66309cda68771bef9bd7a3aebdac819d91201cedca79ab112ea993fb61f558cf` |
| BNCI2014_001 | provider file set A01T/A01E…A09T/A09E | CC BY-ND 4.0 | `MOABB_1_5_0_OFFICIAL_BNCI_DOWNLOAD` | `04a5390f8f36eaadbc0c480ec9377ce1b99caf0b7ab53bad9fda12347995bc49` | 9 | 1440 / 576 / 288 / 288 | `IHARQ-DATASETRECORD-20260806-42c424800627b6ee` / `42c424800627b6ee0be7f47ad602ba49cf4c24a632c1fa69c8c750a4ba77e163` |
| Lee2019_MI | GigaDB DOI 10.5524/100542; MOABB 1.5.0 wrapper; labeled offline/train MI | GPLv3 as recorded by maintained P01 source card; source terms retained | `MOABB_1_5_0_OFFICIAL_GIGADB_DOWNLOAD` | `3a07b2f302da949efd418a0712d5a9427df34dcb8b027ca553fae8e67a849f78` | 54 | 3200 / 1100 / 500 / 600 | `IHARQ-DATASETRECORD-20260806-adb91f25a65e588e` / `adb91f25a65e588ece06884a9598cc92bd932e91c4babc3cacb98c82901596f1` |

Task/labels remain binary `left_hand` versus `right_hand`. PhysioNet MI uses run-context T1/T2 for runs 4/8/12 with T0 excluded; BNCI maps 769/770 and excludes feet/tongue/technical/non-target events; Lee uses left/right and excludes non-supervised source runs. Unknown source events fail closed rather than being relabeled as negative.

### 7.6.2 Split identity and denominators

Split profile: `P01-L1-SPLIT-OFFICIAL-R2`; canonical SplitRecord `IHARQ-SPLITRECORD-20260806-e4e371d332c61e36`; semantic hash `e4e371d332c61e36699f07cb6bed6d0820e14b22d5685dc353d89c1de144c148`. Grouping unit is `(dataset_id, subject_id)` with atomic subjects, deterministic SHA-256 ranking, 60/20/10/10 train/calibration/validation/test allocation and seed `20260804`.

| Dataset | Train subj | Cal subj | Val subj | Test subj | Train windows | Cal windows | Val windows | Test windows |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| PhysioNetMI | 65 | 22 | 11 | 11 | 2949 | 979 | 495 | 495 |
| BNCI2014_001 | 5 | 2 | 1 | 1 | 1440 | 576 | 288 | 288 |
| Lee2019_MI | 32 | 11 | 5 | 6 | 3200 | 1100 | 500 | 600 |
| **Global** | **102** | **35** | **17** | **18** | **7589** | **2655** | **1283** | **1383** |

P02 fit visibility is exact: FULL_TRAIN fits use train only; LOW_LABEL uses inherited calibration-role budget membership; validation owns governed selection/early stopping; test is final evaluation only. P01 leakage audits for group disjointness, duplicates, overlap groups, fit scope and budget-test contamination passed and P02 did not reopen the split.

### 7.6.3 Preprocessing and window identity

Canonical PreprocessingRecord: `IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08`; semantic hash `a11b59eeb3861a0801cd0540702dca2f0e96b9a55fe8d50d078ea2b3a48acb8c`. Inherited sequence: units normalized to volts; original event indices captured; deterministic EEG channel selection; continuous-run demeaning; average reference; joint signal/event resampling to 160 Hz using MNE polyphase/Kaiser beta 5/reflect/`n_jobs=1`; 8–32 Hz fourth-order Butterworth SOS zero-phase filtering with odd padding/padlen 27/minimum 29 samples; cast to float32.

Core profile: `P01-L1-WINDOW-OFFICIAL-R2`, cue +0.5…+3.5 s, 3.0 s, 480 samples at 160 Hz, one official window per included source event, out-of-bounds REJECT, clipping PROHIBITED; closure 12,910/12,910 accepted parents, 0 invalid. A4 family: `P01-L1-A4-WINDOW-FAMILY-FREEZE-R2`; `A4_LONG_MATCHED_3P5S_R2` is cue +0.0…+3.5 s (560 samples), with registered 2 s subviews V0 `[0:320]`, V1 `[120:440]`, V2 `[240:560]`, retaining the same 12,910 matched parents.

Low-label profile: `P01-L1-LOW-CAL-OFFICIAL-R2`; exact nested inherited calibration subsets at 1/2/4/8/16/32 per class, one frozen membership set per budget. No P02 resampling/replacement membership is allowed.

## 7.7 Model portfolio, branch-level configuration, terminal accounting, and checkpoint semantics

The complete accepted A0 portfolio contains 16 branch IDs. Every planned branch has an explicit terminal state; unsuccessful families are not omitted.

| Branch | Family/role | A0 terminal accounting | Executed scope | Actual/frozen configuration summary | A4 status |
| --- | --- | --- | --- | --- | --- |
| SAN-MAJ | sanity | 3 S | FULL only; deterministic | training-frequency majority hard label; prior vector separate | No |
| SAN-STRAT | sanity | 60 S | FULL; 20 repeats/dataset | seeded stratified random using train-role frequencies | No |
| SAN-PERM | sanity diagnostic | 300 S | 100 grouped permutations/dataset | group/source-event atomic full-pipeline label permutation; base simple pipeline | No |
| SAN-PRIOR | sanity diagnostic | 3 S | FULL only | training-prior probability vector | No |
| DIAG-LOGVAR | diagnostic | 3 S | FULL only | log-bandpower/log-variance + L2 logistic | No |
| CLS-CSP-LDA | classical | 18 S / 3 F | FULL + six low-label budgets; deterministic | CSP OAS; shrinkage LDA `lsqr/auto`; validation-selected CSP components 4/6/8 | Yes; FULL pool + low-label |
| CLS-FBCSP-LR | classical | 3 S | FULL primary | bands 8–12/12–16/16–20/20–24/24–28/28–32; order 4; CSP 4 OAS; L2 LR max_iter 2000; validation C in {1,10} | Yes; FULL pool |
| RIE-TS-LR | Riemannian | 21 S | FULL + six low-label budgets; deterministic | OAS covariance -> Riemann tangent -> L2 LR max_iter 2000; validation C in {0.1,1,10} | Yes; FULL + low-label |
| RIE-EA-TS | Riemannian | 3 S | FULL admitted | train-safe Euclidean Alignment + tangent LR; validation C observed in {0.1,1} | Yes when admitted; FULL pool |
| RIE-MDM | Riemannian diagnostic | 3 S | FULL diagnostic | MDM/FgMDM distance-derived semantics, not calibrated probability | No |
| DNN-EEGNET | compact neural | 105 S | FULL + six low-label budgets; 5 seeds | EEGNet/Lawhern-centered P01-compatible variant; Adam lr .001, dropout .5, kernels 40/20, pools 5/10; Stage11 mixed accepted stopping recipes | Yes; FULL + low-label |
| DNN-FBCNET | conditional neural | 15 S | FULL; 5 seeds | FBCNet author-centered: batch16 Adam .001 wd0 constant; max1500/pat200 restore-best validation BACC | Yes if admitted; FULL pool |
| DNN-SEQ | conditional sequence | 15 S | FULL; 5 seeds | DBConformer preferred admitted slot; batch32 Adam .001 wd0 constant max150/pat40 restore-best | Yes if admitted; FULL pool |
| DNN-EGTC | fallback | 15 CS | fallback slots explicit | EEG-TCNet fallback not activated because sequence slot admitted | No in accepted run |
| SSL-CBRAMOD | compact SSL | 105 S | FULL + six low-label budgets; 5 seeds | AdamW body1e-4/head5e-4 wd.05, label smoothing .1, input scale 10000, 160→200 adapter, cosine eta_min1e-6, clip1, max150/pat40; audited checkpoint | Qualified A4; LONG fail-closed |
| SSL-REVE | SSL diagnostic | 3 DB | FULL diagnostic attempts | known P02 overlap/dependency block preserved | No |

Legend: `S=SUCCESS`, `F=FAILED`, `CS=CONDITIONAL_SKIP`, `DB=DEPENDENCY_BLOCKED`. These totals close the 678 official A0 terminal cells: 657 SUCCESS, 3 FAILED, 15 CONDITIONAL_SKIP and 3 DEPENDENCY_BLOCKED. Stage 13 closed **672 successful model checkpoints with zero checkpoint round-trip failures**; Stage 14 closed 672 prediction model partitions with zero missing partitions. Individual checkpoint IDs/SHA-256 values are preserved in `ModelRegistryRecord`, checkpoint manifests and the external artifact index rather than duplicated as a 672-row prose appendix.

### 7.7.1 A4 representative-selection pools

Validation-only A4 representative pools were frozen by role: classical FULL_TRAIN `CLS-CSP-LDA / CLS-FBCSP-LR` and low-label `CLS-CSP-LDA`; Riemannian FULL_TRAIN `RIE-TS-LR / RIE-EA-TS` and low-label `RIE-TS-LR`; neural FULL_TRAIN `DNN-EEGNET / admitted DNN-FBCNET / admitted DNN-SEQ` and low-label `DNN-EEGNET`; SSL admitted `SSL-CBRAMOD`. `SSL-REVE`, sanity/diagnostic branches, MDM and fallback-only EGTC do not enter claim-bearing A4 role selection. The selected representative is frozen on validation evidence only, with test outcomes prohibited from selection.

## 7.8 Seeds, repetitions, candidate selection, and training-policy contract

### 7.8.1 Exact seed derivation

Master seed: `20260804`. For each stochastic purpose, the implementation forms the frozen canonical UTF-8 identity containing master seed, phase, dataset, run family, budget identity, budget repeat, model repeat, purpose and—where applicable—auxiliary repeat. It computes SHA-256, interprets the first 8 hexadecimal digits as an unsigned integer, reduces modulo `2^31-1`, and maps zero to one. Registered purposes include `MODEL_INIT`, `SAMPLER`, `AUGMENT`, `DATALOADER`, `PERMUTATION`, `STAT_BOOTSTRAP`, `STAT_TEST`, and `CHECKPOINT_TIEBREAK`. Actual per-cell seed values remain in run-cell/registry records; the Protocol freezes the derivation rule rather than copying thousands of seed values.

### 7.8.2 Repetition contract

| Surface | Frozen / actual rule |
| --- | --- |
| deterministic classical/Riemannian | 1 model repeat |
| neural / sequence / SSL A0 | 5 model repeats where active |
| budget membership | 1 inherited frozen subset (`P01_FROZEN_SINGLE_SUBSET`) |
| `SAN-PERM` | 100 grouped permutation repeats per dataset |
| `SAN-STRAT` | 20 stochastic repeats per dataset |
| canonical A4 refit repeat | original 0–4 planned; **only repeat 0 executed after Stage18 deviation** |
| Stage18S descriptive anchor extension | additional repeats 1 and 2 for selected post-hoc anchor cells only; not five-repeat confirmatory evidence |

### 7.8.3 Pre-test class-weight policy

`P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2` resolves class weighting only on legal fit/validation evidence. Equal class counts short-circuit to uniform weighting. Where counts are unequal and a branch has native/verified class-weight support, uniform versus sklearn-balanced weighting may be compared under the same selected hyperparameters/seed; validation BACC is primary, macro-F1 secondary, and uniform wins ties. Test access is prohibited. Unsupported classifiers are not silently converted into a different algorithm family.

### 7.8.4 EEGNet segmentation/reconstruction diagnostic challenger

The S&R challenger is diagnostic-only, FULL_TRAIN-only, not an A-number, does not replace primary A0, is not A4-eligible, and is not a P03 primary branch. It uses the same five EEGNet model seeds and validation-only probability candidates `{0.25,0.5,0.75}` with median BACC, then macro-F1, then distance-to-0.5 and lower-probability tie breaks. Final pre-test selections: BNCI2014_001 = 0.75; Lee2019_MI = 0.25; PhysioNetMI = 0.25. All 45 calibration fits and 15 final challenger cells succeeded. Challenger cells remain outside the official 678 A0-cell and 1,218 A4-cell contracts.

## 7.9 Stage 11 scientific amendment and canonical EEGNet history

Stage 11 is a **post-observation scientific runtime amendment**, not a packaging-only repair and not an untouched Build Book execution. Earlier generic/prior stopping-policy behavior raised source-fidelity/collapse-risk concerns. The owner-authorized continuation aligned the EEGNet architecture/input treatment more closely with Lawhern/EEGNet source context while preserving P01 data/split/test isolation. The source-centered record explicitly states that Lawhern's 500-epoch fact is **context**, and that P02's true patience-120-from-epoch-1 continuation is **not claimed as an original Lawhern stopping rule**.

The accepted artifact is `P02-STAGE11-R7H7-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION-R1`; runtime successor `P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION`; Stage-11 attempt `77533b224dad`. P01 bytes were not mutated; test was not used for selection; no performance-threshold gate was introduced.

Crucially, **canonical Stage 11 is a mixed grandfathered recipe lineage**, not a claim that all 105 primary A0 EEGNet cells were retrained under the final R7 stopping rule:

| Recipe lineage | Recipe SHA-256 | Accepted count | Canonical role |
| --- | --- | ---: | --- |
| `P500_FLOOR500` / grandfathered source-centered P500 | `76a601fee7b69395453f240507abc843c63722c548211f43cf2b88647ac7af09` | 101 | sealed primary A0 cells retained rather than needlessly retrained |
| `P120_FLOOR500_R6` | `74fa2011fa0b94a537338792ce9669350e4ca3153b5f1a3ee50ad556d312690e` | 4 | sealed primary A0 cells retained |
| `TRUE_P120_FLOOR1_R7` | `18cbe259c05bfcea6b26934118216d5a60ff14d659906e6e8e2f590ffc502866` | 15 | newly fitted diagnostic S&R challenger cells; max 10,000, patience 120 from epoch 1 |

Thus the 105 canonical primary A0 EEGNet cells are **101 P500 + 4 R6 P120/FLOOR500**, while the 15 R7 TRUE_P120 cells are diagnostic challenger cells. Stage 11 also completed 45 internal S&R probability-calibration fits. All three recipe SHA-256 values remain accepted lineage evidence. The Protocol must not say or imply that the final R7 recipe retroactively replaced every primary A0 model.

History chain: original/generic policy -> observed source-fidelity/collapse-risk concern -> owner-authorized author/source-centered repair -> grandfather valid sealed primary artifacts -> execute true-P120 new/unsealed challenger fits -> validate G11 PASS -> revalidate downstream Stage 12 dependency. Earlier predecessor archives remain preserved as superseded history.

## 7.10 Stage 12 scientific amendment and author/source-centered external-family history

Stage 12 underwent a scientifically material, post-Stage12 forensic policy repair. Primary amendment artifact: `P02-STAGE12-R6-SCIENTIFIC-POLICY-AMENDMENT-R2`; explicit `change_authority = USER_AUTHORIZED_POST_STAGE12_VALIDATION_ONLY_FORENSIC_REPAIR`; candidate policy `ONE_PREDECLARED_AUTHOR_CENTERED_RECIPE_PER_ACTIVE_EXTERNAL_BRANCH`. The amendment froze source/author-centered recipes while retaining P01 compatibility, validation-only early stopping/selection, test isolation, uniform class weighting, and explicit dependency/conditional terminal states.

Accepted Stage-12 attempt: `b9d3bbee230b`; final runtime successor `P02-RUNTIME-SUCCESSOR-R6R5-STAGE12-FBCNET-AUTHOR-HORIZON-1500-200`. After canonical Stage 11 was replaced/revalidated, Stage 12 was revalidated; the final G12 record states `stage12_retraining_implied=false` and `stage12_scientific_artifacts_byte_identical=true` for that later revalidation step.

| Branch | Source/recipe lineage | Accepted training policy | Terminal surface |
| --- | --- | --- | --- |
| `DNN-FBCNET` | `ravikiran-mane/FBCNet`, commit `de1bbdd8a54cb1e466830e3d47070e0e56761a37`, `codes/classify/cv.py` | batch16, Adam, lr .001, wd0, constant, **max1500/pat200**, restore-best; P01 split/validation BACC/test firewall override incompatible author protocol details | 15 SUCCESS |
| `DNN-SEQ` | DBConformer preferred admitted final sequence slot; source-centered compatibility repair | batch32, Adam, lr .001, wd0, constant, max150/pat40, restore-best | 15 SUCCESS |
| `SSL-CBRAMOD` | source-centered CBraMod with audited checkpoint/adaptation | batch64, AdamW, body1e-4/head5e-4, wd .05, label smoothing .1, scale10000, cosine eta_min1e-6, gradclip1, max150/pat40 | 105 SUCCESS |
| `DNN-EGTC` | governed low-resource fallback | not activated while DBConformer final slot admitted | 15 CONDITIONAL_SKIP |
| `SSL-REVE` | known P02 overlap/dependency risk | fail-closed scientific overlap block preserved | 3 DEPENDENCY_BLOCKED |

Total Stage 12 surface: **153 attempted; 135 SUCCESS; 15 CONDITIONAL_SKIP; 3 DEPENDENCY_BLOCKED**. P00/P01 artifacts were not mutated, and test data were not used for hyperparameter selection. The amendment is reported as post-observation; it is not backdated as the original Build Book plan.

## 7.11 Actual Kaggle environment and security boundary

| Resource / package | Actual accepted environment |
| --- | --- |
| Python | 3.12.13 |
| CPU | 4 logical CPUs |
| RAM | 31.348 GiB total; 29.439 GiB available at Stage 01 probe |
| GPU | Tesla T4; CUDA available; 14.562 GiB VRAM |
| disk at Stage 01 | 19.518 GiB total; 19.494 GiB free |
| moabb | 1.5.0 |
| mne | 1.12.1 |
| numpy | 2.2.6 |
| scipy | 1.15.3 |
| pandas | 2.3.1 |
| scikit-learn | 1.7.1 |
| h5py | 3.14.0 |
| pooch | 1.8.2 |
| PyYAML | 6.0.2 |
| pydantic | 2.11.7 |
| jsonschema | 4.25.0 |
| nbformat | 5.10.4 |
| pytest | 8.4.1 |
| torch | 2.13.0 |
| braindecode | 1.6.1 |
| pyriemann | 0.12 |
| huggingface-hub | 1.24.0 |
| safetensors | 0.8.0 |

Credential presence was required and resolved from an `ENVIRONMENT_SECRET_PROVIDER`. **No credential value is Protocol evidence.** Any literal Hugging Face access token, including values that may have appeared in an interactive notebook source during execution, is explicitly excluded from this document, all machine-readable companions, validation outputs, and release surfaces. The security contract is to inject credentials at runtime, never print them, never persist them to manifests/logs, and secret-scan release material.

## 7.12 Executed notebook and stage matrix

| Stage | Function | Gate/output status | Actual Protocol disposition |
| --- | --- | --- | --- |
| 00 | Authority/preflight | PASS | Authority and phase identity intake; deterministic preflight. |
| 01 | Environment | PASS | Python 3.12.13; Tesla T4; exact package pins and secret-provider credential presence recorded. |
| 02 | Cumulative project intake | PASS | P00/P01 state and P01→P02 inputs resolved. |
| 03 | External pointer and conditional asset resolution | PASS | External assets resolved/fail-closed without changing P01 bytes. |
| 04 | P01 validation | PASS | Immutable P01 data/split/preprocessing/window substrate revalidated. |
| 05 | Scientific freeze verification | PASS | P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5; owner-authorized pre-test training-policy amendment retained. |
| 06 | Schema/config/import closure | PASS | 10 schemas; run_config_hash=9e181d2e935d2e9674ca6e05572f49520ad0306a3761362b770f8bee8c78ce13; clean import PASS. |
| 07 | Loader/leakage/role discipline | PASS | P01 roles retained; test isolated from fitting/selection. |
| 08 | Sanity/diagnostic family | PASS | 369 attempted; 369 SUCCESS. |
| 09 | Classical family | PASS | 24 attempted; 21 SUCCESS; 3 FAILED. |
| 10 | Riemannian family | PASS | 27 attempted; 27 SUCCESS. |
| 11 | EEGNet + training-policy challenger | PASS | Canonical author-centered successor; 105 primary SUCCESS; 45 internal S&R calibration fits SUCCESS; 15 diagnostic challenger SUCCESS. |
| 12 | External neural/SSL families | PASS | Canonical author-centered/source-centered successor; 153 attempted; 135 SUCCESS; 15 CONDITIONAL_SKIP; 3 DEPENDENCY_BLOCKED. |
| 13 | Checkpoint closure | PASS | 672 successful model checkpoints; 0 roundtrip failures. |
| 14 | Prediction closure | PASS | 672 model partitions emitted; 0 missing; score semantics complete. |
| 15 | A0 + challenger closure | PASS | 678 planned/terminal; 657 SUCCESS; 3 FAILED; 15 CONDITIONAL_SKIP; 3 DEPENDENCY_BLOCKED; 3942 participant rows; 2625 metric records. |
| 16 | Low-label curves | PASS | 36 records; 216 attempted points; 213 SUCCESS; 3 FAILED; 207 VALID + 9 EXPLICIT_NON_SUCCESS; single frozen subset limitation retained. |
| 17 | Subject/session profiles | PASS | 18 descriptive profile records. |
| 18 | A4 ordinary controls | PASS | 1218 terminal slots; 591 SUCCESS; 576 CONDITIONAL_SKIP; 9 INPUT_INCOMPATIBLE; 42 NOT_APPLICABLE_REPEAT_SLOT; resource-constrained deviation explicitly frozen. |
| 18U | Additional-ablation dispatcher | PASS | NO_ADDITIONAL_FULL_EXECUTION_ABLATION_UNLOCKED; result-dependent unlock prohibited. |
| 19 | Failure/negative evidence | PASS | 648 failures, 340 negative-result notes, 309 diagnostic flags aggregated and preserved. |
| 20 | Downstream readiness | PASS | 1014 prediction partitions checked; P03 contract complete; readiness record emitted. |
| 21 | Figure/table source data | PASS | Governed source tables/figures prepared without Layer10 recomputation. |
| 22 | Handoffs | PASS | Protocol, Phase Analysis, Layer0, Evidence Map, Layer10 and P03 handoffs emitted. |
| 23 | Evidence sufficiency | PASS | missing=[]; all required state flags true. |
| 24 | Bundle/finalization | PASS | Runtime bundle ready; governed G24 PASS; subsequent release packaging/replay changed no science. |

Every governing stage ledger reports `SUCCESS` with its output/gate status `PASS` for the accepted lineage. The stage matrix includes `18U` as the same-notebook additional-ablation dispatcher. Stage 18S is a later supplemental sensitivity surface and is intentionally not substituted for canonical Stage 18/G18.

## 7.13 A0 raw accept-all decoder contract and actual closure

A0 asks what raw accept-all decoder evidence is produced under frozen P01 inputs without calibration, rejection, abstention, or downstream policy. Its exact datasets, split, windows, budgets, model/run lineage, seed identities, and test-after-selection discipline are frozen above.

Required A0 metrics/source evidence:

- primary: balanced accuracy (`BACC`);
- complementary: macro-F1;
- secondary: accuracy;
- conditional: ROC-AUC only when score semantics permit;
- required source data: confusion, class support, prediction completeness, branch success;
- participant-first aggregation and exact denominator accounting.

Actual A0 closure:

| Field | Actual value |
| --- | --- |
| planned / terminal cells | 678 / 678 |
| SUCCESS | 657 |
| FAILED | 3 |
| CONDITIONAL_SKIP | 15 |
| DEPENDENCY_BLOCKED | 3 |
| participant metric rows | 3,942 |
| metric records | 2,625 |
| prediction record complete | YES |
| raw score semantics complete | YES |
| denominator accounting complete | YES |
| checkpoint provenance complete | YES |
| minimum floor | at least one successful classical + one successful Riemannian branch for every dataset |

The three failed and all skipped/blocked cells remain part of the A0 accounting and are not imputed as successes.

## 7.14 Low-label curve contract and actual closure

Low-label evidence inherits the exact P01 calibration-role nested subsets at 1/2/4/8/16/32 examples per class. No new random membership is generated in P02. The curve therefore measures behavior on **one frozen subset realization per budget**, not repeated budget-membership sampling.

Actual Stage 16 closure: 36 curve records; 216 attempted points; 213 successful run points and 3 failed run cells; 207 `VALID` points and 9 `EXPLICIT_NON_SUCCESS` points after terminal-state mapping. All budgets are accounted for. A derived-evidence repair was allowed only to restore/close the analysis surface; it did not retrain models, regenerate predictions, alter scientific configuration, or select on test evidence.

**Claim limitation:** the resulting low-label curves may support behavior under the inherited single-subset protocol, but not variance attributable to repeated low-label subset resampling.

## 7.15 Subject/session heterogeneity and descriptive profile contract

Stage 17 emitted 18 `SubjectProfileRecord`-type descriptive records. These profiles are common-support descriptive evidence for participant/session heterogeneity and difficulty patterns. They are not diagnostic labels, clinical phenotypes, routing policies, or eligibility decisions. Any downstream use must preserve the exact contributing prediction/model/split/budget identities and must not elevate descriptive difficulty into a medical or deployment classification.

## 7.16 A4 ordinary-control contract and resource-constrained deviation

### 7.16.1 Frozen A4 scientific question and six conditions

A4 tests authorized **ordinary** longer-window, multi-window, and fixed ensemble controls against matched CORE evidence, with burden recorded. It is not a learned gating, calibration, abstention, or adaptive-policy ablation.

| Condition | Frozen meaning |
| --- | --- |
| A4-C0-CORE | matched A0 CORE reference |
| A4-C1-LONG-3P5S | exact 3.5-s A4 long representation, refit with frozen recipe/seed; no pad/crop substitution |
| A4-C2-MULTI-HARD-VOTE | deterministic parent-level majority vote over the three fixed views |
| A4-C3-MULTI-PROB-AVG | probability average only when genuine aligned probabilities exist |
| A4-C4-MODEL-HARD-VOTE | fixed ordinary model ensemble hard vote using pre-result role membership |
| A4-C5-MODEL-PROB-AVG | fixed ordinary model probability average only with compatible aligned probabilities |

Hard-vote ties may not use truth. Probability averaging is fail-closed when score/class semantics are incompatible. Representative selection is validation BACC → macro-F1 → lower validation burden → lexical branch ID and is frozen before test.

### 7.16.2 Owner-authorized Stage 18 deviation

The accepted Stage 18 artifact explicitly records `P02-STAGE18-RESOURCE-CONSTRAINED-ANCHOR-BUDGET-SINGLE-REPEAT-R1`, reason `KAGGLE_WALL_CLOCK_CONSTRAINT_OWNER_DECISION`.

This deviation **did not remove** any A4 condition, dataset, representation, or model-family role. It preserved all three datasets, all six A4 conditions, and refit roles `CLASSICAL`, `NEURAL`, `RIEMANNIAN`, `SSL`. It changed the expensive refit execution surface:

- original refit repeat indices: 0–4;
- executed refit repeat index: 0 only;
- declared skipped repeat indices: 1–4;
- deep-model anchor budgets: `1/class`, `8/class`, and `FULL_TRAIN`;
- frozen plan A4 terminal slots: 1,218;
- frozen refit cells: 756;
- declared reduced run cells: 576 = 504 repeat-reduction slots + 72 deep-budget-reduction slots;
- executable refit run cells: 180, of which 54 are deep refits;
- estimated unique deep member fits: reduced from 840 to 72 (91.43% reduction);
- latency measurement repeats: 1.

Per-fit training recipes, representative-selection rules, test isolation, checkpoint roundtrip validation, and statistical comparison definitions were not changed.

### 7.16.3 Actual A4 closure

| Terminal state / closure surface | Actual value |
| --- | --- |
| planned terminal slots | 1,218 |
| SUCCESS | 591 |
| CONDITIONAL_SKIP | 576 |
| INPUT_INCOMPATIBLE | 9 |
| NOT_APPLICABLE_REPEAT_SLOT | 42 |
| representative groups | 21 |
| role-control expected / closed | 756 / 756 |
| C4/C5 expected / closed | 210 / 210 |
| burden rows | 1,218 |
| phase-analysis source complete | YES |

A4 is therefore **executed and evidence-sufficient for the explicitly authorized resource-constrained anchor-budget/single-repeat scope**, but `full_buildbook_replication_equivalence = false`.

### 7.16.4 A4 claim lock

The deviation expressly authorizes anchor-budget deep-model comparison within the executed scope. It does **not** authorize:

- five-repeat/multi-seed A4 stability claims;
- dense deep-model budget-response curves across every inherited budget;
- representation of P02 A4 as full replication of the original Build Book refit grid.

These limitations are mandatory in Phase Analysis, Layer 0 review, Evidence Map entries, Layer 10 cards/figures, and any later manuscript synthesis.

## 7.17 Stage 18S post-hoc balanced sensitivity supplement

`P02-STAGE18S-BALANCED-SENSITIVITY-R1` is retained as **additional post-hoc descriptive sensitivity evidence**. It is not a replacement for canonical Stage 18 and does not modify G18.

The final handoff records:

- status PASS;
- canonical Stage 18 remains the G18 source;
- 216 member receipts;
- 162 supplemental terminal comparison cells, with 135 SUCCESS and 27 INPUT_INCOMPATIBLE;
- `post_hoc = true`;
- not five-repeat confirmatory;
- not full-Build-Book-equivalent;
- original Stage 18 protocol deviation must not be overwritten.

Accordingly, Stage 18S may be used in Phase Analysis as sensitivity/robustness context with explicit post-hoc labeling, but may not upgrade the confirmatory status or erase Stage 18's scope limitation.

## 7.18 A0–A13 disposition matrix and A14 lock

The controlling Protocol v0.1 fixes the official ablation identities. R2 corrects the R1 mislabeling of A2 and restores the exact A5–A13 names.

| Ablation | Official identity | Controlling owner | P02/L2 disposition | P02 evidence/limitation |
| --- | --- | --- | --- | --- |
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | L2 | **APPLICABLE_EXECUTED** | 678 terminal A0 cells; complete with explicit non-success states |
| A1 | Calibrated Decoder / Calibration Visibility | L3 C1 | **NOT_APPLICABLE_WITH_REASON** | downstream; P02 emits raw score substrate only |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | L3 C2 | **NOT_APPLICABLE_WITH_REASON** | downstream threshold baseline; not an L2 uncertainty cell |
| A3 | Uncertainty and Selective Prediction | L3 C2 | **NOT_APPLICABLE_WITH_REASON** | downstream uncertainty/selective-prediction science |
| A4 | Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls | L2 | **APPLICABLE_EXECUTED_WITH_RECORDED_DEVIATION** | all C0–C5 identities preserved; resource-constrained single refit repeat and deep anchors only; no full-grid equivalence |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | L4 | **NOT_APPLICABLE_WITH_REASON** | downstream evidence verification |
| A6 | IHARQ + Evidence-Quality Estimator | L4/L6 | **NOT_APPLICABLE_WITH_REASON** | downstream evidence-quality estimation |
| A7 | IHARQ + RegimeRisk Temporal Trust | L5 | **NOT_APPLICABLE_WITH_REASON** | downstream temporal trust |
| A8 | Learning-to-defer / Deferral Comparison | L6/L7 | **NOT_APPLICABLE_WITH_REASON** | downstream deferral comparison |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | downstream adaptive-policy layer | **NOT_APPLICABLE_WITH_REASON** | downstream supervised adaptive policy |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | simulation-bounded downstream layer | **NOT_APPLICABLE_WITH_REASON** | downstream simulation-bounded bandit |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | simulation-bounded downstream layer | **NOT_APPLICABLE_WITH_REASON** | downstream sequential policy learning |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | stress layer | **NOT_APPLICABLE_WITH_REASON** | downstream stress robustness |
| A13 | Layer 9 MyoSuite/OpenSim/static-replay Embodiment Demo | L9 | **NOT_APPLICABLE_WITH_REASON** | downstream embodiment/static replay |
| A14 | absent/prohibited | governance/protocol lock | **PROHIBITED** | no A14 may be invented/unlocked |

Stage 18U confirmed `NO_ADDITIONAL_FULL_EXECUTION_ABLATION_UNLOCKED`; result-dependent ablation unlocking is prohibited. Not executing a downstream A-cell in P02 does not delete its official identity from the cumulative ladder.

## 7.19 Metrics, statistics, matching, denominators, and analysis contract

### 7.19.1 Metrics

- primary: `BACC`;
- complementary: `F1_MACRO`;
- secondary: `ACC`;
- conditional: `ROC_AUC` when score semantics make it lawful;
- required source fields: confusion, class support, prediction completeness, branch success; A4 additionally records burden/delay.

Not selected for P02 confirmatory use: Kappa, MCC, AUPRC, Brier, NLL, ECE, calibration slope, and risk-coverage. Their absence must not be interpreted as missing evidence for a P02-owned estimand because calibration/selective-risk ownership belongs downstream.

### 7.19.2 Statistical contract

- participant-first aggregation;
- 95% participant-cluster uncertainty;
- 10,000 BCa bootstrap resamples, percentile fallback;
- two-method paired comparison: two-sided paired Wilcoxon;
- multi-method comparison: Friedman followed by predeclared paired Wilcoxon comparisons;
- Holm multiplicity control within the confirmatory family;
- effect sizes: paired median difference, matched-pairs rank-biserial, and Kendall W for Friedman;
- minimum complete participants for an inferential comparison: 5;
- cross-dataset analysis is dataset-stratified; no confirmatory meta-analysis is created by P02.

Stage 18's compute deviation does not change these comparison definitions; it changes which repeat/budget cells are actually eligible to populate them.

### 7.19.3 Matching and denominator discipline

Every comparison must retain enough identity to establish matched support: dataset, subject, session/run, source event/parent window, split, budget, budget repeat, branch/role, model repeat, seed/config and condition/profile identity as applicable. Attrition and incompatibility are explicit. No comparison may silently use a favorable subset without reporting the support difference and reason.

## 7.20 Failure, negative, invalid, blocked, skipped, and diagnostic evidence

Stage 19 aggregated **648 failure entries, 340 negative-result notes, and 309 diagnostic flags**. These include both direct run non-success states and structured diagnostic/negative evidence. They are preservation surfaces, not a single interchangeable error count.

Required distinctions:

- `FAILED`: attempted run/operation reached a failure terminal state;
- `DEPENDENCY_BLOCKED`: required dependency/scientific admission condition was not satisfied;
- `CONDITIONAL_SKIP`: a frozen conditional branch/condition was lawfully not activated;
- `INPUT_INCOMPATIBLE`: exact score/input semantics do not permit the condition;
- `NOT_APPLICABLE_REPEAT_SLOT`: a frozen slot is declared non-applicable under the authorized Stage 18 repeat reduction;
- negative/null scientific observations: valid results that do not support an improvement;
- diagnostic-only evidence: useful for engineering/scientific diagnosis but not claim-bearing primary evidence.

No failed or superseded execution is converted into success evidence. The final accepted lineage may supersede an earlier attempt for current analysis while the earlier attempt remains part of the audit history.

## 7.21 Repair, rerun, amendment, and supersession ledger

| Event | Classification | Scientific configuration changed? | Test-driven selection? | Final disposition |
| --- | --- | --- | --- | --- |
| `P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2` | owner-authorized pre-test training-policy resolution | YES, before relevant final test evaluation | NO | frozen supporting policy; S&R challenger/class weighting governed |
| Stage 11 author-centered EEGNet successors | post-observation scientific training-policy amendment + rerun | YES | NO | final R7H7 successor canonical; predecessors retained as superseded evidence |
| Stage 12 author/source-centered external-family successors | post-observation scientific policy/config amendment + rerun | YES | NO | final R6R5 successor canonical; blocked/skipped branches preserved |
| Stage 16 derived-evidence closure repair | derived analysis/evidence repair | NO training/prediction/config change | NO | accepted; does not change primary run evidence |
| Stage 18 resource-constrained anchor/single-repeat execution | explicit Protocol deviation from Build Book | execution surface reduced; per-fit scientific recipe unchanged | NO | accepted for restricted A4 claim scope; not full Build Book replication |
| Stage 18S sensitivity | post-hoc supplemental analysis/execution | supplemental only; canonical Stage18 unchanged | NO | descriptive sensitivity only |
| original Stage 24 monolithic ZIP attempt | packaging/transport failure (`ENOSPC`) | NO | N/A | superseded by low-disk chunked HF release; failure retained |
| Stage 24 low-disk chunked HF release R2.2 | packaging/release repair | NO | N/A | accepted archival/fallback release |
| Stage 24 finalization replay from full workspace snapshot | release assembly replay | NO scientific-stage or training rerun | N/A | accepted release replay; Stage11/12/18/18S/23/24 source state revalidated |

This ledger is the authoritative post-execution classification for Phase 02. Later documents may summarize it but must not relabel a post-observation scientific amendment as pre-registered.

## 7.22 Gate closure and evidence sufficiency

Every supplied canonical gate record from G00 through G24, including G18U, was parsed. All are PASS with empty blockers; observability is PASS where recorded. Runtime-successor identity remains explicit rather than being collapsed into the final gate status.

| Gate | Stage | Status | Observability | Blockers | Evidence | Runtime successor |
| --- | --- | --- | --- | --- | --- | --- |
| `G00` | `00` | PASS | PASS | [] | `stage_ledger/stage_00.json` |  |
| `G01` | `01` | PASS | PASS | [] | `stage_ledger/stage_01.json` |  |
| `G02` | `02` | PASS | PASS | [] | `stage_ledger/stage_02.json` |  |
| `G03` | `03` | PASS | PASS | [] | `stage_ledger/stage_03.json` |  |
| `G04` | `04` | PASS | PASS | [] | `stage_ledger/stage_04.json` |  |
| `G05` | `05` | PASS | PASS | [] | `stage_ledger/stage_05.json` |  |
| `G06` | `06` | PASS | PASS | [] | `stage_ledger/stage_06.json` |  |
| `G07` | `07` | PASS | PASS | [] | `stage_ledger/stage_07.json` |  |
| `G08` | `08` | PASS | PASS | [] | `stage_artifacts/08_semantic_gate_successor_R1.json` | `P02-RUNTIME-SUCCESSOR-R1-CLASS-WEIGHT-APPLICABILITY-LIVE-CONTINUATION` |
| `G09` | `09` | PASS |  | [] | `diagnostics/runtime_successor/G09_SEMANTIC_AUDIT_R1.json` | `P02-RUNTIME-SUCCESSOR-R2-CANONICAL-LOW-CAL-BUDGET-ID-PARSER-LIVE-CONTINUATION` |
| `G10` | `10` | PASS |  | [] | `diagnostics/runtime_successor/G10_SEMANTIC_AUDIT_R1.json` | `P02-RUNTIME-SUCCESSOR-R2-CANONICAL-LOW-CAL-BUDGET-ID-PARSER-LIVE-CONTINUATION` |
| `G11` | `11` | PASS | PASS | [] | `stage_ledger/stage_11.json` | `P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION` |
| `G12` | `12` | PASS | PASS | [] | `stage_ledger/stage_12.json` | `P02-RUNTIME-SUCCESSOR-R6R5-STAGE12-FBCNET-AUTHOR-HORIZON-1500-200` |
| `G13` | `13` | PASS | PASS | [] | `stage_ledger/stage_13.json` | `P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION` |
| `G14` | `14` | PASS | PASS | [] | `stage_ledger/stage_14.json` | `P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION` |
| `G15` | `15` | PASS | PASS | [] | `stage_ledger/stage_15.json` | `P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION` |
| `G16` | `16` | PASS | PASS | [] | `diagnostics/runtime_successor/G16_SEMANTIC_AUDIT_R1.json` | `P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION` |
| `G17` | `17` | PASS | PASS | [] | `stage_ledger/stage_17.json` | `P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION` |
| `G18` | `18` | PASS | PASS | [] | `stage_ledger/stage_18.json` | `P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1` |
| `G18U` | `18U` | PASS | PASS | [] | `stage_ledger/stage_18U.json` | `P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1` |
| `G19` | `19` | PASS | PASS | [] | `stage_ledger/stage_19.json` | `P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1` |
| `G20` | `20` | PASS | PASS | [] | `stage_ledger/stage_20.json` | `P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1` |
| `G21` | `21` | PASS | PASS | [] | `stage_ledger/stage_21.json` | `P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1` |
| `G22` | `22` | PASS | PASS | [] | `stage_ledger/stage_22.json` | `P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1` |
| `G23` | `23` | PASS | PASS | [] | `stage_ledger/stage_23.json` | `P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1` |
| `G24` | `24` | PASS | PASS | [] | `stage_ledger/stage_24.json` | `P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1` |

G23 closes evidence sufficiency with `missing=[]`; G24 closes runtime bundle/finalization with blockers `[]`. A PASS means the governed **executed** scope is sufficient. It does not imply five-repeat A4 stability, dense deep-budget coverage, or full original Build Book A4 replication equivalence.

## 7.23 Evidence status, interpretation hierarchy, and claim ceiling

Phase Analysis must use:

`measured result → supported interpretation → candidate claim → mechanism hypothesis (only when justified)`.

Candidate claims are **not approved claims** until Layer 0 disposition.

### 7.23.1 P02-supported candidate-claim domains

P02 evidence may support appropriately bounded candidate claims about:

- governed raw accept-all baseline decoder measurement under the frozen P01 protocol;
- model-family comparisons using exact recorded data/split/budget/seed/config/support identities;
- low-label behavior under the inherited single-frozen-subset limitation;
- participant/session heterogeneity as descriptive evidence;
- ordinary A4 longer/multi-window/fixed-ensemble controls within the resource-constrained anchor-budget/single-repeat scope;
- record completeness, checkpoint/prediction provenance, reproducibility surfaces and P03 technical readiness.

### 7.23.2 P02-prohibited standalone claim domains

P02 alone cannot establish:

- clinical efficacy, clinical safety, or deployment safety;
- calibrated probability reliability or calibrated uncertainty;
- abstention/selective-risk/readiness-policy effectiveness;
- policy-learning benefit;
- temporal/stress robustness;
- closed-loop or embodiment effectiveness;
- five-repeat A4 stability;
- dense deep-budget A4 response curves;
- full Build Book A4 replication equivalence.

All public wording must carry the inherited `PUBLIC_EEG_ONLY`, `NON_CLINICAL`, `NO_DEPLOYMENT_CLAIM` limitation family plus the P02-specific A4 and low-label limitations where relevant.

## 7.24 External artifact registry, integrity semantics, and storage precedence

### 7.24.1 Preferred complete Kaggle-workspace snapshot

| Field | Frozen value |
| --- | --- |
| provider / type | Hugging Face / private dataset |
| repository | `Csthv/p02-phase02-final-whole-working-20260814t052120z-b890ff92` |
| immutable Git revision | `bc14961e14f2e48690e55df3577014275f9cbf30` |
| working-tree manifest | `__IHARQ_SNAPSHOT__/WORKING_TREE_MANIFEST.jsonl` |
| working-tree manifest SHA-256 | `564bbb44e67d14da8457ad83d33651ded93dfc6b89ab90f10f78a36a20b8e8f5` |
| snapshot metadata | `__IHARQ_SNAPSHOT__/SNAPSHOT_METADATA.json` |
| source manifest file count | 24,661 |
| per-object continuation index | `release_metadata/all_artifact_location_index.csv` in the local final P02 project state; exact source path, bytes, SHA-256, repo, revision and HF path |
| per-object continuation index SHA-256 / bytes | `540a0c3d4cbc686645ab1fccf088205c02c32a5c34e4b238c91f9c4ec119c12f` / 10,191,241 |
| producer / consumers | P02 / P03–P15, later layers, reproduction |
| access | private; authorized `IHARQ_HF_TOKEN_P02` at runtime |
| license | mixed artifact tree; artifact-level/source licenses control; no fabricated single repository license |
| role | **PREFERRED PRACTICAL P02 CONTINUATION SUBSTRATE** |
| live remote status in final pre-closure audit | `REMOTE_NOT_ACCESSIBLE` through available HF connector; local Stage24 receipt/revision/manifest evidence validated |

A multi-object repository tree does not have a truthful single file-size/SHA field. Its immutable tree identity is the pinned Git revision plus the verified working-tree manifest. Required objects are then verified individually by path, byte count and SHA-256 from the manifest/artifact-location index. Downstream consumers must never select `latest`.

The light cumulative P02 package intentionally externalizes runtime-heavy objects. Audit reconciliation checked the 17,089 entries in the runtime checksum manifest: 68 objects are locally present and hash-correct; all 17,021 externally omitted objects matched `all_artifact_location_index.csv` by **exact relative path and SHA-256**, with zero unmatched externalized objects. This establishes pointer-backed completeness of the light derivative without pretending the heavy files are local.

The full workspace snapshot is preferred because it exposes direct workspace paths and avoids reconstructing routine continuation state from multipart ZIP transports. This is a retrieval precedence, not a replacement of the archival release or a change in scientific authority.

### 7.24.2 Archival/fallback chunked P02 release

| Field | Frozen value |
| --- | --- |
| artifact ID | `P02-STAGE24-ARCHIVAL-CHUNKED-RELEASE-R2` |
| repository | `Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260814t051352z` |
| content revision | `bc88dccd6518aa7b172697be1ef98344997f27ff` |
| manifest revision | `c60c0505faa8076090439277ed1d8ef8c86734b7` |
| final release revision | `257a407b5c7ea37b6c620863ee261c010c8f197c` |
| private / remote completeness | true / PASS in Stage24 local receipts |
| heavy packages | 4; 9,448,804,258 source bytes / 3,968 source files |
| execution-bundle packages | 1 |
| local transport ZIPs | deleted after confirmed HF upload |
| reason for successor | original monolithic Stage24 ZIP failed ENOSPC; low-disk chunked successor repaired transport only |
| scientific configuration changed | NO |
| live remote status in final pre-closure audit | `REMOTE_NOT_ACCESSIBLE`; do not fabricate remote verification |

Exact uploaded transport objects preserved by the accepted remote-resume state:

| Remote path | Bytes | SHA-256 |
| --- | ---: | --- |
| `phase_02/execution_bundle_packages/execution_bundle_package_0001.zip` | 519,305,980 | `c380edff3afe44137afea8a3bb70699bb3a3885c3363198eebf93aad66f23805` |
| `phase_02/heavy_packages/heavy_artifacts_package_0001.zip` | 2,894,348,079 | `5032ab8785b36044d8f8d1635c02fbb10bfca714bb9ecb16223c3d2cf76f1dcf` |
| `phase_02/heavy_packages/heavy_artifacts_package_0002.zip` | 2,893,314,005 | `c596b502ff154c494cdcfa047826617354962f8209c2fbcffe71f79671ed4296` |
| `phase_02/heavy_packages/heavy_artifacts_package_0003.zip` | 2,898,992,543 | `b0778b61170d6998102bf9c471b2133697e61cafbddc16ab67e52dad40f48bf2` |
| `phase_02/heavy_packages/heavy_artifacts_package_0004.zip` | 763,895,568 | `0b0263c867fea1edd4362deee1d7607f9713ec4135ebda4a441729b6ca4273ef` |
| `phase_02/release_manifests/execution_bundle_multipart_manifest_R2.json` | 3,797 | `8f68c1a298414eabd413b0ae6acb49ab35c2524fb63963420376a23d1e698a48` |
| `phase_02/release_manifests/external_artifact_pointer_manifest_R2.json` | 7,791,281 | `765e4d1e4dd12bdc85c4e7435405f04a0bf00ee65d79fa6444e2bdf47e64698b` |
| `phase_02/release_manifests/external_artifact_pointer_manifest_R2.yaml` | 6,775,406 | `b6b2581cc00ee89669b4924c709f7c7e313afcae1425dc81349f7ffad80e979c` |
| `phase_02/release_packages/cumulative_project_state/IHARQ_Project_State_After_Phase_02_R2.zip` | 118,117,660 | `b4f1d12b0fb37faf908a3eadd2d6a43d52efbe7a2601220a030ffd6858b9b8cc` |
| `phase_02/release_packages/github_ready/IHARQ_Cumulative_GitHub_Ready_Through_P02_R2.zip` | 118,118,899 | `2052eff12f5ec4054305577de7557049db45a52118e65d9300b318761c406839` |

Retrieval of the archival release requires `IHARQ_HF_TOKEN_P02`, pinning the exact final revision above (with the recorded content/manifest revisions retained for reconstruction), resolving the exact object path, and verifying its byte count and SHA-256 against the table/Stage24 receipt. Mutable `latest` is prohibited.

The archival release remains a valid fallback for exact packaged transport/release reconstruction and is not invalidated by the preferred workspace route.

## 7.25 Dual-Hugging-Face credential contract for downstream phases

The supplied project state establishes separate private-artifact families: earlier-phase assets use the pre-P02 authorization boundary (including prior `csthv999z` private assets), while P02 external storage uses the `Csthv` repositories frozen in §7.24. The owner additionally states that the credentials are distinct. Future mixed-phase workflows must therefore expose **two independent symbolic secret interfaces**:

| Secret interface | Artifact family | Required behavior |
| --- | --- | --- |
| `IHARQ_HF_TOKEN_PRE_P02` | P00/P01/pre-P02 private HF assets | runtime-only injection; never serialize/log; no fallback to P02 token |
| `IHARQ_HF_TOKEN_P02` | P02 full workspace snapshot and P02 archival release | runtime-only injection; never serialize/log; no fallback to pre-P02 token |

A workflow consuming both families must accept both independently and fail closed for whichever required source is inaccessible. One token must never be assumed to cover both. The historical runtime's environment-variable naming is not rewritten; these are the governed **downstream access interfaces**. Secret values are prohibited from Protocol, machine-readable contracts, logs, notebook outputs, Git/release archives and Layer-10 exports.

## 7.26 Frozen downstream-consumer and analysis-input handoff

Stage 20 checked 1,014 prediction partitions and emitted a PASS Layer-2 readiness surface. Downstream consumers are Phase Analysis, Layer 0, Evidence Map, Layer 10, P03 and later phases/layers, the future cumulative Protocol, thesis/paper synthesis, and reproduction/release.

They must be able to determine canonical versus superseded evidence, retrieve/verify externalized objects, preserve score/class-order semantics, understand allowed analysis scope and prohibited claims, and avoid reconstructing hidden assumptions. The minimum canonical analysis-input paths are frozen in the machine-readable `P02_analysis_contract.yaml` and Appendix B, including A0/A4 completion/statistics/source manifests, low-label/profile sources, challenger statistics/selection, failure summaries, Stage18 deviation, Stage18S supplement artifacts, figure/table source manifest, pre-execution amendment, and readiness record.

P03 may consume P02 raw scores/probabilities and model-family evidence for downstream calibration/uncertainty/selective-prediction work. It may not retroactively alter P02 labels/splits/windows, replace terminal states, or treat P02 readiness as safety evidence. Any new representation or score transformation must be a new governed downstream artifact with explicit lineage.

## 7.27 Residual limitations and claim restrictions

The documentary audit closes with the following **true residual limitations**; none is erased by G23/G24 PASS:

- **scientific/public scope:** public benchmark binary-MI research evidence only; non-clinical and no deployment claim;
- **inherited-data scope:** all P02 conclusions are conditional on the exact P01 labels, split, preprocessing, core/A4 windows and source availability;
- **low-label evidence:** one inherited frozen membership subset per budget; no repeated subset-resampling uncertainty;
- **branch non-success:** 3 classical A0 failures, 15 conditional fallback skips and 3 dependency-blocked SSL cells remain in denominators; A4 includes incompatible and explicitly skipped/non-applicable terminals;
- **Stage 11/12 history:** accepted neural/external evidence includes transparent post-observation, author/source-informed amendments; this is not untouched original pre-registration;
- **Stage 11 mixed lineage:** primary A0 EEGNet contains grandfathered P500/R6 recipes; R7 true-P120 applies to newly fitted diagnostic challenger cells and must not be generalized backward;
- **A4 compute limitation:** only refit repeat 0 executed; deep roles use 1/class, 8/class and FULL_TRAIN anchors; no five-repeat stability, dense deep-budget curve or full Build Book replication-equivalence claim;
- **Stage18S:** post-hoc descriptive sensitivity only; it does not change canonical Stage18/G18 or create five-repeat confirmatory evidence;
- **conditional score semantics:** probability averaging/ROC-AUC are lawful only where compatible genuine score/probability semantics exist;
- **notebook reconstruction:** the owner-supplied final notebook is a post-restart continuation, so Stages 00–18 are reconstructed from canonical ledgers/artifacts rather than a single uninterrupted submitted notebook output stream;
- **external access:** both P02 HF repositories are private and were not live-resolvable through the available connector during this audit; local Stage24 receipts, immutable revisions, manifests, per-object hashes/sizes and pointer reconciliation were sufficient for documentary closure, but downstream remote access still requires authorization;
- **credential separation:** mixed pre-P02/P02 private-HF consumption requires two independently authorized symbolic secrets;
- **environment:** accepted results are tied to the recorded Python/package/GPU/runtime identities and runtime-successor chain;
- **downstream ownership:** calibration, uncertainty, abstention, readiness policy, temporal/stress robustness, simulation and embodiment conclusions remain untested by P02 itself.

These limitations must propagate to Phase Analysis, Layer 0, Evidence Map, Layer 10 and any cumulative/public synthesis using the affected evidence.

## 7.28 Freeze and closure decision

**P02_PROTOCOL_V1_ANNEX_R2_FROZEN_AFTER_SOURCE_COMPLETE_PRE_CLOSURE_AUDIT**

- Phase 02 execution: **ACCEPTED_FOR_PROTOCOL_AND_PHASE_ANALYSIS**;
- evidence sufficiency: **PASS** (`G23=PASS`, `G24=PASS`, blockers `[]`);
- documentary blockers after R2 repair: **0**;
- A0: **COMPLETE**, including explicit non-success terminals;
- A4: **COMPLETE FOR THE GOVERNED RESOURCE-CONSTRAINED ANCHOR-BUDGET/SINGLE-REPEAT SCOPE**;
- full Build Book A4 replication equivalence: **NO**;
- Stage18S: **PASS, POST-HOC DESCRIPTIVE SENSITIVITY ONLY**;
- Stage11 canonical evidence: **mixed grandfathered author/source-centered accepted lineage; exact recipe counts frozen in §7.9**;
- Stage12 canonical evidence: **author/source-centered accepted successor with explicit post-observation change authority**;
- scientific rerun required for Protocol documentary closure: **NO**;
- preferred downstream P02 heavy-artifact source: `Csthv/p02-phase02-final-whole-working-20260814t052120z-b890ff92@bc14961e14f2e48690e55df3577014275f9cbf30`;
- archival fallback: `Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260814t051352z@257a407b5c7ea37b6c620863ee261c010c8f197c`;
- mixed pre-P02/P02 private-HF access: **DUAL SYMBOLIC CREDENTIAL INTERFACE REQUIRED**;
- live remote HF verification in this audit: **UNAVAILABLE/PRIVATE; locally preserved immutable receipt/manifest evidence validated**;
- future cumulative merge: **READY WITHOUT SEMANTIC RECONSTRUCTION**;
- R1 disposition: **SUPERSEDED BY R2 FOR DOCUMENTARY/MACHINE-READABLE CORRECTIONS ONLY; SCIENTIFIC EVIDENCE UNCHANGED**.

# APPENDIX A — MACHINE-READABLE COMPANION FILES

The following companion files are deterministic structured projections of this annex; they do not supersede the canonical Markdown:

- `machine_readable/P02_run_matrix.yaml` — exact accepted stage/run matrix and A0/A4 terminal summaries;
- `machine_readable/P02_analysis_contract.yaml` — metrics, statistical rules, A4 claim restrictions, Stage18S status and interpretation ceiling;
- `machine_readable/P02_external_artifact_access_contract.yaml` — preferred workspace snapshot, archival fallback, immutable revisions and dual-secret interface.

If a machine-readable file and this Markdown disagree, the disagreement is a **freeze-critical Protocol defect** to be corrected before downstream use; neither side may be silently preferred.

# APPENDIX B — MINIMUM PHASE-ANALYSIS INPUT SET

The accepted run exposes at least the following controlling analysis inputs through the Protocol handoff and runtime bundle:

- `runtime/analysis_inputs/a0_completion.json`;
- `runtime/analysis_inputs/a4_completion.json`;
- `runtime/analysis_inputs/a4_role_control_statistics.json`;
- `runtime/analysis_inputs/a4_c4_c5_statistics.json`;
- `runtime/analysis_inputs/a4_c4_c5_comparison_artifacts.jsonl`;
- `runtime/analysis_inputs/a4_burden_source.csv`;
- `runtime/analysis_inputs/stage18_resource_constrained_anchor_budget_deviation.json`;
- `runtime/analysis_inputs/figure_table_source_manifest.json`;
- `runtime/analysis_inputs/failure_negative_summary.json`;
- `runtime/analysis_inputs/a0_closure_source_manifest.json`;
- `runtime/analysis_inputs/a0_participant_metrics.csv`;
- `runtime/analysis_inputs/a0_statistics.json`;
- `runtime/analysis_inputs/a4_participant_metrics.csv`;
- `runtime/analysis_inputs/a4_role_control_participant_comparisons.csv`;
- `runtime/analysis_inputs/a4_c4_c5_participant_comparisons.csv`;
- `runtime/analysis_inputs/low_label_curve_summary.json` and `low_label_metric_source.csv`;
- `runtime/analysis_inputs/subject_profile_summary.json`, `subject_profile_metric_source.csv`, and `session_profile_metric_source.csv`;
- `runtime/analysis_inputs/training_policy_challenger_participant_comparisons.jsonl`, `training_policy_challenger_seed_comparisons.jsonl`, and `training_policy_challenger_terminal_states.jsonl`;
- `runtime/analysis_inputs/training_policy_sr_probability_calibration_candidates.jsonl`;
- `runtime/analysis_inputs/stage18S_R1_combined_cell_effects.csv`, `stage18S_R1_participant_paired_effects.csv`, `stage18S_R1_three_repeat_anchor_stability.csv`, `stage18S_R1_six_budget_mr00_sensitivity.csv`, provenance summaries, and `stage18S_balanced_sensitivity_R1_preexecution_freeze.json`;
- `runtime/manifests/stage_artifacts/20_readiness.json` and canonical `Layer2ReadinessReport` partition;
- `runtime/analysis_inputs/training_policy_challenger_completion.json`;
- `runtime/analysis_inputs/training_policy_challenger_statistics.json`;
- `runtime/analysis_inputs/training_policy_sr_probability_selection.json`;
- `runtime/protocol_change_required/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml`;
- `runtime/handoffs/stage18S_R1_sensitivity_evidence.json` for separately labeled supplemental sensitivity evidence.

Phase Analysis must consume primitive/source records and these governed summaries without Layer 10 recomputation or result-selection changes.

# APPENDIX C — FINAL NO-DRIFT RULES

1. Do not rewrite post-observation Stage 11/12 amendments as pre-registered.
2. Do not merge Stage 18S into canonical Stage 18 or use it to erase the A4 deviation.
3. Do not claim five-repeat A4 stability, dense deep-budget A4 curves, or full Build Book A4 equivalence.
4. Do not omit failed/skipped/blocked/incompatible/non-applicable terminal states.
5. Do not change P01 dataset/split/label/window/low-label membership identities in a downstream analysis of this run.
6. Do not use test evidence for retrospective model/policy selection.
7. Do not choose `latest` for private external artifacts; pin exact revisions and verify hashes/manifests.
8. Do not assume a single Hugging Face credential covers both pre-P02 and P02 assets.
9. Do not serialize, print, log, or publish any literal access token.
10. Do not elevate P02 decoder/readiness evidence into calibration, safety, deployment, policy, robustness or clinical claims.
11. Do not let Layer 10 rerun, retune, reclassify, or strengthen P02 evidence.
12. Do not merge this annex into the cumulative Protocol by paraphrasing away run IDs, deviations, limitations or supersession history.

**END OF PHASE 02 PROTOCOL v1.0 ANNEX R2**
