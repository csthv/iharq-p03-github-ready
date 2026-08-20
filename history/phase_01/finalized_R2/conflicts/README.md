# IHARQ Phase 01 / Layer 01 - Finalized Phase Repository

This repository is the finalized, self-contained **Phase 01 / Layer 01** repository successor for the IHARQ BenchGuard Stretch C project.

It preserves the accepted execution-era repository and adds the completed Phase-1 documentary and reproducibility stack. It **does not merge Phase 0 and Phase 1 repositories**; that owner-directed cross-phase merge is intentionally deferred to the next project-state operation.

## Current Phase-1 status

- Phase execution: **ACCEPTED**
- Official scientific freeze: `P01-L1-OFFICIAL-RUN-FREEZE-R2`
- Config ID: `d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f`
- Accepted stages: **27/27**
- Deterministic gates: **16/16 PASS**
- Regression tests in accepted execution evidence: **50/50 PASS**
- Unresolved Phase-1 blockers: **0**
- Protocol through P01: **FROZEN**
- Cumulative Phase Analysis + embedded Layer 0: **FINALIZED**
- Cumulative Evidence Map through P01: **FINALIZED**
- Cumulative Layer 10 through P01: **FINALIZED / READ-ONLY**
- P01-G15 Phase-2 compatibility: **PASS**
- P02 technical readiness from P01: **PASS**

## Important authority distinction

The original `artifacts/phase_execution_handoff.yaml` and `artifacts/handoffs/phase_01_to_phase_02.yaml` are preserved as **execution-time historical evidence**. Their statements that Protocol/Analysis/Layer0/Evidence Map/Layer10 were not yet complete were true at execution time.

The current post-documentary state is controlled by:

`artifacts/phase_closure/IHARQ_Phase_01_Final_Handoff_and_Phase2_Readiness_R1.yaml`

## Final Phase-1 documents

- `docs/phase_01/implementation/` - controlling pre-run Build Book R10 and P01/L1 Annex R4
- `docs/phase_01/protocol/` - frozen cumulative Protocol v1.0 through P01
- `docs/phase_01/analysis/` - finalized cumulative Phase Analysis with embedded Layer 0
- `docs/phase_01/layer0/` - convenient P01-only non-authoritative Layer 0 derivative
- `docs/phase_01/evidence_map/` - finalized cumulative Evidence Map through P01
- `docs/phase_01/layer10/` - finalized cumulative Layer 10 through P01
- `docs/phase_01/closure/` - final holistic synchronization / P02-readiness report

## Numerical artifacts

This repository intentionally does not duplicate raw EEG or the large HDF5 derived-window arrays.

Core P01 derived-window Dataset:
`csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473`

- Kaggle provider version: **2**
- IHARQ logical immutable revision: **1**
- manifest SHA-256: `dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1`
- windows: **12,910**
- subject shards: **172**

A4 R2 is a future-control data substrate, not a P01 effectiveness result.

## Runtime metadata

The pre-run Build Book originally targeted Python 3.11. The accepted Kaggle execution used Python **3.12.13** under a documented compatibility amendment. The operational `pyproject.toml` in this finalized repository therefore targets Python 3.12, while the historical pre-run authority remains preserved unchanged under `docs/phase_01/implementation/`.

## Verification

Run:

```bash
python scripts/verify_phase01_release.py
python -m compileall -q src runtime_overlays
```

The accepted execution's original 50-test suite is evidenced in the Phase Execution Bundle; it is **not fabricated into this compact GitHub-ready derivative**.

Current repository integrity is governed by:

- `CURRENT_GITHUB_READY_REPOSITORY_MANIFEST.json`
- `REPOSITORY_CHECKSUMS.sha256`

The predecessor `GITHUB_READY_REPOSITORY_MANIFEST.json` remains historical execution-export evidence.

## Phase-2 transition

P01 provides the required technical data contract to P02. Before P02 execution, the project owner plans one separate operation to merge the finalized P00 and P01 GitHub-ready states into a single clean cumulative repository/project-state package. That merge is **not a missing P01 scientific task** and is intentionally not performed here.
