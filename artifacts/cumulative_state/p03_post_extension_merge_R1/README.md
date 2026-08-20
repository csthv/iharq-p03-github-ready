# P03 post-extension cumulative merge R1 — audit package

This directory is the authoritative repository-integration record for the merge of the validated cumulative P00→P02 post-extension R3 baseline with the supplied Phase 03 GitHub-ready post-extension 64/128/256 R1 release.

## Integration policy

1. Preserve the P00→P02 baseline as the cumulative foundation.
2. Map every P03 source file to one explicit cumulative destination and verify size/SHA-256 identity.
3. Promote canonical P03 artifact families into the established root `artifacts/` and `final_state/` structures.
4. Retain the P03 post-extension 64/128/256 tree as a separate current annex instead of overwriting same-named canonical P03 evidence.
5. Retain the accepted P03 implementation snapshot and promote its root-relevant code/config/schema content; use only a documented root Layer 3 non-execution `__init__.py` compatibility shim, and archive every superseded baseline preimage first.
6. Extend cumulative status/navigation/pointer/handoff surfaces without discarding prior P02 detail.
7. Regenerate repository-wide indexes/manifests/checksums only after integration and validation.

## Audit artifacts

- `SOURCE_PACKAGE_IDENTITIES.json` — source ZIP identities and extracted file counts.
- `SOURCE_TO_CUMULATIVE_PATH_MAP.csv` — all 3,447 P03 files, mapped destination, size, hash, disposition.
- `ROOT_IMPLEMENTATION_PROMOTION.csv` — root Layer 3 implementation/config/schema promotion decisions.
- `PREIMAGE_ARCHIVE_MANIFEST.csv` — exact baseline bytes archived before replacement.
- `source_preservation_audit.json` — P02 baseline + P03 source preservation proof.
- `ADDED_FILES.csv` / `REPLACED_FILES.csv` — baseline-to-merged current-tree delta, excluding self-referential audit ledgers as documented.
- `final_merge_validation.json` — consolidated final validation summary.
