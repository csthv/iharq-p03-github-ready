# IHARQ BenchGuard Stretch C — Cumulative Repository Through Phase 01

**Current cumulative state:** `P00_P01_MERGED_VALIDATED_READY_FOR_P02_ENTRY`

This repository is the clean merged successor of:

- Phase 0 GitHub Scholarship Ready R2 (`3dcbe3e82ec7254ce1bd40568b36409d56050538e69a7264f8f1e431be019ef0`); and
- finalized Phase 1 GitHub Ready R2 (`e367d9849684b9e71cedc793da0be0eea02c934fece67513de1fee08a167f2b7`).

It is the **clean input state for Phase 2 preparation**. P02 has not been scientifically executed by this merge.

## Current project state

- P00: preserved engineering/governance foundation; historical Governance-V4 publication-gate wording is retained as provenance but does not control the current V6.1 workflow.
- P01: execution accepted and fully finalized through Protocol, cumulative Phase Analysis + embedded Layer 0, Evidence Map, Layer 10, closure and P02 technical handoff.
- P02 entry readiness: **PASS**.
- P02 execution: **NOT STARTED**. A P02 implementation/Protocol freeze must precede P02 execution.
- A0–A13: readiness/foundation state only where not executed.
- A14: **ABSENT / PROHIBITED**.
- A4 R2: data substrate ready; effectiveness **not evaluated in P01**.
- Clinical/deployment claim boundary: `PUBLIC_EEG_ONLY`, `NON_CLINICAL`, `NO_DEPLOYMENT_CLAIM`.

## Authority and navigation

- Current Governance + seven core authorities: `docs/authorities/current/`
- P00 final document set: `docs/phase_00/final_documents/`
- P01 final documents: `docs/phase_01/`
- Current cumulative merge/Phase-2 handoff: `artifacts/cumulative_state/`
- P00/P01 phase-specific environments: `environments/`
- Historical conflicting root/current-status files: `history/`

## Phase-2 input

Use `artifacts/cumulative_state/IHARQ_P00_P01_to_P02_Clean_Input_Handoff_R1.yaml`. It binds the P00 foundation to the accepted P01 data/protocol outputs and explicitly carries the P01 record counts and external Dataset identities.

## Verification

```bash
python scripts/verify_cumulative_release.py
python -m compileall -q src runtime_overlays
```

The original P00 publication-tree verifier and the P01 finalized-tree verifier apply to their exact predecessor snapshots, not to this cumulative tree. Its source identity is recorded in `release_assets/predecessor_references/README.md`.
