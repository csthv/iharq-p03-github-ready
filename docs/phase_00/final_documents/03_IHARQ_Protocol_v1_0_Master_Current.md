<!--
SYNCHRONIZED_DISTRIBUTION_SNAPSHOT
canonical_source_path: docs/authorities/protocol_v1_0/master/IHARQ_Protocol_v1_0_Master_R2.md
source_sha256: 938fcaab2be30d2e59ccc5082a9c3cc6c2ccc3e8889b352099aa514b96e046d4
authority_status: AUTHORITATIVE_CURRENT_SOURCE
supersession_status: CURRENT
body_after_this_comment_matches_canonical_source: true
-->

---
title: "IHARQ BenchGuard Stretch C — Protocol v1.0 Master Authority"
document_id: "IHARQ-PROTOCOL-V1-MASTER-R2"
version: "1.0-R2"
status: "FROZEN_WITH_NONBLOCKING_LIMITATIONS"
review_mode: "LLM_ONLY_MULTI_PASS_FAIL_CLOSED"
publication_strategy: "LOCAL_FIRST_SINGLE_PUBLICATION"
protocol_freeze_sha256: "881d7f705bfdacc0c00b4fb547a35e9b8dad60114314ca13f4fec115c3cb9d82"
---

# IHARQ BenchGuard Stretch C
# Experiment, Ablation, and Evaluation Protocol v1.0 — Project-Wide Master Authority

## Document control

| Field | Frozen value |
| --- | --- |
| project_id | IHARQ-BENCHGUARD-STRETCH-C |
| protocol_id | IHARQ-PROTOCOL-V1-MASTER-R2 |
| protocol_version | 1.0-R2 |
| document_scope | PROJECT_WIDE_MASTER |
| effective_date | 2026-08-03 |
| registration_timestamp | 2026-08-03T15:07:37+03:30 |
| registration_or_archive_uri | LOCAL_PACKAGE_SNAPSHOT |
| registration_snapshot_hash | 881d7f705bfdacc0c00b4fb547a35e9b8dad60114314ca13f4fec115c3cb9d82 |
| identity_mode | LOCAL_PACKAGE_SNAPSHOT |
| source_snapshot_id | P00-LOCAL-FIRST-FINALIZATION-HANDOFF-R1 |
| source_snapshot_sha256 | bcbf5c70e4b0ca09caa73c3f0963d8cc1bc0adbc0741fad60ef6cd936ca66c95 |
| repository_commit | NOT_APPLICABLE_LOCAL_FIRST |
| publication_strategy | LOCAL_FIRST_SINGLE_PUBLICATION |
| github_ci_required | false |
| current_status | FROZEN_WITH_NONBLOCKING_LIMITATIONS |
| authority_manifest_id | IHARQ-PV1-INDEPENDENT-SOURCE-INTAKE-R2 |
| build_book_version | IHARQ-IBB-R3-P00-LOCAL-FIRST-ANNEX-R5 |
| registry_version | R44 |
| review_mode | LLM_ONLY_MULTI_PASS_FAIL_CLOSED |
| human_review_used | false |
| unresolved_llm_dissent | NONE |

## Independent final-audit successor control

This R2 successor was issued after an independent requirement-level and adversarial audit of the complete local R1 Protocol package. R1 is preserved as immutable historical evidence. R2 corrects source-exhaustion coverage, review-mode drift, project-state gate drift, missing independent-audit ledgers, and unproven future-annex extensibility evidence. GitHub is explicitly excluded as a current source of truth because the repository has not yet received the local final package.

- predecessor package SHA-256: `a262975819fa3af912e4ee96c61d6b4df2ef2e713e64f53546f8dfeace879400`
- controlling implementation snapshot SHA-256: `bcbf5c70e4b0ca09caa73c3f0963d8cc1bc0adbc0741fad60ef6cd936ca66c95`
- independent audit prompt: `IHARQ-P00-PROTOCOL-V1-FINAL-INDEPENDENT-AUDIT-R1`
- audit review mode: `LLM_ONLY_MULTI_PASS_FAIL_CLOSED`
- current publication strategy: `LOCAL_FIRST_SINGLE_PUBLICATION`
- GitHub current-authority status: `NOT_USED_NOT_CURRENT`

## 1. Purpose and authority

This master freezes project-wide Protocol identities, timing and evidence-status rules, amendment and deviation governance, global run-cell and comparison requirements, A0–A13 semantics, evidence-product interfaces, and the inheritance contract for phase annexes. It does not redesign the architecture, select methods for the first time, invent canonical records, implement code, report observed results, approve claims, or authorize Layer 10 recomputation.

The master and its phase annexes are binding only when their human-readable and machine-readable identities agree, deterministic validation passes, source snapshot hashes resolve, and the five role-separated LLM reviews record no unresolved material objection.

## 2. Scope-partitioned authority and conflict resolution

| Authority | Owned surface | Protocol boundary |
| --- | --- | --- |
| Governance V4 | timing modes, master/annex structure, closure order | may not be overridden by phase annex convenience |
| Architecture | P00-P15, L0-L10, A0-A13 and boundaries | may not be renamed by configs or reports |
| Registry R44 | canonical records, fields, aliases, lifecycle/status vocabularies | Protocol references but does not invent |
| Execution and Evidence Plan R41 | phase products, gates, evidence roles and exit criteria | Protocol makes requirements exact |
| Protocol v0.1/R42 | A0-A13 fairness, matching, leakage, denominators, negatives, no A14 | v1.0 populates reserved exact profiles |
| Phase Playbook R41 | entry/run/repair/handoff order | Protocol does not reorder phases silently |
| Method Selection R2 | accepted methods and decisions | Protocol does not select methods post hoc |
| Nuts-and-Bolts R2 | algorithms, validators, failure behavior | Protocol freezes versions/profiles, not code internals |
| Build Book R3/R5 | paths, packages, commands, environments, tests | Protocol references executable realization |

Conflicts are classified by affected surface, routed to the owning authority, recorded with affected descendants and migration consequences, and resolved before dependent Protocol fields are frozen. Averaging or silently merging incompatible wording is prohibited. The Phase identity drift discovered in implementation configs was resolved through `PV1-PHASE-IDENTITY-MIGRATION-R1`, owned by Architecture.

## 3. Master-plus-annex inheritance

The project has one master Protocol authority and one independently frozen annex per phase. The master owns global identities and rules. A phase annex owns exact phase questions, run cells, input/output identities, configurations, timing mode, execution budgets, analysis contract, evidence class and handoff fields. A future annex may use `PHASE_ANNEX_OWNED`, `TO_BE_REGISTERED_IN_PXX`, or `NOT_APPLICABLE_TO_MASTER`; uncontrolled placeholders are prohibited in the frozen master.

P01–P15 may be created without rewriting this master. A change to a global identity or rule requires a master successor and an explicit impact review for every annex.

## 4. Review and publication governance

Review is LLM-only and fail-closed. Deterministic evidence outranks LLM consensus. The accepted publication strategy is `LOCAL_FIRST_SINGLE_PUBLICATION`; local package/snapshot identities and SHA-256 values are authoritative at this stage. GitHub CI, commits, PRs, tags and releases are not required and were not attempted.

## 5. Timing modes and evidence ceilings

- **Mode A:** Protocol frozen before a claim-bearing run. Maximum evidence class may be confirmatory when all gates pass.
- **Mode B:** Operational run precedes final annex. Observed results remain engineering, exploratory or retrospective; later freezing cannot upgrade them.
- **Mode C:** Scientific choices are frozen before execution and only predeclared administrative metadata is completed afterward; no-result-contingent-change evidence is mandatory.

Every annex declares its mode and evidence consequence separately. P00 is Mode B for the historical conformance evidence because material engineering rules were repaired after observed failures.

## 6. Freeze surfaces

- `FS-ID`: phase, ablation, source, dataset/split/artifact and authority identities.
- `FS-SCI`: scientific questions, comparisons, eligibility, matching, estimands, exclusions and analysis rules.
- `FS-EXEC`: source snapshot/commit, environment, configs, seeds, budgets, simulator/stress/reward profiles.
- `FS-ANALYSIS`: analysis implementation, metric dictionaries, estimators, tables/figures and failure views.
- `FS-RELEASE`: accepted/invalid inventories, attrition release, source bundles, claim/evidence and Layer 10 handoffs.

A change to any frozen surface creates a successor or amendment and triggers topological invalidation of affected descendants.

## 7. Status axes

Document maturity, evidence class, record lifecycle, run validity and claim disposition remain separate. Document maturity never upgrades evidence class. Claim approval is owned by Layer 0 after the Phase Evidence Report. Template-local aliases map one-to-one to accepted Registry values and may not replace them silently.

## 8. Official phase register

| Phase | Official name | Master role | Status |
| --- | --- | --- | --- |
| P00 | Repository, Configuration, and Record Schema | Global identity only; exact values annex-owned | Created |
| P01 | Public Data and Split Protocol | Global identity only; exact values annex-owned | Master ready |
| P02 | Baseline Decoders | Global identity only; exact values annex-owned | Master ready |
| P03 | Calibration and Uncertainty | Global identity only; exact values annex-owned | Master ready |
| P04 | IHARQ-lite Evidence Verification | Global identity only; exact values annex-owned | Master ready |
| P05 | RegimeRisk Temporal Trust | Global identity only; exact values annex-owned | Master ready |
| P06 | Evidence-Quality Estimator and Supervised Adaptive-IHARQ | Global identity only; exact values annex-owned | Master ready |
| P07 | Learning-to-Defer | Global identity only; exact values annex-owned | Master ready |
| P08 | Simulated Closed-Loop Readiness | Global identity only; exact values annex-owned | Master ready |
| P09 | StressForge-Lite | Global identity only; exact values annex-owned | Master ready |
| P10 | Contextual Bandit | Global identity only; exact values annex-owned | Master ready |
| P11 | Reinforcement-Learning Policy | Global identity only; exact values annex-owned | Master ready |
| P12 | MyoSuite Embodiment Demo | Global identity only; exact values annex-owned | Master ready |
| P13 | OpenSim Replay or Optional Comparison | Global identity only; exact values annex-owned | Master ready |
| P14 | Dashboard and Cards | Global identity only; exact values annex-owned | Master ready |
| P15 | Final Thesis Integration | Global identity only; exact values annex-owned | Master ready |

## 9. Official layer register

| Layer | Owned surface | Protocol rule |
| --- | --- | --- |
| L0 | Claim safety, evidence sufficiency, wording, downgrade, limitations, lifecycle | Owner preserved; Protocol freezes applicable exact references |
| L1 | Data, labels, splits, windows, preprocessing, manifests | Owner preserved; Protocol freezes applicable exact references |
| L2 | Decoder families, controls, predictions, model identity | Owner preserved; Protocol freezes applicable exact references |
| L3 | Calibration, uncertainty, selective prediction, registered operating points | Owner preserved; Protocol freezes applicable exact references |
| L4 | IHARQ evidence verification, reasons, combination, fallback, unsafe states | Owner preserved; Protocol freezes applicable exact references |
| L5 | Temporal features, trust, regime logic, stop-loss | Owner preserved; Protocol freezes applicable exact references |
| L6 | Evidence quality, policy, deferral, costs, supervised/adaptive readiness | Owner preserved; Protocol freezes applicable exact references |
| L7 | State, action, transition, reward, cost, session, rollout, simulator diagnostics | Owner preserved; Protocol freezes applicable exact references |
| L8 | Stress taxonomy, profiles, schedules, injection, clean/stressed matching | Owner preserved; Protocol freezes applicable exact references |
| L9 | Simulation platform, command mapping, safety gates, outcomes, embodiment evidence | Owner preserved; Protocol freezes applicable exact references |
| L10 | Read-only provenance, dashboards, cards, exports, reproduction and release presentation | Owner preserved; Protocol freezes applicable exact references |

Layer 0 governs claims after evidence exists. Layers 1–9 produce scientific or technical evidence. Layer 10 is read-only and cannot repair, rematch, retune, recompute, strengthen limitations, approve claims or create primary evidence.

## 10. Evaluation-mode registry

`EM-OFFLINE`, `EM-EVIDENCE`, `EM-TEMPORAL`, `EM-POLICY`, `EM-CLOSEDLOOP`, `EM-STRESS`, `EM-EMBODIMENT`, and `EM-DASHBOARD` are distinct modes. Every run cell declares one primary mode and any secondary modes; incompatible modes are not pooled without a registered estimand and claim boundary.

## 11. Official A0–A13 ladder and no-A14 lock

| ID | Official identity | P00 disposition | Global constraint |
| --- | --- | --- | --- |
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A1 | Calibrated Decoder / Calibration Visibility | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A3 | Uncertainty and Selective Prediction | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A4 | Longer-Window, Multi-Window Voting/Averaging, and Ordinary Ensemble Controls | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A6 | IHARQ + Evidence-Quality Estimator | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A7 | IHARQ + RegimeRisk Temporal Trust | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A8 | Learning-to-Defer / Deferral Comparison | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |
| A13 | Layer 9 MyoSuite/OpenSim/Static-Replay Embodiment Demo | READINESS_ONLY_NOT_ACTIVATED in P00 | A14 prohibited |

A12.5 is a local synchronized Layer 8/Layer 9 comparison under A12/A13, not a global A14. `A14` is invalid in configs, schemas, CLI, validators, reports and handoffs.

## 12. Global data, split, chronology and visibility controls

Dataset/source eligibility, split roles, calibration/threshold fitting roles, chronology, dual clocks, field visibility and reuse decisions must be frozen in the applicable annex. Test/evaluation fields cannot be visible to training, calibration, threshold selection or decision-time logic. Temporal joins require strict predecessor legality and explicit clock uncertainty. Reuse is by exact identity; semantic change requires derivation or rerun.

## 13. Global run-cell contract

Every run cell records cell ID, phase, evaluation mode, source snapshot/commit, environment, config hash, input artifacts, seed or `NOT_APPLICABLE`, budgets, command, expected outputs, inclusion/invalidity rules, evidence class, limitations, rerun rule and downstream consumers. Missing required identity blocks the cell.

## 14. Matching, comparison and denominator governance

A matched comparison freezes eligible set, key dimensions, conditional keys, independent unit, common support, arm compatibility, attrition, unmatched disposition and estimand. Denominators are conserved through expected → discovered → eligible → attempted → valid → matched → analyzed → released. Missing/unmatched/invalid records remain explicit.

## 15. Metric, estimand and analysis governance

Every metric binds to a MetricDictionary identity, formula, direction, unit, denominator, aggregation, tie/endpoint/smoothing rules, inference method and claim role. Statistical units and dependence profiles are explicit. Multiplicity, selection, equivalence/noninferiority/no-harm margins, missingness, subgroup and sensitivity plans are annex-owned and frozen before claim-bearing execution.

## 16. Negative, null, harmful and failed evidence

Negative, null, equivalent, harmful, invalid, blocked, unmatched and diagnostic-only results remain visible. They cannot be dropped because they weaken a narrative. Failed runs are preserved with exact reason, invalidation and rerun disposition. Layer 10 must include negative/failure panels where applicable.

## 17. Specialized A10–A13 clauses

A10 requires actual propensities, support/ESS, estimator sensitivity, cross-fitting where applicable, frozen outer evaluation and no future leakage. A11 requires demonstrated sequential necessity, legal masks, reward/cost versions, valid trajectories, checkpoint identity and held-out frozen evaluation. A12 requires versioned stress profiles/schedules/seeds and clean/stressed matching. A13 requires platform/task/mapping/safety/outcome identities and explicit simulation/embodiment-proxy limitations.

## 18. Layer 0 and Layer 10 interfaces

The Protocol supplies claim ceilings, candidate statement interfaces, mandatory limitations and evidence identities; Layer 0 alone issues disposition after the Phase Evidence Report. Layer 10 consumes accepted saved evidence and mapped claims read-only. Any recomputation, repair, rematching, retuning or limitation weakening invalidates the Layer 10 package.

## 19. Evidence products and lifecycle

The immutable run bundle includes source/config/environment identities, inputs/outputs, logs, tests, gates, limitations and hashes. Later products follow Governance V4 order: Phase Analysis → Phase Evidence Report → Layer 0 disposition → Evidence Map → Layer 10 package → release/handoff. This master does not create those final products.

## 20. Amendment, deviation and supersession

Pre-run amendments may change scientific/execution rules after owning-authority and LLM review. Mode C administrative completion is restricted to fields declared administrative before execution. Deviations do not change the contract silently. Post-hoc analyses are exploratory and separately identified. Scientific corrections after release create successor artifacts and invalidate descendants.

## 21. Machine-readable authority

The authoritative machine companions are located under `docs/authorities/protocol_v1_0/machine_readable/`. Their IDs, phase/layer/ablation sets, timing mode, source snapshot, run cells, analysis contract and gate statuses must match this master and the P00 annex.

## 22. Validation and definition of done

Acceptance requires structural, parsing, semantic, cross-authority, hash, human/machine no-drift and local execution validation; five LLM passes; no unresolved material objection; no A14; no empirical P00 cell; no premature downstream final document; and an immutable local snapshot identity.

## Appendix A — Protocol profile ledger

| Profile | Purpose | P00 status | Future owner |
| --- | --- | --- | --- |
| PV1-001 | Threshold applicability profile | REFERENCE_ONLY_FUTURE_PHASE | P03 |
| PV1-002 | Dependence profile | APPLICABLE_FOUNDATION_PROFILE | P01/P03 and later |
| PV1-003 | Temporal history profile | REFERENCE_ONLY_FUTURE_PHASE | P05 |
| PV1-004 | Priority/guard profile | REFERENCE_ONLY_FUTURE_PHASE | P04/P06/P07 |
| PV1-005 | Budget profile | REFERENCE_ONLY_FUTURE_PHASE | P04/P06-P11 |
| PV1-006 | Cost/burden profile | REFERENCE_ONLY_FUTURE_PHASE | P04/P06-P11 |
| PV1-007 | Combination relation profile | REFERENCE_ONLY_FUTURE_PHASE | P02-P04 |
| PV1-008 | A5 identity profile | REFERENCE_ONLY_FUTURE_PHASE | P04 |
| PV1-009 | Local A5 profile | REFERENCE_ONLY_FUTURE_PHASE | P04 |
| PV1-010 | Matched comparison profile | APPLICABLE_FOUNDATION_PROFILE | all later comparison phases |
| PV1-011 | Metric profile | APPLICABLE_FOUNDATION_PROFILE | all later evidence phases |
| PV1-012 | A7 causal profile | REFERENCE_ONLY_FUTURE_PHASE | P05 and later |
| MET-R11 | Protocol R42 metric-interface closure ledger | APPLICABLE_FOUNDATION_PROFILE | P00 readiness; values phase-annex-owned |

## Appendix B — Source coverage

The source snapshot manifest includes Governance V4, all seven core authorities, Build Book R3 and Phase 0 annex successors, all Phase 0 prompts/audits/finalization records, the R3 Protocol template, and this creation prompt. Requirement-level mappings are in `protocol_requirement_ledger.csv`.

## Appendix C — Nonblocking limitations

1. The portable registry-resolved cross-version `uv.lock` remains incomplete and fail-closed; the exact verified Python 3.13.5 runtime lock is available.
2. Python 3.11 and 3.12 were unavailable locally; Python 3.13.5 passed the full predecessor suite and Protocol validations.
3. Historical P00 conformance remains Mode B engineering/retrospective evidence; freezing this master does not upgrade it.
