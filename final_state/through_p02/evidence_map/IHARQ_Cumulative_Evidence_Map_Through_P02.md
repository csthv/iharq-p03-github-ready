---
title: "IHARQ Cumulative Evidence Map Through P02"
canonical_map_id: "IHARQ-CUMULATIVE-EVIDENCE-MAP-THROUGH-P02-R1"
release_id: "P00-P02-EVIDENCE-MAP-RELEASE-R1"
generated_at: "2026-08-14T21:30:00+03:30"
status: "FINALIZED"
---

# IHARQ Cumulative Evidence Map Through P02

> **Primary deliverable.** This Evidence Map is the current navigational/provenance layer between governed scientific interpretation and downstream Layer 10 rendering. It organizes evidence; it does not approve claims. Claim authorization is inherited from Layer 0.

## 1. Provenance model

`Claim -> Finding -> Interpretation/Analysis -> Metric/Statistic -> Protocol/Comparison -> Run -> Execution Artifact -> Source/External Artifact -> Manifest/Hash/Revision`

Limitations, negative evidence, historical supersessions, literature roles, figures and tables are linked into the same chain. External literature is never treated as project empirical evidence.

## 2. Coverage summary

- Reviewed claim rows: **37** (19 preserved P00/P01 + 10 P02 + 8 cumulative).
- Finding rows: **49**.
- P02 canonical analysis-input evidence nodes: **38**.
- Total evidence nodes: **69**.
- Artifact registry rows: **47**.
- Relationship rows: **146**.
- Current Layer 10 figures: **14**; tables: **13**.

## 3. Historical preservation

The P00/P01 Evidence Map is not rebuilt from memory. Its 19 claim rows are preserved from `IHARQ-CUMULATIVE-EVIDENCE-MAP-THROUGH-P01-R1`, and the predecessor package is embedded byte-for-byte under `preserved_prior/`. Additive P02/cumulative relationships do not change historical Layer 0 wording or disposition.

## 4. P02 evidence saturation

The finalized P02 Phase Analysis had **104/104 expected-evidence requirements dispositioned** (72 fully analyzed, 32 not applicable), **46 actual evidence families dispositioned**, and **38 canonical analysis inputs**. This downstream map preserves those evidence families through claim, finding, limitation, negative-evidence or non-claim supporting roles. No material P02 evidence family is permitted to disappear merely because it is not selected for a Layer 10 figure.

### P02 claim-to-evidence mappings

#### P02-CLM-001/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** Under the frozen P01 subject-grouped binary motor-imagery protocol, P02 established a complete multi-family raw accept-all decoder/baseline measurement spine across the three activated public EEG datasets; this is Layer-2 measurement evidence and does not establish calibration, abstention, clinical effectiveness, safety, or deployment readiness.

**Findings:** `P02-FIND-001`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `analysis_inputs/a0_completion.json`, `analysis_inputs/a0_participant_metrics.csv`

**Exact numeric support:** `{"A0_terminal_cells": 678, "SUCCESS": 657, "FAILED": 3, "CONDITIONAL_SKIP": 15, "DEPENDENCY_BLOCKED": 3, "datasets": 3}`

**Limitations:** `PUBLIC_EEG_ONLY`, `NO_CALIBRATION_POLICY_CLAIM`

**Layer 10:** figures none; tables `L10-P02-TBL-001`

#### P02-CLM-002/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** Within full-training A0, descriptive decoder ordering was dataset-dependent: CSP-LDA led the single-participant BNCI2014_001 test split, while DBConformer had the highest participant-first mean BACC on Lee2019_MI and PhysioNetMI. These rankings are descriptive and do not establish a universal winning decoder.

**Findings:** `P02-FIND-002`, `P02-FIND-003`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `table_sources/P02_Table_A0_fulltrain_branch_summary.csv`

**Exact numeric support:** `{"full_training_descriptive_leaders": {"BNCI2014_001": {"branch_id": "CLS-CSP-LDA", "participant_first_mean_BACC": 0.6388888888888888, "participants": 1}, "Lee2019_MI": {"branch_id": "DNN-SEQ", "participant_first_mean_BACC": 0.795, "participants": 6}, "PhysioNetMI": {"branch_id": "DNN-SEQ", "participant_first_mean_BACC": 0.649724517906336, "participants": 11}}}`

**Limitations:** `DATASET_HETEROGENEITY`, `BNCI_TEST_PARTICIPANTS_1`

**Layer 10:** figures `L10-P02-FIG-001`, `L10-P02-FIG-009`, `L10-P02-FIG-010`; tables `L10-P02-TBL-001`

#### P02-CLM-003/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** On PhysioNetMI full-training A0, the governed Friedman comparison detected overall decoder heterogeneity (statistic 20.544, p=0.00451, Kendall W=0.267), while no individual alternative-versus-CSP-LDA contrast survived Holm correction; the omnibus result therefore does not identify a statistically supported pairwise winner.

**Findings:** `P02-FIND-003`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `analysis_inputs/a0_statistics.json`

**Exact numeric support:** `{"PhysioNetMI_Friedman_statistic": 20.544, "p_value": 0.00451, "Kendall_W": 0.267, "Lee2019_MI_Friedman_p": 0.148, "Holm_significant_alt_vs_CSP_LDA": 0}`

**Limitations:** `MULTIPLICITY`, `PARTICIPANT_HETEROGENEITY`

**Layer 10:** figures `L10-P02-FIG-001`; tables `L10-P02-TBL-001`

#### P02-CLM-004/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** Across the governed 1, 2, 4, 8, 16 and 32 labels/class P02 low-label surface, performance was difficult, non-monotonic and rank-changing under one frozen subset per budget; the evidence does not support a stable or universal sample-efficiency ordering among the evaluated branches.

**Findings:** `P02-FIND-005`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `analysis_inputs/low_label_curve_summary.json`, `analysis_inputs/low_label_metric_source.csv`

**Exact numeric support:** `{"governed_low_label_budgets_per_class": [1, 2, 4, 8, 16, 32], "leader_changes": {"BNCI2014_001": 4, "Lee2019_MI": 4, "PhysioNetMI": 6}, "design": "single frozen subset per budget"}`

**Limitations:** `SINGLE_FROZEN_SUBSET`, `NO_LOW_LABEL_REPEAT_STABILITY`

**Layer 10:** figures `L10-P02-FIG-002`, `L10-P02-FIG-003`, `L10-P02-FIG-004`; tables `L10-P02-TBL-002`, `L10-P02-TBL-003`

#### P02-CLM-005/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** The preserved P02 training-correction history shows that model viability and optimization behavior under the implemented configurations depended materially on training-policy choice. This supports treating inadequate optimization as distinct from demonstrated architectural incapacity, but does not establish universal test-set gains, architecture superiority, or theoretical invalidity of the earlier generic policy.

**Findings:** `P02-FIND-006`, `P02-FIND-008`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `runtime/diagnostics/runtime_successor/stage11_maximum_analysis/stage11_source_centered_recipe.json`, `machine_readable P02 Protocol run matrix`

**Exact numeric support:** `{"Stage12_validation_only_examples": [{"dataset_id": "BNCI2014_001", "branch_id": "DNN-FBCNET", "A_BACC": 0.5, "B_BACC": 0.7222222222222222, "absolute_delta_BACC": 0.2222222222222222, "claim_bearing": false}, {"dataset_id": "PhysioNetMI", "branch_id": "DNN-FBCNET", "A_BACC": 0.6395092565383486, "B_BACC": 0.6601038299539622, "absolute_delta_BACC": 0.0205945734156136, "claim_bearing": false}, {"dataset_id": "PhysioNetMI", "branch_id": "DNN-SEQ", "A_BACC": 0.6985502987559996, "B_BACC": 0.7167940052894505, "absolute_delta_BACC": 0.0182437065334508, "claim_bearing": false}, {"dataset_id": "PhysioNetMI", "branch_id": "SSL-CBRAMOD", "A_BACC": 0.5, "B_BACC": 0.6384072876873348, "absolute_delta_BACC": 0.1384072876873348, "claim_bearing": false}], "test_role_loaded": false}`

**Limitations:** `POST_OBSERVATION_AMENDMENT`, `DIAGNOSTIC_VALIDATION_EVIDENCE`

**Layer 10:** figures `L10-P02-FIG-005`; tables `L10-P02-TBL-004`, `L10-P02-TBL-005`

#### P02-CLM-006/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** The Stage-11 S&R diagnostic challenger did not yield a consistent participant-level BACC improvement over the canonical primary EEGNet across BNCI2014_001, Lee2019_MI and PhysioNetMI; it remains diagnostic-only and does not replace primary A0 evidence.

**Findings:** `P02-FIND-007`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `analysis_inputs/training_policy_challenger_statistics.json`

**Exact numeric support:** `{"diagnostic_challenger": [{"dataset_id": "BNCI2014_001", "n": 5, "median_delta_BACC": -0.0347222222222222, "ci_low": -0.0763888888888889, "ci_high": -0.0347222222222221, "p_value": 0.125, "rank_biserial": -0.8666666666666667}, {"dataset_id": "Lee2019_MI", "n": 30, "median_delta_BACC": 0.01, "ci_low": -0.005, "ci_high": 0.025, "p_value": 0.2309220325143355, "rank_biserial": 0.2586206896551724}, {"dataset_id": "PhysioNetMI", "n": 55, "median_delta_BACC": 0.0, "ci_low": -0.0343477914915631, "ci_high": 0.0029761904761905, "p_value": 0.455185419014922, "rank_biserial": -0.1190130624092888}]}`

**Limitations:** `DIAGNOSTIC_ONLY`

**Layer 10:** figures `L10-P02-FIG-005`; tables `L10-P02-TBL-005`

#### P02-CLM-007/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** Within the canonical resource-constrained A4 scope, none of the 756 governed C1-C3 role-control statistical rows reached raw p<=0.05. This is an absence of statistically detected improvement under the executed scope, not proof that the true effect is zero and not evidence of five-repeat or dense-budget stability.

**Findings:** `P02-FIND-009`, `P02-FIND-010`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `analysis_inputs/a4_completion.json`, `analysis_inputs/stage18_resource_constrained_anchor_budget_deviation.json`

**Exact numeric support:** `{"governed_C1_C3_statistical_rows": 756, "raw_p_le_0_05": 0, "scope": "single canonical refit repeat / governed deep anchor budgets"}`

**Limitations:** `SINGLE_REPEAT`, `DEEP_ANCHOR_BUDGETS`

**Layer 10:** figures `L10-P02-FIG-006`; tables `L10-P02-TBL-006`

#### P02-CLM-008/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** A hard-vote ensemble was not uniformly beneficial: one governed PhysioNetMI full-training C4 comparison at repeat 4 showed a Holm-significant disadvantage relative to the validation-selected EEGNet constituent (median delta BACC -0.0435; Holm p=0.0371). This cell-specific negative result does not establish that ensembles are generally inferior.

**Findings:** `P02-FIND-011`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `analysis_inputs/a4_c4_c5_statistics.json`

**Exact numeric support:** `{"Holm_significant_rows": 1, "significant_rows": [{"comparison_id": "P02-A4-PhysioNetMI-ENSEMBLE-A4-C4-MODEL-HARD-VOTE-FULL_TRAIN-ER04:VS_STRONGEST", "dataset_id": "PhysioNetMI", "condition_id": "A4-C4-MODEL-HARD-VOTE", "budget_id": "FULL_TRAIN", "repeat": 4, "strongest_constituent_branch": "DNN-EEGNET", "closure_status": "COMPLETE", "n": 11.0, "median_delta_BACC": -0.0434782608695651, "p_value": 0.0185546875, "holm_adjusted_p": 0.037109375, "rank_biserial": -0.7878787878787878, "ci_low": -0.1304347826086956, "ci_high": -0.0119047619047618}]}`

**Limitations:** `CELL_SPECIFIC_EFFECT`

**Layer 10:** figures none; tables `L10-P02-TBL-007`

#### P02-CLM-009/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** Post-hoc Stage18S sensitivity evidence shows that A4 effect direction can change across descriptive repeats and budgets (22/45 anchor trajectories mixed-sign; all 15 six-budget MR00 trajectories changed sign at least once). This supports the existing claim ceiling but remains POST_HOC/DESCRIPTIVE/SENSITIVITY evidence and does not modify canonical Stage18/G18.

**Findings:** `P02-FIND-012`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `analysis_inputs/stage18S_R1_decision_support_summary.json`, `analysis_inputs/stage18S_R1_three_repeat_anchor_stability.csv`, `analysis_inputs/stage18S_R1_six_budget_mr00_sensitivity.csv`

**Exact numeric support:** `{"three_repeat_anchor_trajectories": 45, "all_negative": 7, "mixed": 22, "all_positive": 16, "six_budget_trajectories": 15, "six_budget_with_sign_flip": 15}`

**Limitations:** `POST_HOC_ONLY`, `THREE_REPEAT_NOT_FIVE_REPEAT`

**Layer 10:** figures `L10-P02-FIG-007`; tables `L10-P02-TBL-008`

#### P02-CLM-010/v1

**Layer 0 disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed claim:** P02 provides a fail-closed, provenance-rich Layer-2 evidence substrate for downstream use while preserving successful and non-success outcomes, including 648 FailureCaseIndex records, 340 NegativeResultNotes and 309 DiagnosticOnlyFlags. This is technical evidence readiness, not deployment readiness or future-phase scientific success.

**Findings:** `P02-FIND-013`, `P02-FIND-014`

**Run:** `P02-L2-OFFICIAL-RUN-R4DYN-9e181d2e935d`

**Analysis sources:** `analysis_inputs/failure_negative_summary.json`, `negative_and_failed_results/`

**Exact numeric support:** `{"FailureCaseIndex": 648, "NegativeResultNote": 340, "DiagnosticOnlyFlag": 309, "failure_terminal_breakdown": {"CONDITIONAL_SKIP": 591, "NOT_APPLICABLE_REPEAT_SLOT": 42, "INPUT_INCOMPATIBLE": 9, "FAILED": 3, "DEPENDENCY_BLOCKED": 3}}`

**Limitations:** `DOWNSTREAM_SCIENCE_NOT_EXECUTED`

**Layer 10:** figures `L10-P02-FIG-008`; tables `L10-P02-TBL-009`

## 5. Cumulative P00-P02 claim provenance

### CUM-CLM-001/v1

**Disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed text:** Through P02, IHARQ has a governed evidence chain linking validated foundation contracts, the frozen P01 provenance-traceable EEG substrate, and P02 Layer-2 decoder evidence through explicit identities, manifests and handoffs; this traceability does not by itself establish clinical or deployment effectiveness.

**Cumulative findings:** `CF-01`, `CF-02`, `CF-09`

**Contributing phase evidence:** resolved through `cumulative_findings.yaml`, `results_to_claims.yaml`, and the phase-local finding/evidence nodes.

**Limitations:** Technical traceability is not scientific/clinical effectiveness by itself.

### CUM-CLM-002/v1

**Disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed text:** The P02 decoder analyses consume the frozen P01 subject-grouped, denominator-conserving binary motor-imagery data contract rather than a P02-local redefinition of labels, split or core windows, subject to the scope of the implemented registered integrity and leakage checks.

**Cumulative findings:** `CF-02`

**Contributing phase evidence:** resolved through `cumulative_findings.yaml`, `results_to_claims.yaml`, and the phase-local finding/evidence nodes.

**Limitations:** Bounded to the implemented registered leakage/disjointness checks.

### CUM-CLM-003/v1

**Disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed text:** Across the three governed P02 datasets, decoder-family ordering is context-dependent rather than universally ordered, and participant heterogeneity on the multi-participant datasets limits any global winner claim; BNCI2014_001 is descriptive at the participant-inference level because its held-out P02 test set contains one participant.

**Cumulative findings:** `CF-03`, `CF-11`

**Contributing phase evidence:** resolved through `cumulative_findings.yaml`, `results_to_claims.yaml`, and the phase-local finding/evidence nodes.

**Limitations:** BNCI held-out test participant n=1; no universal rank claim.

### CUM-CLM-004/v1

**Disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed text:** The deterministic low-label populations prepared in P01 expose difficult, non-monotonic and rank-changing P02 behavior across the governed 1-32 labels/class surface; one frozen subset per budget prevents a stable repeated-subset sample-efficiency claim.

**Cumulative findings:** `CF-04`

**Contributing phase evidence:** resolved through `cumulative_findings.yaml`, `results_to_claims.yaml`, and the phase-local finding/evidence nodes.

**Limitations:** Single frozen subset per budget; no repeated-subset stability.

### CUM-CLM-005/v1

**Disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed text:** P01 resolved A4 data-feasibility by freezing a fully matched R2 substrate. Under P02’s accepted constrained A4 execution, no generic C1-C3 statistically detected improvement was observed, and post-hoc Stage18S further shows repeat/budget sign sensitivity. These results do not establish zero effect, five-repeat stability, dense-budget behavior, or full original-grid equivalence.

**Cumulative findings:** `CF-05`, `CF-06`

**Contributing phase evidence:** resolved through `cumulative_findings.yaml`, `results_to_claims.yaml`, and the phase-local finding/evidence nodes.

**Limitations:** Single canonical refit repeat, deep anchor budgets, Stage18S post-hoc.

### CUM-CLM-006/v1

**Disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed text:** The P02 correction history shows that apparent model viability under the implemented configurations depended on training-policy choice while the inherited P00/P01 data and identity foundations remained unchanged; this supports a reproduction/optimization-sensitivity interpretation, not universal architecture superiority or guaranteed gains from source-aligned settings.

**Cumulative findings:** `CF-07`

**Contributing phase evidence:** resolved through `cumulative_findings.yaml`, `results_to_claims.yaml`, and the phase-local finding/evidence nodes.

**Limitations:** Diagnostic/validation evidence does not establish universal test-set gains or architecture superiority.

### CUM-CLM-007/v1

**Disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed text:** Across P00-P02, fail-closed validation and explicit retention of failures, supersessions, null/negative results and diagnostic states provide an auditable project history in which non-success evidence remains available for interpretation; this process does not guarantee scientific correctness or deployment safety.

**Cumulative findings:** `CF-08`, `CF-09`

**Contributing phase evidence:** resolved through `cumulative_findings.yaml`, `results_to_claims.yaml`, and the phase-local finding/evidence nodes.

**Limitations:** Different negative-evidence classes are not quantitatively interchangeable.

### CUM-CLM-008/v1

**Disposition:** `APPROVED_WITH_QUALIFICATIONS`

**Reviewed text:** At the end of P02, canonical Layer-2 evidence is technically ready for governed downstream consumption, including P03, while explicit scope, repeat/stability, access and non-clinical limitations remain mandatory handoff constraints; this does not imply future-phase scientific success.

**Cumulative findings:** `CF-12`

**Contributing phase evidence:** resolved through `cumulative_findings.yaml`, `results_to_claims.yaml`, and the phase-local finding/evidence nodes.

**Limitations:** Downstream science is not yet executed.

## 6. Negative and superseded evidence

- P01 A4 effectiveness claim `P01-CLM-011/v1` remains historically DEFERRED and is linked to later P02 A4 evidence rather than rewritten.
- P02 retains 648 FailureCaseIndex records, 340 NegativeResultNotes and 309 DiagnosticOnlyFlags as distinct evidence classes.
- Stage11 diagnostic challenger remains diagnostic-only.
- Stage18S remains post-hoc descriptive sensitivity evidence.
- Failed, dependency-blocked, incompatible, skipped and not-applicable cells remain visible and mapped.

## 7. External artifact provenance

P01 numerical arrays remain governed by their Kaggle pointer identities. P02 uses a separate Hugging Face credential class. The preferred P02 continuation source is the immutable full-workspace snapshot; the chunked release is archival/fallback. Mutable `latest` retrieval is prohibited.

**Credential classes:** `IHARQ_HF_TOKEN_PRE_P02` and `IHARQ_HF_TOKEN_P02`. Literal values are never stored.

### Preferred P02 continuation source

- repository: `Csthv/p02-phase02-final-whole-working-20260814t052120z-b890ff92`
- immutable revision: `bc14961e14f2e48690e55df3577014275f9cbf30`
- manifest: `__IHARQ_SNAPSHOT__/WORKING_TREE_MANIFEST.jsonl`
- manifest SHA-256: `564bbb44e67d14da8457ad83d33651ded93dfc6b89ab90f10f78a36a20b8e8f5`
- per-object integrity index SHA-256: `540a0c3d4cbc686645ab1fccf088205c02c32a5c34e4b238c91f9c4ec119c12f`

### Archival P02 source

- repository: `Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260814t051352z`
- immutable final release revision: `257a407b5c7ea37b6c620863ee261c010c8f197c`
- content revision: `bc88dccd6518aa7b172697be1ef98344997f27ff`
- manifest revision: `c60c0505faa8076090439277ed1d8ef8c86734b7`

## 8. Literature evidence boundary

Literature is represented with explicit roles such as `EXTERNAL_METHOD_REFERENCE` and `EXTERNAL_CONTEXTUAL_COMPARISON`. It may contextualize EEGNet, FBCNet, DBConformer, CBraMod, the public datasets and BCI reproducibility, but it cannot prove an IHARQ measured result. Bibliographic metadata was freshly verified on 2026-08-14.

## 9. Figure/table two-way provenance

Every current Layer 10 figure/table is registered in `figure_table_provenance.yaml` with claim IDs, finding IDs, source data, output path, checksum and limitations. No Layer 10 artifact is allowed to create a new scientific population, metric, denominator or claim.

## 10. Orphan tests

- Reviewed claims without findings/evidence: **0 material orphans**.
- P02 material evidence without finding/limitation/negative/support role: **0 material orphans**.
- Broken P02 external revision/hash references: **0 identified**.
- Claim-bearing Layer 10 artifacts without Evidence Map support: **0**.

**EVIDENCE_MAP_THROUGH_P02_STATUS = FINALIZED**
