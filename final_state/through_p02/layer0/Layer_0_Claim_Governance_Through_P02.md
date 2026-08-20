---
title: "IHARQ Layer 0 Claim Governance Through P02"
layer0_id: "IHARQ-CUMULATIVE-LAYER0-THROUGH-P02-R1"
release_id: "P00-P02-LAYER0-RELEASE-R1"
generated_at: "2026-08-14T21:30:00+03:30"
status: "FINALIZED"
---

# IHARQ Layer 0 Claim Governance Through P02

> **Authority boundary.** Layer 0 governs claim wording, scope, qualification and prohibition. It does not change measurements, counts, metrics, run inclusion, source evidence, Protocol records or the finalized Phase Analysis.

## Executive governance decision

The current Layer 0 state contains **37 reviewed claims**: **2 APPROVED**, **33 APPROVED_WITH_QUALIFICATIONS**, **1 DEFERRED**, and **1 REJECTED**. The 19 P00/P01 reviewed claims are preserved historically; 10 P02 candidate claims and 8 cumulative P00-P02 claims are newly reviewed under the same taxonomy.

P02 does not erase earlier decisions. In particular, `P01-CLM-011/v1` remains historically **DEFERRED** because P01 did not test A4 effectiveness. P02 later supplies governed evidence that does not support a generic C1-C3 improvement under the executed constrained scope; the current resolution is carried by `P02-CLM-007/v1` and `CUM-CLM-005/v1`, not by retroactive rewriting of the P01 disposition.

## Governance invariants

- P00/P01 historical claim IDs, reviewed wording and dispositions remain preserved.
- All 10 P02 candidate claims are dispositioned.
- All 8 cumulative candidate claims are dispositioned.
- Stage18S remains post-hoc/descriptive/sensitivity evidence.
- A4 resource restrictions remain mandatory claim ceilings.
- Diagnostic Stage11 evidence does not replace primary A0.
- Technical readiness is not deployment or clinical readiness.
- Negative/null evidence is governed with the same scope discipline as positive evidence.

## P02 reviewed claims

### P02-CLM-001/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-001`

**Reviewed wording:** Under the frozen P01 subject-grouped binary motor-imagery protocol, P02 established a complete multi-family raw accept-all decoder/baseline measurement spine across the three activated public EEG datasets; this is Layer-2 measurement evidence and does not establish calibration, abstention, clinical effectiveness, safety, or deployment readiness.

**Evidence class:** `LAYER2_MEASUREMENT_CLOSURE`

**Claim ceiling:** `SUPPORTED`

**Supporting findings:** `P02-FIND-001`

**Numeric support:** `{"A0_terminal_cells": 678, "SUCCESS": 657, "FAILED": 3, "CONDITIONAL_SKIP": 15, "DEPENDENCY_BLOCKED": 3, "datasets": 3}`

**Mandatory qualification:** Raw accept-all decoder evidence only; not clinical or safety evidence.

**Prohibited stronger wording:** Do not call P02 calibration-, threshold-, abstention-, safety-, or deployment-ready.

**Post-hoc/diagnostic status:** `NO`

### P02-CLM-002/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-002`

**Reviewed wording:** Within full-training A0, descriptive decoder ordering was dataset-dependent: CSP-LDA led the single-participant BNCI2014_001 test split, while DBConformer had the highest participant-first mean BACC on Lee2019_MI and PhysioNetMI. These rankings are descriptive and do not establish a universal winning decoder.

**Evidence class:** `DESCRIPTIVE_MODEL_HETEROGENEITY`

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Supporting findings:** `P02-FIND-002`, `P02-FIND-003`

**Numeric support:** `{"full_training_descriptive_leaders": {"BNCI2014_001": {"branch_id": "CLS-CSP-LDA", "participant_first_mean_BACC": 0.6388888888888888, "participants": 1}, "Lee2019_MI": {"branch_id": "DNN-SEQ", "participant_first_mean_BACC": 0.795, "participants": 6}, "PhysioNetMI": {"branch_id": "DNN-SEQ", "participant_first_mean_BACC": 0.649724517906336, "participants": 11}}}`

**Mandatory qualification:** Descriptive rankings; no universal winner; BNCI inferential n=1.

**Prohibited stronger wording:** Do not claim one decoder is universally best across datasets or participants.

**Post-hoc/diagnostic status:** `NO`

### P02-CLM-003/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-003`

**Reviewed wording:** On PhysioNetMI full-training A0, the governed Friedman comparison detected overall decoder heterogeneity (statistic 20.544, p=0.00451, Kendall W=0.267), while no individual alternative-versus-CSP-LDA contrast survived Holm correction; the omnibus result therefore does not identify a statistically supported pairwise winner.

**Evidence class:** `GOVERNED_STATISTICAL_RESULT`

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Supporting findings:** `P02-FIND-003`

**Numeric support:** `{"PhysioNetMI_Friedman_statistic": 20.544, "p_value": 0.00451, "Kendall_W": 0.267, "Lee2019_MI_Friedman_p": 0.148, "Holm_significant_alt_vs_CSP_LDA": 0}`

**Mandatory qualification:** Global omnibus heterogeneity is not evidence that a specific decoder is superior.

**Prohibited stronger wording:** Do not convert omnibus heterogeneity into a significant pairwise winner claim.

**Post-hoc/diagnostic status:** `NO`

### P02-CLM-004/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-004`

**Reviewed wording:** Across the governed 1, 2, 4, 8, 16 and 32 labels/class P02 low-label surface, performance was difficult, non-monotonic and rank-changing under one frozen subset per budget; the evidence does not support a stable or universal sample-efficiency ordering among the evaluated branches.

**Evidence class:** `DESCRIPTIVE_LOW_LABEL`

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Supporting findings:** `P02-FIND-005`

**Numeric support:** `{"governed_low_label_budgets_per_class": [1, 2, 4, 8, 16, 32], "leader_changes": {"BNCI2014_001": 4, "Lee2019_MI": 4, "PhysioNetMI": 6}, "design": "single frozen subset per budget"}`

**Mandatory qualification:** One frozen subset per budget; descriptive only.

**Prohibited stronger wording:** Do not claim stable sample-efficiency ordering or subset-robust low-label behavior.

**Post-hoc/diagnostic status:** `NO`

### P02-CLM-005/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-005`

**Reviewed wording:** The preserved P02 training-correction history shows that model viability and optimization behavior under the implemented configurations depended materially on training-policy choice. This supports treating inadequate optimization as distinct from demonstrated architectural incapacity, but does not establish universal test-set gains, architecture superiority, or theoretical invalidity of the earlier generic policy.

**Evidence class:** `METHODOLOGICAL_CORRECTION`

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Supporting findings:** `P02-FIND-006`, `P02-FIND-008`

**Numeric support:** `{"Stage12_validation_only_examples": [{"dataset_id": "BNCI2014_001", "branch_id": "DNN-FBCNET", "A_BACC": 0.5, "B_BACC": 0.7222222222222222, "absolute_delta_BACC": 0.2222222222222222, "claim_bearing": false}, {"dataset_id": "PhysioNetMI", "branch_id": "DNN-FBCNET", "A_BACC": 0.6395092565383486, "B_BACC": 0.6601038299539622, "absolute_delta_BACC": 0.0205945734156136, "claim_bearing": false}, {"dataset_id": "PhysioNetMI", "branch_id": "DNN-SEQ", "A_BACC": 0.6985502987559996, "B_BACC": 0.7167940052894505, "absolute_delta_BACC": 0.0182437065334508, "claim_bearing": false}, {"dataset_id": "PhysioNetMI", "branch_id": "SSL-CBRAMOD", "A_BACC": 0.5, "B_BACC": 0.6384072876873348, "absolute_delta_BACC": 0.1384072876873348, "claim_bearing": false}], "test_role_loaded": false}`

**Mandatory qualification:** Mechanistic interpretation; source diagnostics are not a direct claim of test-set performance improvement for every model.

**Prohibited stronger wording:** Do not claim architecture superiority or theoretical invalidity of the original uniform policy.

**Post-hoc/diagnostic status:** `NO`

### P02-CLM-006/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-006`

**Reviewed wording:** The Stage-11 S&R diagnostic challenger did not yield a consistent participant-level BACC improvement over the canonical primary EEGNet across BNCI2014_001, Lee2019_MI and PhysioNetMI; it remains diagnostic-only and does not replace primary A0 evidence.

**Evidence class:** `DIAGNOSTIC_NEGATIVE_RESULT`

**Claim ceiling:** `SUPPORTED`

**Supporting findings:** `P02-FIND-007`

**Numeric support:** `{"diagnostic_challenger": [{"dataset_id": "BNCI2014_001", "n": 5, "median_delta_BACC": -0.0347222222222222, "ci_low": -0.0763888888888889, "ci_high": -0.0347222222222221, "p_value": 0.125, "rank_biserial": -0.8666666666666667}, {"dataset_id": "Lee2019_MI", "n": 30, "median_delta_BACC": 0.01, "ci_low": -0.005, "ci_high": 0.025, "p_value": 0.2309220325143355, "rank_biserial": 0.2586206896551724}, {"dataset_id": "PhysioNetMI", "n": 55, "median_delta_BACC": 0.0, "ci_low": -0.0343477914915631, "ci_high": 0.0029761904761905, "p_value": 0.455185419014922, "rank_biserial": -0.1190130624092888}]}`

**Mandatory qualification:** Not an A-number and not a replacement for primary A0.

**Prohibited stronger wording:** Do not claim the Stage11 challenger improved EEGNet generally.

**Post-hoc/diagnostic status:** `DIAGNOSTIC_ONLY`

### P02-CLM-007/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-007`

**Reviewed wording:** Within the canonical resource-constrained A4 scope, none of the 756 governed C1-C3 role-control statistical rows reached raw p<=0.05. This is an absence of statistically detected improvement under the executed scope, not proof that the true effect is zero and not evidence of five-repeat or dense-budget stability.

**Evidence class:** `GOVERNED_ABLATION_NEGATIVE_NULL_RESULT`

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Supporting findings:** `P02-FIND-009`, `P02-FIND-010`

**Numeric support:** `{"governed_C1_C3_statistical_rows": 756, "raw_p_le_0_05": 0, "scope": "single canonical refit repeat / governed deep anchor budgets"}`

**Mandatory qualification:** Absence of detected effects is not proof of zero effect; canonical deep scope is reduced.

**Prohibited stronger wording:** Do not claim zero A4 effect, five-repeat stability, dense deep-budget characterization, or full-grid equivalence.

**Post-hoc/diagnostic status:** `NO`

### P02-CLM-008/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-008`

**Reviewed wording:** A hard-vote ensemble was not uniformly beneficial: one governed PhysioNetMI full-training C4 comparison at repeat 4 showed a Holm-significant disadvantage relative to the validation-selected EEGNet constituent (median delta BACC -0.0435; Holm p=0.0371). This cell-specific negative result does not establish that ensembles are generally inferior.

**Evidence class:** `CELL_SPECIFIC_NEGATIVE_ABLATION_RESULT`

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Supporting findings:** `P02-FIND-011`

**Numeric support:** `{"Holm_significant_rows": 1, "significant_rows": [{"comparison_id": "P02-A4-PhysioNetMI-ENSEMBLE-A4-C4-MODEL-HARD-VOTE-FULL_TRAIN-ER04:VS_STRONGEST", "dataset_id": "PhysioNetMI", "condition_id": "A4-C4-MODEL-HARD-VOTE", "budget_id": "FULL_TRAIN", "repeat": 4, "strongest_constituent_branch": "DNN-EEGNET", "closure_status": "COMPLETE", "n": 11.0, "median_delta_BACC": -0.0434782608695651, "p_value": 0.0185546875, "holm_adjusted_p": 0.037109375, "rank_biserial": -0.7878787878787878, "ci_low": -0.1304347826086956, "ci_high": -0.0119047619047618}]}`

**Mandatory qualification:** Do not generalize from one corrected comparison to all ensembles.

**Prohibited stronger wording:** Do not claim ensembles are generally inferior; one corrected comparison was negative.

**Post-hoc/diagnostic status:** `NO`

### P02-CLM-009/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-009`

**Reviewed wording:** Post-hoc Stage18S sensitivity evidence shows that A4 effect direction can change across descriptive repeats and budgets (22/45 anchor trajectories mixed-sign; all 15 six-budget MR00 trajectories changed sign at least once). This supports the existing claim ceiling but remains POST_HOC/DESCRIPTIVE/SENSITIVITY evidence and does not modify canonical Stage18/G18.

**Evidence class:** `POST_HOC_SENSITIVITY`

**Claim ceiling:** `POST_HOC_ONLY`

**Supporting findings:** `P02-FIND-012`

**Numeric support:** `{"three_repeat_anchor_trajectories": 45, "all_negative": 7, "mixed": 22, "all_positive": 16, "six_budget_trajectories": 15, "six_budget_with_sign_flip": 15}`

**Mandatory qualification:** Descriptive/post-hoc only; does not modify canonical G18.

**Prohibited stronger wording:** Do not present Stage18S as confirmatory or as modifying G18.

**Post-hoc/diagnostic status:** `POST_HOC_DESCRIPTIVE_SENSITIVITY`

### P02-CLM-010/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `P02-CLAIM-CAND-010`

**Reviewed wording:** P02 provides a fail-closed, provenance-rich Layer-2 evidence substrate for downstream use while preserving successful and non-success outcomes, including 648 FailureCaseIndex records, 340 NegativeResultNotes and 309 DiagnosticOnlyFlags. This is technical evidence readiness, not deployment readiness or future-phase scientific success.

**Evidence class:** `REPRODUCIBILITY_NEGATIVE_EVIDENCE`

**Claim ceiling:** `SUPPORTED`

**Supporting findings:** `P02-FIND-013`, `P02-FIND-014`

**Numeric support:** `{"FailureCaseIndex": 648, "NegativeResultNote": 340, "DiagnosticOnlyFlag": 309, "failure_terminal_breakdown": {"CONDITIONAL_SKIP": 591, "NOT_APPLICABLE_REPEAT_SLOT": 42, "INPUT_INCOMPATIBLE": 9, "FAILED": 3, "DEPENDENCY_BLOCKED": 3}}`

**Mandatory qualification:** Technical readiness is not deployment readiness.

**Prohibited stronger wording:** Do not equate technical evidence readiness with deployment readiness.

**Post-hoc/diagnostic status:** `NO`

## Cumulative P00-P02 reviewed claims

### CUM-CLM-001/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `CC-01`

**Reviewed wording:** Through P02, IHARQ has a governed evidence chain linking validated foundation contracts, the frozen P01 provenance-traceable EEG substrate, and P02 Layer-2 decoder evidence through explicit identities, manifests and handoffs; this traceability does not by itself establish clinical or deployment effectiveness.

**Supporting cumulative findings:** `CF-01`, `CF-02`, `CF-09`

**Supporting phases:** P00, P01, P02

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Mandatory qualification:** Technical traceability is not scientific/clinical effectiveness by itself.

**Prohibited stronger wording:** Do not state that the complete project is deployment-ready or clinically validated.

### CUM-CLM-002/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `CC-02`

**Reviewed wording:** The P02 decoder analyses consume the frozen P01 subject-grouped, denominator-conserving binary motor-imagery data contract rather than a P02-local redefinition of labels, split or core windows, subject to the scope of the implemented registered integrity and leakage checks.

**Supporting cumulative findings:** `CF-02`

**Supporting phases:** P01, P02

**Claim ceiling:** `SUPPORTED`

**Mandatory qualification:** Bounded to the implemented registered leakage/disjointness checks.

**Prohibited stronger wording:** Do not claim that every conceivable leakage mechanism is impossible.

### CUM-CLM-003/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `CC-03`

**Reviewed wording:** Across the three governed P02 datasets, decoder-family ordering is context-dependent rather than universally ordered, and participant heterogeneity on the multi-participant datasets limits any global winner claim; BNCI2014_001 is descriptive at the participant-inference level because its held-out P02 test set contains one participant.

**Supporting cumulative findings:** `CF-03`, `CF-11`

**Supporting phases:** P01, P02

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Mandatory qualification:** BNCI held-out test participant n=1; no universal rank claim.

**Prohibited stronger wording:** Do not claim DBConformer, CSP-LDA or any other decoder is universally best.

### CUM-CLM-004/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `CC-04`

**Reviewed wording:** The deterministic low-label populations prepared in P01 expose difficult, non-monotonic and rank-changing P02 behavior across the governed 1-32 labels/class surface; one frozen subset per budget prevents a stable repeated-subset sample-efficiency claim.

**Supporting cumulative findings:** `CF-04`

**Supporting phases:** P01, P02

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Mandatory qualification:** Single frozen subset per budget; no repeated-subset stability.

**Prohibited stronger wording:** Do not claim stable low-label resilience or universal sample-efficiency superiority.

### CUM-CLM-005/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `CC-05`

**Reviewed wording:** P01 resolved A4 data-feasibility by freezing a fully matched R2 substrate. Under P02’s accepted constrained A4 execution, no generic C1-C3 statistically detected improvement was observed, and post-hoc Stage18S further shows repeat/budget sign sensitivity. These results do not establish zero effect, five-repeat stability, dense-budget behavior, or full original-grid equivalence.

**Supporting cumulative findings:** `CF-05`, `CF-06`

**Supporting phases:** P01, P02

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Mandatory qualification:** Single canonical refit repeat, deep anchor budgets, Stage18S post-hoc.

**Prohibited stronger wording:** Do not claim A4 has zero effect, is five-repeat stable, or is fully equivalent to the originally planned dense grid.

### CUM-CLM-006/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `CC-06`

**Reviewed wording:** The P02 correction history shows that apparent model viability under the implemented configurations depended on training-policy choice while the inherited P00/P01 data and identity foundations remained unchanged; this supports a reproduction/optimization-sensitivity interpretation, not universal architecture superiority or guaranteed gains from source-aligned settings.

**Supporting cumulative findings:** `CF-07`

**Supporting phases:** P00, P01, P02

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Mandatory qualification:** Diagnostic/validation evidence does not establish universal test-set gains or architecture superiority.

**Prohibited stronger wording:** Do not claim the original uniform policy was theoretically invalid or that source-aligned settings universally improve every model.

### CUM-CLM-007/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `CC-07`

**Reviewed wording:** Across P00-P02, fail-closed validation and explicit retention of failures, supersessions, null/negative results and diagnostic states provide an auditable project history in which non-success evidence remains available for interpretation; this process does not guarantee scientific correctness or deployment safety.

**Supporting cumulative findings:** `CF-08`, `CF-09`

**Supporting phases:** P00, P01, P02

**Claim ceiling:** `SUPPORTED_WITH_QUALIFICATION`

**Mandatory qualification:** Different negative-evidence classes are not quantitatively interchangeable.

**Prohibited stronger wording:** Do not claim that fail-closed process guarantees scientific correctness or deployment safety.

### CUM-CLM-008/v1 - APPROVED_WITH_QUALIFICATIONS

**Source candidate:** `CC-08`

**Reviewed wording:** At the end of P02, canonical Layer-2 evidence is technically ready for governed downstream consumption, including P03, while explicit scope, repeat/stability, access and non-clinical limitations remain mandatory handoff constraints; this does not imply future-phase scientific success.

**Supporting cumulative findings:** `CF-12`

**Supporting phases:** P01, P02

**Claim ceiling:** `SUPPORTED`

**Mandatory qualification:** Downstream science is not yet executed.

**Prohibited stronger wording:** Do not equate technical handoff readiness with future scientific success.

## Historical P00/P01 preservation and P02 effect

- `P00-CLM-001/v2` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_QUALIFIED_CURRENT`.
- `P00-CLM-002/v2` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_QUALIFIED_CURRENT`.
- `P00-CLM-003/v2` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_QUALIFIED_CURRENT`.
- `P00-CLM-004/v2` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_QUALIFIED_CURRENT`.
- `P00-CLM-005/v2` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_QUALIFIED_CURRENT`.
- `P00-CLM-006/v2` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_QUALIFIED_CURRENT`.
- `P00-CLM-007/v2` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_QUALIFIED_CURRENT`.
- `P01-CLM-001/v1` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_HISTORICAL`.
- `P01-CLM-002/v1` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_HISTORICAL`.
- `P01-CLM-003/v1` - historical disposition `APPROVED` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_HISTORICAL`.
- `P01-CLM-004/v1` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_HISTORICAL`.
- `P01-CLM-005/v1` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_HISTORICAL`.
- `P01-CLM-006/v1` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `STRENGTHENING_EVIDENCE`; current state `ACTIVE_QUALIFIED_WITH_P02_REALIZED_DOWNSTREAM_USE`.
- `P01-CLM-007/v1` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `STRENGTHENING_EVIDENCE`; current state `ACTIVE_QUALIFIED_WITH_P02_REALIZED_DOWNSTREAM_USE`.
- `P01-CLM-008/v1` - historical disposition `APPROVED` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_HISTORICAL`.
- `P01-CLM-009/v1` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `NO_CHANGE`; current state `ACTIVE_HISTORICAL`.
- `P01-CLM-010/v1` - historical disposition `APPROVED_WITH_QUALIFICATIONS` preserved; P02 effect `STRENGTHENING_EVIDENCE`; current state `ACTIVE_QUALIFIED_WITH_P02_REALIZED_DOWNSTREAM_USE`.
- `P01-CLM-011/v1` - historical disposition `DEFERRED` preserved; P02 effect `SUPERSESSION`; current state `HISTORICAL_DEFERRED_CLAIM_RESOLVED_BY_P02_GENERIC_IMPROVEMENT_NOT_SUPPORTED_UNDER_EXECUTED_SCOPE`.
- `P01-CLM-012/v1` - historical disposition `REJECTED` preserved; P02 effect `STRENGTHENING_EVIDENCE`; current state `REJECTED_SCOPE_BOUNDARY_REMAINS_ACTIVE_THROUGH_P02`.

## Layer 0 closure gate

- Every material P02 candidate claim reviewed: **PASS**.
- Every cumulative candidate claim reviewed: **PASS**.
- Major limitations mapped: **PASS**.
- Stage18S post-hoc boundary encoded: **PASS**.
- A4 resource claim ceiling encoded: **PASS**.
- Prohibited stronger wording registered: **PASS**.
- Measurements/Protocol/execution changed by Layer 0: **NO**.

**LAYER0_THROUGH_P02_STATUS = FINALIZED**
