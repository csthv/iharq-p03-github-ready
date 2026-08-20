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
