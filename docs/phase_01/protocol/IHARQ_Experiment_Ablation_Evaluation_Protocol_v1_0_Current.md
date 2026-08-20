---
title: "IHARQ Experiment, Ablation, Evaluation, Execution, and Analysis Protocol v1.0 — Single Canonical Cumulative Through Phase 1"
document_id: "IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1"
version: "1.0-CUM-P01-R1"
status: "FROZEN"
authority_representation: "SINGLE_CANONICAL_DOCUMENT"
phases_represented: ["P00", "P01"]
generation_timestamp: "2026-08-08T00:11:00+03:30"
current_governance: "V6.1_SINGLE_TRACK"
---

# IHARQ BenchGuard Stretch C
# Experiment, Ablation, Evaluation, Execution, and Analysis Protocol v1.0
## Single Canonical Cumulative Authority Through Phase 1

**Current Protocol authority:** `IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1`  
**Version:** `1.0-CUM-P01-R1`  
**Status:** **FROZEN**  
**Phases represented:** P00, P01  
**P01 final execution decision:** **ACCEPTED**  
**Current freeze-critical blockers:** **0**  

> **Authority singularity rule.** This Markdown file is the single current Protocol v1.0 authority. The Word file delivered with it is a format-equivalent, non-authoritative presentation derivative generated from this canonical Markdown. Historical Master R2/R3, P00/P01 annex files, and former separate run/analysis files remain provenance sources only; they do not compete with this file as current Protocol truth.

## Document control

| Field | Current controlling value |
| --- | --- |
| protocol_id | IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1 |
| version | 1.0-CUM-P01-R1 |
| authority_representation | SINGLE_CANONICAL_DOCUMENT |
| phases | P00, P01 |
| generation_timestamp | 2026-08-08T00:11:00+03:30 |
| governance | Governance V6.1 single-track |
| P01 scientific freeze | P01-L1-OFFICIAL-RUN-FREEZE-R2 |
| P01 config ID | d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01 execution status | ACCEPTED |
| unresolved blockers | 0 |
| future update rule | P02 and later extend this same cumulative Protocol document |

## Owner-directed document-architecture consolidation

The project owner has directed a transition from a fragmented Protocol-v1 distribution (master + phase annexes + separate machine-readable run/analysis surfaces) to **one cumulative canonical Protocol v1.0 document**. This is an authority-representation consolidation only.

| Consolidation question | Disposition |
| --- | --- |
| scientific contract changed | NO |
| historical execution changed | NO |
| phase identity changed | NO |
| ablation identity changed | NO |
| analysis rules silently removed | NO |
| traceability reduced | NO |
| authority representation consolidated | YES |

### Predecessor representation and supersession

- `IHARQ-PROTOCOL-V1-MASTER-R3` — predecessor project-wide component; its substantive current rules are internalized in Part I.
- `IHARQ-PROTOCOL-V1-P00-ANNEX-R2` — exact P00 phase history; preserved verbatim in Part II.
- `IHARQ-PROTOCOL-V1-P01-ANNEX-R1` — exact P01 execution-and-analysis contract; preserved in Part III.
- predecessor cumulative `run_matrix.yaml`, `analysis_contract.yaml`, ablation/readiness and amendment/repair ledgers — internalized in Parts IV–X and structured appendices.
- `IHARQ-PROTOCOL-V1-MASTER-R2` remains a historical predecessor with SHA-256 `938fcaab2be30d2e59ccc5082a9c3cc6c2ccc3e8889b352099aa514b96e046d4`; it is not current workflow governance.

No prior Protocol history is deleted; separate predecessor files are simply no longer separately authoritative.

## How to read this cumulative Protocol

- **Part I** is the current project-wide Protocol authority inherited from Master R3 and updated only for single-document authority representation.
- **Part II** preserves the Phase 0 Protocol v1.0 Annex R2 exactly as historical/current inherited P00 protocol content.
- **Part III** preserves the Phase 1 Protocol contract, including pre-run intent, actual execution, repairs and final accepted state.
- **Parts IV–XI** are cumulative registers that de-duplicate repeated definitions and provide one project-level cross-phase view.
- **Appendices A–I** contain structured machine-readable blocks generated from the same canonical values and validation matrices.

Historical terms (for example P00 `timing_mode: B`) remain valid descriptions of historical evidence classification but do not reintroduce obsolete workflow modes into current Governance V6.1.

---

# PART I — PROJECT-WIDE PROTOCOL AUTHORITY

> **Provenance note:** The substantive rules below are inherited from predecessor Master R3 (`IHARQ-PROTOCOL-V1-MASTER-R3`). Under the owner-directed consolidation, they now operate through `IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1` rather than through a separate current master file.

## Document control

| Field | Frozen value |
| --- | --- |
| project_id | IHARQ-BENCHGUARD-STRETCH-C |
| protocol_id | IHARQ-PROTOCOL-V1-MASTER-R3 |
| protocol_version | 1.0-R3 |
| document_scope | PROJECT_WIDE_MASTER |
| effective_date | 2026-08-07 |
| registration_timestamp | 2026-08-07T23:36:00+03:30 |
| registration_or_archive_uri | LOCAL_PROTOCOL_PACKAGE_SNAPSHOT |
| identity_mode | CONTENT_HASHED_LOCAL_PACKAGE |
| predecessor_id | IHARQ-PROTOCOL-V1-MASTER-R2 |
| predecessor_file_sha256 | 938fcaab2be30d2e59ccc5082a9c3cc6c2ccc3e8889b352099aa514b96e046d4 |
| predecessor_protocol_freeze_sha256 | 881d7f705bfdacc0c00b4fb547a35e9b8dad60114314ca13f4fec115c3cb9d82 |
| current_governance | Governance V6.1 single-track |
| current_workflow | ZIP-first; Kaggle-centered; evidence-insufficiency loopback only; Protocol-after-sufficient-execution |
| p00_annex | IHARQ-PROTOCOL-V1-P00-ANNEX-R2 — preserved unchanged as historical/current inherited authority |
| p01_annex | IHARQ-PROTOCOL-V1-P01-ANNEX-R1 |
| p01_execution_status | ACCEPTED |
| current_status | FROZEN_WITH_NONBLOCKING_LIMITATIONS |
| registry_version | R44 |
| review_mode | MULTI_PASS_FAIL_CLOSED_DOCUMENT_AND_EXECUTION_AUDIT |
| human_review_used | false |
| unresolved_freeze_critical_objection | NONE |

## R3 successor and governance-migration control

R3 is required because Master R2 contains **Governance V4-era timing-mode and publication/workflow machinery** that no longer describes the controlling project procedure. Governance V6.1 now owns a single direct phase workflow: inspect cumulative project state, implement/execute, assess evidence sufficiency, repair only evidence-insufficient scope, then complete Protocol v1.0, the Phase Evidence/Results/Interpretation Report, Layer 0 review, Evidence Map, Layer 10, and the updated cumulative ZIP. R2 remains immutable historical evidence.

R3 makes the minimum global semantic migration necessary:

- replaces timing-mode workflow machinery as a **current governing process** with V6.1 single-track chronology;
- preserves P00 `Mode B` only as historical evidence classification attached to the P00 execution record;
- removes any implication that GitHub synchronization/CI is required for normal intermediate-phase continuation;
- updates the phase register to record the existence/freeze of the P01 annex;
- retains all stable project-wide scientific rules, phase/layer identities, A0-A13 ladder, no-A14 lock, fairness, leakage, matching, denominator, negative-result, Layer 0 and Layer 10 boundaries;
- adds no P01-specific dataset/configuration details to the master; those remain annex-owned.

No P00 scientific or engineering history is rewritten.

## 1. Purpose and authority

This master freezes project-wide Protocol identities, evidence-status rules, amendment/deviation governance, global run-cell/comparison requirements, A0-A13 semantics, evidence-product interfaces, and the inheritance contract for phase annexes. It does not redesign Architecture, select methods post hoc, invent Registry objects, implement code, report scientific findings, approve claims, or permit Layer 10 recomputation.

The master plus phase annexes are binding only when human-readable and machine-readable identities agree, deterministic validation passes, source snapshots/hashes resolve, and no freeze-critical objection remains.

## 2. Scope-partitioned authority and conflict resolution

| Authority | Owned surface | Protocol boundary |
| --- | --- | --- |
| Governance V6.1 | current document/workflow governance, continuation, Protocol-after-execution, cumulative ZIP strategy | supersedes older workflow/timing machinery; cannot alter scientific authorities |
| Architecture | P00-P15, L0-L10, A0-A13 and system boundaries | identities may not be renamed by configs/reports |
| Registry R44 | canonical records, fields, aliases, lifecycle/status, lineage/interfaces | Protocol references; does not invent |
| Execution and Evidence Plan R41 | phase products, gates, evidence roles, exit criteria | Protocol makes required identities/execution exact |
| Protocol v0.1/R42 + Protocol v1.0 | fairness, matching, leakage, denominators, exclusions, negative evidence, ablations, analysis governance | v1 records actual execution and freezes future analysis without post-hoc upgrading |
| Phase Playbook R41 | operational order, lawful repair and handoff | minimum-scope repair; failed evidence preserved |
| Method Selection R2 | accepted datasets/methods/strategies | Protocol may not select new methods based on results |
| Nuts-and-Bolts R2 | technical behavior, validators, failure semantics | Protocol freezes accepted profile identities and parameters |
| Implementation Build Book | executable realization, paths, environment intent, configs, run cells/gates | pre-run intent; actual execution evidence may document lawful runtime amendments |
| Final phase execution bundle | actual environment/run IDs/failures/amendments/accepted outputs | controls what actually happened on execution-owned surfaces |

Conflicts are classified by affected surface and routed to the owning authority. Historical values are preserved; the current controlling value is explicit; incompatible values are never averaged or silently merged.

## 3. Master-plus-annex inheritance

There is one project-wide master and one independently frozen annex per phase. The master owns global identities/rules; each annex owns exact phase questions, inputs, configs, execution identities, analysis contract, evidence ceiling, amendments and handoffs. A global semantic change requires a master successor and annex-impact review.

## 4. Current review, publication and project-state governance

Review is fail-closed and deterministic evidence outranks prose. During intermediate phases, the cumulative ZIP/package and its external immutable pointers are the controlling project state. GitHub and Hugging Face are optional complements for oversized/public artifacts; routine GitHub pull/synchronization/CI is not a phase-continuation requirement.

## 5. Current chronology and historical evidence classification

**Current governing chronology has no Protocol timing modes.** For every phase: pre-run frozen intent is preserved; actual execution is recorded; failed attempts and amendments remain visible; evidence sufficiency is evaluated; only the minimum evidence-insufficient scope is repaired/rerun; Protocol v1.0 is then completed from the accepted execution without post-hoc manipulation.

Historical labels such as P00 `Mode B` remain valid only as immutable descriptions of historical evidence chronology. They are not current workflow branches and cannot be used to create a second process track. Evidence class/claim ceiling still depends on chronology and whether choices were made before or after observing results.

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
| P01 | Public Data and Split Protocol | Global identity only; exact values annex-owned | Annex frozen in P01 R1 |
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

The immutable run bundle includes source/config/environment identities, inputs/outputs, logs, tests, gates, limitations and hashes. Later products follow Governance V6.1 single-track order: Protocol v1.0 phase annex → Phase Evidence, Results, and Interpretation Report → Layer 0 disposition → Evidence Map → Layer 10 package → cumulative project ZIP/handoff. This master does not create those final products.

## 20. Amendment, deviation and supersession

Pre-run amendments may change scientific/execution rules after owning-authority review. Post-execution Protocol completion records what actually happened and may not upgrade retrospective evidence. Deviations do not change the contract silently. Post-hoc analyses are exploratory and separately identified. Scientific corrections after release create successor artifacts and invalidate descendants.

## 21. Structured authority and machine-readable singularity

The authoritative machine companions are located under `docs/authorities/protocol_v1_0/machine_readable/`. Their IDs, phase/layer/ablation sets, current single-track governance status, historical timing classifications where retained solely for audit, source snapshots, run cells, analysis contracts and gate statuses must match this master and phase annexes.

## 22. Validation and definition of done

Acceptance requires structural, parsing, semantic, cross-authority, hash, human/machine no-drift, execution-conformance, no-post-hoc, A0-A13/no-A14, lineage/integrity, security, downstream-usability and adversarial validation; no unresolved freeze-critical objection; no A14; and exact phase-level evidence identities.

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


## Appendix D — R3 migration ledger summary

- predecessor master: `IHARQ-PROTOCOL-V1-MASTER-R2`
- predecessor file SHA-256: `938fcaab2be30d2e59ccc5082a9c3cc6c2ccc3e8889b352099aa514b96e046d4`
- predecessor P00 annex: `IHARQ-PROTOCOL-V1-P00-ANNEX-R2` (unchanged)
- migration owner: Governance V6.1 on workflow/timing/project-state surfaces
- P01 addition: `IHARQ-PROTOCOL-V1-P01-ANNEX-R1`
- scientific effect of master migration: **NONE**
- P00 execution/history invalidated: **NO**
- additional P00 computation required: **NO**

---

# PART II — PHASE 00 PROTOCOL

> **Exact preservation note:** The complete P00 Annex R2 below is reproduced verbatim from the Phase 0 Protocol v1.0 package. Source SHA-256: `a0dbabfc1c5be739955696f8b5d32d9cdbdedf563a1c9225d9767599bbfbd7b5`. Its `master_protocol_id` and Mode-B fields are historical frozen metadata. They do not create a second current Protocol authority.

---
title: "IHARQ Protocol v1.0 Phase Annex — P00 Repository, Configuration, and Record Schema"
document_id: "IHARQ-PROTOCOL-V1-P00-ANNEX-R2"
master_protocol_id: "IHARQ-PROTOCOL-V1-MASTER-R2"
version: "1.0-R2"
status: "FROZEN_WITH_NONBLOCKING_LIMITATIONS"
timing_mode: "B"
timing_subtype: "ADMINISTRATIVE_FOUNDATION"
evidence_ceiling: "ENGINEERING_FOUNDATION_CONFORMANCE"
protocol_freeze_sha256: "881d7f705bfdacc0c00b4fb547a35e9b8dad60114314ca13f4fec115c3cb9d82"
---

# Protocol v1.0 Phase Annex — P00 Repository, Configuration, and Record Schema

## Document control

| Field | Frozen value |
| --- | --- |
| annex_id | IHARQ-PROTOCOL-V1-P00-ANNEX-R2 |
| master_protocol_id | IHARQ-PROTOCOL-V1-MASTER-R2 |
| phase_id | P00 |
| official_name | Repository, Configuration, and Record Schema |
| version | 1.0-R2 |
| registration_timestamp | 2026-08-03T15:07:37+03:30 |
| timing_mode | B |
| timing_subtype | ADMINISTRATIVE_FOUNDATION |
| evidence_ceiling | ENGINEERING_FOUNDATION_CONFORMANCE |
| identity_mode | LOCAL_PACKAGE_SNAPSHOT |
| source_snapshot_sha256 | bcbf5c70e4b0ca09caa73c3f0963d8cc1bc0adbc0741fad60ef6cd936ca66c95 |
| protocol_freeze_sha256 | 881d7f705bfdacc0c00b4fb547a35e9b8dad60114314ca13f4fec115c3cb9d82 |
| publication_strategy | LOCAL_FIRST_SINGLE_PUBLICATION |
| github_ci_required | false |
| active_empirical_ablations | [] |
| claim_bearing_empirical_cells | [] |
| scientific_effectiveness_claims_allowed | false |
| status | FROZEN_WITH_NONBLOCKING_LIMITATIONS |

## Independent final-audit successor control

This R2 annex supersedes the frozen R1 annex only on Protocol-owned audit and package-governance surfaces. The Phase 0 engineering scope, Mode B timing determination, evidence ceiling, no-empirical-cell boundary, and local-first identity remain unchanged. The successor adds source-exhaustive requirement traceability, normalized review provenance, field-level human/machine drift evidence, explicit placeholder classification, and a passing synthetic P01 inheritance test.

## 1. Phase declaration and purpose

P00 freezes the administrative and engineering foundation contract for authority intake, source/package identity, schemas, record families, configurations, typed IDs, JCS/SHA-256 hashing, manifests, lineage, lifecycle, fixtures, validators, tests, integration, local reproduction, package integrity and downstream document readiness. It contains no empirical claim-bearing cell and does not activate A0–A13.

## 2. Timing-mode audit and evidence consequence

The selected mode is **B**. Broad requirements and gates existed before execution, but the exact Protocol annex, complete fixture taxonomy, validation rules, manifest exclusions, runtime-lock corrections, bounded runner behavior and package freeze rules were finalized through observed failure-and-repair cycles. That history does not satisfy Mode C no-result-contingent-change requirements.

Historical runs therefore remain `ENGINEERING` / `RETROSPECTIVE` foundation-conformance evidence. They may support bounded infrastructure and reproducibility findings, but not confirmatory scientific, clinical, deployment, safety or regulatory claims. A future prospective Mode C rerun is required only if the project wants prospective administrative-foundation registration; it is not required to preserve the historical engineering record.

## 3. Source and implementation freeze

- source snapshot: `IHARQ_Phase_0_Local_First_Finalization_and_Readiness_COMPLETE_R1.zip`
- source snapshot SHA-256: `bcbf5c70e4b0ca09caa73c3f0963d8cc1bc0adbc0741fad60ef6cd936ca66c95`
- authority manifest: `IHARQ-PV1-AUTHORITY-SNAPSHOT-R1`
- local-finalization handoff: `P00-LOCAL-FIRST-FINALIZATION-HANDOFF-R1`
- environment: Python 3.13.5 locally verified
- exact local dependency closure: `REQUIREMENTS-LOCK-LOCAL-EXACT-R3`
- portable uv lock: `COMPLETE_UV_LOCK_DEFERRED_ENVIRONMENTALLY`
- schemas/configs/records/fixtures/validators/tests/gates: exact catalogs in the source snapshot
- freeze identity: `720a38906046738d29d0bf63087eeda0c03211a7ee9d397b0dd2870037050605`

## 4. Exact scope

Applicable: authority resolution; repository-package structure; schema/config/record coverage; typed IDs; canonical serialization and SHA-256; seeds or explicit `NOT_APPLICABLE`; manifests; lineage/lifecycle/supersession/invalidation; valid and malformed fixtures; validator/test coverage; L0–L10 foundation integration; A0–A13 readiness and A14 rejection; local CI-equivalent execution; clean reproduction; package checksum reconciliation; future phase/document contracts.

Not applicable: real datasets and scientific splits; model training/inference; calibration fitting or threshold selection; IHARQ effectiveness evaluation; temporal inference; policy learning; closed-loop scientific simulation; stress or embodiment execution; scientific metric estimation; statistical superiority; clinical or real-world claims.

## 5. Scientific applicability dispositions

| Surface | P00 status | Reason | Future owner |
| --- | --- | --- | --- |
| Dataset eligibility | NOT_APPLICABLE | Only authority packages and explicit mock/non-empirical fixtures are used | P01 and later dataset-bearing phases |
| Calibration/threshold selection | NOT_APPLICABLE | No predictions or operating points are fitted in P00 | P03 |
| Scientific estimands | NOT_APPLICABLE | P00 uses deterministic engineering inventory/conformance only | Applicable later annex |
| Statistical inference | NOT_APPLICABLE | No scientific population or treatment effect exists | Applicable later annex |
| A10 policy/OPE | NOT_APPLICABLE | No adaptation or OPE occurs | P10 |
| Stress and embodiment outcomes | NOT_APPLICABLE | Only schemas, fixtures and interfaces are validated | P09/P12/P13 |

## 6. Engineering run matrix

| Cell ID | Purpose | Registered command | Pass criterion |
| --- | --- | --- | --- |
| P00-CELL-AUTHORITY-INTAKE | Verify authority/source identities and requirement disposition | python scripts/run_local_first_finalization_audit.py | All authority hashes resolve; requirement ledger has no missing applicable disposition |
| P00-CELL-SCHEMA-COVERAGE | Validate JSON Schema and record-family coverage | python scripts/run_static_checks.py | All schemas parse and catalog references resolve |
| P00-CELL-CONFIG-RESOLUTION | Resolve strict P00 configuration | python -m iharq.cli phase validate-inputs --phase P00 --profile configs/phases/p00.yaml | Strict configuration validates; phase identity matches P00 |
| P00-CELL-IDENTITY-JCS-HASH | Validate typed IDs, canonical serialization, SHA-256 and golden vectors | python -m pytest -q tests/test_canonical.py tests/test_lineage_lifecycle.py | All deterministic identity/hash tests pass |
| P00-CELL-VALID-FIXTURES | Accept all valid and integrated non-empirical fixtures | python -m pytest -q tests/test_valid_fixtures.py | Every registered valid/integrated bundle passes |
| P00-CELL-MALFORMED-FIXTURES | Reject the complete malformed taxonomy | python -m pytest -q tests/test_negative_fixtures.py tests/test_audit1_negative_fixtures.py tests/test_audit2_negative_fixtures.py tests/test_audit3_negative_fixtures.py | Every malformed category produces a deterministic failure |
| P00-CELL-VALIDATOR-TEST-COVERAGE | Run complete deterministic suite | python -m pytest -q -p no:cacheprovider | Complete suite passes with no hidden deselection |
| P00-CELL-A0-A13-READINESS | Verify A0-A13 readiness and reject A14 | python scripts/run_phase0_final_implementation_audit.py | A0-A13 foundation hooks complete; A14 rejected |
| P00-CELL-L0-L3-INTEGRATION | Verify L0-L3 integration foundation | python scripts/run_official_layer_audit_1.py | Audit 1 regression passes |
| P00-CELL-POLICY-UPDATE | Verify update-enabled policy traceability | python scripts/run_official_layer_audit_2.py | Update trace, before/after policy IDs, reward/config/seed and limitations preserved |
| P00-CELL-FROZEN-EVALUATION | Verify frozen-evaluation immutability | python scripts/run_official_layer_audit_2.py | No mutation; disabled-update evidence and mode warning present |
| P00-CELL-L8-STRESS-LINEAGE | Verify clean-to-stressed lineage and limitations | python scripts/run_official_layer_audit_3.py | Stress lineage and matching pass |
| P00-CELL-L9-EMBODIMENT-PROXY | Verify simulation-only embodiment proxy contracts | python scripts/run_official_layer_audit_3.py | Proxy limitations and safety/reward lineage pass |
| P00-CELL-L10-READ-ONLY | Verify Layer 10 source-only behavior | python scripts/run_official_layer_audit_3.py | No upstream mutation, rematching, retuning, claim approval or primary evidence creation |
| P00-CELL-MANIFEST-RECONCILIATION | Regenerate and compare repository manifest | python scripts/reconcile_repository_manifest.py && python scripts/reconcile_repository_manifest.py --check | Manifest matches governed tree after transient exclusions |
| P00-CELL-LOCAL-REPRODUCTION | Reproduce from clean isolated local copy | python scripts/run_local_reproduction.py | Isolated reproduction passes using exact verified local dependency closure |
| P00-CELL-PACKAGE-INTEGRITY | Build and verify repository-ready archive | python -m iharq.cli package build --output protocol_package_test.zip && python -m iharq.cli package verify --archive protocol_package_test.zip | Archive CRC, file count and hashes reconcile |
| P00-CELL-FUTURE-PHASE-CONTRACTS | Verify P00-P15 reusable contracts and L0-L10 foundations | python scripts/run_phase0_final_implementation_audit.py | All phase contracts and layer foundations have complete dispositions |
| P00-CELL-NEXT-DOCUMENT-READINESS | Verify six downstream readiness packages | python scripts/run_local_first_finalization_audit.py | Six readiness packages exist and are clearly non-final |

All cells use `ablation_id = NOT_APPLICABLE`, `scientific_matching_key = NOT_APPLICABLE`, `scientific_estimand = NOT_APPLICABLE`, and `scientific_seed_set = NOT_APPLICABLE`, except deterministic fixture seeds where a test explicitly requires a stable identity.

## 7. Engineering analysis contract

The registered analysis is descriptive and deterministic. It reports exact expected/discovered/validated/failed/excluded/invalid/accepted inventories for artifacts, schemas, configs, records, fixtures, validators, tests, gates, integration chains, hashes, manifests, environment/lock evidence, clean reproduction and package integrity. It does not compute scientific performance, p-values, treatment effects, superiority, calibration effectiveness, stress robustness or simulator performance.

## 8. PV1/MET applicability

| Profile | Purpose | P00 disposition | Future owner |
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

No future scientific numerical value is populated. P00 validates only profile existence, IDs, versions, hooks, validators and the absence of hidden defaults.

## 9. A0–A13 readiness and A14 rejection

| ID | Official identity | P00 status |
| --- | --- | --- |
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | READINESS_ONLY_NOT_ACTIVATED |
| A1 | Calibrated Decoder / Calibration Visibility | READINESS_ONLY_NOT_ACTIVATED |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | READINESS_ONLY_NOT_ACTIVATED |
| A3 | Uncertainty and Selective Prediction | READINESS_ONLY_NOT_ACTIVATED |
| A4 | Longer-Window, Multi-Window Voting/Averaging, and Ordinary Ensemble Controls | READINESS_ONLY_NOT_ACTIVATED |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | READINESS_ONLY_NOT_ACTIVATED |
| A6 | IHARQ + Evidence-Quality Estimator | READINESS_ONLY_NOT_ACTIVATED |
| A7 | IHARQ + RegimeRisk Temporal Trust | READINESS_ONLY_NOT_ACTIVATED |
| A8 | Learning-to-Defer / Deferral Comparison | READINESS_ONLY_NOT_ACTIVATED |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | READINESS_ONLY_NOT_ACTIVATED |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | READINESS_ONLY_NOT_ACTIVATED |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | READINESS_ONLY_NOT_ACTIVATED |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | READINESS_ONLY_NOT_ACTIVATED |
| A13 | Layer 9 MyoSuite/OpenSim/Static-Replay Embodiment Demo | READINESS_ONLY_NOT_ACTIVATED |

A14 is prohibited. A12.5 remains a local synchronized comparison under A12/A13 and is not a global ablation.

## 10. Layer participation and noninterference

| Layer | P00 foundation role | Noninterference rule |
| --- | --- | --- |
| L0 | Claim safety, evidence sufficiency, wording, downgrade, limitations, lifecycle | Foundation contracts only; no scientific execution or ownership reassignment |
| L1 | Data, labels, splits, windows, preprocessing, manifests | Foundation contracts only; no scientific execution or ownership reassignment |
| L2 | Decoder families, controls, predictions, model identity | Foundation contracts only; no scientific execution or ownership reassignment |
| L3 | Calibration, uncertainty, selective prediction, registered operating points | Foundation contracts only; no scientific execution or ownership reassignment |
| L4 | IHARQ evidence verification, reasons, combination, fallback, unsafe states | Foundation contracts only; no scientific execution or ownership reassignment |
| L5 | Temporal features, trust, regime logic, stop-loss | Foundation contracts only; no scientific execution or ownership reassignment |
| L6 | Evidence quality, policy, deferral, costs, supervised/adaptive readiness | Foundation contracts only; no scientific execution or ownership reassignment |
| L7 | State, action, transition, reward, cost, session, rollout, simulator diagnostics | Foundation contracts only; no scientific execution or ownership reassignment |
| L8 | Stress taxonomy, profiles, schedules, injection, clean/stressed matching | Foundation contracts only; no scientific execution or ownership reassignment |
| L9 | Simulation platform, command mapping, safety gates, outcomes, embodiment evidence | Foundation contracts only; no scientific execution or ownership reassignment |
| L10 | Read-only provenance, dashboards, cards, exports, reproduction and release presentation | Foundation contracts only; no scientific execution or ownership reassignment |

Layer 0 cannot modify measurements, metrics, denominators, matching, predictions or empirical records. Layer 10 cannot recompute, repair, rematch, retune, hide negatives, weaken limitations, approve claims or create primary evidence.

## 11. Local-first gate crosswalk

| Gate | Status | Protocol evidence |
| --- | --- | --- |
| P0-GATE-01 | PASS | P00-CELL-AUTHORITY-INTAKE |
| P0-GATE-02 | PASS | P00-CELL-SCHEMA-COVERAGE |
| P0-GATE-03 | PASS | P00-CELL-CONFIG-RESOLUTION |
| P0-GATE-04 | PASS | P00-CELL-IDENTITY-JCS-HASH |
| P0-GATE-05 | PASS | P00-CELL-VALID-FIXTURES |
| P0-GATE-06 | PASS | P00-CELL-MALFORMED-FIXTURES |
| P0-GATE-07 | PASS | P00-CELL-VALIDATOR-TEST-COVERAGE |
| P0-GATE-08 | PASS | P00-CELL-A0-A13-READINESS |
| P0-GATE-09 | PASS | P00-CELL-L0-L3-INTEGRATION |
| P0-GATE-10 | PASS | P00-CELL-POLICY-UPDATE |
| P0-GATE-11 | PASS | P00-CELL-FROZEN-EVALUATION |
| P0-GATE-12 | PASS | P00-CELL-L8-STRESS-LINEAGE |
| P0-GATE-13_FOUNDATION | PASS | P00-CELL-L9-EMBODIMENT-PROXY |
| P0-GATE-14_FOUNDATION | PASS | P00-CELL-L10-READ-ONLY |
| P0-GATE-15 | PASS | P00-CELL-MANIFEST-RECONCILIATION |
| P0-GATE-16_IMPLEMENTATION | PASS_WITH_NONBLOCKING_LIMITATIONS | P00-CELL-LOCAL-REPRODUCTION |
| P0-GATE-17_LOCAL | PASS | P00-CELL-PACKAGE-INTEGRITY |
| P0-GATE-18 | DEFERRED_TO_LATER_GOVERNED_PHASE0_CLOSURE | P00-CELL-FUTURE-PHASE-CONTRACTS |

GitHub CI is `NOT_APPLICABLE_BY_ACCEPTED_WORKFLOW_STRATEGY`; it is neither attempted nor simulated.

## 12. No-drift, amendment and deviation

Mode C no-drift is not claimed for historical runs. From this freeze forward, any affected source, schema, config, fixture, test, gate, environment, run-cell or analysis change requires an amendment or successor, descendant invalidation, rerun disposition and regenerated hashes. Clerical corrections require before/after digests and proof of unchanged semantics.

## 13. Evidence and downstream handoffs

The annex prepares, but does not create, the final Phase Analysis, Phase Evidence Report, Layer 0 disposition, accepted Evidence Map, Layer 10 package, final release or Phase 1 handoff. Downstream input specifications are provided under `docs/authorities/protocol_v1_0/downstream_readiness/`.

## 14. Limitations

1. Portable cross-version `uv.lock` is incomplete and explicitly fail-closed.
2. Python 3.11 and 3.12 were unavailable locally; Python 3.13.5 passed.
3. Historical conformance is Mode B engineering/retrospective, not prospective Mode C.
4. The annex governs deterministic foundation evidence only; it does not authorize scientific claims.

## 15. Freeze decision

`P00_PROTOCOL_V1_MASTER_AND_ANNEX_FROZEN_WITH_NONBLOCKING_LIMITATIONS`.

All freeze-critical P00 fields are resolved. Human and machine IDs match. The remaining limitations do not prevent exact local use of the annex but must be inherited by future execution/analysis records.

### P00 cumulative consolidation disposition

- P00 scientific/engineering meaning: **PRESERVED**.
- P00 historical Mode-B evidence ceiling: **PRESERVED**.
- P00 empirical ablations: **NONE executed**.
- P00 run matrix: **19 cells preserved in Part IV / Appendix B**.
- P00 analysis contract: **6 deterministic engineering analyses preserved in Part V / Appendix C**.
- Current workflow machinery: **Governance V6.1**, not historical Governance V4 timing modes.
- Additional P00 computation: **NOT REQUIRED**.

---

# PART III — PHASE 01 PROTOCOL

> **Predecessor integration note:** The Phase 01 Annex R1 content below is the accepted P01 contract and is internalized here. Its historical `master_protocol_id: IHARQ-PROTOCOL-V1-MASTER-R3` records its creation lineage; the current controlling Protocol identity is this cumulative document.

---
title: "IHARQ Protocol v1.0 — Phase 01 Annex: Public Data and Split Protocol"
document_id: "IHARQ-PROTOCOL-V1-P01-ANNEX-R1"
version: "1.0-P01-R1"
status: "FROZEN_WITH_EXPLICIT_EXECUTION_AMENDMENTS_AND_DOWNSTREAM_REQUIREMENTS"
master_protocol_id: "IHARQ-PROTOCOL-V1-MASTER-R3"
phase_id: "P01"
primary_layer: "L1"
scientific_freeze: "P01-L1-OFFICIAL-RUN-FREEZE-R2"
config_id: "d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f"
registration_timestamp: "2026-08-07T23:36:00+03:30"
execution_status: "ACCEPTED"
---

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

# PART IV — CUMULATIVE RUN MATRIX

The cumulative run matrix retains phase identity while eliminating separate current run-matrix authority files. P00 cells preserve their historical Mode-B engineering evidence classification. P01 rows represent the final accepted 00–26 lineage; failed attempts are retained in rerun history rather than erased.

## P00 engineering run matrix — 19 preserved cells

| Cell | Purpose | Command | Evidence status | Limitations | Rerun rule |
| --- | --- | --- | --- | --- | --- |
| P00-CELL-AUTHORITY-INTAKE | Verify authority/source identities and requirement disposition | python scripts/run_local_first_finalization_audit.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-SCHEMA-COVERAGE | Validate JSON Schema and record-family coverage | python scripts/run_static_checks.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-CONFIG-RESOLUTION | Resolve strict P00 configuration | python -m iharq.cli phase validate-inputs --phase P00 --profile configs/phases/p00.yaml | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-IDENTITY-JCS-HASH | Validate typed IDs, canonical serialization, SHA-256 and golden vectors | python -m pytest -q tests/test_canonical.py tests/test_lineage_lifecycle.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-VALID-FIXTURES | Accept all valid and integrated non-empirical fixtures | python -m pytest -q tests/test_valid_fixtures.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-MALFORMED-FIXTURES | Reject the complete malformed taxonomy | python -m pytest -q tests/test_negative_fixtures.py tests/test_audit1_negative_fixtures.py tests/test_audit2_negative_fixtures.py tests/test_audit3_negative_fixtures.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-VALIDATOR-TEST-COVERAGE | Run complete deterministic suite | python -m pytest -q -p no:cacheprovider | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-A0-A13-READINESS | Verify A0-A13 readiness and reject A14 | python scripts/run_phase0_final_implementation_audit.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-L0-L3-INTEGRATION | Verify L0-L3 integration foundation | python scripts/run_official_layer_audit_1.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-POLICY-UPDATE | Verify update-enabled policy traceability | python scripts/run_official_layer_audit_2.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-FROZEN-EVALUATION | Verify frozen-evaluation immutability | python scripts/run_official_layer_audit_2.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-L8-STRESS-LINEAGE | Verify clean-to-stressed lineage and limitations | python scripts/run_official_layer_audit_3.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-L9-EMBODIMENT-PROXY | Verify simulation-only embodiment proxy contracts | python scripts/run_official_layer_audit_3.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-L10-READ-ONLY | Verify Layer 10 source-only behavior | python scripts/run_official_layer_audit_3.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-MANIFEST-RECONCILIATION | Regenerate and compare repository manifest | python scripts/reconcile_repository_manifest.py && python scripts/reconcile_repository_manifest.py --check | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-LOCAL-REPRODUCTION | Reproduce from clean isolated local copy | python scripts/run_local_reproduction.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-PACKAGE-INTEGRITY | Build and verify repository-ready archive | python -m iharq.cli package build --output protocol_package_test.zip && python -m iharq.cli package verify --archive protocol_package_test.zip | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-FUTURE-PHASE-CONTRACTS | Verify P00-P15 reusable contracts and L0-L10 foundations | python scripts/run_phase0_final_implementation_audit.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |
| P00-CELL-NEXT-DOCUMENT-READINESS | Verify six downstream readiness packages | python scripts/run_local_first_finalization_audit.py | ENGINEERING_RETROSPECTIVE_MODE_B | NON_EMPIRICAL; NON_CLAIM_BEARING | Rerun after any affected source/config/schema/test/manifest change |

## P01 accepted execution stage matrix — 27 stages

| Stage | Purpose | Status | Validity | Actual outputs | Repair/rerun history |
| --- | --- | --- | --- | --- | --- |
| P01-STAGE-00 | Corrected bootstrap and persistent isolated worker | PASS | VALID_FINAL_ACCEPTED_LINEAGE | authority_manifest.json | — |
| P01-STAGE-01 | Environment | PASS | VALID_FINAL_ACCEPTED_LINEAGE | environment_manifest.json | — |
| P01-STAGE-02 | Project and input intake | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-03 | Authority and configuration | PASS | VALID_FINAL_ACCEPTED_LINEAGE | config_snapshot/official_run_freeze_manifest.json | — |
| P01-STAGE-04 | Phase 0 regression | PASS | VALID_FINAL_ACCEPTED_LINEAGE | reports/phase_01/tests/phase0_and_runtime_regression.json | — |
| P01-STAGE-05 | Source resolution | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-06 | Dataset registry | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-07 | Pass 1: verified source acquisition and bounded loading | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | R49 local stale revision guard failed before worker submission; R50 same-session continuation submitted Stage 07 once; PASS |
| P01-STAGE-08 | Metadata normalization | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-09 | Label mapping | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-10 | Preprocessing compilation | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-11 | Split construction and frozen fit population | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-12 | Low-calibration budgets | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-13 | Pass 2A: bounded preprocessing fit | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-14 | Adopt verified core and materialize matched A4 R2 | PASS | VALID_FINAL_ACCEPTED_LINEAGE | external_artifact_pointers/derived_windows_dataset.json; reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json | R45 canonical record-ID normalization episode and later R48/R49 A4 implementation/profile repairs; accepted Stage 14 materialized A4 R2 while core was adopted unchanged |
| P01-STAGE-15 | Validate and commit the separate A4 R2 Dataset | PASS | VALID_FINAL_ACCEPTED_LINEAGE | external_artifact_pointers/derived_windows_dataset.json; external_artifact_pointers/a4_window_family_dataset.json | A4 persistence/remote manifest validation after R48/R49 hardening; PASS |
| P01-STAGE-16 | Record validation | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-17 | Leakage audit | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-18 | A0–A13 readiness | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | Original missing-module failure; R51/R52 recovery-cell defects; R53 worker-env import repair; PASS |
| P01-STAGE-19 | Cards | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-20 | Manifests | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-21 | Negative register | PASS | VALID_FINAL_ACCEPTED_LINEAGE | negative_and_failed_results/run_failures_and_blockers.json | — |
| P01-STAGE-22 | P02 and later compatibility | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-23 | Evidence sufficiency | PASS | VALID_FINAL_ACCEPTED_LINEAGE | reports/phase_01/preliminary_gate_evaluation.json | — |
| P01-STAGE-24 | Repair metadata | PASS | VALID_FINAL_ACCEPTED_LINEAGE | reports/phase_01/repair_reentry.json | — |
| P01-STAGE-25 | Final export preparation | PASS | VALID_FINAL_ACCEPTED_LINEAGE | — | — |
| P01-STAGE-26 | Terminal decision and bundle export | PASS | VALID_FINAL_ACCEPTED_LINEAGE | /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip.sha256; /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_GitHub_Ready_Repository_d03f0a7c869d_20260807143013-663eab13.zip; /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_GitHub_Ready_Repository_d03f0a7c869d_20260807143013-663eab13.zip.sha256; reports/phase_01/repository_release_plan.json | Original worker packaging BLOCKED by secret scan; R54 repack/redaction repaired external release without duplicating Stage 26; final canonical stage record PASS |

**Cumulative stage/cell denominator:** P00 = 19 historical engineering cells; P01 = 27 accepted execution stages. No P01 stage identity is duplicated in the final canonical lineage.

---

# PART V — CUMULATIVE ANALYSIS CONTRACT

No inferential statistics are invented for P00 or P01. P00 is deterministic engineering-foundation analysis; P01 is deterministic data-protocol/reproducibility closure. Downstream scientific/model analyses belong to later phases.

## P00 allowed analyses

| Analysis ID | Inventory | Method | Evidence ceiling | Scientific inference |
| --- | --- | --- | --- | --- |
| P00-AN-ARTIFACT-COVERAGE | expected/discovered/validated/failed/excluded/invalid/accepted artifacts | exact counts and path reconciliation | ENGINEERING_FOUNDATION_CONFORMANCE | No inferential scientific claims |
| P00-AN-SCHEMA-CONFIG | schemas/configs/record families | catalog-to-file-to-validator coverage | ENGINEERING_FOUNDATION_CONFORMANCE | No inferential scientific claims |
| P00-AN-FIXTURE-RESULTS | valid/integrated/malformed fixtures | pass/reject counts with explicit denominator | ENGINEERING_FOUNDATION_CONFORMANCE | No inferential scientific claims |
| P00-AN-TEST-GATES | tests/validators/gates | deterministic result and gate evidence crosswalk | ENGINEERING_FOUNDATION_CONFORMANCE | No inferential scientific claims |
| P00-AN-INTEGRATION | L0-3, L3-7, L7-10, update, frozen, stress, embodiment, L10 | identity/lineage/limitation preservation | ENGINEERING_FOUNDATION_CONFORMANCE | No inferential scientific claims |
| P00-AN-REPRODUCTION | runtime lock, environment snapshot, clean reproduction and package integrity | exact hashes and exit codes | ENGINEERING_FOUNDATION_CONFORMANCE | No inferential scientific claims |

**P00 prohibited analyses:** scientific superiority; treatment effects; p-values; clinical endpoints; model/calibration/stress/simulator performance claims.

## P01 allowed analyses

| Analysis ID | Analysis | Unit | Denominator | Aggregation | Interpretation ceiling |
| --- | --- | --- | --- | --- | --- |
| P01-AC-001-SOURCE-INVENTORY | Source inventory, provenance, license and checksum reconciliation | source file/dataset | all activated source files/datasets | counts and exact hash reconciliation | data provenance/reproducibility only |
| P01-AC-002-SPLIT | Subject-group split allocation and disjointness | subject group and derived window | all admitted subjects and accepted core windows | role counts by dataset and global | split/leakage correctness only |
| P01-AC-003-DENOMINATOR | Accepted event/window denominator conservation | accepted source event | 12,910 accepted parent events | expected/discovered/valid window counts by dataset/role | data-materialization closure only |
| P01-AC-004-QUALITY | Quality/validation closure | quality summary/window | 489 | flag/hard-invalid counts by dataset | quality annotation/validity only |
| P01-AC-005-LEAKAGE | Leakage and visibility checks | subject/event/window/budget membership | all assigned groups/windows/budget identities | deterministic boolean checks | absence of detected contract leakage under implemented checks |
| P01-AC-006-EXTERNAL | External artifact persistence and integrity | external artifact/shard/index | declared governed artifacts | version/hash/size/count reconciliation | reproducible retrieval/integrity only |
| P01-AC-007-ABLATION-READINESS | A0-A13 foundation readiness and A14 absence | ablation identity | exact A0-A13 set (14 identities) | readiness disposition per identity | foundation readiness only; no effectiveness |
| P01-AC-008-A4 | A4 R2 data-substrate synchronization/feasibility accounting | parent event / registered A4 view | 12,910 core parent events | matched counts/profile identity/feasibility boundary | future A4 substrate readiness; NOT A4 effectiveness |
| P01-AC-009-ENVIRONMENT | Environment and reproducibility amendment reconciliation | execution environment/profile | one accepted P01 execution environment | exact versions/resources/amendment classifications | execution reproducibility only |
| P01-AC-010-GATES-REPAIRS | Gate closure and failed/superseded attempt accounting | gate/stage/repair episode | 16 gates; 27 accepted stages; all material repair episodes | status/blocker/repair classification | execution closure only |

**Global negative/missingness rule:** preserve failures, invalid/unmatched/diagnostic evidence; missingness never becomes zero-success.  
**Global no-post-hoc rule:** no result-dependent relabeling, denominator changes, source replacement or retrospective preregistration; A4 R2 foundation is not effectiveness evidence.

---

# PART VI — CUMULATIVE ABLATION AND CONTROL REGISTER

The authoritative global ladder is exactly A0–A13. P00 created foundation identities but executed no empirical ablation. P01 produced Layer-1 foundation readiness for all A0–A13 and executed none scientifically. A14 is prohibited/absent.

| ID | Official identity | P00 disposition | P01 foundation | Executed in P01 | Downstream | Evidence limitation |
| --- | --- | --- | --- | --- | --- | --- |
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A1 | Calibrated Decoder / Calibration Visibility | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A3 | Uncertainty and Selective Prediction | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A4 | Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | A4_R2_FUTURE_CONFIRMATORY_ONLY; R1_4S_PROFILE_INFEASIBLE |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A6 | IHARQ + Evidence-Quality Estimator | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A7 | IHARQ + RegimeRisk Temporal Trust | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A8 | Learning-to-defer / Deferral Comparison | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |
| A13 | Layer 9 Simulation-Only Embodiment Demo | FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL | FOUNDATION_READY | false | P02-P15 | FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE |

## A14 prohibition

`A14 = PROHIBITED / ABSENT`. There is no valid A14 selector, run, result or claim. Any occurrence of “A14” in this document is solely an explicit prohibition/absence statement. Local A12.x identities, where they exist in upstream architecture, remain A12.x and are not renamed A14.

## A4 cumulative chronology

1. **PRE-RUN / EARLY PROPOSAL:** +0.0…+4.0 s A4 longer window (640 samples) was proposed.
2. **FEASIBILITY FAILURE:** valid parent event `PhysioNetMI:104:0:8:event:24` had only 560 samples after cue; the 4.0 s profile required 80 nonexistent samples.
3. **GOVERNED REPAIR:** no padding, clipping, fabrication or event dropping was allowed.
4. **FINAL R2 FOUNDATION:** `A4_LONG_MATCHED_3P5S_R2`, +0.0…+3.5 s, 560 samples; `A4_MULTI_3X2S_UNIFORM_0P75S_R2` with slices 0:320, 120:440, 240:560.
5. **MATCHED DENOMINATOR:** 12,910/12,910 core parent events.
6. **P01 EVIDENCE STATE:** `FOUNDATION_READY`; `executed_in_p01 = false`.
7. **FUTURE CONFIRMATORY CONTRACT:** downstream A4 use must inherit exact R2 identities; substitution requires governed amendment/invalidation analysis.

---

# PART VII — CUMULATIVE AMENDMENT, DEVIATION, SUPERSESSION, AND RERUN REGISTER

## Material P01 repair/rerun history

| Repair | Stage/surface | Classification | Defect | Science changed | Data changed | Rerun scope | Resolution |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R45 / SAME-SESSION CORE-ADOPTION NORMALIZATION | 14 | CANONICALIZATION_FIX | Existing verified core adoption blocked because date-bearing upstream record IDs changed dependent semantic hashes despite otherwise equivalent scientific records. | False | False | fresh worker/bundle plus affected adoption path; preserved persistent checkpoints | Dependency-order full-record equivalence with exact upstream-ID mapping plus exact remote manifest hash; core Dataset not mutated/reuploaded. |
| R46 | runtime overlay | IMPLEMENTATION_BUG_FIX | Missing datetime/timezone runtime imports. | False | False | affected runtime path only | Required imports added. |
| R47 | A4 profile canonicalization | CANONICALIZATION_FIX | Float literals in hash-bearing A4 profile could cause governed representation drift. | False | False | profile serialization/validation only | Governed decimal strings used for hash-bearing seconds fields. |
| R48 | 14-15 A4 materialization/persistence | IMPLEMENTATION_BUG_FIX + PERSISTENCE_FIX | A4 child interface/set handling and storage identity/read verification gaps; resumability and exact remote manifest closure hardened. | False | False | A4 child/interface and persistence path | Child interface corrected; reader/storage identity closure, synthetic E2E, resumable subject checkpoints and remote manifest verification added. |
| R49 / P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 | 14-15 A4 profile | SCIENTIFIC_CONTRACT_CHANGE (A4 ALTERNATIVE ONLY) | Original proposed A4 +0.0..+4.0 s window is impossible for one valid released parent event (PhysioNetMI:104:0:8:event:24) without 80 nonexistent samples. | True | True | A4 materialization path with exact 12,910 matched parent events | R2 freezes +0.0..+3.5 s 560-sample tensor and three registered 2 s slices; no drop/pad/clip; confirmatory use prohibited until Protocol sync and downstream execution. |
| R50 | 07 | INTEGRATION_FIX | Stale local DISPLAY_REVISION guard expected R42 while live runtime was R49; Stage 07 had not yet been submitted. | False | False | submit Stage 07 once using live worker; no 00-06 replay | Revision guard corrected; Stage 07 PASS. |
| R51-R53 / P01-L1-R53-STAGE18-WORKER-ENV-IMPORT-PROBE-R1 | 18 | INTEGRATION_FIX | A4 readiness wrapper imported write_json from nonexistent module; two recovery-cell validation mistakes then occurred (malformed shim newline and notebook-kernel import probe outside worker PYTHONPATH). | False | False | Stage 18 only after worker-environment import probe | Compatibility shim re-exported authoritative manifests.write_json and was probed under exact worker_env; Stage 18 PASS and readiness artifact verified. |
| P01-L1-R54-FINAL-EXPORT-SECRET-REDACTION-R1 | 26 external release closure | SECURITY/PACKAGING_FIX | Live Kaggle credential was serialized into environment_amendment and the secret scanner correctly blocked the contaminated export. | False | False | redaction/repack/final integrity only; original worker Stage 26 not duplicated | Secret-like environment values redacted; final bundle/repository rebuilt; exact-token scan, manifests and checksums PASS; contaminated failed release is non-authoritative. |

## Protocol/document supersession and structural consolidation

| Change | Type | Predecessor | Successor | Scientific effect | Current disposition |
| --- | --- | --- | --- | --- | --- |
| Master R2→R3 | GOVERNANCE_MIGRATION | IHARQ-PROTOCOL-V1-MASTER-R2 | IHARQ-PROTOCOL-V1-MASTER-R3 | NONE | V6.1 current workflow; R2 historical |
| P00 R1→R2 | INDEPENDENT_AUDIT_SUCCESSOR | IHARQ-PROTOCOL-V1-P00-ANNEX-R1 | IHARQ-PROTOCOL-V1-P00-ANNEX-R2 | NONE | R2 P00 content preserved |
| P01 Annex R1 | PHASE_ADDITION | none | IHARQ-PROTOCOL-V1-P01-ANNEX-R1 | Records actual accepted P01; no post-hoc effectiveness claim | Internalized into cumulative Protocol |
| Single-file consolidation | DOCUMENT_STRUCTURE_CONSOLIDATION | Master R3 + P00 R2 + P01 R1 + separate structured surfaces | IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1 | NONE | One current authority; predecessors historical/source only |

### Amendment classification principles

- Only the A4 R1→R2 **alternative profile** is a `SCIENTIFIC_CONTRACT_CHANGE`, limited to the future A4 control; the official P01 core did not change.
- Python 3.12 compatibility is `EXECUTION_COMPATIBILITY_CHANGE`.
- adaptive-disk policy is `RESOURCE_POLICY_CHANGE`.
- R45/R46/R47/R48/R50/R51–R53 are canonicalization/implementation/integration/persistence fixes as recorded.
- R54 is `SECURITY/PACKAGING_FIX`.
- No listed non-A4 repair changed dataset membership, labels, split, preprocessing, official core window, metric, core denominator or claim ceiling.

---

# PART VIII — CUMULATIVE ENVIRONMENT AND REPRODUCIBILITY REGISTER

| Phase/state | Environment | Status/consequence |
| --- | --- | --- |
| P00 historical execution | Python 3.13.5 exact verified local runtime; portable cross-version lock incomplete | Mode-B engineering foundation; nonblocking portability limitation |
| P01 pre-run intent | Kaggle image intent; Python >=3.11,<3.12; exact package pins; original 60 GiB minimum disk | Historical intended environment |
| P01 accepted execution | Python 3.12.13; package pins matched; `P01-L1-KAGGLE-ENV-FREEZE-R5` | Accepted execution compatibility amendment; scientific values unchanged |
| P01 resource amendment | `P01-L1-KAGGLE-ADAPTIVE-DISK-R1`; observed free disk 18.94 GiB | Resource-policy amendment; no scientific effect |
| P01 release security | R54 redaction/repack after secret scanner blocked contaminated Stage-26 export | Final package token scan PASS; contaminated release non-authoritative |

Deterministic/runtime identities must be carried with reproductions. Environment differences never silently authorize scientific-contract changes.

---

# PART IX — CUMULATIVE EXTERNAL ARTIFACT REGISTER

P00 has no Protocol-critical oversized numerical Dataset pointer. P01 externalizes the large numerical arrays while preserving compact governed manifests/pointers in the project state. A handle alone is insufficient; exact revision and manifest hash are mandatory.

| Artifact | Provider | Handle | Provider rev | Logical rev | Format | Access | Manifest SHA-256 | Local copy state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | Kaggle | csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473 | 2 | 1 | LOSSLESS_HDF5_SUBJECT_SHARDS | PRIVATE | dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1 | SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD |
| P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | Kaggle | csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108 | 1 | 2 | LOSSLESS_HDF5_MATCHED_3P5S_SUBJECT_SHARDS_WITH_REGISTERED_VIRTUAL_MULTIWINDOW_VIEWS | PRIVATE | 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305 | A4_SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD |

The official core Dataset remains immutable/reused; the A4 Dataset is a separate alternative-window substrate. Neither may be silently regenerated or substituted by a downstream consumer.

---

# PART X — CUMULATIVE LIMITATION AND EVIDENCE-CEILING REGISTER

| Limitation ID | Scope | Origin | Description | Evidence consequence | Claim consequence | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P00-ENGINEERING-FOUNDATION-ONLY | P00 | P00 | P00 evidence is Mode-B engineering/retrospective foundation evidence and contains no empirical claim-bearing cell. | ENGINEERING_FOUNDATION_CONFORMANCE only | No scientific effectiveness claim | ACTIVE_HISTORICAL_LIMIT |
| P00-PORTABLE-LOCK-INCOMPLETE | P00 | P00 | Portable registry-resolved cross-version uv.lock incomplete; exact verified Python 3.13.5 runtime lock available. | Cross-version portability not proven | No effect on P00 engineering validation already executed | NONBLOCKING |
| PUBLIC_EEG_ONLY | P01 | P01 | P01 uses selected public EEG datasets only. | Bounds P01 evidence interpretation/reproduction | Must be inherited by downstream claim/evidence products | ACTIVE |
| NON_CLINICAL | P01 | P01 | P01 evidence is non-clinical research data/protocol evidence. | Bounds P01 evidence interpretation/reproduction | Must be inherited by downstream claim/evidence products | ACTIVE |
| NO_DEPLOYMENT_CLAIM | P01 | P01 | P01 does not establish deployment safety/effectiveness. | Bounds P01 evidence interpretation/reproduction | Must be inherited by downstream claim/evidence products | ACTIVE |
| PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS | P01 | P01 | Core and A4 numerical datasets require private Kaggle access and exact revision/hash verification. | Bounds P01 evidence interpretation/reproduction | Must be inherited by downstream claim/evidence products | ACTIVE |
| A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | P01 | P01 | A4 R2 emerged from feasibility repair and is future-confirmatory only; no P01 effectiveness result. | Bounds P01 evidence interpretation/reproduction | Must be inherited by downstream claim/evidence products | ACTIVE |
| ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT | P01 | P01 | Accepted P01 execution used Python 3.12.13 under documented compatibility amendment. | Bounds P01 evidence interpretation/reproduction | Must be inherited by downstream claim/evidence products | ACTIVE |
| ADAPTIVE_DISK_RESOURCE_AMENDMENT | P01 | P01 | Accepted P01 execution used adaptive disk policy rather than original 60 GiB preflight. | Bounds P01 evidence interpretation/reproduction | Must be inherited by downstream claim/evidence products | ACTIVE |

## Cumulative evidence ceilings

- **P00:** engineering-foundation conformance only; no empirical scientific-effectiveness claim.
- **P01:** provenance, intake correctness, labels/exclusions, split/leakage integrity, preprocessing/window materialization, quality, lineage, denominator closure, external persistence and downstream readiness.
- **Not established through P01:** decoder superiority, calibration benefit, A4 effectiveness, clinical benefit, deployment safety, policy-learning benefit, stress robustness, temporal-trust benefit, embodiment/control effectiveness.
- Layer 0, not this Protocol, later approves/qualifies/blocks claim wording.

---

# PART XI — DOWNSTREAM ANALYSIS AND PHASE HANDOFF CONTRACTS

## Phase 1 Evidence, Results, and Interpretation Report

May consume this Protocol, the accepted P01 execution bundle, the embedded analysis contract and exact run identities. It owns comprehensive results/findings/interpretation/candidate claims. It may not alter this Protocol retrospectively.

## Layer 0

Consumes evidence ceilings, limitations and stable evidence identities. It owns claim approval/qualification/blocking and may not change measurements.

## Evidence Map

Consumes stable run/record/artifact IDs and Layer-0 dispositions to map claims to evidence/manuscript locations. It does not redefine Protocol contracts.

## Layer 10

Consumes read-only governed records/manifests/results. It renders cards/tables/figures/reproducibility views and must never hide negative/diagnostic evidence or recompute hidden experimental logic.

## P01 → P02 technical consumption contract

P02 may consume the exact verified core Dataset pointer and, for A4 only under an explicit downstream Protocol/analysis cell, the exact A4 R2 Dataset/profile. It must inherit the canonical label maps, subject split, preprocessing, window profiles, config identity, parent-event matching keys and limitations. It is explicitly prohibited from silent relabeling, rewindowing, split mutation, test leakage, denominator substitution or A4 profile substitution. Any such change requires a governed amendment and descendant invalidation/rerun assessment.

## Forward rule for future phases

**P02 and every later phase extend this same cumulative Protocol v1.0 document.** Phase-specific content remains clearly sectioned internally, but no future phase creates a competing separately authoritative Protocol file. Historical revisions may be archived by content hash. Only one current Protocol revision is authoritative at a time.

---

# APPENDIX A — STRUCTURED PROTOCOL METADATA

The YAML block below is authoritative structured content embedded in the same canonical document.

```yaml
protocol_id: IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1
version: 1.0-CUM-P01-R1
authority_representation: SINGLE_CANONICAL_DOCUMENT
status: FROZEN
generation_timestamp: '2026-08-08T00:11:00+03:30'
phases_represented:
- P00
- P01
current_governance: V6.1_SINGLE_TRACK
scientific_contract_changed_by_consolidation: false
historical_execution_changed: false
phase_identity_changed: false
ablation_identity_changed: false
analysis_rules_silently_removed: false
traceability_reduced: false
authority_representation_consolidated: true
predecessor_protocol_components:
- id: IHARQ-PROTOCOL-V1-MASTER-R3
  role: PROJECT_WIDE_PREDECESSOR_COMPONENT
  status: HISTORICAL_SOURCE_AFTER_CONSOLIDATION
- id: IHARQ-PROTOCOL-V1-P00-ANNEX-R2
  role: P00_PREDECESSOR_COMPONENT
  status: PRESERVED_INTERNAL_PHASE_SECTION
- id: IHARQ-PROTOCOL-V1-P01-ANNEX-R1
  role: P01_PREDECESSOR_COMPONENT
  status: PRESERVED_INTERNAL_PHASE_SECTION
p01:
  scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
  config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
  execution_status: ACCEPTED
  unresolved_blockers: 0
future_rule: P02_AND_LATER_EXTEND_THIS_SAME_CUMULATIVE_PROTOCOL_DOCUMENT
```

# APPENDIX B — STRUCTURED CUMULATIVE RUN MATRIX

```yaml
run_matrix_id: IHARQ-PROTOCOL-V1-CUMULATIVE-RUN-MATRIX-THROUGH-P01-R1
schema_version: 1.0-through-p01-r1
generated_at: '2026-08-08T00:11:00+03:30'
current_workflow: V6.1_SINGLE_TRACK
preserved_p00:
  source_run_matrix_id: P00-PV1-ENGINEERING-RUN-MATRIX-R2
  historical_master_protocol_id: IHARQ-PROTOCOL-V1-MASTER-R2
  historical_annex_id: IHARQ-PROTOCOL-V1-P00-ANNEX-R2
  historical_timing_mode: B
  preserved_cells:
  - cell_id: P00-CELL-AUTHORITY-INTAKE
    purpose: Verify authority/source identities and requirement disposition
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - manifests/authority_manifest.yaml
    - catalogs/final_requirement_ledger.csv
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - manifests/authority_manifest.yaml
    - catalogs/final_requirement_ledger.csv
    command: python scripts/run_local_first_finalization_audit.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: All authority hashes resolve; requirement ledger has no missing applicable disposition
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-SCHEMA-COVERAGE
    purpose: Validate JSON Schema and record-family coverage
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - catalogs/final_schema_catalog.yaml
    - schemas/
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - catalogs/final_schema_catalog.yaml
    - schemas/
    command: python scripts/run_static_checks.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: All schemas parse and catalog references resolve
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-CONFIG-RESOLUTION
    purpose: Resolve strict P00 configuration
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - configs/project.yaml
    - configs/phases/p00.yaml
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - configs/project.yaml
    - configs/phases/p00.yaml
    command: python -m iharq.cli phase validate-inputs --phase P00 --profile configs/phases/p00.yaml
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Strict configuration validates; phase identity matches P00
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-IDENTITY-JCS-HASH
    purpose: Validate typed IDs, canonical serialization, SHA-256 and golden vectors
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - src/iharq/canonical.py
    - src/iharq/ids.py
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - src/iharq/canonical.py
    - src/iharq/ids.py
    command: python -m pytest -q tests/test_canonical.py tests/test_lineage_lifecycle.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: All deterministic identity/hash tests pass
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-VALID-FIXTURES
    purpose: Accept all valid and integrated non-empirical fixtures
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - fixtures/valid/
    - fixtures/integrated/
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - fixtures/valid/
    - fixtures/integrated/
    command: python -m pytest -q tests/test_valid_fixtures.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Every registered valid/integrated bundle passes
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-MALFORMED-FIXTURES
    purpose: Reject the complete malformed taxonomy
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - fixtures/invalid/
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - fixtures/invalid/
    command: python -m pytest -q tests/test_negative_fixtures.py tests/test_audit1_negative_fixtures.py tests/test_audit2_negative_fixtures.py
      tests/test_audit3_negative_fixtures.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Every malformed category produces a deterministic failure
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-VALIDATOR-TEST-COVERAGE
    purpose: Run complete deterministic suite
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - tests/
    - catalogs/final_validator_catalog.yaml
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - tests/
    - catalogs/final_validator_catalog.yaml
    command: python -m pytest -q -p no:cacheprovider
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Complete suite passes with no hidden deselection
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-A0-A13-READINESS
    purpose: Verify A0-A13 readiness and reject A14
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - catalogs/final_ablation_readiness_matrix.yaml
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - catalogs/final_ablation_readiness_matrix.yaml
    command: python scripts/run_phase0_final_implementation_audit.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: A0-A13 foundation hooks complete; A14 rejected
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-L0-L3-INTEGRATION
    purpose: Verify L0-L3 integration foundation
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - fixtures/integrated/layers_0_3_official_audit.json
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - fixtures/integrated/layers_0_3_official_audit.json
    command: python scripts/run_official_layer_audit_1.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Audit 1 regression passes
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-POLICY-UPDATE
    purpose: Verify update-enabled policy traceability
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - fixtures/integrated/update_enabled_official_audit2.json
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - fixtures/integrated/update_enabled_official_audit2.json
    command: python scripts/run_official_layer_audit_2.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Update trace, before/after policy IDs, reward/config/seed and limitations preserved
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-FROZEN-EVALUATION
    purpose: Verify frozen-evaluation immutability
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - fixtures/integrated/frozen_evaluation_official_audit2.json
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - fixtures/integrated/frozen_evaluation_official_audit2.json
    command: python scripts/run_official_layer_audit_2.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: No mutation; disabled-update evidence and mode warning present
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-L8-STRESS-LINEAGE
    purpose: Verify clean-to-stressed lineage and limitations
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - fixtures/integrated/stress_lineage_official_audit3.json
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - fixtures/integrated/stress_lineage_official_audit3.json
    command: python scripts/run_official_layer_audit_3.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Stress lineage and matching pass
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-L9-EMBODIMENT-PROXY
    purpose: Verify simulation-only embodiment proxy contracts
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - fixtures/integrated/embodiment_proxy_official_audit3.json
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - fixtures/integrated/embodiment_proxy_official_audit3.json
    command: python scripts/run_official_layer_audit_3.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Proxy limitations and safety/reward lineage pass
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-L10-READ-ONLY
    purpose: Verify Layer 10 source-only behavior
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - fixtures/integrated/layer10_readonly_official_audit3.json
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - fixtures/integrated/layer10_readonly_official_audit3.json
    command: python scripts/run_official_layer_audit_3.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: No upstream mutation, rematching, retuning, claim approval or primary evidence creation
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-MANIFEST-RECONCILIATION
    purpose: Regenerate and compare repository manifest
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - manifests/repository_file_manifest.json
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - manifests/repository_file_manifest.json
    command: python scripts/reconcile_repository_manifest.py && python scripts/reconcile_repository_manifest.py --check
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Manifest matches governed tree after transient exclusions
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-LOCAL-REPRODUCTION
    purpose: Reproduce from clean isolated local copy
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - requirements-lock.txt
    - reports/phase_00/local_clean_reproduction_R1.json
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - requirements-lock.txt
    - reports/phase_00/local_clean_reproduction_R1.json
    command: python scripts/run_local_reproduction.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Isolated reproduction passes using exact verified local dependency closure
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-PACKAGE-INTEGRITY
    purpose: Build and verify repository-ready archive
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - manifests/package_file_manifest.json
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - manifests/package_file_manifest.json
    command: python -m iharq.cli package build --output protocol_package_test.zip && python -m iharq.cli package verify --archive
      protocol_package_test.zip
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Archive CRC, file count and hashes reconcile
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-FUTURE-PHASE-CONTRACTS
    purpose: Verify P00-P15 reusable contracts and L0-L10 foundations
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - catalogs/final_all_phase_artifact_contract_matrix.yaml
    - catalogs/final_all_layer_artifact_matrix.yaml
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - catalogs/final_all_phase_artifact_contract_matrix.yaml
    - catalogs/final_all_layer_artifact_matrix.yaml
    command: python scripts/run_phase0_final_implementation_audit.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: All phase contracts and layer foundations have complete dispositions
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  - cell_id: P00-CELL-NEXT-DOCUMENT-READINESS
    purpose: Verify six downstream readiness packages
    authority_sources:
    - Governance V4
    - Build Book R3/R5
    - Protocol R42 as applicable
    input_identities:
    - docs/readiness/phase_00/
    environment_identity: P00-LOCAL-ENVIRONMENT-LOCK-REPORT-R1
    config_identity: configs/phases/p00.yaml
    fixture_test_identities:
    - docs/readiness/phase_00/
    command: python scripts/run_local_first_finalization_audit.py
    expected_outputs:
    - durable local report/log
    - deterministic exit status
    pass_criteria: Six readiness packages exist and are clearly non-final
    invalidity_rules:
    - nonzero exit
    - missing expected artifact
    - manifest/hash mismatch
    - unexpected source mutation
    evidence_status: ENGINEERING_RETROSPECTIVE_MODE_B
    limitations:
    - NON_EMPIRICAL
    - NON_CLAIM_BEARING
    rerun_rule: Rerun after any affected source/config/schema/test/manifest change
  source_file_sha256: 9dfc032f8f6bc05164b6c7f3e038a8ac5b43c56906adddc255fd8c8cf0918054
p01:
  annex_id: IHARQ-PROTOCOL-V1-P01-ANNEX-R1
  execution_status: ACCEPTED
  cells:
  - cell_id: P01-STAGE-00
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids: []
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Corrected bootstrap and persistent isolated worker
    expected_outputs:
    - authority_manifest.json
    actual_outputs:
    - authority_manifest.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-01
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids: []
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Environment
    expected_outputs:
    - environment_manifest.json
    actual_outputs:
    - environment_manifest.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-02
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids: []
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Project and input intake
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-03
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids: []
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Authority and configuration
    expected_outputs:
    - config_snapshot/official_run_freeze_manifest.json
    actual_outputs:
    - config_snapshot/official_run_freeze_manifest.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-04
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids: []
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Phase 0 regression
    expected_outputs:
    - reports/phase_01/tests/phase0_and_runtime_regression.json
    actual_outputs:
    - reports/phase_01/tests/phase0_and_runtime_regression.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-05
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids: []
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Source resolution
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-06
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids: []
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Dataset registry
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-07
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids: []
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: 'Pass 1: verified source acquisition and bounded loading'
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history:
    - R49 local stale revision guard failed before worker submission
    - R50 same-session continuation submitted Stage 07 once; PASS
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-08
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids: []
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Metadata normalization
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-09
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: NOT_APPLICABLE
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Label mapping
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-10
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: NOT_APPLICABLE
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Preprocessing compilation
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-11
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: 20260804
    budget: NOT_APPLICABLE
    command_or_stage: Split construction and frozen fit population
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-12
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: 20260804
    budget:
    - 1
    - 2
    - 4
    - 8
    - 16
    - 32
    command_or_stage: Low-calibration budgets
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-13
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: NOT_APPLICABLE
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: 'Pass 2A: bounded preprocessing fit'
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-14
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: A4
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Adopt verified core and materialize matched A4 R2
    expected_outputs:
    - external_artifact_pointers/derived_windows_dataset.json
    - reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json
    actual_outputs:
    - external_artifact_pointers/derived_windows_dataset.json
    - reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history:
    - R45 canonical record-ID normalization episode and later R48/R49 A4 implementation/profile repairs; accepted Stage 14
      materialized A4 R2 while core was adopted unchanged
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-15
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: A4
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Validate and commit the separate A4 R2 Dataset
    expected_outputs:
    - external_artifact_pointers/derived_windows_dataset.json
    - external_artifact_pointers/a4_window_family_dataset.json
    actual_outputs:
    - external_artifact_pointers/derived_windows_dataset.json
    - external_artifact_pointers/a4_window_family_dataset.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history:
    - A4 persistence/remote manifest validation after R48/R49 hardening; PASS
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-16
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Record validation
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-17
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Leakage audit
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-18
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: A4
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: A0–A13 readiness
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history:
    - Original missing-module failure; R51/R52 recovery-cell defects; R53 worker-env import repair; PASS
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-19
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Cards
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-20
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Manifests
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-21
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Negative register
    expected_outputs:
    - negative_and_failed_results/run_failures_and_blockers.json
    actual_outputs:
    - negative_and_failed_results/run_failures_and_blockers.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-22
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: P02 and later compatibility
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-23
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Evidence sufficiency
    expected_outputs:
    - reports/phase_01/preliminary_gate_evaluation.json
    actual_outputs:
    - reports/phase_01/preliminary_gate_evaluation.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-24
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Repair metadata
    expected_outputs:
    - reports/phase_01/repair_reentry.json
    actual_outputs:
    - reports/phase_01/repair_reentry.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-25
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Final export preparation
    expected_outputs: []
    actual_outputs: []
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history: []
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
  - cell_id: P01-STAGE-26
    phase_id: P01
    layer_id: L1
    evaluation_mode: EM-OFFLINE
    scientific_freeze: P01-L1-OFFICIAL-RUN-FREEZE-R2
    config_id: d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f
    source_snapshot_id: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
    environment_id: P01-L1-KAGGLE-ENV-FREEZE-R5
    input_artifact_ids: []
    external_pointer_ids:
    - P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
    - P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
    dataset_ids:
    - PhysioNetMI
    - BNCI2014_001
    - Lee2019_MI
    split_id: IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    label_map_ids:
    - IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9
    - IHARQ-LABELMAPRECORD-20260806-587dcfff81307768
    - IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c
    preprocessing_id: IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08
    window_profile_id: P01-L1-WINDOW-OFFICIAL-R2
    ablation_id: NOT_APPLICABLE
    seed: NOT_APPLICABLE
    budget: NOT_APPLICABLE
    command_or_stage: Terminal decision and bundle export
    expected_outputs:
    - /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip
    - /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip.sha256
    - /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_GitHub_Ready_Repository_d03f0a7c869d_20260807143013-663eab13.zip
    - /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_GitHub_Ready_Repository_d03f0a7c869d_20260807143013-663eab13.zip.sha256
    - reports/phase_01/repository_release_plan.json
    actual_outputs:
    - /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip
    - /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip.sha256
    - /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_GitHub_Ready_Repository_d03f0a7c869d_20260807143013-663eab13.zip
    - /kaggle/working/iharq_p01_l1/IHARQ_P01_L1_GitHub_Ready_Repository_d03f0a7c869d_20260807143013-663eab13.zip.sha256
    - reports/phase_01/repository_release_plan.json
    status: PASS
    evidence_class: ENGINEERING_DATA_PROTOCOL_FOUNDATION
    validity: VALID_FINAL_ACCEPTED_LINEAGE
    failure_or_exclusion_rule: FAIL_CLOSED; preserve failed evidence; rerun only affected scope
    limitations:
    - PUBLIC_EEG_ONLY
    - NON_CLINICAL
    - NO_DEPLOYMENT_CLAIM
    rerun_history:
    - Original worker packaging BLOCKED by secret scan; R54 repack/redaction repaired external release without duplicating
      Stage 26; final canonical stage record PASS
    downstream_consumers:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
    - Layer 10
    - P02
canonical_protocol_id: IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1
```

# APPENDIX C — STRUCTURED CUMULATIVE ANALYSIS CONTRACT

```yaml
analysis_contract_id: IHARQ-PROTOCOL-V1-CUMULATIVE-ANALYSIS-CONTRACT-THROUGH-P01-R1
schema_version: 1.0-through-p01-r1
generated_at: '2026-08-08T00:11:00+03:30'
preserved_p00:
  source_analysis_contract_id: P00-PV1-ENGINEERING-ANALYSIS-CONTRACT-R2
  historical_master_protocol_id: IHARQ-PROTOCOL-V1-MASTER-R2
  historical_annex_id: IHARQ-PROTOCOL-V1-P00-ANNEX-R2
  exact_predecessor:
    analysis_contract_id: P00-PV1-ENGINEERING-ANALYSIS-CONTRACT-R2
    phase_id: P00
    analysis_type: DETERMINISTIC_ENGINEERING_FOUNDATION
    allowed_analyses:
    - analysis_id: P00-AN-ARTIFACT-COVERAGE
      inventory: expected/discovered/validated/failed/excluded/invalid/accepted artifacts
      method: exact counts and path reconciliation
    - analysis_id: P00-AN-SCHEMA-CONFIG
      inventory: schemas/configs/record families
      method: catalog-to-file-to-validator coverage
    - analysis_id: P00-AN-FIXTURE-RESULTS
      inventory: valid/integrated/malformed fixtures
      method: pass/reject counts with explicit denominator
    - analysis_id: P00-AN-TEST-GATES
      inventory: tests/validators/gates
      method: deterministic result and gate evidence crosswalk
    - analysis_id: P00-AN-INTEGRATION
      inventory: L0-3, L3-7, L7-10, update, frozen, stress, embodiment, L10
      method: identity/lineage/limitation preservation
    - analysis_id: P00-AN-REPRODUCTION
      inventory: runtime lock, environment snapshot, clean reproduction and package integrity
      method: exact hashes and exit codes
    prohibited_analyses:
    - scientific superiority
    - treatment effects
    - p-values
    - clinical endpoints
    - model/calibration/stress/simulator performance claims
    denominator_fields:
    - expected
    - discovered
    - validated
    - failed
    - excluded
    - invalid
    - accepted
    missingness_rule: Missing inventory items remain missing/invalid; never converted to zero-success
    negative_result_rule: Preserve all failures and repaired evidence; do not hide or overwrite
    release_status: REGISTERED_FOR_FUTURE_PHASE_ANALYSIS_NOT_EXECUTED_IN_THIS_PROTOCOL_CREATION_TASK
    master_protocol_id: IHARQ-PROTOCOL-V1-MASTER-R2
    annex_id: IHARQ-PROTOCOL-V1-P00-ANNEX-R2
  source_file_sha256: 0a1a498ab5408b31809ce09def94bcd4c34f7def20e11ce46ac15a37e4e998fd
p01:
  annex_id: IHARQ-PROTOCOL-V1-P01-ANNEX-R1
  analysis_type: DETERMINISTIC_DATA_PROTOCOL_AND_REPRODUCIBILITY_CLOSURE
  inferential_statistics: NOT_APPLICABLE_IN_P01; no p-values/CIs invented
  analyses:
  - analysis_id: P01-AC-001-SOURCE-INVENTORY
    analysis: Source inventory, provenance, license and checksum reconciliation
    inputs:
    - DatasetRecords
    - source inventory
    - source version/license report
    statistical_unit: source file/dataset
    denominator: all activated source files/datasets
    aggregation: counts and exact hash reconciliation
    expected_outputs:
    - source inventory reconciliation table
    interpretation_ceiling: data provenance/reproducibility only
    invalidity_rules:
    - missing required source identity or checksum blocks admission
    missingness_rules:
    - missing remains missing/invalid, never zero-success
    downstream_use:
    - Phase 1 Report
    - Evidence Map
    - P02
  - analysis_id: P01-AC-002-SPLIT
    analysis: Subject-group split allocation and disjointness
    inputs:
    - IHARQ-SPLITRECORD-20260806-e4e371d332c61e36
    - window records
    statistical_unit: subject group and derived window
    denominator: all admitted subjects and accepted core windows
    aggregation: role counts by dataset and global
    expected_outputs:
    - subject/window role count tables
    - disjointness status
    interpretation_ceiling: split/leakage correctness only
    invalidity_rules:
    - any subject intersection across roles blocks
    missingness_rules:
    - unassigned subject is invalid
    downstream_use:
    - Phase 1 Report
    - P02
  - analysis_id: P01-AC-003-DENOMINATOR
    analysis: Accepted event/window denominator conservation
    inputs:
    - WindowRecords
    - window timing report
    statistical_unit: accepted source event
    denominator: 12,910 accepted parent events
    aggregation: expected/discovered/valid window counts by dataset/role
    expected_outputs:
    - 12,910/12,910 core closure
    - 0 invalid windows
    interpretation_ceiling: data-materialization closure only
    invalidity_rules:
    - missing/duplicate/out-of-bounds window invalidates denominator row
    missingness_rules:
    - never impute missing event/window
    downstream_use:
    - Phase 1 Report
    - P02
  - analysis_id: P01-AC-004-QUALITY
    analysis: Quality/validation closure
    inputs:
    - ArtifactFlagRecords
    - quality coverage
    - validation reports
    statistical_unit: quality summary/window
    denominator: 489
    aggregation: flag/hard-invalid counts by dataset
    expected_outputs:
    - quality summary counts
    interpretation_ceiling: quality annotation/validity only
    invalidity_rules:
    - hard invalid not admitted to valid denominator
    missingness_rules:
    - missing quality evidence blocks quality-available claim
    downstream_use:
    - Phase 1 Report
    - Layer 0
  - analysis_id: P01-AC-005-LEAKAGE
    analysis: Leakage and visibility checks
    inputs:
    - split record
    - leakage contamination report
    - budget registry
    statistical_unit: subject/event/window/budget membership
    denominator: all assigned groups/windows/budget identities
    aggregation: deterministic boolean checks
    expected_outputs:
    - PASS/issue ledger
    interpretation_ceiling: absence of detected contract leakage under implemented checks
    invalidity_rules:
    - any contamination blocks gate
    missingness_rules:
    - missing join key fails closed
    downstream_use:
    - Phase 1 Report
    - P02
  - analysis_id: P01-AC-006-EXTERNAL
    analysis: External artifact persistence and integrity
    inputs:
    - core pointer
    - A4 pointer
    - manifests
    - checksums
    statistical_unit: external artifact/shard/index
    denominator: declared governed artifacts
    aggregation: version/hash/size/count reconciliation
    expected_outputs:
    - external pointer audit
    interpretation_ceiling: reproducible retrieval/integrity only
    invalidity_rules:
    - unverified revision/hash blocks consumption
    missingness_rules:
    - handle without immutable identity/checksum insufficient
    downstream_use:
    - P02
    - Layer 10
  - analysis_id: P01-AC-007-ABLATION-READINESS
    analysis: A0-A13 foundation readiness and A14 absence
    inputs:
    - layer1_ablation_readiness_l1_v1.json
    statistical_unit: ablation identity
    denominator: exact A0-A13 set (14 identities)
    aggregation: readiness disposition per identity
    expected_outputs:
    - 14 readiness rows
    - A14 absence PASS
    interpretation_ceiling: foundation readiness only; no effectiveness
    invalidity_rules:
    - missing A0-A13 row or any A14 selector/run/result/claim blocks
    missingness_rules:
    - missing readiness row is not NOT_APPLICABLE unless owner authority says so
    downstream_use:
    - Phase 1 Report
    - future phase annexes
  - analysis_id: P01-AC-008-A4
    analysis: A4 R2 data-substrate synchronization/feasibility accounting
    inputs:
    - A4 pointer
    - A4 R2 freeze
    - historical feasibility evidence
    statistical_unit: parent event / registered A4 view
    denominator: 12,910 core parent events
    aggregation: matched counts/profile identity/feasibility boundary
    expected_outputs:
    - 12,910 matched longer views
    - 38,730 virtual members
    - protocol sync audit
    interpretation_ceiling: future A4 substrate readiness; NOT A4 effectiveness
    invalidity_rules:
    - drop/pad/clip/fabricate parent event; profile drift; claim A4 executed in P01
    missingness_rules:
    - unavailable extra samples prohibit the infeasible profile rather than padding
    downstream_use:
    - future P02 A4 execution
  - analysis_id: P01-AC-009-ENVIRONMENT
    analysis: Environment and reproducibility amendment reconciliation
    inputs:
    - environment manifest
    - environment amendment
    - adaptive disk policy
    statistical_unit: execution environment/profile
    denominator: one accepted P01 execution environment
    aggregation: exact versions/resources/amendment classifications
    expected_outputs:
    - environment amendment audit
    interpretation_ceiling: execution reproducibility only
    invalidity_rules:
    - unrecorded freeze-critical environment drift blocks
    missingness_rules:
    - unknown freeze-critical package version is unresolved
    downstream_use:
    - Phase 1 Report
    - reproduction
  - analysis_id: P01-AC-010-GATES-REPAIRS
    analysis: Gate closure and failed/superseded attempt accounting
    inputs:
    - P01-G01..G16
    - notebook outputs
    - repair ledgers
    - R54 evidence
    statistical_unit: gate/stage/repair episode
    denominator: 16 gates; 27 accepted stages; all material repair episodes
    aggregation: status/blocker/repair classification
    expected_outputs:
    - gate table
    - repair ledger
    - 0 unresolved blockers
    interpretation_ceiling: execution closure only
    invalidity_rules:
    - hidden material failure; blocker; checksum/security failure
    missingness_rules:
    - unexplained failed attempt is unresolved
    downstream_use:
    - Phase 1 Report
    - Layer 0
    - Evidence Map
  global_negative_rule: Preserve failed, invalid, unmatched, negative and diagnostic evidence; never convert missing to zero-success.
  global_no_posthoc_rule: No result-dependent relabeling, denominator changes, source replacement or retrospective preregistration;
    A4 R2 foundation is not effectiveness evidence.
  release_status: FROZEN_FOR_PHASE_1_REPORT_ANALYSIS
canonical_protocol_id: IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1
```

# APPENDIX D — STRUCTURED CUMULATIVE ABLATION REGISTER

```yaml
register_id: IHARQ-PROTOCOL-V1-CUMULATIVE-ABLATION-REGISTER-THROUGH-P01-R1
canonical_protocol_id: IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1
entries:
- ablation_id: A0
  official_identity: Raw Decoder / Accept-All Raw Decoder Reference
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A1
  official_identity: Calibrated Decoder / Calibration Visibility
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A2
  official_identity: Simple Registered Threshold / Confidence-Threshold Baseline
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A3
  official_identity: Uncertainty and Selective Prediction
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A4
  official_identity: Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: A4_R2_FUTURE_CONFIRMATORY_ONLY; R1_4S_PROFILE_INFEASIBLE
- ablation_id: A5
  official_identity: IHARQ-lite / Rule-Based Evidence Verification
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A6
  official_identity: IHARQ + Evidence-Quality Estimator
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A7
  official_identity: IHARQ + RegimeRisk Temporal Trust
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A8
  official_identity: Learning-to-defer / Deferral Comparison
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A9
  official_identity: Supervised Adaptive-IHARQ / Adaptive Readiness Policy
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A10
  official_identity: Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A11
  official_identity: Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A12
  official_identity: StressForge Stress Tests / Controlled Stress Robustness
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
- ablation_id: A13
  official_identity: Layer 9 Simulation-Only Embodiment Demo
  owner: DOWNSTREAM_AUTHORITY
  p00_disposition: FOUNDATION_IDENTITY_ONLY; NOT_ACTIVE; NO_EMPIRICAL_CELL
  p01_foundation_status: FOUNDATION_READY
  activated_in_p01: false
  executed_in_p01: false
  downstream_phase: P02-P15
  missing_key_behavior: NOT_READY_OR_DIAGNOSTIC_ONLY
  limitation: FOUNDATION_READINESS_IS_NOT_EFFECTIVENESS_EVIDENCE
a14:
  status: PROHIBITED_ABSENT
  selector: false
  run: false
  result: false
  claim: false
```

# APPENDIX E — STRUCTURED EXTERNAL ARTIFACT REGISTER

```yaml
register_id: IHARQ-PROTOCOL-V1-CUMULATIVE-EXTERNAL-ARTIFACT-REGISTER-THROUGH-P01-R1
canonical_protocol_id: IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1
entries:
- artifact_id: P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473
  provider: Kaggle
  handle: csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473
  provider_dataset_version: 2
  logical_revision: 1
  manifest_sha256: dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1
  format: LOSSLESS_HDF5_SUBJECT_SHARDS
  access: PRIVATE
  local_copy_status: SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD
  producer_phase: P01
  consumer_phases:
  - P02-P15
  validity: VALID_VERIFIED_POINTER
- artifact_id: P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13
  provider: Kaggle
  handle: csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108
  provider_dataset_version: 1
  logical_revision: 2
  manifest_sha256: 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305
  format: LOSSLESS_HDF5_MATCHED_3P5S_SUBJECT_SHARDS_WITH_REGISTERED_VIRTUAL_MULTIWINDOW_VIEWS
  access: PRIVATE
  local_copy_status: A4_SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD
  producer_phase: P01
  consumer_phases:
  - P02-P15
  validity: VALID_VERIFIED_POINTER
```

# APPENDIX F — SOURCE / AUTHORITY UTILIZATION MATRIX

| Source | Authority role | Reviewed? | Relevant requirements | Protocol locations | Conflicts found | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Governance V6.1 | current workflow/document governance | YES | single-track, evidence sufficiency, repair loop, post-execution Protocol, ZIP-first, no quality reduction | Parts I, VII, XI; freeze controls | old timing/workflow modes superseded | current V6.1 rules control; history preserved | USED |
| Seven governing authorities package | Architecture/Registry/Execution Plan/Protocol v0.1/Playbook/Method/Nuts-and-Bolts | YES | all project/P00/P01 protocol-relevant rules | Parts I-III, VI, X-XI | scope-owner conflicts routed by authority ownership | no silent merge; controlling owner retained | USED |
| Phase 0 Protocol v1.0 Master R2 | direct P00 project-wide predecessor | YES | project-wide Protocol rules and historical Mode-B/timing machinery | Part I history + supersession register | V6.1 supersedes timing/workflow machinery, not scientific/engineering meaning | R2 archived by hash; valid rules carried into current project-wide section | USED |
| Phase 0 Protocol v1.0 Annex R2 | direct P00 phase protocol predecessor | YES | P00 exact identity, scope, engineering run matrix, analysis contract, evidence ceiling, no empirical cells | Part II; Parts IV-V | historical timing terminology differs from current workflow | P00 text preserved verbatim; terminology labelled historical | USED |
| Phase 0 Protocol v1.0 run matrix R2 | P00 machine predecessor | YES | 19 deterministic engineering cells | Part IV; Appendix B | none | preserved inside cumulative matrix | USED |
| Phase 0 Protocol v1.0 analysis contract R2 | P00 machine predecessor | YES | 6 deterministic engineering analyses; prohibited scientific analyses | Part V; Appendix C | none | preserved inside cumulative analysis contract | USED |
| Phase 0 full implementation/execution repository | upstream inherited engineering state | YES | schemas, IDs, hashing, validators, handoffs, limitations | Parts I-II, XI | none material unresolved | reuse; no P00 rerun | USED |
| Phase 1 Implementation Build Book package | P01 pre-run executable intent | YES | datasets, labels, split, budgets, preprocessing, windows, quality, environment intent, gates, persistence | Part III | Python/disk/A4 actual execution differs on documented surfaces | preserve intended vs actual chronology | USED |
| Executed Phase 1 notebook | actual attempt/repair chronology | YES | Stages 00-26, failures, continuations, accepted lineage | Part III 36-39; Part VII | source code alone not success evidence | final bundle controls final status; notebook preserves chronology | USED |
| Final P01 execution bundle | primary actual P01 evidence | YES | records, gates, tests, pointers, A4, handoffs, R54, checksums | Parts III-IX, XI | none unresolved | execution-owned facts taken from final accepted bundle | USED |
| Protocol v1.0 through P01 predecessor package | immediate consolidation predecessor | YES | Master R3, P00/P01 annexes, cumulative run/analysis, ledgers, prior validation | all parts | fragmented authority representation conflicts with owner single-file decision | substantive content internalized; predecessor files historical/support only | USED |
| Owner master consolidation/finalization prompt | current task-level structural decision | YES | single canonical file, ten-pass audit, cross-phase/harmony, future same-file extension | document control, all cumulative parts, validation | changes distribution model only | document-structure consolidation; no scientific change | USED |

# APPENDIX G — CROSS-DOCUMENT CONSISTENCY MATRIX

| Cross-check | Surface | Required state | Observed/consolidated state | Status |
| --- | --- | --- | --- | --- |
| Governance ↔ Protocol | Workflow | V6.1 single-track; Protocol after sufficient execution | Current cumulative authority uses V6.1; historical Mode-B retained only as evidence classification | PASS |
| Architecture ↔ P01 | Phase/layer ownership | P01 Public Data and Split Protocol; L1 data/provenance/split/window readiness | P01 section owns no decoder-performance claims | PASS |
| Registry ↔ P01 | Record/lineage identities | DatasetRecord/LabelMap/Split/Preprocessing/Window/Validation identities | Exact canonical IDs retained; no dangling authority redefinition | PASS |
| Build Book ↔ execution | Intended vs actual | pre-run Python 3.11/60GiB/A4 proposal vs actual 3.12/adaptive disk/A4 R2 | Both preserved with explicit classifications | PASS |
| P00 ↔ P01 | Inheritance | P00 schemas/hashing/lineage/A0-A13/no-A14 foundation extended by P01 actual L1 records | P00 not rewritten; P01 extends | PASS |
| P01 narrative ↔ run matrix | Stage identity | 00-26 accepted final lineage | 27 P01 stage rows; failures in rerun history | PASS |
| P01 ↔ A4 | Chronology/evidence ceiling | R1 4s infeasible; R2 3.5s foundation ready; executed_in_p01=false | No A4 effectiveness claim | PASS |
| P01 ↔ external pointers | Persistence identity | core provider v2/logical rev1; A4 provider v1/logical rev2 | exact handles/revisions/manifest hashes | PASS |
| Protocol ↔ downstream products | Boundary | Protocol freezes contracts; Report interprets; L0 approves claims; Evidence Map maps; L10 renders | No downstream authority stolen | PASS |

# APPENDIX H — HUMAN / STRUCTURED NO-DRIFT VALIDATION

The finalization validator parses Appendices A–E directly from this Markdown and asserts the freeze-critical values against the narrative and source artifacts. Required equalities include: cumulative Protocol ID; P01 config/scientific freeze/status; dataset IDs; SplitRecord ID; PreprocessingRecord ID; core/A4 profile identities; exact A0–A13 set; A14 absence; actual Python 3.12.13; external Dataset handles/provider revisions/manifest hashes; 12,910 core denominator; 0 invalid core windows; 27 P01 stages; 16/16 P01 gates; 0 unresolved blockers.

**Required outcome:** `HUMAN_STRUCTURED_NO_DRIFT = PASS`.

# APPENDIX I — PROTOCOL FREEZE AND INTEGRITY MANIFEST

```yaml
protocol_id: IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1
version: 1.0-CUM-P01-R1
status: FROZEN
authority_representation: SINGLE_CANONICAL_DOCUMENT
generation_timestamp: '2026-08-08T00:11:00+03:30'
p00_annex_source_sha256: a0dbabfc1c5be739955696f8b5d32d9cdbdedf563a1c9225d9767599bbfbd7b5
historical_master_r2_sha256: 938fcaab2be30d2e59ccc5082a9c3cc6c2ccc3e8889b352099aa514b96e046d4
p01_execution_bundle_sha256: 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e
p01_execution_status: ACCEPTED
p01_unresolved_blockers: 0
a4_executed_in_p01: false
additional_p01_computation_required: false
next_documentary_output: Phase 1 Evidence, Results, and Interpretation Report
future_protocol_update_rule: EXTEND_SAME_CANONICAL_DOCUMENT
```

---

# FINAL FREEZE DECISION

**PROTOCOL_V1_SINGLE_CANONICAL_THROUGH_P01: PASS — FROZEN**

- Protocol authority: `SINGLE_CANONICAL_DOCUMENT`
- phases represented: P00, P01
- P00 preservation: PASS
- P01 integration: PASS
- inter-level harmony: PASS
- intra-level harmony: PASS
- cross-phase harmony: PASS
- authority conformance: PASS
- execution fidelity: PASS
- A0–A13: PASS
- A14 absence: PASS
- A4 R2 synchronization: PASS
- repair/rerun history: PASS
- environment amendments: PASS
- external artifacts: PASS
- human/structured no-drift: PASS
- secrets: PASS
- freeze-critical blockers: **0**
- additional P01 computation required: **NO**
- Phase 1 Report readiness: **READY**
- P02 technical contract readiness: **READY**, subject to the Governance V6.1 documentary closure sequence before formal phase transition.
