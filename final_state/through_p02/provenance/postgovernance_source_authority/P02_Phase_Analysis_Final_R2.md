---
title: "IHARQ BenchGuard Stretch C - Phase 02 / Layer 2 Evidence, Results, and Interpretation Report"
subtitle: "Decoder and Baseline Measurement Spine - Paper-Oriented Scientific Analysis"
phase_id: P02
layer_id: L2
analysis_release_id: P02-PHASE-ANALYSIS-FINAL-R2
run_id: P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d
revision: Final R2
status: FINALIZED_WITH_EXPLICIT_NONBLOCKING_LIMITATIONS
---

# IHARQ BenchGuard Stretch C
## Phase 02 / Layer 2 - Phase Evidence, Results, and Interpretation Report
### Decoder and Baseline Measurement Spine - Final R2

**Canonical run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`  
**Analysis release:** `P02-PHASE-ANALYSIS-FINAL-R2`  
**Protocol authority:** IHARQ Protocol v1.0 through P02; finalized P02 Annex R2  
**Primary layer:** L2 - Decoder and Baseline Measurement Spine  
**Document role:** scientific analytical record of Phase 02  

> **Evidence hierarchy used in this report.** Project measurements are separated from supported interpretations, candidate claims, and mechanism hypotheses. Candidate claims remain pending Layer 0 review. Stage 18S is post-hoc descriptive sensitivity evidence and is never merged into confirmatory Stage 18. The resource-constrained A4 scope is treated as evidence-sufficient for its authorized scope, not as equivalent to the complete original Build Book grid.

> **Final analytical closure.** This Final R2 revision is the last evidence-closure pass before Layer 0. It re-triangulates upstream expectations, canonical execution, the 38 Protocol-authorized Phase Analysis inputs, supporting runtime diagnostics/negative-evidence records, and the narrative interpretation. The finalization adds exact low-label interval/ranking analysis, exact Stage-12 diagnostic deltas, participant-heterogeneity summaries, failure-category accounting, A4 burden summaries, phase/stage/ablation/model/dataset/metric/failure coverage matrices, claim-readiness/prohibited-wording controls, and a fresh primary-source literature verification record. It introduces **no new confirmatory statistical test family** and does not reopen the finalized Protocol. Remaining limitations are properties of the lawful P02 evidence, not unresolved analytical omissions.

# Executive Scientific Summary

Phase 02 is the first IHARQ phase that turns the frozen public-EEG substrate produced by P01 into a governed **decoder and baseline measurement spine**. The phase evaluates plural classical, Riemannian, compact/deep neural, and pretrained/foundation-model branches under a common subject-grouped test protocol; preserves prediction and checkpoint provenance; measures raw accept-all decoder behavior; creates low-label and participant/session evidence; and executes the ordinary A4 longer-window, multi-view, and ensemble controls. It does **not** own calibration, thresholding, abstention, readiness policy, clinical safety, temporal trust, stress robustness, simulation, or embodiment.

The accepted A0 run closed **678/678** planned cells: **657 SUCCESS, 3 FAILED, 15 CONDITIONAL_SKIP, and 3 DEPENDENCY_BLOCKED**. This is scientifically important because P02 does not present only successful decoders: unsuccessful branches, unsupported dependencies, and low-label failures remain part of the evidence.

The dominant A0 result is **heterogeneity rather than a universal winner**. At full training, CSP-LDA was descriptively highest on BNCI2014_001 (BACC 0.639), but that dataset has only one held-out test participant and therefore cannot support participant-level inference. DBConformer (`DNN-SEQ`) had the highest participant-first mean BACC on Lee2019_MI (0.795) and PhysioNetMI (0.650). On PhysioNetMI the eight-model Friedman test detected overall heterogeneity (statistic 20.544, p=0.00451, Kendall W=0.267), while Lee2019_MI did not (p=0.148). Crucially, no governed alternative-versus-CSP-LDA pairwise comparison survived Holm correction on either multi-participant dataset. The defensible conclusion is therefore not “model X wins,” but that **decoder behavior depends materially on dataset and participant context**.

Low-label decoding was difficult. Across the frozen 1, 2, 4, 8, 16, and 32 labels/class budgets, the four governed low-label branches often remained near chance, rankings changed with budget and dataset, and CSP-LDA at one label/class was explicitly non-success on all three datasets. Because P01 froze **one exact subset per budget**, these curves characterize the executed subsets; they do not establish repeated-subset sample-efficiency stability.

The Stage 11/12 correction history is itself a methodological result. Stage 11 did not simply “switch EEGNet to a better hyperparameter set.” The accepted primary EEGNet lineage is explicitly mixed: 101 primary cells remain sealed under the prior P500 recipe and four under R6 P120/FLOOR500; 15 later TRUE_P120/FLOOR1 R7 cells belong to a diagnostic challenger. Stage 12 likewise demonstrates why model-specific source/author recipes matter: targeted validation diagnostics show that source-centered candidate configurations can rescue some collapsed generic configurations, but not every confirmation trajectory succeeds. The scientifically bounded lesson is that **optimization failure can confound model evaluation**, not that author settings guarantee superior test performance.

A4 closed all six official conditions across all three datasets, but under a documented compute-driven deviation. The canonical Stage 18 surface comprises **1,218 terminal cells**: 591 SUCCESS, 576 CONDITIONAL_SKIP, 9 INPUT_INCOMPATIBLE, and 42 NOT_APPLICABLE_REPEAT_SLOT. All conditions, datasets, model-family roles, and representations were retained, but refit repeats were reduced from 0-4 to repeat 0 and deep refits were limited to **1/class, 8/class, and FULL_TRAIN** anchors. This reduced estimated unique deep member fits from 840 to 72 (91.4% reduction) while preserving the comparison identities and test-isolation rules. Consequently, A4 supports anchor-budget/single-repeat conclusions but **not** five-repeat stability, a dense deep-budget response curve, or full original-grid replication equivalence.

Within this governed A4 scope, the ordinary C1-C3 role controls produced **no raw p<=0.05 result across 756 statistical rows**. Effects were generally small and heterogeneous. Among C4/C5 ensemble-versus-strongest-constituent comparisons, only one row survived Holm correction: PhysioNetMI full-training hard voting at ensemble repeat 4 underperformed the validation-selected EEGNet constituent (median delta BACC -0.0435; raw p=0.0186; Holm p=0.0371; rank-biserial -0.788; 95% bootstrap CI -0.1304 to -0.0119). This is a useful negative result: adding an ensemble operation is not automatically beneficial.

Stage 18S strengthens the **limitation diagnosis**, not the confirmatory claim. Across 45 three-repeat anchor trajectories, 22 had mixed signs, while all 15 MR00 six-budget trajectories changed sign somewhere across supervision budgets. This sensitivity is descriptive/post-hoc and does not retroactively create the five-repeat confirmatory evidence that canonical Stage 18 lacks.

The external literature supports the methodological framing but not direct numerical benchmarking. EEGNet was introduced as a compact depthwise/separable CNN intended to generalize across BCI paradigms and limited-data regimes; FBCNet explicitly encodes filter-bank and variance structure for MI; DBConformer combines temporal and spatial conformer branches; CBraMod is a criss-cross pretrained EEG foundation model. Their original datasets, tasks, splits, supervision amounts, and evaluation regimes differ materially from IHARQ's binary subject-grouped protocol. P02 therefore uses those studies as **architecture/training-context references**, not as an apples-to-apples leaderboard.

# 1. Phase 02 Scientific Role and Scope

## 1.1 Layer 2 responsibility

The finalized Protocol defines L2 as a **measurement layer**. P02 consumes the exact P01 dataset, split, preprocessing, label, core-window, A4-window, and low-calibration identities. It trains or qualifies decoder families, records prediction/score evidence, measures raw accept-all behavior, builds participant/session and low-label profiles, executes A4 controls, and emits a fail-closed readiness record.

The phase boundary is analytically essential. A high BACC in P02 is not a calibrated confidence estimate, and a low BACC is not a readiness-policy decision. Calibration, uncertainty, thresholding, abstention/selective prediction, temporal/stress robustness, simulation, and embodiment are downstream responsibilities.

## 1.2 Cumulative progression from P00 and P01

P00 established the engineering, schema, authority, validation, and claim-governance foundation. P01 established the public-data contract: three source datasets, frozen subject groups, legal binary left/right labels, preprocessing/window identities, low-calibration populations, leakage checks, A4 matching substrate, and downstream pointers. P02 **inherits** rather than re-derives that substrate. This continuity is important because decoder differences can then be interpreted as Layer-2 evidence rather than as artifacts of silently changing split membership or preprocessing.

P01's most relevant inherited facts are: 172 subject groups across the three sources; train/calibration/validation/test subject counts 102/35/17/18; 12,910 accepted parent events mapped to 12,910 valid core windows; the official 3 s 160 Hz core window; the matched 3.5 s A4 family; and one frozen low-calibration subset at each budget {1,2,4,8,16,32} per class. P02's preflight confirmed these identities without mutating P00/P01.

### 1.3 Research questions answered by P02

The finalized Protocol and executed analysis contract support five paper-oriented questions:

- **RQ1 - Decoder landscape:** How do admitted Layer-2 decoder families differ across the three frozen datasets and held-out participants under full training?
- **RQ2 - Supervision sensitivity:** How do the four governed low-label branches behave across the inherited {1,2,4,8,16,32} labels/class budgets, and what can be concluded under a single frozen-subset design?
- **RQ3 - Training fidelity:** What does the Stage 11/12 amendment history reveal about separating optimization/training-policy failure from architectural incapacity, without turning diagnostic searches into claim-bearing test evidence?
- **RQ4 - A4 controls:** Within the resource-constrained but protocol-authorized A4 scope, do longer windows, multi-view decoding, or ordinary model ensembles provide reproducible advantages over their governed references?
- **RQ5 - Reliability boundary:** Which failures, incompatibilities, participant effects, repeat/budget sensitivities, and evidence limitations must travel downstream with the P02 decoder substrate?

### 1.4 Continuity with established P01 findings

| Earlier finding | P02 relationship | P02 analytical consequence |
|---|---|---|
| `P01-FIND-014` frozen P02 data contract | **INHERITS / CONFIRMS consumption** | P02 evaluates decoders without silently relabeling, rewindowing, or changing subject roles. |
| `P01-FIND-007` frozen low-calibration budget identities | **EXTENDS** | The inherited identities become actual low-label decoder measurements in P02. |
| `P01-FIND-008` A0-A13 Layer-1 readiness | **EXTENDS for A0/A4; DOES_NOT_TEST the rest** | P02 executes A0 and A4 while preserving the downstream status of the other ablations and A14 prohibition. |
| `P01-FIND-009/010` matched A4 R2 substrate and 3.5 s feasibility correction | **EXTENDS** | P02 uses the matched 3.5 s A4 substrate for controlled decoder comparisons rather than revisiting Layer-1 feasibility. |
| `P01-FIND-011` environment/resource amendments preserved the frozen core contract | **INHERITS** | P02 likewise distinguishes execution amendments from scientific identity and records compute-driven scope limits explicitly. |

# 2. Governing Analytical Contract

The finalized Protocol v1.0 freezes 38 canonical P02 analysis inputs. This report does not introduce a new confirmatory analysis family. The inferential unit is the participant where available. BACC is primary, macro-F1 is complementary, ACC is secondary, and ROC-AUC is conditional on valid score semantics. The frozen procedures use 95% confidence intervals, 10,000-resample participant-cluster bootstrap (BCa where available, otherwise governed fallback), paired two-sided Wilcoxon tests, Friedman omnibus tests for multi-model comparisons, Holm correction within governed families, and effect sizes including rank-biserial correlation or Kendall W. The minimum paired participant count is five. Cross-dataset synthesis is stratified/descriptive; no confirmatory cross-dataset meta-analysis is authorized.

# 3. Data, Split, and Evaluation Context

| Dataset | P02 test participants | P02 test windows | Source context | Key interpretive consequence |
|---|---:|---:|---|---|
| BNCI2014_001 | 1 | 288 | BCI Competition IV 2a source family; IHARQ uses a binary left/right subset and its own subject-group roles | Dataset-level performance is descriptive; participant-level inferential tests are not available. |
| Lee2019_MI | 6 | 600 | OpenBMI / Lee et al. public EEG dataset | Supports participant-paired statistics, but n remains modest. |
| PhysioNetMI | 11 | 495 | PhysioNet EEG Motor Movement/Imagery source | Largest P02 held-out participant group and strongest basis for participant-level inference. |

The core P02 signal identity is inherited from P01: 160 Hz, 8-32 Hz processing, 3 s core windows (480 samples), binary legal left/right task, float32 storage, and subject-disjoint roles. A4 additionally consumes the matched 3.5 s substrate (560 samples) and its registered multi-view members. These are **IHARQ conditions**; they should not be equated with the original papers' training/test protocols.

# 4. Models and Method Families

P02 deliberately spans heterogeneous decoder families rather than treating “deep learning” as a single comparator. The A0 scientific surface includes sanity/diagnostic branches, classical CSP/FBCSP, Riemannian tangent-space/alignment/MDM methods, EEGNet, FBCNet, DBConformer in the `DNN-SEQ` slot, CBraMod, and governed skipped/blocked alternatives. `DNN-EGTC` is a conditional fallback and was skipped; `SSL-REVE` remained dependency-blocked. Their absence is preserved rather than silently removing them from the planned family accounting.

For interpretive purposes, the principal branches are:

- **CSP-LDA / FBCSP-LR**: spatial/filter-bank classical baselines;
- **RIE-TS-LR / RIE-EA-TS / RIE-MDM**: covariance/Riemannian baselines;
- **EEGNet**: compact depthwise/separable CNN;
- **FBCNet**: filter-bank CNN with variance aggregation;
- **DBConformer**: dual temporal/spatial conformer architecture;
- **CBraMod**: pretrained criss-cross EEG foundation-model branch.

# 5. Phase 02 Execution Evolution

## 5.1 Preflight through baseline families

Stages 00-10 established authority/input integrity, loaded inherited P01 state, resolved branch/configuration semantics, and executed the deterministic/classical/Riemannian foundation. Two engineering/runtime-successor episodes in Stages 08-10 repaired class-weight applicability and canonical low-cal budget parsing without changing the scientific configuration. These matter for reproducibility but do not create new scientific comparisons.

## 5.2 Stage 11 - EEGNet and training-policy history

Stage 11 is scientifically important because its accepted state is **not** one homogeneous rerun. The post-observation correction identified that the R6 continuation displayed patience 120 while retaining `min_epochs_before_early_stop=500`; therefore it could not stop before epoch 500. The prospective R7 continuation changed the active rule for remaining/unsealed fits to true patience 120 from epoch 1, while explicitly grandfathering already sealed evidence.

Canonical primary A0 provenance is therefore:

| EEGNet primary/challenger provenance | Cell count | Scientific role |
|---|---:|---|
| P500 / FLOOR500 sealed primary | 101 | Canonical primary A0 |
| R6 P120 / FLOOR500 sealed primary | 4 | Canonical primary A0 |
| R7 TRUE_P120 / FLOOR1 | 15 | Diagnostic challenger only |

This historical distinction prevents a post-hoc rewrite such as “all EEGNet primary cells used the final R7 recipe.” They did not.

The separate S&R diagnostic challenger was selected by validation-only probability search (candidates 0.25, 0.5, 0.75; test access prohibited). Its test-set participant comparison against the canonical primary does **not** show a consistent improvement:

| Dataset      |   Participant pairs |   Median ΔBACC |   95% CI low |   95% CI high |   Wilcoxon p |   Rank-biserial |
|:-------------|--------------------:|---------------:|-------------:|--------------:|-------------:|----------------:|
| BNCI2014_001 |                   5 |         -0.035 |       -0.076 |        -0.035 |       0.125  |          -0.867 |
| Lee2019_MI   |                  30 |          0.01  |       -0.005 |         0.025 |       0.2309 |           0.259 |
| PhysioNetMI  |                  55 |          0     |       -0.034 |         0.003 |       0.4552 |          -0.119 |

The BNCI median effect was negative, Lee positive but small, and PhysioNet exactly zero; none of the Wilcoxon tests reached p<=0.05. This is a useful negative finding: the diagnostic augmentation/selection challenger should not be retrospectively presented as the reason canonical EEGNet performs as it does.

![Stage 11 diagnostic challenger participant-level effects](figures/P02_Figure_04_training_policy_challenger_effect.png)

## 5.3 Stage 12 - source/author-centered external models

Stage 12 underwent a scientifically material source-centered amendment. The canonical accepted recipes include, among other details, FBCNet batch size 16, Adam lr=0.001, max 1500 epochs and patience/no-decrease window 200; DBConformer batch 32, Adam lr=0.001, max 150 and patience 40; and CBraMod with AdamW, separate body/head learning rates, governed scaling, max 150 and patience 40. Test data were excluded from hyperparameter selection.

A preserved validation-only A/B/C diagnostic subset demonstrates exactly why the correction mattered and exactly where its evidentiary boundary lies:

| Dataset      | Branch      |   A BACC | A collapsed   |   B BACC | B collapsed   |    ΔBACC |   Δ percentage points |   C confirm mean BACC |   C confirm SD |   C collapsed |   C n |
|:-------------|:------------|---------:|:--------------|---------:|:--------------|---------:|----------------------:|----------------------:|---------------:|--------------:|------:|
| BNCI2014_001 | DNN-FBCNET  | 0.500000 | True          | 0.722222 | False         | 0.222222 |             22.222222 |              0.500000 |       0.000000 |             5 |     5 |
| PhysioNetMI  | DNN-FBCNET  | 0.639509 | False         | 0.660104 | False         | 0.020595 |              2.059457 |              0.652615 |       0.028169 |             0 |     5 |
| PhysioNetMI  | DNN-SEQ     | 0.698550 | False         | 0.716794 | False         | 0.018244 |              1.824371 |              0.713248 |       0.010908 |             0 |     5 |
| PhysioNetMI  | SSL-CBRAMOD | 0.500000 | True          | 0.638407 | False         | 0.138407 |             13.840729 |              0.646753 |       0.004518 |             0 |     5 |

The **A→B validation changes** were +0.222222 BACC (+22.222222 percentage points) for BNCI2014_001 FBCNet, +0.020595 (+2.059457 points) for PhysioNetMI FBCNet, +0.018244 (+1.824371 points) for PhysioNetMI DBConformer, and +0.138407 (+13.840729 points) for PhysioNetMI CBraMod. The A configuration was collapsed at BACC=0.500000 for BNCI FBCNet and PhysioNet CBraMod; the B configuration was not collapsed in either case. The five-run C confirmation then exposed an important asymmetry: BNCI FBCNet returned to an exact mean BACC of 0.500000 with 5/5 collapsed confirmation runs, whereas PhysioNet FBCNet, DBConformer, and CBraMod had 0/5 collapsed confirmation runs with mean BACC 0.652615, 0.713248, and 0.646753 respectively.

These are **validation-only, non-claim-bearing diagnostics** (`test_role_loaded=false`, `claim_bearing=false` in all four job summaries). They demonstrate that training/optimization choices can materially alter apparent viability, not that the B candidate is a universal test-set improvement. The scientifically defensible conclusion is therefore architecture- and dataset-dependent optimization sensitivity: a generic training policy can make a viable architecture appear collapsed, while source-centered settings do not guarantee stability or superiority. Canonical model effectiveness remains governed by A0.

The exact source-preserving values are in `table_sources/P02_Table_Stage12_validation_before_after_exact.csv`.

## 5.4 Canonical downstream closure

Stages 13-17 consolidated low-label, participant/session, A0, and analysis-input evidence. Stage 18 executed A4 under the authorized resource deviation; Stage 18U and the separate Stage 18S family provided closure/supplementary evidence without changing canonical G18. Stages 19-24 preserved negative evidence, readiness, figure/table sources, protocol/analysis handoffs, downstream bundles, and release/finalization. All governed gates through final closure passed with no unresolved blocker.

# 6. A0 - Full Scientific Analysis

## 6.1 Completion and terminal outcomes

A0 completed **678/678** planned cells. Terminal accounting was:

| Terminal status | Count |
|---|---:|
| SUCCESS | 657 |
| FAILED | 3 |
| CONDITIONAL_SKIP | 15 |
| DEPENDENCY_BLOCKED | 3 |

The three FAILED cells are the one-label/class CSP-LDA low-label cells, one in each dataset. The 15 conditional skips correspond to the E-GTC fallback branch; the three dependency blocks belong to SSL-REVE. Their explicit preservation matters because a benchmark that silently drops unsupported or failed methods can create a misleading impression of universal executability.

## 6.2 Full-training model performance

Participant-first full-training summary:

| Dataset              | Model       |   participants |   BACC_mean |   BACC_median | BACC_sd   |   F1_mean |   ACC_mean |   ROC_AUC_mean |
|:---------------------|:------------|---------------:|------------:|--------------:|:----------|----------:|-----------:|---------------:|
| BNCI2014_001         | CSP-LDA     |              1 |       0.639 |         0.639 | NA        |     0.639 |      0.639 |          0.678 |
| BNCI2014_001         | FBCSP-LR    |              1 |       0.628 |         0.628 | NA        |     0.628 |      0.628 |          0.677 |
| BNCI2014_001         | EEGNet      |              1 |       0.609 |         0.609 | NA        |     0.598 |      0.609 |          0.645 |
| BNCI2014_001         | FBCNet      |              1 |       0.481 |         0.481 | NA        |     0.478 |      0.481 |          0.474 |
| BNCI2014_001         | DBConformer |              1 |       0.528 |         0.528 | NA        |     0.523 |      0.528 |          0.553 |
| BNCI2014_001         | EA-TS       |              1 |       0.611 |         0.611 | NA        |     0.584 |      0.611 |          0.699 |
| BNCI2014_001         | TS-LR       |              1 |       0.615 |         0.615 | NA        |     0.587 |      0.615 |          0.699 |
| BNCI2014_001         | CBraMod     |              1 |       0.551 |         0.551 | NA        |     0.534 |      0.551 |          0.572 |
| Lee2019_MI / OpenBMI | CSP-LDA     |              6 |       0.715 |         0.7   | 0.183     |     0.663 |      0.715 |          0.807 |
| Lee2019_MI / OpenBMI | FBCSP-LR    |              6 |       0.653 |         0.66  | 0.135     |     0.606 |      0.653 |          0.8   |
| Lee2019_MI / OpenBMI | EEGNet      |              6 |       0.742 |         0.725 | 0.176     |     0.723 |      0.742 |          0.806 |
| Lee2019_MI / OpenBMI | FBCNet      |              6 |       0.719 |         0.691 | 0.167     |     0.695 |      0.719 |          0.816 |
| Lee2019_MI / OpenBMI | DBConformer |              6 |       0.795 |         0.743 | 0.129     |     0.785 |      0.795 |          0.883 |
| Lee2019_MI / OpenBMI | EA-TS       |              6 |       0.752 |         0.78  | 0.198     |     0.709 |      0.752 |          0.853 |
| Lee2019_MI / OpenBMI | TS-LR       |              6 |       0.747 |         0.78  | 0.202     |     0.7   |      0.747 |          0.853 |
| Lee2019_MI / OpenBMI | CBraMod     |              6 |       0.668 |         0.643 | 0.163     |     0.646 |      0.668 |          0.729 |
| PhysioNetMI          | CSP-LDA     |             11 |       0.596 |         0.542 | 0.148     |     0.545 |      0.586 |          0.637 |
| PhysioNetMI          | FBCSP-LR    |             11 |       0.564 |         0.548 | 0.122     |     0.532 |      0.56  |          0.63  |
| PhysioNetMI          | EEGNet      |             11 |       0.628 |         0.579 | 0.124     |     0.613 |      0.63  |          0.691 |
| PhysioNetMI          | FBCNet      |             11 |       0.618 |         0.562 | 0.128     |     0.592 |      0.617 |          0.701 |
| PhysioNetMI          | DBConformer |             11 |       0.65  |         0.598 | 0.135     |     0.642 |      0.654 |          0.695 |
| PhysioNetMI          | EA-TS       |             11 |       0.618 |         0.561 | 0.116     |     0.594 |      0.618 |          0.694 |
| PhysioNetMI          | TS-LR       |             11 |       0.613 |         0.562 | 0.118     |     0.587 |      0.614 |          0.697 |
| PhysioNetMI          | CBraMod     |             11 |       0.545 |         0.493 | 0.092     |     0.54  |      0.544 |          0.557 |

![A0 full-training model performance by dataset](figures/P02_Figure_01_A0_fulltrain_model_by_dataset.png)

Three patterns dominate.

First, **the ranking is not stable across datasets**. CSP-LDA is descriptively strongest on BNCI2014_001, while DBConformer is strongest by participant-first mean BACC on Lee2019_MI and PhysioNetMI. EEGNet, Riemannian tangent-space variants, and FBCNet form a relatively competitive middle tier on the two multi-participant datasets, but the exact order changes.

Second, the numeric spread is not negligible. On Lee2019_MI, participant-first mean BACC ranges from 0.795 for DBConformer to 0.653 for FBCSP-LR among the principal successful branches shown above; on PhysioNetMI it ranges from 0.650 for DBConformer to 0.545 for CBraMod. Yet these mean differences coexist with substantial participant variability and multiplicity-adjusted pairwise uncertainty.

Third, CBraMod does not automatically dominate because it is pretrained/foundation-scale. Under this P02 task and adaptation protocol, its participant-first mean BACC was 0.668 on Lee2019_MI and 0.545 on PhysioNetMI, below several task-specific and classical/Riemannian branches. This is not evidence against foundation models generally; it is evidence that **pretraining scale does not remove task-, adaptation-, and protocol-dependence**.

## 6.3 Governed statistical comparison

| Dataset              |   n | Status           | Friedman   | p        | Kendall W   |
|:---------------------|----:|:-----------------|:-----------|:---------|:------------|
| BNCI2014_001         |   1 | DESCRIPTIVE_ONLY | NA         | NA       | NA          |
| Lee2019_MI / OpenBMI |   6 | PASS             | 10.781     | 0.1485   | 0.257       |
| PhysioNetMI          |  11 | PASS             | 20.544     | 0.004507 | 0.267       |

PhysioNetMI shows a statistically detectable global model effect (p=0.00451), with Kendall W=0.267 indicating a modest-to-moderate rank-consistency effect rather than overwhelming dominance. Lee2019_MI's omnibus p=0.148 does not support rejecting equal model ranks under the governed test. BNCI2014_001 has one test participant and is correctly descriptive-only.

The paired alternative-versus-CSP-LDA post-hoc results are:

| Dataset              | Alternative   |   Median ΔBACC |   raw p |   Holm p |   Rank-biserial |   95% CI low |   95% CI high |
|:---------------------|:--------------|---------------:|--------:|---------:|----------------:|-------------:|--------------:|
| Lee2019_MI / OpenBMI | FBCSP-LR      |         -0.035 | 0.4688  |        1 |          -0.381 |       -0.36  |         0.06  |
| Lee2019_MI / OpenBMI | EEGNet        |          0.025 | 0.1875  |        1 |           0.733 |       -0.005 |         0.056 |
| Lee2019_MI / OpenBMI | FBCNet        |          0.004 | 0.8438  |        1 |           0.143 |       -0.042 |         0.034 |
| Lee2019_MI / OpenBMI | DBConformer   |          0.129 | 0.1562  |        1 |           0.714 |       -0.043 |         0.151 |
| Lee2019_MI / OpenBMI | EA-TS         |          0.04  | 0.3438  |        1 |           0.476 |       -0.065 |         0.1   |
| Lee2019_MI / OpenBMI | TS-LR         |          0.04  | 0.5625  |        1 |           0.333 |       -0.075 |         0.1   |
| Lee2019_MI / OpenBMI | CBraMod       |         -0.062 | 0.09375 |        1 |          -0.81  |       -0.098 |        -0.012 |
| PhysioNetMI          | FBCSP-LR      |         -0.042 | 0.2783  |        1 |          -0.394 |       -0.113 |         0.02  |
| PhysioNetMI          | EEGNet        |          0.035 | 0.123   |        1 |           0.545 |       -0.033 |         0.056 |
| PhysioNetMI          | FBCNet        |          0.053 | 0.3203  |        1 |           0.364 |       -0.066 |         0.062 |
| PhysioNetMI          | DBConformer   |          0.062 | 0.06738 |        1 |           0.636 |       -0.019 |         0.081 |
| PhysioNetMI          | EA-TS         |          0.063 | 0.2783  |        1 |           0.394 |       -0.119 |         0.098 |
| PhysioNetMI          | TS-LR         |          0.063 | 0.3652  |        1 |           0.333 |       -0.143 |         0.099 |
| PhysioNetMI          | CBraMod       |         -0.012 | 0.2402  |        1 |          -0.424 |       -0.176 |         0.013 |

No Holm-adjusted pairwise comparison is significant. This is not a contradiction with the PhysioNet omnibus result: an omnibus test can detect overall rank heterogeneity while the individual reference contrasts lack multiplicity-adjusted evidence. It is therefore scientifically inappropriate to turn the descriptive DBConformer lead into a confirmatory claim that DBConformer is superior to CSP-LDA.

## 6.4 Participant heterogeneity

![Lee2019_MI participant distributions](figures/P02_Figure_02_Lee2019_MI_participant_distribution.png)

![PhysioNetMI participant distributions](figures/P02_Figure_02_PhysioNetMI_participant_distribution.png)

Participant variation is large enough to change the interpretation of mean rankings. On Lee2019_MI, DBConformer spans **0.662000-0.964000** across six test participants (SD 0.129050), while CSP-LDA spans **0.500000-0.990000** (SD 0.182729) and TS-LR spans **0.510000-1.000000** (SD 0.201660). On PhysioNetMI, DBConformer spans **0.516071-0.929447** across eleven participants (SD 0.135274), CSP-LDA spans **0.444664-0.867589** (SD 0.147744), and TS-LR spans **0.509881-0.888340** (SD 0.117579). Thus, a branch that has the best participant-first mean can still be substantially weaker for particular individuals.

A complementary descriptive difficulty summary averages BACC across the nine main full-training branches **within each participant**; it is not a personalization-policy test and it does not choose a model from the participant's test result. Selected low/high participants are:

| Dataset     |   Participant ID |   Branches |   Mean BACC across main branches |      Min |      Max |
|:------------|-----------------:|-----------:|---------------------------------:|---------:|---------:|
| Lee2019_MI  |                6 |          9 |                         0.574667 | 0.490000 | 0.746000 |
| Lee2019_MI  |               15 |          9 |                         0.596667 | 0.490000 | 0.760000 |
| Lee2019_MI  |               30 |          9 |                         0.598000 | 0.514000 | 0.708000 |
| Lee2019_MI  |               19 |          9 |                         0.774222 | 0.650000 | 0.870000 |
| Lee2019_MI  |                3 |          9 |                         0.829333 | 0.610000 | 0.950000 |
| Lee2019_MI  |               36 |          9 |                         0.896222 | 0.630000 | 1.000000 |
| PhysioNetMI |                6 |          9 |                         0.505820 | 0.431548 | 0.559524 |
| PhysioNetMI |               98 |          9 |                         0.521871 | 0.444664 | 0.567589 |
| PhysioNetMI |               39 |          9 |                         0.524352 | 0.420949 | 0.629447 |
| PhysioNetMI |               48 |          9 |                         0.703469 | 0.500000 | 0.807115 |
| PhysioNetMI |               71 |          9 |                         0.740580 | 0.608696 | 0.929447 |
| PhysioNetMI |               93 |          9 |                         0.791634 | 0.545455 | 0.888340 |

For Lee2019_MI, the across-branch participant mean ranges from **0.574667** to **0.896222**; for PhysioNetMI it ranges from **0.505820** to **0.791634**. This confirms that heterogeneity is not merely a small change in branch ordering: some held-out participants are systematically difficult across many representation families. P02 therefore supports a heterogeneity finding and a motivation for future participant-aware work, but **does not validate personalization or model routing**.

Exact participant/model dispersion and participant difficulty summaries are preserved in `table_sources/P02_Table_participant_heterogeneity_summary.csv` and `table_sources/P02_Table_participant_difficulty_summary.csv`.

# 7. Low-Label / Budget Analysis

The governed low-label surface contains **216 metric-source rows**: three datasets × four eligible branches × six budgets × three metrics (BACC, macro-F1, ACC). At the run-cell level, **213/216 succeeded and 3/216 failed**; the three failures are CSP-LDA at 1 label/class, one per dataset. The curve artifact retains all legal budgets without interpolation. Every budget uses the same exact inherited single frozen subset identity, so these trajectories are reproducible but do not estimate variation over alternative subset draws.

## 7.1 BNCI2014_001

| Model   | 1        |        2 |        4 |        8 |       16 |       32 |
|:--------|:---------|---------:|---------:|---------:|---------:|---------:|
| CBraMod | 0.497917 | 0.506944 | 0.508333 | 0.520833 | 0.527778 | 0.516667 |
| CSP-LDA | NA       | 0.527778 | 0.604167 | 0.486111 | 0.527778 | 0.496528 |
| EEGNet  | 0.524306 | 0.525000 | 0.535417 | 0.541667 | 0.568750 | 0.507639 |
| TS-LR   | 0.541667 | 0.562500 | 0.590278 | 0.486111 | 0.520833 | 0.520833 |

![BNCI low-label curve](figures/P02_Figure_03_low_label_BNCI2014_001.png)

The exact BACC leader changes from TS-LR at 1/class (0.541667) and 2/class (0.562500), to CSP-LDA at 4/class (0.604167), to EEGNet at 8/class (0.541667) and 16/class (0.568750), and back to TS-LR at 32/class (0.520833). This sequence alone rules out a stable model ranking over the frozen budget path. The one held-out BNCI participant also makes all such changes descriptive-only.

## 7.2 Lee2019_MI

| Model   | 1        |        2 |        4 |        8 |       16 |       32 |
|:--------|:---------|---------:|---------:|---------:|---------:|---------:|
| CBraMod | 0.502667 | 0.484000 | 0.495667 | 0.510667 | 0.488000 | 0.492667 |
| CSP-LDA | NA       | 0.500000 | 0.496667 | 0.461667 | 0.566667 | 0.518333 |
| EEGNet  | 0.527333 | 0.498333 | 0.524333 | 0.522667 | 0.498000 | 0.522667 |
| TS-LR   | 0.501667 | 0.493333 | 0.498333 | 0.535000 | 0.570000 | 0.528333 |

![Lee low-label curve](figures/P02_Figure_03_low_label_Lee2019_MI.png)

The leader changes from EEGNet at 1/class (0.527333), to CSP-LDA at 2/class (0.500000), back to EEGNet at 4/class (0.524333), then to TS-LR at 8, 16 and 32/class (0.535000, 0.570000 and 0.528333). Even the 32/class values remain far below the corresponding full-training participant-first means: for example, TS-LR is 0.528333 at 32/class versus 0.746667 full training (Δ=-0.218333), while EEGNet is 0.522667 versus 0.741667 (Δ=-0.219000).

## 7.3 PhysioNetMI

| Model   | 1        |        2 |        4 |        8 |       16 |       32 |
|:--------|:---------|---------:|---------:|---------:|---------:|---------:|
| CBraMod | 0.494341 | 0.503863 | 0.493245 | 0.505408 | 0.506486 | 0.485537 |
| CSP-LDA | NA       | 0.545814 | 0.501886 | 0.515990 | 0.527848 | 0.503863 |
| EEGNet  | 0.491736 | 0.496982 | 0.498419 | 0.497054 | 0.525530 | 0.526249 |
| TS-LR   | 0.513026 | 0.500000 | 0.511498 | 0.502066 | 0.548239 | 0.521559 |

![PhysioNet low-label curve](figures/P02_Figure_03_low_label_PhysioNetMI.png)

The leader alternates repeatedly: TS-LR at 1/class (0.513026), CSP-LDA at 2/class (0.545814), TS-LR at 4/class (0.511498), CSP-LDA at 8/class (0.515990), TS-LR at 16/class (0.548239), and EEGNet at 32/class (0.526249). At 32/class, EEGNet is still 0.101262 BACC below its full-training mean (0.627511); TS-LR is 0.091669 below full training (0.613228).

## 7.4 Exact interval changes and rank reversals

The budget leaders are:

- **BNCI2014_001:** 1:TS-LR (0.541667), 2:TS-LR (0.562500), 4:CSP-LDA (0.604167), 8:EEGNet (0.541667), 16:EEGNet (0.568750), 32:TS-LR (0.520833).
- **Lee2019_MI:** 1:EEGNet (0.527333), 2:CSP-LDA (0.500000), 4:EEGNet (0.524333), 8:TS-LR (0.535000), 16:TS-LR (0.570000), 32:TS-LR (0.528333).
- **PhysioNetMI:** 1:TS-LR (0.513026), 2:CSP-LDA (0.545814), 4:TS-LR (0.511498), 8:CSP-LDA (0.515990), 16:TS-LR (0.548239), 32:EEGNet (0.526249).

The largest adjacent change for each branch/dataset is preserved rather than smoothed away:

- BNCI2014_001 / CSP-LDA: largest adjacent change ending at 8/class = -0.118056 BACC.
- BNCI2014_001 / EEGNet: largest adjacent change ending at 32/class = -0.061111 BACC.
- BNCI2014_001 / TS-LR: largest adjacent change ending at 8/class = -0.104167 BACC.
- BNCI2014_001 / CBraMod: largest adjacent change ending at 8/class = +0.012500 BACC.
- Lee2019_MI / CSP-LDA: largest adjacent change ending at 16/class = +0.105000 BACC.
- Lee2019_MI / EEGNet: largest adjacent change ending at 2/class = -0.029000 BACC.
- Lee2019_MI / TS-LR: largest adjacent change ending at 32/class = -0.041667 BACC.
- Lee2019_MI / CBraMod: largest adjacent change ending at 16/class = -0.022667 BACC.
- PhysioNetMI / CSP-LDA: largest adjacent change ending at 4/class = -0.043927 BACC.
- PhysioNetMI / EEGNet: largest adjacent change ending at 16/class = +0.028476 BACC.
- PhysioNetMI / TS-LR: largest adjacent change ending at 16/class = +0.046173 BACC.
- PhysioNetMI / CBraMod: largest adjacent change ending at 32/class = -0.020949 BACC.

These exact changes demonstrate why terms such as *sample efficiency*, *saturation*, or *diminishing returns* would be too strong here. Curves frequently reverse direction. Because P02 has only one frozen subset at each budget, the observed reversals cannot be cleanly partitioned into model response versus subset-composition effects.

## 7.5 Interpretation and claim ceiling

The strongest defensible conclusion is negative/qualified: **extreme label scarcity remains difficult and the frozen P02 design does not establish a stable universal sample-efficiency ordering among CSP-LDA, tangent-space LR, EEGNet and CBraMod.** The evidence does not support statements such as “EEGNet is more label-efficient than Riemannian methods,” “foundation-model pretraining solves low-label MI,” or “performance improves monotonically with labels.” A prospective repeated-subset experiment is required to estimate subset variance and a stable budget-response relationship.

Exact point values, full-training deltas, ranks, adjacent increments, leaders, and rank changes are preserved in `table_sources/P02_Table_low_label_exact_deltas_and_ranks.csv`, `P02_Table_low_label_interval_deltas.csv`, and `P02_Table_low_label_budget_leaders_and_rank_changes.csv`.

# 8. Secondary Metrics and Class-Wise Evidence

The governed metric hierarchy prevents a secondary score from silently replacing BACC. Macro-F1 is complementary, ACC is secondary, and ROC-AUC is conditional on valid score semantics. At full training the main BACC pattern is largely corroborated by macro-F1 and ACC, but AUC can rank score-producing branches differently:

| Dataset | BACC leader | Macro-F1 leader | ACC leader | Conditional ROC-AUC leader |
|---|---|---|---|---|
| BNCI2014_001 | CSP-LDA (0.639) | CSP-LDA (0.639) | CSP-LDA (0.639) | EA-TS (0.699) |
| Lee2019_MI | DBConformer (0.795) | DBConformer (0.785) | DBConformer (0.795) | DBConformer (0.883) |
| PhysioNetMI | DBConformer (0.650) | DBConformer (0.642) | DBConformer (0.654) | FBCNet (0.701) |

The first three metrics therefore support the main dataset-dependent BACC narrative without creating a separate winner-selection rule. The PhysioNet AUC ordering is a useful reminder that discrimination ranking based on continuous scores need not match the hard-decision BACC ordering. Because ROC-AUC is unavailable or semantically inapplicable for some branches, it is not used to produce a universal cross-family leaderboard.

The canonical 38-input Phase Analysis contract does **not** include a standalone confusion-matrix or class-wise error-summary artifact. Prediction records and score semantics are preserved in the execution substrate, but computing a new confusion-analysis family here would exceed the frozen Phase Analysis input contract. Accordingly, this report does not invent class-wise claims. A later governed analysis may use the preserved predictions if its own Protocol authorizes that computation.

`table_sources/P02_Table_A0_secondary_metric_leaders.csv` preserves the exact metric-leader values used in this section.

# 9. Model- and Family-Level Interpretation

## 9.1 Classical and Riemannian baselines

CSP-LDA remains a strong baseline: it leads BNCI descriptively and provides the governed reference for A0 post-hoc tests. Riemannian tangent-space/alignment variants are competitive on Lee and PhysioNet and sometimes exceed CSP-LDA descriptively. This is consistent with the broader BCI literature in which covariance/Riemannian representations can be competitive and data-efficient, but P02's exact task/split makes direct numerical comparison to older Riemannian papers inappropriate.

## 9.2 EEGNet

EEGNet is competitive on Lee/PhysioNet and remains a scientifically valuable compact neural baseline. Its Stage 11 history shows, however, that training-rule provenance is part of the result: the primary surface is mixed across grandfathered recipes. The diagnostic challenger does not provide a consistent improvement, so the final report separates **recipe-history correctness** from **performance superiority**.

## 9.3 FBCNet

FBCNet performs strongly on PhysioNet and reasonably on Lee but poorly on the single BNCI test participant. Stage12 diagnostics show both the value and limitation of author-centered optimization: a source-centered candidate can rescue a collapsed diagnostic configuration, yet confirmation may still fail. This fits the architecture's filter-bank/variance motivation while underscoring dataset-specific optimization sensitivity.

## 9.4 DBConformer

DBConformer is the descriptive full-training leader on Lee and PhysioNet. The original DBConformer paper emphasizes separate long-range temporal and inter-channel modeling and reports broad performance gains across several EEG paradigms. P02 is consistent with the possibility that such a dual representation is useful, but the current evidence does not isolate which architectural component caused the advantage, and Holm-adjusted reference comparisons do not establish confirmatory superiority.

## 9.5 CBraMod

CBraMod's weaker P02 A0 results relative to several smaller task-specific models are scientifically informative. The original model is a large pretrained criss-cross foundation architecture designed to generalize across diverse tasks and formats. P02 exercises a narrower binary MI transfer setting with governed model-local adaptation. The gap illustrates why “foundation model” should not be treated as a synonym for “automatically superior under every downstream supervision regime.” Mechanistic explanations remain hypotheses because P02 did not ablate pretraining, adapter design, or representation mismatch separately.

# 10. A4 - Full Scientific Analysis

## 10.1 Scientific purpose and conditions

A4 asks whether ordinary input/view/ensemble manipulations alter Layer-2 decoder evidence under controlled matched comparisons. The six official conditions are:

- C0: core reference;
- C1: longer 3.5 s window;
- C2: multi-view hard vote;
- C3: multi-view probability average;
- C4: model hard-vote ensemble;
- C5: model probability-average ensemble.

C1-C3 are compared against C0 within governed model-family roles. C4/C5 are compared against the validation-selected strongest constituent; test outcomes are prohibited from choosing that constituent.

## 10.2 Resource-constrained canonical design

The executed Stage18 design differs from the original high-cost Build Book surface:

| Design element | Original plan | Canonical Stage 18 |
|---|---|---|
| Refit repeat indices | 0,1,2,3,4 | 0 only |
| Deep refit budgets | full frozen budget grid | 1/class, 8/class, FULL_TRAIN anchors |
| Conditions | C0-C5 | C0-C5 preserved |
| Datasets | 3 | all 3 preserved |
| Refit roles | classical, neural, Riemannian, SSL | all preserved |
| Estimated unique deep member fits | 840 | 72 |
| Claim of full Build Book equivalence | intended target | explicitly **false** |

The 91.4% estimated reduction in unique deep member fits was a compute decision, not a change to the per-fit scientific recipe, representative-selection logic, test isolation, checkpoint round-trip rule, or statistical comparison definition.

A4 terminal accounting:

| Terminal status | Count |
|---|---:|
| SUCCESS | 591 |
| CONDITIONAL_SKIP | 576 |
| INPUT_INCOMPATIBLE | 9 |
| NOT_APPLICABLE_REPEAT_SLOT | 42 |

The distinction between **planned slots** and **executable canonical cells** is important: conditional skips represent declared reduction, not missing unexplained evidence.

## 10.3 C1-C3 role-control results

| Dataset              | role_id    | Condition          |   evaluable_effect_cells |   median_cell_effect |   positive_cells |   negative_cells |   zero_cells | min_raw_p   | min_holm_p   |
|:---------------------|:-----------|:-------------------|-------------------------:|---------------------:|-----------------:|-----------------:|-------------:|:------------|:-------------|
| BNCI2014_001         | CLASSICAL  | C1-LONG-3P5S       |                        6 |                0.009 |                4 |                2 |            0 | NA          | NA           |
| BNCI2014_001         | CLASSICAL  | C2-MULTI-HARD-VOTE |                        6 |                0.007 |                3 |                3 |            0 | NA          | NA           |
| BNCI2014_001         | CLASSICAL  | C3-MULTI-PROB-AVG  |                        6 |               -0.005 |                2 |                3 |            1 | NA          | NA           |
| BNCI2014_001         | NEURAL     | C1-LONG-3P5S       |                        3 |               -0.003 |                1 |                2 |            0 | NA          | NA           |
| BNCI2014_001         | NEURAL     | C2-MULTI-HARD-VOTE |                        3 |               -0.003 |                1 |                2 |            0 | NA          | NA           |
| BNCI2014_001         | NEURAL     | C3-MULTI-PROB-AVG  |                        3 |               -0.021 |                1 |                2 |            0 | NA          | NA           |
| BNCI2014_001         | RIEMANNIAN | C1-LONG-3P5S       |                        7 |                0.003 |                4 |                3 |            0 | NA          | NA           |
| BNCI2014_001         | RIEMANNIAN | C2-MULTI-HARD-VOTE |                        7 |                0.014 |                7 |                0 |            0 | NA          | NA           |
| BNCI2014_001         | RIEMANNIAN | C3-MULTI-PROB-AVG  |                        7 |                0.021 |                6 |                1 |            0 | NA          | NA           |
| BNCI2014_001         | SSL        | C2-MULTI-HARD-VOTE |                        3 |                0.052 |                3 |                0 |            0 | NA          | NA           |
| BNCI2014_001         | SSL        | C3-MULTI-PROB-AVG  |                        3 |                0.024 |                2 |                1 |            0 | NA          | NA           |
| Lee2019_MI / OpenBMI | CLASSICAL  | C1-LONG-3P5S       |                        6 |                0     |                1 |                1 |            4 | 0.125       | 0.375        |
| Lee2019_MI / OpenBMI | CLASSICAL  | C2-MULTI-HARD-VOTE |                        6 |                0     |                2 |                2 |            2 | 0.0625      | 0.375        |
| Lee2019_MI / OpenBMI | CLASSICAL  | C3-MULTI-PROB-AVG  |                        6 |                0     |                2 |                2 |            2 | 0.0625      | 0.375        |
| Lee2019_MI / OpenBMI | NEURAL     | C1-LONG-3P5S       |                        3 |               -0.005 |                1 |                2 |            0 | 0.125       | 0.375        |
| Lee2019_MI / OpenBMI | NEURAL     | C2-MULTI-HARD-VOTE |                        3 |               -0.005 |                1 |                2 |            0 | 0.4375      | 0.875        |
| Lee2019_MI / OpenBMI | NEURAL     | C3-MULTI-PROB-AVG  |                        3 |                0     |                1 |                1 |            1 | 0.3125      | 0.875        |
| Lee2019_MI / OpenBMI | RIEMANNIAN | C1-LONG-3P5S       |                        7 |                0     |                1 |                2 |            4 | 0.5         | 1            |
| Lee2019_MI / OpenBMI | RIEMANNIAN | C2-MULTI-HARD-VOTE |                        7 |                0     |                1 |                1 |            5 | 0.25        | 1            |
| Lee2019_MI / OpenBMI | RIEMANNIAN | C3-MULTI-PROB-AVG  |                        7 |                0     |                1 |                2 |            4 | 0.1875      | 1            |
| Lee2019_MI / OpenBMI | SSL        | C2-MULTI-HARD-VOTE |                        3 |               -0.005 |                1 |                2 |            0 | 0.2812      | 0.5625       |
| Lee2019_MI / OpenBMI | SSL        | C3-MULTI-PROB-AVG  |                        3 |                0.025 |                2 |                1 |            0 | 0.1875      | 0.5625       |
| PhysioNetMI          | CLASSICAL  | C1-LONG-3P5S       |                        6 |                0     |                1 |                1 |            4 | 0.07812     | 0.2344       |
| PhysioNetMI          | CLASSICAL  | C2-MULTI-HARD-VOTE |                        6 |                0     |                1 |                1 |            4 | 0.4609      | 1            |
| PhysioNetMI          | CLASSICAL  | C3-MULTI-PROB-AVG  |                        6 |                0     |                1 |                0 |            5 | 0.4258      | 1            |
| PhysioNetMI          | NEURAL     | C1-LONG-3P5S       |                        3 |                0     |                1 |                0 |            2 | 0.4648      | 1            |
| PhysioNetMI          | NEURAL     | C2-MULTI-HARD-VOTE |                        3 |                0     |                1 |                0 |            2 | 0.6523      | 1            |
| PhysioNetMI          | NEURAL     | C3-MULTI-PROB-AVG  |                        3 |                0     |                1 |                0 |            2 | 0.6836      | 1            |
| PhysioNetMI          | RIEMANNIAN | C1-LONG-3P5S       |                        7 |                0     |                2 |                0 |            5 | 0.1934      | 0.5801       |
| PhysioNetMI          | RIEMANNIAN | C2-MULTI-HARD-VOTE |                        7 |                0     |                1 |                2 |            4 | 0.1953      | 0.7188       |
| PhysioNetMI          | RIEMANNIAN | C3-MULTI-PROB-AVG  |                        7 |                0     |                2 |                0 |            5 | 0.25        | 0.7188       |
| PhysioNetMI          | SSL        | C2-MULTI-HARD-VOTE |                        3 |               -0.003 |                1 |                2 |            0 | 0.1641      | 0.3281       |
| PhysioNetMI          | SSL        | C3-MULTI-PROB-AVG  |                        3 |                0     |                1 |                1 |            1 | 0.6377      | 0.6377       |

![A4 role-control effects](figures/P02_Figure_05_A4_role_control_effects.png)

Across all 756 statistical rows, **zero** produced raw p<=0.05. Several groups have positive or negative median cell effects, but signs vary by dataset, role and budget. The data therefore do not support a simple claim that longer windows, hard-voted views, or probability-averaged views systematically improve decoder performance.

The absence of significance should not be interpreted as proof of no effect. The canonical deep surface is deliberately reduced; some role/budget rows are non-evaluable due to participant-count or compatibility rules; and Stage18S later shows repeat/budget sensitivity. The correct scientific statement is that **no statistically detectable C1-C3 improvement emerged under the frozen canonical A4 tests**.

## 10.4 C4/C5 ensemble controls

Only one governed C4/C5 row survives Holm correction:

| Dataset     | Condition          | budget_id   |   repeat | Strongest constituent   |   n |   median_delta_BACC |   p_value |   holm_adjusted_p |   rank_biserial |   ci_low |   ci_high |
|:------------|:-------------------|:------------|---------:|:------------------------|----:|--------------------:|----------:|------------------:|----------------:|---------:|----------:|
| PhysioNetMI | C4-MODEL-HARD-VOTE | FULL_TRAIN  |        4 | EEGNet                  |  11 |              -0.043 |   0.01855 |           0.03711 |          -0.788 |    -0.13 |    -0.012 |

This result is negative for the ensemble: on PhysioNetMI full training at ensemble repeat 4, hard voting reduced participant-level BACC relative to validation-selected EEGNet. Several other C4/C5 rows have raw p<=0.05 but do not survive the family correction and therefore are not promoted to confirmatory findings.

The practical implication is that aggregation complexity carries no automatic accuracy entitlement. An ensemble can combine complementary errors, but it can also dilute the strongest constituent or amplify correlated weaknesses.

## 10.5 Burden and practical significance

A4 performance must be interpreted together with evidence-acquisition and computation burden. The canonical burden source shows that C1 lengthens the observation horizon from **3.0 s to 3.5 s**. C2/C3 evaluate three views/members, while C4/C5 evaluate four model members; these conditions therefore add inference and aggregation work before any accuracy benefit is considered.

Across successful burden rows, the descriptive batch-1/model-evaluation latency medians are approximately **0.003007 s (C0)**, **0.006025 s (C1)**, **0.026557 s (C2/C3)**, and **0.021292 s (C4/C5)**. Median aggregation latency is about **0.003456 s for C2 hard vote**, **0.001812 s for C3 probability averaging**, **0.002756 s for C4 hard vote**, and **0.000242 s for C5 probability averaging**. These are execution-environment descriptive burdens, **not deployment latency benchmarks**.

This burden matters because the governed efficacy results do not show a consistent compensating advantage: the 756 C1-C3 role-control comparisons contain zero raw p-values <=0.05, and the only Holm-significant C4/C5 comparison is negative. P02 therefore does not justify additional ordinary view/ensemble complexity on the premise of a reliable accuracy gain. The proper conclusion is a **performance-burden trade-off under the tested P02 environment**, not a universal deployment recommendation.

The exact condition-level burden summary is preserved in `table_sources/P02_Table_A4_burden_summary.csv`.

# 11. Stage 18S - Supplemental Sensitivity Analysis

Stage 18S is **post-hoc descriptive**. It was introduced after canonical Stage18 to examine whether the resource-constrained conclusions were sensitive to additional repeats and intermediate-budget probes. It does not change G18, does not turn three repeats into the originally intended five-repeat confirmatory design, and does not establish full Build Book equivalence.

| Dataset              |   ALL_NEGATIVE |   MIXED |   ALL_POSITIVE |   Median repeat SD ΔBACC |
|:---------------------|---------------:|--------:|---------------:|-------------------------:|
| BNCI2014_001         |              2 |       9 |              4 |                    0.032 |
| Lee2019_MI / OpenBMI |              1 |       7 |              7 |                    0.015 |
| PhysioNetMI          |              4 |       6 |              5 |                    0.011 |

![Stage18S sign consistency](figures/P02_Figure_06_Stage18S_sign_consistency.png)

Of 45 anchor trajectories, 22 are MIXED, 16 ALL_POSITIVE, and 7 ALL_NEGATIVE. The overall median repeat SD of delta BACC is 0.0159 and the 90th percentile is 0.0369. Dataset medians are highest on BNCI (~0.0323), lower on Lee (~0.0155), and lower again on PhysioNet (~0.0111).

The six-budget MR00 probe is even more cautionary: **15/15 trajectories contain at least one sign flip** across the six evaluated budgets (1,4,8,16,32,FULL; budget 2 was intentionally absent from this supplement). This means that an A4 manipulation can appear helpful at one supervision level and harmful at another. The supplement therefore **qualifies** any temptation to generalize an anchor-budget sign across the entire label regime.

# 12. Failure, Negative Results, and Diagnostics

Failure and non-success evidence is part of the scientific record, but the record families have different semantics and must not be summed as if they were one failure count.

The canonical aggregation reports **648 FailureCaseIndex records, 340 NegativeResultNote records, and 309 DiagnosticOnlyFlag records**. Within `FailureCaseIndex`, the exact governed terminal-state breakdown is:

| FailureCaseIndex code      |   Count |   Denominator |   Fraction |
|:---------------------------|--------:|--------------:|-----------:|
| CONDITIONAL_SKIP           |     591 |           648 |   0.912037 |
| NOT_APPLICABLE_REPEAT_SLOT |      42 |           648 |   0.064815 |
| INPUT_INCOMPATIBLE         |       9 |           648 |   0.013889 |
| FAILED                     |       3 |           648 |   0.004630 |
| DEPENDENCY_BLOCKED         |       3 |           648 |   0.004630 |

The branch/role distribution is:

| Code                       | Branch / role                 |   Count |
|:---------------------------|:------------------------------|--------:|
| CONDITIONAL_SKIP           | NEURAL_VALIDATION_SELECTED    |     288 |
| CONDITIONAL_SKIP           | SSL_VALIDATION_SELECTED       |     288 |
| CONDITIONAL_SKIP           | DNN-EGTC                      |      15 |
| DEPENDENCY_BLOCKED         | SSL-REVE                      |       3 |
| FAILED                     | CLS-CSP-LDA                   |       3 |
| INPUT_INCOMPATIBLE         | SSL_VALIDATION_SELECTED       |       9 |
| NOT_APPLICABLE_REPEAT_SLOT | PRE_RESULT_ROLE_MEMBERSHIP    |      30 |
| NOT_APPLICABLE_REPEAT_SLOT | CLASSICAL_VALIDATION_SELECTED |      12 |

The three `FAILED` records are exactly the CSP-LDA 1-label/class low-label cells, one in each dataset. The three `DEPENDENCY_BLOCKED` records belong to SSL-REVE. The 15 A0 `CONDITIONAL_SKIP` records belong to the DNN-EGTC fallback branch, while the much larger A4 conditional-skip volume records scientifically governed non-execution of expensive/refit cells under the authorized design. The nine `INPUT_INCOMPATIBLE` A4 cases are preserved rather than coerced into scores, and the 42 `NOT_APPLICABLE_REPEAT_SLOT` records explicitly encode repeat slots made inapplicable by the authorized resource deviation.

All **340 NegativeResultNote** records are `NO_CONFIRMED_POSITIVE_EFFECT` evidence from A4 comparisons. Their preservation does **not** prove equivalence or zero effect; it prevents null/non-positive comparisons from disappearing. All **309 DiagnosticOnlyFlag** records have reason `DIAGNOSTIC_BRANCH`: 300 permutation-sanity records plus three each from prior sanity, log-variance diagnostic, and Riemannian MDM diagnostic branches. These records cannot silently become claim-bearing evidence.

The scientifically useful lesson is that P02 distinguishes at least four different phenomena: (1) true attempted-cell failure, (2) planned/conditional non-execution, (3) input/semantic incompatibility, and (4) deliberately diagnostic evidence. This prevents both survivorship bias and the opposite error of describing every non-success state as a runtime crash.

Exact failure-code/branch tables are preserved in `table_sources/P02_Table_failure_category_breakdown.csv` and `P02_Table_failure_code_summary.csv`; the final failure coverage matrix is `machine_readable/P02_failure_coverage_matrix.csv`.

# 13. Cross-Dataset Synthesis

Three cross-dataset conclusions are supported.

**First, no model family is universally first.** BNCI descriptively favors CSP-LDA; Lee and PhysioNet favor DBConformer by mean BACC. Recent benchmark work likewise emphasizes dataset/participant dependence in EEG decoding, but P02's own evidence is sufficient to make the bounded statement without relying on external papers.

**Second, low-label difficulty generalizes more clearly than low-label ordering.** Across all three datasets, most 1-32/class points are close to chance and no model follows a universal monotonic curve. The exact best point changes.

**Third, A4 effects are heterogeneous rather than uniformly beneficial.** The canonical C1-C3 tests are null under the governed family, while Stage18S reveals sign instability across repeat and budget. This is a stronger scientific result than selecting isolated positive cells.

# 14. Comparison With Original Model Papers and Authoritative Sources

**Fresh verification for Final R2.** Model/dataset provenance and training-context statements in this section were rechecked on 2026-08-14 against primary or author-controlled sources: the original EEGNet paper and ARL EEGModels repository; the FBCNet author repository/publication lineage; the DBConformer PubMed record and author repository; the ICLR CBraMod paper and author repository; the OpenBMI/GigaScience paper; the official PhysioNet EEG Motor Movement/Imagery dataset page; the official BCI Competition IV dataset description; and original Riemannian-geometry BCI literature. These sources are used to explain architecture and evaluation differences. Their headline performance values are **not treated as direct IHARQ benchmarks** unless dataset, split, preprocessing, participant regime, supervision, task and metric are sufficiently aligned. `literature/P02_literature_fresh_verification.json` records the verification metadata and comparability class.

The literature table is intentionally comparability-aware:

| Study                  | Model/topic                        | Original setting                                                                                                               | IHARQ relation                                                                                                                                                      | Comparability                                                   | Key use                                                                                                                                                |
|:-----------------------|:-----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lawhern et al. 2018    | EEGNet                             | Four BCI paradigms; within- and cross-subject; compact depthwise/separable CNN; limited-data emphasis                          | EEGNet is one P02 neural decoder; IHARQ uses frozen P01 binary left/right task, subject-group split, 160 Hz 8-32 Hz 3 s windows, governed validation/test isolation | methodological reference only / partial architecture comparison | Motivates compact EEG-specific architecture and source-centered training recipe; not a direct performance benchmark.                                   |
| Mane et al. 2020/2021  | FBCNet                             | Filter-bank multi-view MI decoder with variance layer; subject-specific/cross-validation settings including OpenBMI/BCIC-IV-2a | P02 uses author-centered model construction but IHARQ split, binary task, preprocessing, low-label budgets and test isolation differ                                | methodological reference only                                   | Supports use of filter-bank/variance inductive bias; source diagnostics informed Stage12 author-centered horizon.                                      |
| Wang et al. 2026       | DBConformer                        | Dual temporal/spatial Conformer across MI, seizure and SSVEP under four evaluation settings                                    | P02 DNN-SEQ resolves to DBConformer with P01-compatibility patch and IHARQ-specific binary subject-group protocol                                                   | methodological reference only                                   | Context for strong descriptive full-training performance on two IHARQ datasets; headline paper results are not numerically comparable.                 |
| Wang et al. 2025       | CBraMod                            | Criss-cross EEG foundation model; masked pretraining; 10 downstream tasks across 12 public datasets                            | P02 fine-tunes/uses governed CBraMod branch under P01 binary MI substrate and P02 model-local adaptation                                                            | methodological reference only                                   | Context for foundation-model branch and the difficulty of transferring generic pretrained representations under constrained task-specific supervision. |
| Barachant et al. 2013  | Riemannian covariance methods      | Covariance-matrix classification with Riemannian kernel for MI BCI                                                             | P02 includes Riemannian tangent-space and alignment variants under a common subject-grouped test protocol                                                           | methodological reference only                                   | Context for competitive classical/Riemannian baselines and covariance geometry.                                                                        |
| Chevallier et al. 2024 | MOABB reproducibility benchmark    | 30 pipelines, 36 public datasets; standardized benchmark spanning raw, Riemannian and deep pipelines                           | P02 similarly values multi-family, multi-dataset comparison but uses its own frozen P01 split/budget/ablation contract                                              | contextual benchmark only                                       | Supports interpretation that model-family performance is evaluation-regime dependent and reproducible benchmarking matters.                            |
| Wang et al. 2024       | EEGPT                              | 10M-parameter pretrained transformer; multi-task EEG pretraining and linear probing                                            | Not executed in P02; contextualizes contemporary foundation-model direction and challenges of inter-subject/channel heterogeneity                                   | methodological reference only                                   | Broader literature positioning only; not an IHARQ comparator.                                                                                          |
| Lee et al. 2019        | OpenBMI / Lee2019_MI dataset       | Large EEG dataset/toolbox spanning MI and other BCI paradigms                                                                  | Source dataset for Lee2019_MI; P01 imposes IHARQ binary labels, preprocessing and subject-group roles                                                               | dataset provenance; protocol differs                            | Dataset provenance and external context.                                                                                                               |
| Schalk 2009            | EEG Motor Movement/Imagery Dataset | 64-channel BCI2000 motor execution/imagery recordings                                                                          | Source dataset for PhysioNetMI; P01 freezes legal left/right MI subset, preprocessing and subject-group split                                                       | dataset provenance; protocol differs                            | Dataset provenance.                                                                                                                                    |
| Tangermann et al. 2012 | BCI Competition IV dataset 2a      | 22 EEG channels; four-class MI; competition train/test sessions                                                                | Source family underlying BNCI2014_001; IHARQ uses binary left/right task and own frozen subject-group roles                                                         | dataset provenance / contextual only                            | Dataset provenance and warning against direct comparison to four-class competition scores.                                                             |

## 14.1 EEGNet

Lawhern et al. (2018) introduced EEGNet as a compact EEG-specific CNN using depthwise and separable convolutions and evaluated it across multiple BCI paradigms, including sensory-motor rhythms, in within- and cross-subject settings. The authors explicitly emphasized compactness and limited-data performance. P02's use is conceptually aligned with that architecture, but IHARQ changes the dataset roles, task labels, sampling/window identity, validation rule, and training continuation. Consequently, the original paper is a **methodological reference**, not a directly comparable performance target.

## 14.2 FBCNet

Mane et al. designed FBCNet around multi-view filter-bank features, learned spatial filters, and a variance aggregation layer, motivated partly by limited training data in MI. P02's author-centered FBCNet diagnostics explicitly consulted source implementation horizons. Yet the original subject-specific/cross-validation settings and IHARQ's subject-grouped held-out participants are not equivalent. P02's BNCI result, for example, must not be compared naively with the published four-class BCI Competition score.

## 14.3 DBConformer

The DBConformer paper describes parallel temporal and spatial Conformer branches with channel attention and reports strong results across multiple EEG paradigms. P02's descriptive lead on Lee/PhysioNet is directionally compatible with the possibility that such spatiotemporal modeling is useful, but P02 does not isolate the branches or reproduce the original evaluation settings. Thus the paper supports architectural interpretation, not causal attribution or numeric equivalence.

## 14.4 CBraMod

CBraMod was presented at ICLR 2025 as a pretrained criss-cross EEG foundation model that separates spatial and temporal dependency modeling and was evaluated across numerous downstream tasks/datasets. P02's weaker results under binary MI do not conflict with that paper because downstream adaptation, split, data volume and metric regime differ. They instead illustrate the general transfer-learning point that a pretrained representation can remain sensitive to downstream alignment and fine-tuning.

## 14.5 Classical/Riemannian context

Barachant et al. and subsequent Riemannian BCI work provide methodological precedent for covariance-based representations that avoid or complement conventional spatial filtering. P02's competitive RIE-TS-LR/RIE-EA-TS behavior on Lee/PhysioNet is consistent with that family remaining a serious baseline. MOABB-style reproducibility studies further reinforce the value of comparing classical, Riemannian and deep pipelines under standardized protocols rather than assuming neural dominance.

# 15. Broader Literature Positioning

The current literature increasingly emphasizes three issues that are directly relevant to P02 interpretation:

1. **Reproducibility and evaluation protocol matter.** MOABB's broad open benchmark exists precisely because results can change materially with dataset and evaluation regime. P02 contributes a project-specific version of that principle by freezing all branches onto the same P01 substrate and preserving negative results.
2. **Participant heterogeneity remains a central BCI problem.** Recent large-scale benchmarking continues to show that aggregate rankings can hide subject-level optimum variation. P02's broad participant ranges on Lee/PhysioNet are consistent with that concern, although P02 does not validate personalization.
3. **Pretraining/foundation models are promising but not a substitute for downstream evaluation.** EEGPT and CBraMod exemplify large-scale self-supervised/foundation approaches. P02 adds a controlled counterpoint: under one concrete binary MI regime, smaller task-specific and classical/Riemannian models can remain competitive or superior.

Two recent directions further sharpen the interpretation without changing the P02 evidence itself. A 2025 few-shot cross-subject MI study (TCPL) explicitly treats scarce labels and inter-subject variability as a specialized adaptation problem, which is consistent with P02's observation that a generic single-subset low-label curve is not enough to establish stable sample efficiency. Recent EEG foundation-model benchmarking also emphasizes standardized downstream evaluation; this is directly relevant to the fact that CBraMod does not automatically dominate the smaller P02 decoders. A June 2026 MOABB-oriented preprint likewise reports substantial participant-specific variation in decoder optimality, but because its within-participant evaluation regime differs from IHARQ's frozen subject-grouped held-out roles, it is used only as contextual support for the importance of heterogeneity, not as a numerical comparator.

No novelty claim is made on the basis of this literature scan alone. A cautious future formulation is that **the combination of frozen subject-group evaluation, plural decoder families, explicit low-label budgets, controlled A4 roles, preserved failure evidence, and source-aware amendment history appears unusually audit-oriented**, but a formal novelty claim would require a dedicated systematic review.

# 16. Direct Phase 02 Findings

| Finding      | Evidence-bounded statement                                                                                                                                                                                                                                                                                                                                                         | Scope                                                | Key limitation                                                                                           |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| P02-FIND-001 | P02 closed the first governed Layer-2 decoder/baseline measurement spine over the frozen P01 data substrate: A0 reached 678/678 terminal cells and preserved raw prediction, score, checkpoint, failure, and participant-level evidence.                                                                                                                                           | Layer-2 raw accept-all measurement spine.            | Non-clinical; no calibration/threshold/abstention claims.                                                |
| P02-FIND-002 | Full-training decoder ordering was dataset-dependent. CSP-LDA led BNCI2014_001 descriptively (BACC 0.639; one held-out participant), whereas DBConformer/DNN-SEQ had the highest participant-first mean BACC on Lee2019_MI (0.795) and PhysioNetMI (0.650).                                                                                                                        | Full-training A0 test evidence.                      | Ranking is descriptive and heterogeneous across datasets.                                                |
| P02-FIND-003 | The governed A0 omnibus test detected model-family heterogeneity on PhysioNetMI (Friedman statistic 20.544, p=0.00451, Kendall W=0.267) but not on Lee2019_MI (p=0.148); no pairwise alternative-versus-CSP-LDA comparison survived Holm correction on Lee2019_MI or PhysioNetMI.                                                                                                  | Governed A0 model comparison.                        | Does not establish a universal winning decoder.                                                          |
| P02-FIND-004 | Participant heterogeneity was substantial in the multi-participant datasets: several leading full-training branches spanned near-chance to very high participant BACC, so pooled means conceal materially different individual outcomes.                                                                                                                                           | Participant heterogeneity.                           | P02 does not test a personalization policy.                                                              |
| P02-FIND-005 | The frozen low-label analysis did not show a smooth universal sample-efficiency curve. At 1-32 labels/class most aggregate BACC points remained near chance, model ranking changed with budget and dataset, and CSP-LDA at 1/class was explicitly non-success on all three datasets.                                                                                               | Low-label A0 surface.                                | One frozen subset; no repeated subset sampling; no interpolation.                                        |
| P02-FIND-006 | Stage 11 required an explicit prospective stopping-rule correction: previously sealed EEGNet fits were grandfathered, while only remaining/unsealed fits adopted TRUE_P120/FLOOR1. The canonical primary lineage therefore remains mixed (101 P500, 4 R6 P120/FLOOR500); 15 R7 TRUE_P120/FLOOR1 fits belong to a diagnostic challenger and do not replace the primary A0 evidence. | Stage11 historical/canonical identity.               | Mixed recipe lineage prevents a false all-R7 primary interpretation.                                     |
| P02-FIND-007 | The Stage 11 diagnostic S&R challenger did not provide evidence of a consistent test-set advantage over the canonical primary EEGNet: median paired ΔBACC was -0.0347 on BNCI2014_001, +0.010 on Lee2019_MI, and 0.000 on PhysioNetMI, with Wilcoxon p values 0.125, 0.231 and 0.455 respectively.                                                                                 | Diagnostic challenger only.                          | Does not rewrite primary A0 or enter A4 selection.                                                       |
| P02-FIND-008 | Stage 12 diagnostics demonstrate architecture-specific optimization sensitivity rather than a universal training recipe: source/author-centered candidate B removed targeted A-collapse for BNCI FBCNet and PhysioNet CBraMod in validation diagnostics, but BNCI FBCNet C-confirmation still collapsed in 5/5 confirmation seeds.                                                 | Methodological interpretation of Stage12 correction. | Claim-bearing test inference comes from canonical A0, not the A/B/C diagnostic search.                   |
| P02-FIND-009 | A4 completed all six governed condition identities across all three datasets, but under an explicit resource-constrained single-repeat/deep-anchor deviation: 1,218 terminal cells comprised 591 SUCCESS, 576 CONDITIONAL_SKIP, 9 INPUT_INCOMPATIBLE and 42 NOT_APPLICABLE_REPEAT_SLOT.                                                                                            | Resource-constrained canonical Stage18.              | No five-repeat stability; reduced deep budget grid; not full Build Book equivalence.                     |
| P02-FIND-010 | Across the 756 governed C1-C3 role-control statistical rows, no comparison reached raw p<=0.05; condition effects were generally small, heterogeneous in sign, and dependent on dataset/role/budget.                                                                                                                                                                               | Ordinary A4 C1-C3 controls.                          | Deep roles restricted to anchor budgets/repeat0 in canonical Stage18.                                    |
| P02-FIND-011 | Within the governed C4/C5 ensemble-versus-strongest-constituent family, one comparison survived Holm correction: on PhysioNetMI full training at ensemble repeat 4, the hard-vote ensemble underperformed validation-selected EEGNet by median ΔBACC -0.0435 (raw p=0.0186; Holm p=0.0371; rank-biserial -0.788; 95% bootstrap CI -0.1304 to -0.0119).                             | One governed C4 comparison identity.                 | Does not imply ensembles are generally inferior across datasets/budgets/repeats.                         |
| P02-FIND-012 | Stage 18S shows that A4 effect direction is sensitive to repeat and supervision budget: 22/45 three-repeat anchor trajectories were MIXED and all 15 six-budget MR00 trajectories changed sign at least once.                                                                                                                                                                      | Stage18S sensitivity supplement.                     | Not confirmatory; does not modify G18 or create five-repeat evidence.                                    |
| P02-FIND-013 | Negative evidence is a first-class P02 result: the release preserves 648 failure/non-success records, 340 NegativeResultNotes and 309 DiagnosticOnlyFlags, including branch dependency blocks, conditional skips, input incompatibilities and not-applicable repeat slots.                                                                                                         | Failure and negative-result accounting.              | Counts include governed non-success states that should not be conflated with unexpected runtime crashes. |
| P02-FIND-014 | P02 is evidence-sufficient for its governed Layer-2 scope and downstream handoff, but its evidence ceiling remains a measurement ceiling: it supports decoder/baseline, low-label descriptive, ordinary A4 control and readiness claims, not calibrated uncertainty, threshold/abstention policy, clinical safety, temporal robustness, stress robustness or embodiment claims.    | Downstream readiness.                                | Downstream layers must carry P02 limitations forward.                                                    |

# 17. Supported Interpretations

## P02-FIND-002/003 - No universal decoder winner

The measured full-training rankings and governed tests support **dataset-dependent decoder suitability**, not universal model dominance. The PhysioNet omnibus establishes model heterogeneity while corrected pairwise tests leave the identity of a superior reference alternative unresolved.

## P02-FIND-004 - Participant variability is scientifically material

Wide participant distributions indicate that a dataset mean is an incomplete summary of decoder behavior. This supports carrying subject-profile evidence into later analysis and motivates, but does not validate, future participant-aware selection.

## P02-FIND-005 - Label scarcity remains an unresolved stressor

The low-label surface shows that severe supervision reduction pushes many models toward chance and creates non-monotonic model/dataset behavior. Because subset repeats were not executed, the evidence supports a **difficulty/heterogeneity** interpretation rather than a stable sample-efficiency ordering.

## P02-FIND-006/008 - Training fidelity is part of fair architecture evaluation

Stage11/12 history demonstrates that an implementation can be structurally correct while a stopping horizon, optimizer schedule, input scale, or model-local recipe remains scientifically consequential. This supports the methodological principle that failed optimization should be diagnosed before concluding that the architecture lacks capacity.

## P02-FIND-010/011/012 - A4 does not justify a generic “more views/ensembles help” story

The canonical C1-C3 family is null under governed tests; one C4 ensemble is significantly worse than its strongest constituent; and Stage18S reveals sign instability. The joint interpretation is **conditionality**: longer context and aggregation can help or hurt depending on dataset, model role, repeat and supervision budget.

# 18. Candidate Claims for Layer 0 Review

| Claim              | Candidate wording                                                                                                                                                                                                                                                            | Ceiling                      | Required qualification                                                                                                     | Manuscript role                             |
|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------|:---------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|
| P02-CLAIM-CAND-001 | Under the frozen P01 subject-grouped binary motor-imagery protocol, P02 established a complete multi-family raw decoder/baseline measurement spine across three public EEG datasets.                                                                                         | SUPPORTED                    | Raw accept-all decoder evidence only; not clinical or safety evidence.                                                     | Methods / empirical foundation              |
| P02-CLAIM-CAND-002 | Decoder-family performance was dataset-dependent rather than universally ordered: DBConformer was descriptively strongest at full training on Lee2019_MI and PhysioNetMI, while CSP-LDA led the single-participant BNCI2014_001 test split.                                  | SUPPORTED_WITH_QUALIFICATION | Descriptive rankings; no universal winner; BNCI inferential n=1.                                                           | Main/secondary result                       |
| P02-CLAIM-CAND-003 | PhysioNetMI exhibited statistically detectable overall decoder heterogeneity under the governed A0 comparison, but no individual alternative-versus-CSP-LDA contrast survived Holm correction.                                                                               | SUPPORTED_WITH_QUALIFICATION | Global omnibus heterogeneity is not evidence that a specific decoder is superior.                                          | Main result / discussion                    |
| P02-CLAIM-CAND-004 | Extreme low-label decoding remained difficult and non-monotonic under the single frozen subset design; P02 does not support a universal sample-efficiency ordering among CSP-LDA, tangent-space, EEGNet and CBraMod.                                                         | SUPPORTED_WITH_QUALIFICATION | One frozen subset per budget; descriptive only.                                                                            | Secondary result / limitation               |
| P02-CLAIM-CAND-005 | The Phase-02 training-correction history demonstrates that optimization/training-policy fidelity can materially affect whether an EEG architecture appears collapsed or viable, so optimization failure should not automatically be interpreted as architectural incapacity. | SUPPORTED_WITH_QUALIFICATION | Mechanistic interpretation; source diagnostics are not a direct claim of test-set performance improvement for every model. | Discussion / reproducibility observation    |
| P02-CLAIM-CAND-006 | The Stage-11 S&R diagnostic challenger did not yield a consistent participant-level BACC improvement over the canonical primary EEGNet across the three datasets.                                                                                                            | SUPPORTED                    | Not an A-number and not a replacement for primary A0.                                                                      | Negative methodological result / supplement |
| P02-CLAIM-CAND-007 | Within the canonical resource-constrained A4 execution, the C1-C3 longer/multi-view role controls did not produce statistically detectable improvements after the governed paired testing procedure.                                                                         | SUPPORTED_WITH_QUALIFICATION | Absence of detected effects is not proof of zero effect; canonical deep scope is reduced.                                  | Ablation result / negative result           |
| P02-CLAIM-CAND-008 | A hard-vote model ensemble was not uniformly beneficial: one governed PhysioNetMI full-training comparison showed a Holm-significant disadvantage relative to the validation-selected strongest constituent.                                                                 | SUPPORTED_WITH_QUALIFICATION | Do not generalize from one corrected comparison to all ensembles.                                                          | Negative ablation result / discussion       |
| P02-CLAIM-CAND-009 | Post-hoc Stage18S sensitivity evidence indicates that A4 effect direction can change across repeats and budgets, reinforcing the Protocol restriction against five-repeat stability or dense-budget response claims from canonical Stage18.                                  | POST_HOC_ONLY                | Descriptive/post-hoc only; does not modify canonical G18.                                                                  | Supplement / limitation justification       |
| P02-CLAIM-CAND-010 | P02 provides a fail-closed, provenance-rich Layer-2 evidence substrate for downstream phases while preserving unsuccessful, incompatible, skipped and diagnostic outcomes rather than retaining successful models only.                                                      | SUPPORTED                    | Technical readiness is not deployment readiness.                                                                           | Methods / reproducibility / supplement      |

No claim in this table is Layer-0 approved by virtue of appearing here.

# 19. Mechanism Hypotheses

| Hypothesis   | Observed pattern                                                                                                 | Proposed mechanism (not measured)                                                                                                                                                         | Future test                                                                                           |
|:-------------|:-----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| P02-HYP-001  | Strong full-training model ordering changed across datasets and participants.                                    | Differences in channel montage, sample volume, participant heterogeneity and architecture inductive biases may change which representations are most useful.                              | Factorial/standardized cross-dataset representation study or participant-aware model selection study. |
| P02-HYP-002  | Stage12 source-centered diagnostics rescued some collapsed configurations but not every confirmation trajectory. | Architectures have materially different optimization and scaling requirements; a uniform training horizon can confound optimization failure with model capacity.                          | Prospectively frozen model-specific vs uniform training-policy ablation.                              |
| P02-HYP-003  | Low-label curves were near chance and non-monotonic for many model/dataset combinations.                         | With very small fixed calibration subsets, subset composition and participant shift may dominate architecture-level sample-efficiency differences.                                        | Repeated low-label subset sampling under a prospective protocol.                                      |
| P02-HYP-004  | A4 C1-C3 effects were small/heterogeneous and Stage18S showed frequent sign changes.                             | Longer windows and multi-view aggregation trade additional signal/context against model mismatch, noise and participant-specific variability; net effect can change with budget and seed. | Full prospective five-repeat A4 replication with dense deep-budget grid.                              |

These are explicitly hypotheses. P02 does not isolate the proposed mechanisms causally.

# 20. Expectation Versus Observation

| Pre-execution expectation / responsibility | Observation | Classification |
|---|---|---|
| Establish plural decoder/baseline measurement spine | A0 complete with all planned terminal states and prediction/checkpoint substrate | SUPPORTED |
| Evaluate meaningful model-family differences | Overall heterogeneity present on PhysioNet; descriptive ranking differences across datasets | PARTIALLY_SUPPORTED / DATASET_DEPENDENT |
| Obtain interpretable low-label curves | Curves produced, but often near chance/non-monotonic under one frozen subset | PARTIALLY_SUPPORTED |
| Execute A4 longer/multi-view/ensemble controls | All six conditions closed under resource-constrained design | SUPPORTED_WITH_DESIGN_DEVIATION |
| Expect A4 improvements | No C1-C3 raw p<=0.05; one negative C4 corrected effect | NOT_SUPPORTED_AS_GENERAL_CLAIM |
| Preserve reproducibility and failures | Failure/negative/diagnostic states and release provenance preserved | SUPPORTED |

# 21. Limitations and Claim Ceilings

## 21.1 A4 compute limitation

Canonical Stage18 executes one refit repeat and deep anchor budgets only. This is the largest analytical limitation because it prevents repeat-stability and dense-budget claims. What remains valid are the observed anchor/single-repeat comparisons and their governed statistics.

## 21.2 Low-label single-subset limitation

Each budget corresponds to one frozen P01 subset. The design supports exact reproducibility but not a sampling distribution over possible calibration subsets. Non-monotonic curves may therefore reflect both model behavior and subset composition.

## 21.3 Dataset/test-participant scope

BNCI has only one held-out participant, Lee six, PhysioNet eleven. Cross-dataset pooled meta-analysis is prohibited, and P02 should not characterize its three sources as universal EEG populations.

## 21.4 Post-hoc Stage18S

Stage18S is valuable precisely because it exposes sensitivity, but it is post-hoc. Its descriptive repeat/budget patterns may qualify claims; they cannot manufacture confirmatory evidence absent from Stage18.

## 21.5 Model adaptation and original-paper comparability

P02 deliberately preserves IHARQ data/split/test-isolation rules while adapting heterogeneous model implementations. This improves within-project fairness but means headline numbers from original publications are rarely directly comparable.

## 21.6 Non-clinical measurement boundary

All sources are public research EEG datasets. P02 provides decoder measurement and downstream technical readiness, not clinical efficacy, safety, real-time deployment, calibrated trust, or embodied-system validation.

# 22. Relation to Project-Wide Objectives and P03

P02's durable output is a **canonical prediction/evidence substrate**. P03 and later layers may consume accepted checkpoints, predictions, score semantics, participant profiles, A0 reference evidence, A4 controls, and failure records. They must preserve P02's identities and limitations. In particular, later calibration/threshold work must not treat raw P02 scores as already calibrated, and later policy/readiness work must not use P02 decoder ranking as a safety decision.

# 23. Paper/Thesis Reuse Guide

| Manuscript section | P02 analytical material | Preferred evidence | Important qualification |
|---|---|---|---|
| Methods | Frozen P01 substrate + plural L2 decoder families + participant-first statistics | Sections 1-5; Protocol identities | Keep P02 measurement boundary explicit |
| Results - baseline | Full-training A0 ranking and statistics | P02-FIND-002/003; Figure 1; A0 tables | No universal winner |
| Results - heterogeneity | Participant distributions | P02-FIND-004; Figure 2 | No personalization claim |
| Results - low label | Budget curves | P02-FIND-005; Figure 3 series | Single frozen subset |
| Results/Discussion - training | Stage11/12 history | P02-FIND-006/007/008; Figure 4; Stage12 table | Distinguish diagnostic vs claim-bearing evidence |
| Ablation Study | A4 C1-C5 | P02-FIND-009/010/011; Figure 5 | Single-repeat/deep-anchor claim ceiling |
| Supplement | Stage18S | P02-FIND-012; Figure 6 | POST_HOC_ONLY |
| Negative Results | Failed/blocked/skipped branches and null A4 controls | P02-FIND-007/010/011/013 | Preserve terminal semantics |
| Discussion | Literature positioning, optimization sensitivity, heterogeneity | Sections 14-19 | Mechanisms remain hypotheses |
| Limitations | A4, low-label, participant scope, post-hoc supplement | Section 21 | Do not overstate into invalidation |

## 23.1 Candidate paper narrative - subject to later project-wide synthesis

A defensible P02 contribution to a future manuscript is not a conventional "new model wins" story. The evidence supports a more useful sequence:

1. **Motivation:** reliable downstream uncertainty/policy work requires a frozen, plural decoder measurement spine rather than one arbitrarily chosen baseline.
2. **Design:** P02 evaluates classical, Riemannian, compact/deep neural, and pretrained branches across three public EEG sources under a common subject-grouped contract, while explicitly probing scarce-label behavior.
3. **Result 1 - heterogeneous baseline landscape:** several decoder families are viable, but rankings vary by dataset and participant; the full-training descriptive leader is not universally confirmatory after multiplicity control.
4. **Result 2 - low-label difficulty:** severe supervision scarcity remains near-chance and non-monotonic for many branch/dataset combinations under the single frozen-subset design.
5. **Methodological result - training fidelity:** Stage 11/12 show that architecture-specific source/author training rules can matter enough to change collapse/viability diagnostics, while not guaranteeing universal test gains.
6. **Ablation result - ordinary A4 controls:** longer/multi-view/ensemble manipulations are not uniformly beneficial; the canonical C1-C3 family is null under its governed tests and one hard-vote ensemble comparison is significantly worse than its strongest constituent.
7. **Limitation/sensitivity:** compute constraints restrict canonical A4 to a single repeat/deep anchor budgets; Stage18S indicates sign instability and therefore reinforces, rather than removes, the claim ceiling.
8. **Implication:** P02 provides the auditable raw decoder substrate against which later calibration, uncertainty, thresholding, abstention, temporal robustness, and safety-governance layers must demonstrate added value.

This narrative remains a **candidate manuscript organization**, not a final publication claim set. Layer 0 and later cross-phase synthesis retain claim-governance authority.

# 24. Layer 0 Handoff

Layer 0 should review the ten candidate claims in `machine_readable/P02_candidate_claims.yaml`. Priority review issues are:

- wording around DBConformer's descriptive lead versus non-significant corrected reference contrasts;
- whether the methodological training-fidelity claim is sufficiently bounded to diagnostic evidence;
- explicit A4 language that prevents five-repeat/dense-budget/full-grid overclaiming;
- Stage18S's POST_HOC_ONLY designation;
- prohibition of clinical, safety, calibration, threshold, abstention, robustness and embodiment claims.

# 25. Evidence Map Handoff

`machine_readable/P02_results_to_claims.yaml` maps each finding to canonical analysis sources, the accepted run ID, candidate claims and limitations. The Evidence Map should preserve exact source paths and later add Layer-0 disposition IDs, manuscript locations, figure/table IDs and release assets rather than rediscovering evidence from narrative prose.

# 26. Layer 10 Handoff

The strongest Phase-02 visualization candidates are the full-training multi-model comparison, participant-distribution figures, low-label curves, the training-policy challenger effect plot, A4 role-control effect view and Stage18S sign-consistency view. Layer 10 should treat these as analytical sources only: it may render/provenance-link them but may not recompute or strengthen the evidence.

# 27. Results-to-Claim Traceability

| Finding      | Candidate claim(s)                     | Primary source                                                                                     | Limitation                                                                                               |
|:-------------|:---------------------------------------|:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| P02-FIND-001 | P02-CLAIM-CAND-001                     | analysis_inputs/a0_completion.json                                                                 | Non-clinical; no calibration/threshold/abstention claims.                                                |
| P02-FIND-002 | P02-CLAIM-CAND-002                     | table_sources/P02_Table_A0_fulltrain_branch_summary.csv                                            | Ranking is descriptive and heterogeneous across datasets.                                                |
| P02-FIND-003 | P02-CLAIM-CAND-002, P02-CLAIM-CAND-003 | analysis_inputs/a0_statistics.json                                                                 | Does not establish a universal winning decoder.                                                          |
| P02-FIND-004 | —                                      | analysis_inputs/subject_profile_metric_source.csv                                                  | P02 does not test a personalization policy.                                                              |
| P02-FIND-005 | P02-CLAIM-CAND-004                     | analysis_inputs/low_label_curve_summary.json                                                       | One frozen subset; no repeated subset sampling; no interpolation.                                        |
| P02-FIND-006 | P02-CLAIM-CAND-005                     | runtime/diagnostics/runtime_successor/stage11_maximum_analysis/stage11_source_centered_recipe.json | Mixed recipe lineage prevents a false all-R7 primary interpretation.                                     |
| P02-FIND-007 | P02-CLAIM-CAND-006                     | analysis_inputs/training_policy_challenger_statistics.json                                         | Does not rewrite primary A0 or enter A4 selection.                                                       |
| P02-FIND-008 | P02-CLAIM-CAND-005                     | runtime/diagnostics/stage12_R6_ABC_author_adaptive_R1/job_summaries/*.json                         | Claim-bearing test inference comes from canonical A0, not the A/B/C diagnostic search.                   |
| P02-FIND-009 | P02-CLAIM-CAND-007                     | analysis_inputs/a4_completion.json                                                                 | No five-repeat stability; reduced deep budget grid; not full Build Book equivalence.                     |
| P02-FIND-010 | P02-CLAIM-CAND-007                     | analysis_inputs/a4_role_control_statistics.json                                                    | Deep roles restricted to anchor budgets/repeat0 in canonical Stage18.                                    |
| P02-FIND-011 | P02-CLAIM-CAND-008                     | analysis_inputs/a4_c4_c5_statistics.json                                                           | Does not imply ensembles are generally inferior across datasets/budgets/repeats.                         |
| P02-FIND-012 | P02-CLAIM-CAND-009                     | analysis_inputs/stage18S_R1_decision_support_summary.json                                          | Not confirmatory; does not modify G18 or create five-repeat evidence.                                    |
| P02-FIND-013 | P02-CLAIM-CAND-010                     | analysis_inputs/failure_negative_summary.json                                                      | Counts include governed non-success states that should not be conflated with unexpected runtime crashes. |
| P02-FIND-014 | P02-CLAIM-CAND-010                     | Protocol v1.0 analysis contract                                                                    | Downstream layers must carry P02 limitations forward.                                                    |

# 28. Final Scientific Synthesis

Phase 02 succeeds scientifically not because every advanced model or every A4 manipulation improved performance, but because it produces a controlled, auditable **measurement landscape**.

The landscape has four major properties. First, full-training decoder performance is meaningfully above chance for several families but **dataset- and participant-dependent**. Second, severe label scarcity remains difficult and does not yield a stable universal model ordering. Third, training-policy fidelity matters enough that optimization failure must be separated from architectural failure, yet source-centered settings do not guarantee a consistent challenger gain. Fourth, ordinary longer-window/multi-view/ensemble A4 changes are not uniformly beneficial; the canonical tests are predominantly null/heterogeneous and supplemental sensitivity reveals substantial sign instability.

These are paper-worthy outcomes precisely because they resist a simplistic winner narrative. P02 establishes what later IHARQ layers need: exact raw decoder evidence, failure semantics, participant and budget profiles, ordinary ablation controls, and a clear claim ceiling. The strongest future scientific use of P02 is therefore as the **governed baseline against which later calibration, uncertainty, policy and robustness layers must demonstrate additional value**.

# 29. Final Evidence-Closure Matrices

The Final R2 closure pass explicitly checks the chain **expected by authorities -> executed -> produced -> analyzed**. Detailed machine-readable matrices are delivered with the report; the closure summary is:

| Matrix                    |   Rows | Closure                                                                                         |
|:--------------------------|-------:|:------------------------------------------------------------------------------------------------|
| Expected evidence         |    104 | All upstream P02/L2 requirements dispositioned; analytical vs operational roles separated       |
| Actual evidence inventory |     46 | 38 canonical analysis inputs + material supporting Stage11/12/raw negative-evidence sources     |
| Stage coverage            |     27 | 26 canonical stages + Stage18S supplement dispositioned                                         |
| Ablation coverage         |     15 | A0-A13 plus rejected A14 dispositioned                                                          |
| Model coverage            |     16 | 16 branches dispositioned                                                                       |
| Dataset coverage          |      3 | 3 datasets individually and cross-dataset analyzed                                              |
| Metric coverage           |      6 | BACC primary; F1/ACC secondary; ROC-AUC conditional; classwise not invented; burden descriptive |
| Failure coverage          |      7 | FailureCaseIndex/NegativeResultNote/DiagnosticOnlyFlag semantics separated                      |

No scientifically material P02 responsibility is left as `MISSING_FROM_ANALYSIS` or `PRESENT_BUT_SHALLOW`. Requirements that are workflow/serialization/packaging responsibilities rather than scientific analytical questions are marked `NOT_APPLICABLE` to analytical depth rather than being falsely expanded into scientific findings.

## 29.1 Stage coverage

All 26 canonical Stage/Gate pairs and the Stage18S supplement are dispositioned in `machine_readable/P02_stage_coverage_matrix.csv`. Engineering-only stages are treated concisely; Stages 11, 12, 15-19 and Stage18S receive the scientific depth appropriate to the evidence they produced.

## 29.2 Ablation coverage

`machine_readable/P02_ablation_coverage_matrix.csv` explicitly dispositions A0-A13 and preserves A14 as rejected/prohibited. Only A0 and A4 are P02 analytical executions; downstream ablations remain downstream responsibilities and are not inferred from raw P02 decoder evidence.

## 29.3 Model, dataset, metric, and failure coverage

The final model matrix dispositions all 16 branches, including sanity/diagnostic, failed, conditional-skip, dependency-blocked and successful families. The dataset matrix covers BNCI2014_001, Lee2019_MI and PhysioNetMI individually and in cross-dataset synthesis. The metric matrix separates BACC, macro-F1, ACC and conditional ROC-AUC from unexecuted class-wise analyses. The failure matrix preserves exact count/denominator/reason/canonical-impact semantics.

# 30. Final Candidate-Claim Readiness and Prohibited Stronger Wording

Candidate claims remain **pending Layer 0 review**. Final R2 adds an explicit safety surface so the next governance step does not need to infer the boundary from prose:

| candidate_claim_id   | claim_text                                                                                                                                                                                                                                                                   | claim_ceiling                | prohibited_stronger_wording                                                                                       | layer0_readiness              |
|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------|:------------------------------------------------------------------------------------------------------------------|:------------------------------|
| P02-CLAIM-CAND-001   | Under the frozen P01 subject-grouped binary motor-imagery protocol, P02 established a complete multi-family raw decoder/baseline measurement spine across three public EEG datasets.                                                                                         | SUPPORTED                    | Do not call P02 calibration-, threshold-, abstention-, safety-, or deployment-ready.                              | READY_FOR_REVIEW_NOT_APPROVED |
| P02-CLAIM-CAND-002   | Decoder-family performance was dataset-dependent rather than universally ordered: DBConformer was descriptively strongest at full training on Lee2019_MI and PhysioNetMI, while CSP-LDA led the single-participant BNCI2014_001 test split.                                  | SUPPORTED_WITH_QUALIFICATION | Do not claim one decoder is universally best across datasets or participants.                                     | READY_FOR_REVIEW_NOT_APPROVED |
| P02-CLAIM-CAND-003   | PhysioNetMI exhibited statistically detectable overall decoder heterogeneity under the governed A0 comparison, but no individual alternative-versus-CSP-LDA contrast survived Holm correction.                                                                               | SUPPORTED_WITH_QUALIFICATION | Do not convert omnibus heterogeneity into a significant pairwise winner claim.                                    | READY_FOR_REVIEW_NOT_APPROVED |
| P02-CLAIM-CAND-004   | Extreme low-label decoding remained difficult and non-monotonic under the single frozen subset design; P02 does not support a universal sample-efficiency ordering among CSP-LDA, tangent-space, EEGNet and CBraMod.                                                         | SUPPORTED_WITH_QUALIFICATION | Do not claim stable sample-efficiency ordering or subset-robust low-label behavior.                               | READY_FOR_REVIEW_NOT_APPROVED |
| P02-CLAIM-CAND-005   | The Phase-02 training-correction history demonstrates that optimization/training-policy fidelity can materially affect whether an EEG architecture appears collapsed or viable, so optimization failure should not automatically be interpreted as architectural incapacity. | SUPPORTED_WITH_QUALIFICATION | Do not claim architecture superiority or theoretical invalidity of the original uniform policy.                   | READY_FOR_REVIEW_NOT_APPROVED |
| P02-CLAIM-CAND-006   | The Stage-11 S&R diagnostic challenger did not yield a consistent participant-level BACC improvement over the canonical primary EEGNet across the three datasets.                                                                                                            | SUPPORTED                    | Do not claim the Stage11 challenger improved EEGNet generally.                                                    | READY_FOR_REVIEW_NOT_APPROVED |
| P02-CLAIM-CAND-007   | Within the canonical resource-constrained A4 execution, the C1-C3 longer/multi-view role controls did not produce statistically detectable improvements after the governed paired testing procedure.                                                                         | SUPPORTED_WITH_QUALIFICATION | Do not claim zero A4 effect, five-repeat stability, dense deep-budget characterization, or full-grid equivalence. | READY_FOR_REVIEW_NOT_APPROVED |
| P02-CLAIM-CAND-008   | A hard-vote model ensemble was not uniformly beneficial: one governed PhysioNetMI full-training comparison showed a Holm-significant disadvantage relative to the validation-selected strongest constituent.                                                                 | SUPPORTED_WITH_QUALIFICATION | Do not claim ensembles are generally inferior; one corrected comparison was negative.                             | READY_FOR_REVIEW_NOT_APPROVED |
| P02-CLAIM-CAND-009   | Post-hoc Stage18S sensitivity evidence indicates that A4 effect direction can change across repeats and budgets, reinforcing the Protocol restriction against five-repeat stability or dense-budget response claims from canonical Stage18.                                  | POST_HOC_ONLY                | Do not present Stage18S as confirmatory or as modifying G18.                                                      | READY_FOR_REVIEW_NOT_APPROVED |
| P02-CLAIM-CAND-010   | P02 provides a fail-closed, provenance-rich Layer-2 evidence substrate for downstream phases while preserving unsuccessful, incompatible, skipped and diagnostic outcomes rather than retaining successful models only.                                                      | SUPPORTED                    | Do not equate technical evidence readiness with deployment readiness.                                             | READY_FOR_REVIEW_NOT_APPROVED |

The complete machine-readable version is `machine_readable/P02_claim_readiness.csv`. Nothing in this table constitutes approval.

# 31. Final Unresolved-Question Register

The analysis closes without manufacturing answers to questions the executed design cannot settle:

1. **Low-label subset stability:** would repeated independent subsets produce stable sample-efficiency rankings?
2. **A4 repeat stability:** would effect directions stabilize under the originally envisioned five repeats?
3. **Dense deep-budget response:** what happens between the executed 1/class, 8/class and FULL_TRAIN anchors?
4. **Participant-aware selection:** would a prospective participant-aware selector outperform a fixed decoder family?
5. **Training-policy mechanism:** which specific optimization component causes the Stage11/12 architecture-dependent sensitivity?

These are preserved in `machine_readable/P02_unresolved_questions.yaml`; none is silently answered by post-hoc reinterpretation.

# 32. Final Scientific Closure Statement

After the final evidence-completeness, numerical-depth, interpretive-depth, claim-safety, paper-reuse and coherence passes, Phase 02 supports the following bounded scientific memory:

- P02 established a complete, provenance-preserving Layer-2 decoder measurement substrate with A0 fully closed and unsuccessful states retained.
- Full-training model performance is **dataset- and participant-dependent**; descriptive leaders differ by dataset, and multiplicity-adjusted A0 comparisons do not support a universal pairwise winner.
- The full governed low-label trajectory is difficult, non-monotonic and rank-reversing under one frozen subset per budget; stable sample-efficiency ordering is not established.
- Stage11/12 demonstrate that source/author training fidelity can materially change apparent collapse/viability, but diagnostic rescue does not establish universal test superiority.
- Canonical A4 is scientifically usable for its authorized single-repeat/anchor-budget scope, but C1-C3 provide no statistically detected positive effect under the governed family and the only Holm-significant C4/C5 result is a negative hard-vote comparison.
- Stage18S strengthens the **limitation**, not the confirmatory claim: repeat/budget effect signs are often unstable and all 15 MR00 budget trajectories change sign somewhere in the descriptive probe.
- Failure, null and diagnostic evidence is preserved with exact semantics instead of being sanitized away.
- The literature supports using these results as a controlled project-specific measurement study; it does not justify naive cross-paper leaderboard claims.
- Ten candidate claims are ready for Layer 0 review with explicit prohibited stronger wording; four mechanism hypotheses remain clearly non-causal hypotheses.

The analytical document is therefore complete. Its remaining limitations are genuine properties of the executed scientific design - especially A4 repeat/budget contraction, the single-subset low-label design, BNCI's one held-out test participant, Stage18S's post-hoc status, and external-study comparability - rather than missing Phase Analysis work.

**P02_PHASE_ANALYSIS_STATUS = FINALIZED_WITH_EXPLICIT_NONBLOCKING_LIMITATIONS**

# Appendices

## Appendix A - Canonical identities

- Phase: `P02`
- Layer: `L2`
- Run: `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`
- Run configuration SHA-256: `9e181d2e935d2e9674ca6e05572f49520ad0306a3761362b770f8bee8c78ce13`
- Scientific freeze: `P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5`
- Scientific freeze SHA-256: `7449216c988eec14191ba85300d720547f06fbc6ac7020e9e142bf12a4b0a598`
- Logical notebook ID: `IHARQ-P02-COMPLETE-EXECUTION-AND-ANALYSIS-R4`
- Runtime source fingerprint: `a54bfa816acc6763c1d1042b8c65cf54ae04ec774c57ec50de86014a6730c5fa`
- Runtime revision config SHA-256: `d82334535e397c681d6172694da96d3fff0143ffb1b63a18876ee1f7778f60a1`
- Stage-plan SHA-256: `043eb30e008af910d37c563e8be8c719ef881cf009aec3e34687dc97bdc34aad`
- Analysis release: `P02-PHASE-ANALYSIS-FINAL-R2`

## Appendix B - A0 numeric source

See `table_sources/P02_Table_A0_fulltrain_branch_summary.csv`, `P02_Table_A0_participant_first_fulltrain_source.csv`, and canonical `analysis_inputs/a0_statistics.json`.

## Appendix C - A4 numeric source

See `table_sources/P02_Table_A4_role_control_statistics.csv`, `P02_Table_A4_C4_C5_statistics.csv`, and canonical A4 analysis inputs.

## Appendix D - Literature references

1. Lawhern VJ et al. **EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces.** Journal of Neural Engineering. 2018;15(5):056013. DOI: 10.1088/1741-2552/aace8c. https://pubmed.ncbi.nlm.nih.gov/29932424/
2. Mane R et al. **A Multi-view CNN with Novel Variance Layer for Motor Imagery Brain Computer Interface.** IEEE EMBC 2020; FBCNet extended work/toolbox: arXiv:2104.01233. https://pubmed.ncbi.nlm.nih.gov/33018625/
3. Wang Z et al. **DBConformer: Dual-Branch Convolutional Transformer for EEG Decoding.** IEEE Journal of Biomedical and Health Informatics. 2026;30(5):4134-4147. DOI: 10.1109/JBHI.2025.3622725. https://pubmed.ncbi.nlm.nih.gov/41129442/
4. Wang J et al. **CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding.** ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/bbbd6d915cb90be21c1254a82d45cedd-Abstract-Conference.html
5. Barachant A et al. **Classification of covariance matrices using a Riemannian-based kernel for BCI applications.** Neurocomputing. 2013;112:172-178. DOI: 10.1016/j.neucom.2012.12.039.
6. Chevallier S et al. **The largest EEG-based BCI reproducibility study for open science: the MOABB benchmark.** arXiv:2404.15319 (2024).
7. Wang G et al. **EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals.** NeurIPS 2024. DOI: 10.52202/079017-1239.
8. Lee M-H et al. **EEG dataset and OpenBMI toolbox for three BCI paradigms: an investigation into BCI illiteracy.** GigaScience. 2019;8(5):giz002. DOI: 10.1093/gigascience/giz002.
9. Schalk G. **EEG Motor Movement/Imagery Dataset v1.0.0.** PhysioNet. 2009. DOI: 10.13026/C28G6P.
10. Tangermann M et al. **Review of the BCI Competition IV.** Frontiers in Neuroscience. 2012;6:55. DOI: 10.3389/fnins.2012.00055.
11. Wang P, Xie T, Zhou Y, Gong P, Chan RHM. **TCPL: task-conditioned prompt learning for few-shot cross-subject motor imagery EEG decoding.** Frontiers in Neuroscience. 2025;19:1689286. DOI: 10.3389/fnins.2025.1689286. https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1689286/full
12. Xiong W et al. **EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models.** arXiv:2508.17742 (2025). https://arxiv.org/abs/2508.17742
13. Vasques X, Barbaste P, Oullier O. **Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders.** arXiv:2606.24394 (2026 preprint). https://arxiv.org/abs/2606.24394

## Appendix E - Machine-readable analytical package

- `machine_readable/P02_findings.yaml`
- `machine_readable/P02_candidate_claims.yaml`
- `machine_readable/P02_results_to_claims.yaml`
- `machine_readable/P02_mechanism_hypotheses.yaml`
- `machine_readable/P02_ablation_analysis.yaml`
- `machine_readable/P02_failure_negative_result_summary.yaml`
- `machine_readable/P02_paper_evidence_index.yaml`
- `machine_readable/P02_downstream_handoff.yaml`
- `machine_readable/P02_analysis_index.yaml`
- `machine_readable/P02_literature_comparison.csv`
- `machine_readable/P02_literature_references.json`
- `machine_readable/P02_canonical_analysis_inputs.yaml`
- `machine_readable/P02_stage_result_index.csv`
- `machine_readable/P02_statistical_summary.csv`
- `machine_readable/P02_figure_table_traceability.yaml`
- `machine_readable/P02_analysis_source_inventory.yaml`


## Appendix F - Frozen canonical Phase Analysis input contract

The finalized P02 Protocol authorizes exactly **38 canonical Phase Analysis inputs**. This report uses that contract as a hard analytical boundary:

1. `runtime/analysis_inputs/a0_completion.json`
2. `runtime/analysis_inputs/a0_closure_source_manifest.json`
3. `runtime/analysis_inputs/a0_participant_metrics.csv`
4. `runtime/analysis_inputs/a0_statistics.json`
5. `runtime/analysis_inputs/a4_completion.json`
6. `runtime/analysis_inputs/a4_participant_metrics.csv`
7. `runtime/analysis_inputs/a4_role_control_statistics.json`
8. `runtime/analysis_inputs/a4_role_control_participant_comparisons.csv`
9. `runtime/analysis_inputs/a4_c4_c5_statistics.json`
10. `runtime/analysis_inputs/a4_c4_c5_comparison_artifacts.jsonl`
11. `runtime/analysis_inputs/a4_c4_c5_participant_comparisons.csv`
12. `runtime/analysis_inputs/a4_burden_source.csv`
13. `runtime/analysis_inputs/low_label_curve_summary.json`
14. `runtime/analysis_inputs/low_label_metric_source.csv`
15. `runtime/analysis_inputs/subject_profile_summary.json`
16. `runtime/analysis_inputs/subject_profile_metric_source.csv`
17. `runtime/analysis_inputs/session_profile_metric_source.csv`
18. `runtime/analysis_inputs/failure_negative_summary.json`
19. `runtime/analysis_inputs/figure_table_source_manifest.json`
20. `runtime/analysis_inputs/training_policy_challenger_completion.json`
21. `runtime/analysis_inputs/training_policy_challenger_statistics.json`
22. `runtime/analysis_inputs/training_policy_challenger_participant_comparisons.jsonl`
23. `runtime/analysis_inputs/training_policy_challenger_seed_comparisons.jsonl`
24. `runtime/analysis_inputs/training_policy_challenger_terminal_states.jsonl`
25. `runtime/analysis_inputs/training_policy_sr_probability_calibration_candidates.jsonl`
26. `runtime/analysis_inputs/training_policy_sr_probability_selection.json`
27. `runtime/analysis_inputs/stage18_resource_constrained_anchor_budget_deviation.json`
28. `runtime/analysis_inputs/stage18S_balanced_sensitivity_R1_preexecution_freeze.json`
29. `runtime/analysis_inputs/stage18S_R1_combined_cell_effects.csv`
30. `runtime/analysis_inputs/stage18S_R1_participant_paired_effects.csv`
31. `runtime/analysis_inputs/stage18S_R1_three_repeat_anchor_stability.csv`
32. `runtime/analysis_inputs/stage18S_R1_six_budget_mr00_sensitivity.csv`
33. `runtime/analysis_inputs/stage18S_R1_member_training_provenance.csv`
34. `runtime/analysis_inputs/stage18S_R1_training_provenance_summary.csv`
35. `runtime/protocol_change_required/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml`
36. `runtime/handoffs/stage18S_R1_sensitivity_evidence.json`
37. `runtime/manifests/stage_artifacts/20_readiness.json`
38. `runtime/manifests/record_partitions/Layer2ReadinessReport/P02-L2-READINESS-P03.json`

All 38 paths are locally present in the accepted P02 light runtime state and are checksum-indexed in `machine_readable/P02_canonical_analysis_inputs.yaml`.

## Appendix G - Stage-result index

The main narrative expands only scientifically consequential stages; this index preserves the complete canonical stage progression plus the distinct Stage18S supplement.

| record_type     | stage_or_supplement_id   | attempt_id   | status   | observability_status   | purpose                                                                            | runtime_successor_id                                                                    | evidentiary_role                                           |
|:----------------|:-------------------------|:-------------|:---------|:-----------------------|:-----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|:-----------------------------------------------------------|
| CANONICAL_STAGE | 00                       | 634837763ab9 | SUCCESS  | PASS                   | authority identity and notebook/build-book/freeze preflight                        | nan                                                                                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 01                       | d4ab0101ea08 | SUCCESS  | PASS                   | environment, resource, and credential interface preflight                          | nan                                                                                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 02                       | c87fadef7bcd | SUCCESS  | PASS                   | cumulative prior-state resolution                                                  | nan                                                                                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 03                       | 5b6834384730 | SUCCESS  | PASS                   | external/local pointer resolution                                                  | nan                                                                                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 04                       | 3ec63b778b7d | SUCCESS  | PASS                   | P01 frozen-input validation and immutability checks                                | nan                                                                                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 05                       | 39df114163ce | SUCCESS  | PASS                   | scientific freeze, run-cell routing, and training-policy declarations              | nan                                                                                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 06                       | 879c816b6a5b | SUCCESS  | PASS                   | schema/config import and clean-process validation                                  | nan                                                                                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 07                       | f96233a7477e | SUCCESS  | PASS                   | data-loader, label, denominator, split, and leakage contract validation            | nan                                                                                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 08                       | 83b1345dfb42 | SUCCESS  | PASS                   | sanity and diagnostic family execution                                             | P02-RUNTIME-SUCCESSOR-R1-CLASS-WEIGHT-APPLICABILITY-LIVE-CONTINUATION                   | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 09                       | c31206f11c83 | SUCCESS  | PASS                   | classical decoder family execution (CSP-LDA, FBCSP-LR)                             | P02-RUNTIME-SUCCESSOR-R2-CANONICAL-LOW-CAL-BUDGET-ID-PARSER-LIVE-CONTINUATION           | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 10                       | 8e4ca693efde | SUCCESS  | PASS                   | Riemannian family execution (TS-LR, EA-TS, MDM diagnostic)                         | P02-RUNTIME-SUCCESSOR-R2-CANONICAL-LOW-CAL-BUDGET-ID-PARSER-LIVE-CONTINUATION           | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 11                       | 77533b224dad | SUCCESS  | PASS                   | EEGNet neural family execution and training-policy amendment/challenger history    | nan                                                                                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 12                       | b9d3bbee230b | SUCCESS  | PASS                   | conditional external/deep/foundation families and source-centered training recipes | P02-RUNTIME-SUCCESSOR-R6R5-STAGE12-FBCNET-AUTHOR-HORIZON-1500-200                       | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 13                       | 01b2fde44053 | SUCCESS  | PASS                   | checkpoint closure and round-trip validation                                       | P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 14                       | 6f67192684bf | SUCCESS  | PASS                   | prediction/score-semantics closure                                                 | P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 15                       | 0cedb7522386 | SUCCESS  | PASS                   | A0 and training-policy challenger analytical closure                               | P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 16                       | bb462cca110e | SUCCESS  | PASS                   | low-label analytical materialization and inherited-budget identity repair          | P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 17                       | 785dd4d86f13 | SUCCESS  | PASS                   | participant/session profile materialization                                        | P02-RUNTIME-SUCCESSOR-R7H7-STAGE11-EEGNET-AUTHOR-CENTERED-10000E-TRUE-P120-CONTINUATION | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 18                       | a91f9d90814c | SUCCESS  | PASS                   | A4 canonical resource-constrained execution and statistics                         | P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 18U                      | 6c35912e38f7 | SUCCESS  | PASS                   | A4 unlock/authority-contract closure                                               | P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 19                       | 243091602665 | SUCCESS  | PASS                   | failure, negative-result, and diagnostic evidence aggregation                      | P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 20                       | b5a19c3412a2 | SUCCESS  | PASS                   | Layer-2 readiness and P03 substrate decision                                       | P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 21                       | 3d6646e74d1e | SUCCESS  | PASS                   | figure/table source-family closure                                                 | P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 22                       | 6bad6ea9c5ff | SUCCESS  | PASS                   | Protocol/Phase Analysis/Layer0/EvidenceMap/Layer10/P03 handoffs                    | P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 23                       | 0e3f7416ac5e | SUCCESS  | PASS                   | evidence-sufficiency closure                                                       | P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1                     | CANONICAL_EXECUTION_HISTORY                                |
| CANONICAL_STAGE | 24                       | 5027e6f7359e | SUCCESS  | PASS                   | final bundle/release and external-preservation finalization                        | P02-RUNTIME-SUCCESSOR-R10-STAGE18-A4-ANCHOR-BUDGET-SINGLE-REPEAT-R1                     | CANONICAL_EXECUTION_HISTORY                                |
| SUPPLEMENT      | 18S                      | nan          | PASS     | PASS                   | post-hoc balanced sensitivity supplement for repeat/budget stability diagnosis     | nan                                                                                     | POST_HOC_DESCRIPTIVE_ONLY; canonical Stage18/G18 unchanged |

The canonical run matrix contains 26 stage records (00-24 plus 18U). Stage18S is deliberately listed as a **supplement**, not as a replacement canonical stage or a new G18.

## Appendix H - Analytical source and figure/table traceability

- `machine_readable/P02_analysis_source_inventory.yaml` records the authority/execution/prior-analysis/literature source families used to construct this report.
- `machine_readable/P02_figure_table_traceability.yaml` maps every generated figure and numeric table-source file to the canonical execution source from which it was derived.
- `machine_readable/P02_statistical_summary.csv` collects existing governed statistical outputs for navigation; it does not add a new test family.
- `table_sources/P02_Table_low_label_budget_deltas.csv` contains descriptive adjacent-budget deltas only; no inferential or monotonicity test was added.

**Phase Analysis status: COMPLETE_FOR_LAYER0_EVIDENCE_MAP_LAYER10_HANDOFF**


These external headline performance values are not directly comparable to the IHARQ results because the datasets, labels, split regimes, supervision levels, preprocessing pipelines, and metric definitions differ materially across studies.

## Appendix I - Finalization closure artifacts

The following closure artifacts are authoritative companions to this Final R2 analysis:

- `machine_readable/P02_expected_evidence_matrix.csv`
- `machine_readable/P02_actual_evidence_inventory.csv`
- `machine_readable/P02_phase_completeness_matrix.csv`
- `machine_readable/P02_stage_coverage_matrix.csv`
- `machine_readable/P02_ablation_coverage_matrix.csv`
- `machine_readable/P02_model_coverage_matrix.csv`
- `machine_readable/P02_dataset_coverage_matrix.csv`
- `machine_readable/P02_metric_coverage_matrix.csv`
- `machine_readable/P02_failure_coverage_matrix.csv`
- `machine_readable/P02_claim_readiness.csv`
- `machine_readable/P02_unresolved_questions.yaml`
- `literature/P02_literature_fresh_verification.json`
- `validation/P02_Phase_Analysis_Final_R2_Validation.json`

These artifacts make the expected/actual/analyzed triangulation and downstream claim boundaries machine-readable.

