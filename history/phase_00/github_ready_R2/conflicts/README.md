# IHARQ BenchGuard Stretch C

**IHARQ BenchGuard Stretch C** is a governed, layered research-engineering architecture for keeping implementation, evidence, claims, and presentation synchronized across a multi-phase reliability research programme.

> **Local package status:** `P00_GITHUB_MANUAL_PACKAGE_READY_WITH_NONBLOCKING_LIMITATIONS`. This tree was generated locally from the exact verified R5 advanced repository. It has not been uploaded to GitHub. `P0-GATE-18` remains `READY_TO_PASS_AFTER_VERIFIED_PUBLICATION`; Phase 0 is ready for publication and closure but is not formally closed; Phase 1 is ready but not authorized.

## 1. Research motivation

Complex research systems can appear reproducible while their implementation, evidence, claims, and presentation quietly drift apart. IHARQ separates these concerns into explicit authorities, records, interfaces, tests, claim ceilings, evidence maps, and read-only presentation products so that later empirical work can be reproduced and challenged without silently changing its meaning.

## 2. System overview

The repository defines a Phase 0 engineering foundation for a broader P00-P15 programme. It provides:

- stable package, schema, configuration, contract, identity, hashing, lineage, lifecycle, and manifest foundations;
- valid and malformed fixtures with fail-closed validation;
- explicit phase and layer responsibilities;
- Protocol, Analysis, Layer 0, Evidence Map, and Layer 10 handoff surfaces;
- a complete 18-document current Phase 0 reading set;
- deterministic local validation and clean reproduction.

## 3. Architecture at a glance

The project uses three coordinated axes:

- **phases P00-P15** define when work may occur;
- **layers L0-L10** define which subsystem owns each responsibility;
- **ablations A0-A13** define future controlled comparisons, while **A14 is rejected**.

The controlling architecture and authority stack are indexed in [docs/authorities/current/README.md](docs/authorities/current/README.md). A concise architecture guide is available at [docs/architecture/README.md](docs/architecture/README.md).

## 4. P00-P15 phase model

- **P00** establishes repository, configuration, record-schema, validation, and handoff foundations.
- **P01-P15** are later governed phases that may introduce data, models, calibration, policy, stress, embodiment, analysis, and publication work only after their entry conditions and Protocol annexes are frozen.

See [docs/future_phases/README.md](docs/future_phases/README.md) for the bounded future-phase interface.

## 5. L0-L10 layer model

- **L0:** claim safety and scope governance;
- **L1:** data and protocol foundations;
- **L2:** decoder/model interfaces;
- **L3:** calibration and uncertainty;
- **L4:** IHARQ evidence verification;
- **L5:** temporal trust / RegimeRisk;
- **L6:** readiness and deferral policy;
- **L7:** closed-loop policy foundations;
- **L8:** StressForge foundations;
- **L9:** embodiment/demo foundations;
- **L10:** reproducibility and read-only presentation.

The complete publication matrix is at [reports/phase_00/current_manifests/phase_0_layer_responsibility_matrix.csv](reports/phase_00/current_manifests/phase_0_layer_responsibility_matrix.csv).

## 6. Current Phase 0 publication scope

```yaml
phase_id: P00
phase_name: Repository, Configuration, and Record Schema
protocol_subtype: ADMINISTRATIVE_FOUNDATION
timing_mode: B
evidence_ceiling: ENGINEERING_FOUNDATION_CONFORMANCE
claim_bearing_empirical_cells: []
active_empirical_ablations: []
a0_to_a13_status: READINESS_ONLY_NOT_ACTIVATED
a14_status: REJECTED
publication_state: LOCAL_GITHUB_PACKAGE_READY
p0_gate_18: READY_TO_PASS_AFTER_VERIFIED_PUBLICATION
phase0: READY_FOR_PUBLICATION_AND_CLOSURE
phase1: READY_BUT_NOT_AUTHORIZED
```

## 7. What Phase 0 establishes

Phase 0 establishes the governed engineering foundation: package structure, schemas, configurations, canonical/local records, interfaces, stable IDs, serialization and hashing rules, lineage and lifecycle records, manifests, valid fixtures, malformed fail-closed fixtures, deterministic validators, layer/phase contracts, environment capture, and downstream handoffs.

## 8. What Phase 0 does not claim

Phase 0 does **not** establish model or decoder effectiveness, calibration improvement, uncertainty improvement, policy improvement, IHARQ effectiveness, RegimeRisk effectiveness, stress robustness, simulation or embodiment effectiveness, clinical validity, medical approval, deployment readiness, universal portability, or empirical ablation results.

## 9. Implementation highlights

- 30 directly browsable Python source files under `src/iharq/`;
- 85 JSON schemas;
- 35 configuration profiles;
- 32 phase-contract files covering P00-P15 inputs and outputs;
- 267 valid, integrated, and malformed fixtures in the clean public derivative;
- direct current authorities and the complete final-document distribution;
- GitHub CI is not a Phase 0 gate; validation is local-only and no GitHub-hosted result is claimed.

## 10. Current verification summary

The controlling R5 source archive is `IHARQ_Phase_0_Final_Whole_Stack_Independent_Double_Checked_Repository_COMPLETE_R5(2).zip`:

- SHA-256: `afac80fca6eb1fb52c24dc6914cb63bbd395b0f04e514640b7ee89e9cc12cab0`;
- size: `27,952,891` bytes;
- ZIP CRC: pass;
- source package manifest: **2,004/2,004** files verified;
- deterministic tests: **214/214** across three non-overlapping exit-clean shards (34 + 67 + 113);
- executable adversarial mutations: **39/39** pass;
- current final Markdown documents: **18/18** verified;
- verified runtime: Python **3.13.5** with the recorded 22-distribution dependency closure.

The clean derivative has its own public operational tests and clean-reproduction workflow. Results are recorded in [publication/local_build_report.md](publication/local_build_report.md) and the external local-validation report delivered with this package.

## 11. Fixture interpretation

- `fixtures/valid/` contains canonical accepted examples.
- `fixtures/integrated/` exercises cross-layer and handoff chains.
- `fixtures/invalid/` contains distinct malformed categories expected to fail closed.
- Fixture rejection is engineering evidence about validators; it is not empirical scientific evidence.

See [fixtures/README.md](fixtures/README.md).

## 12. A0-A13 readiness and A14 rejection

A0-A13 have Phase 0 foundation records and future Protocol-controlled activation requirements. None was activated or executed in P00, and no numerical ablation result is reported. A14 is rejected and has no accepted selector, Protocol cell, result, or claim. See [docs/phase_00/ablations/README.md](docs/phase_00/ablations/README.md).

## 13. Repository structure

- `src/iharq/` - implementation foundation;
- `schemas/`, `configs/`, `contracts/` - governed machine-readable interfaces;
- `fixtures/` and `tests/` - accepted and fail-closed verification surfaces;
- `scripts/` - local validation, packaging, and reproduction tools;
- `docs/authorities/current/` - controlling authority stack;
- `docs/phase_00/final_documents/` - complete 18-document current set;
- `reports/phase_00/` - current handoffs, manifests, and concise audit summaries;
- `manifests/` - publication, source-crosswalk, release, and checksum records;
- `provenance/` - full-archive identity and release instructions;
- `publication/` - local build and source-selection evidence.

## 14. Installation

The accepted local environment is Python 3.13.5. Python 3.11 and 3.12 remain unverified in the accepted environment.

```bash
python -m pip install -r requirements-lock.txt
python -m pip install -e . --no-deps --no-build-isolation
```

`uv.lock` is intentionally omitted because the source lock was incomplete/non-authoritative for portable reproduction.

## 15. Exact local validation commands

```bash
python scripts/verify_runtime_lock.py
python -m pytest -q -p no:cacheprovider
python scripts/verify_publication_tree.py
python scripts/run_local_reproduction.py --no-write-report
```

The CLI also exposes:

```bash
python -m iharq.cli local test
python -m iharq.cli local reproduce
```

## 16. Reproduction

Reproduction copies the repository to a clean temporary directory, performs a no-dependency editable install, runs the public operational suite, and verifies the publication manifest. See [docs/phase_00/reproduction/README.md](docs/phase_00/reproduction/README.md).

## 17. Final Phase 0 document index

The complete directly selectable reading set is at [docs/phase_00/final_documents/README.md](docs/phase_00/final_documents/README.md). It contains all 18 current files from the Build Book through the Phase 0-to-Phase 1 handoff.

## 18. Protocol, Analysis, Layer 0, Evidence Map, and Layer 10

- [Protocol](docs/protocol/README.md) controls evidence mode and future activation.
- [Analysis](docs/phase_00/analysis/README.md) reports observed Phase 0 engineering results without empirical inflation.
- [Layer 0](docs/phase_00/layer0/README.md) controls claim wording and limitations.
- [Evidence Map](docs/phase_00/evidence_map/README.md) links claims to evidence and outputs.
- [Layer 10](docs/phase_00/layer10/README.md) provides read-only presentation and reproduction views without recomputation.

## 19. Known limitations

- exact local verification is recorded for Python 3.13.5 only;
- Python 3.11 and 3.12 remain unverified in the accepted environment;
- the portable `uv.lock` is incomplete/non-authoritative and therefore omitted;
- the project license remains owner-controlled and pending;
- no GitHub upload, release upload, remote-byte check, or P0-GATE-18 adjudication is performed by this local packaging workflow.

## 20. Phase 1 readiness and entry conditions

Phase 1 is ready but not authorized. Entry requires:

1. freezing the P01 Protocol Annex;
2. resolving dataset revision, checksum, and license;
3. resolving environment and resource budgets;
4. validating split, leakage, and chronology controls;
5. reusing rather than regenerating the Phase 0 schemas, configurations, contracts, and identity rules.

## 21. Provenance and full archive

The normal main tree intentionally excludes internal audit bulk and superseded history. The exact R5 source archive belongs in the separately delivered release-assets package. See [provenance/full_phase0_archive.md](provenance/full_phase0_archive.md).

## 22. Citation

Citation metadata is in [CITATION.cff](CITATION.cff). Authorship, release date, and final license must be confirmed by the project owner at publication.

## 23. Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [CODEOWNERS](CODEOWNERS).

## 24. License status

Public visibility does not grant reuse rights. Until the project owner selects a license, [LICENSE_PENDING.md](LICENSE_PENDING.md) controls.
