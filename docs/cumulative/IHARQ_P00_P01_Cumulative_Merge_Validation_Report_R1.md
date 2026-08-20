# IHARQ P00+P01 Cumulative Merge Validation Report R1

## Final decision

**PASS — the merged cumulative repository is a clean Phase-2 input state.**

- P00 GitHub predecessor validator: PASS.
- P01 finalized predecessor validator: 24/24 PASS.
- cumulative repository verifier: 40/40 PASS.
- P01 closure verifier inside cumulative tree: 24/24 PASS.
- current-source compile: PASS with bytecode redirected outside the repository.
- current structured controls: 14/14 parse PASS.
- P00 source-file accounting: 588/588.
- P01 non-transient source-file accounting: 13,224/13,224.
- intentionally excluded P01 bytecode/transients: 112.
- unexplained source loss: 0.
- open blockers: 0.

## Authority result

The current authority directory contains Governance V6.1 plus the seven core authorities. The P00 Governance-V4 GitHub authority snapshot and obsolete publication/authorization status remain preserved under `history/` and do not compete with current authority.

## P02 result

The merged repository contains the required P02 entry manifest families (`AuthorityManifest`, `RepositoryManifest`, `EnvironmentManifest`, `ConfigSnapshot`, `InputManifest`) and the current P00+P01→P02 handoff. P01-G15 remains PASS and the P01 contract carries 3 DatasetRecords, 12,910 WindowRecords, 1 SplitRecord, 1 PreprocessingRecord, 3 LabelMapRecords, and 1 ValidationReport.

**Green light:** begin the governed P02 preparation workflow from this repository. **Do not begin P02 scientific execution until P02's own implementation, Protocol/analysis contract, configuration, environment, and run freeze are created and validated.**
