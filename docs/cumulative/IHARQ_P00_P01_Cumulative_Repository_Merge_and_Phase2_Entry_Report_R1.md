# IHARQ P00+P01 Cumulative Repository Merge and Phase-2 Entry Report R1

## Decision

The Phase-0 GitHub Scholarship Ready R2 tree and finalized Phase-1 GitHub Ready R2 tree were reconciled into one cumulative current repository. No scientific result, Phase-1 record, reviewed claim, Evidence Map relation, or Layer-10 value was recomputed or strengthened.

## Source identities

- P00 clean GitHub tree: `IHARQ_Phase_0_GitHub_Scholarship_Ready_R2(6).zip` — SHA-256 `3dcbe3e82ec7254ce1bd40568b36409d56050538e69a7264f8f1e431be019ef0`.
- P00 release-assets carrier: `IHARQ_Phase_0_GitHub_Release_Assets_R2(1).zip` — SHA-256 `db09e25436252af1739e2d1e8bc8996ae85c24a8f6728e757a9e67e100282619`.
- P01 finalized GitHub tree: `IHARQ_P01_Finalized_GitHub_Ready_R2.zip` — SHA-256 `e367d9849684b9e71cedc793da0be0eea02c934fece67513de1fee08a167f2b7`.

## Path reconciliation

- P00 files: 588
- P01 files: 13336
- common paths: 70
- byte-identical common paths: 62
- genuinely different common paths: 8
- P00-only paths: 518
- P01-only paths: 13266
- transient bytecode excluded from current tree: 112

The eight differing common paths are resolved in `artifacts/cumulative_state/path_conflict_resolution.json`; every displaced predecessor is preserved under `history/`.

## Authority reconciliation

`docs/authorities/current/` now contains Governance V6.1 and the current seven core authorities. The P00 Governance-V4 authority snapshot remains historical under `history/phase_00/github_ready_R2/authority_snapshot_V4/`.

## Environment reconciliation

No false cross-phase single-runtime claim is made. P00's exact GitHub-ready environment metadata is under `environments/phase_00/`; P01's accepted operational environment metadata is under `environments/phase_01/`. The root operational metadata follows finalized P01/P02-entry tooling only.

## P02 entry

P01's current closure handoff records P01-G15 PASS and concrete references to 3 DatasetRecords, 12,910 WindowRecords, 1 SplitRecord, 1 PreprocessingRecord, 3 LabelMapRecords, and 1 ValidationReport. The cumulative handoff preserves these requirements and adds the current authority/repository/input manifests expected by the P02 foundation contract.

**Green light:** the cumulative state is suitable to begin the governed P02 preparation workflow after validation. P02 scientific execution remains not started and must wait for a P02-specific implementation/Protocol freeze.
