# IHARQ BenchGuard Stretch C — Cumulative GitHub-Ready Repository Through Phase 03, Post-Extension 64/128/256

**Current cumulative state:** `P00_P01_P02_P03_POST_EXTENSION_MERGED_VALIDATED_READY_FOR_P04_INTAKE`

This repository is the provenance-preserving cumulative GitHub-ready state for **Phase 00 + Phase 01 + Phase 02 + Phase 03**, including the governed 64/128/256 post-extension evidence supplied for P02 and P03. It is intentionally more than a concatenation: P03 content is mapped into the established cumulative architecture, accepted Layer 3 implementation is promoted into the root import/config/schema surface, canonical and post-extension P03 scopes remain distinguishable, superseded predecessor bytes are archived, and cumulative status/manifests/checksums/indexes are regenerated.

## Start here

1. `CURRENT_PROJECT_STATUS.json` — machine-readable cumulative state.
2. `current_document_index.md` — human navigation across P00→P03 authorities and evidence.
3. `docs/phase_03/README.md` — P03 integration/scientific-scope guide.
4. `artifacts/handoffs/phase_03_to_phase_04/p03_handoff_manifest.json` — canonical P03→P04 handoff.
5. `final_state/through_p03/` — P03 final export/closure/provenance state.
6. `external_artifact_pointer_manifest.yaml` — cumulative external-artifact resolution entry point.

## P03 current state

- Canonical execution receipts: `current/phase_03/canonical_execution/`
- Accepted implementation snapshot: `current/phase_03/implementation/`
- Canonical P03 artifact families: `artifacts/.../phase_03/`
- Post-extension 64/128/256 annex: `current/phase_03/post_extension_64_128_256/`
- Release metadata / heavy pointers / location index: `current/phase_03/release_metadata/`
- Final closure/provenance: `final_state/through_p03/`

The P03 package reports that current analysis is self-sufficient without retrieval of the heavy repository; large/raw/checkpoint/reproduction payloads remain external and are resolved through the exact immutable pointers in the release metadata. The dedicated P03 heavy repository is `Csthv/iharq-p03-postext-64-128-256-r1-heavy-1833e865bcb88ff8` at immutable revision `2b5b465fafdcd4c590d24e90ee0932571d7658a9`.

## Scientific and governance boundary

This merge does **not** rerun scientific models, retune or reselect thresholds, use test data for selection, approve candidate claims, perform a no-rule rescue, or author downstream Protocol v1 / Phase Analysis / Layer 0 / Evidence Map / final Layer 10 consumer outputs. Canonical P03 and the post-extension 64/128/256 evidence are both retained and are not collapsed into one ambiguous evidence surface. Existing P00→P02 limitations remain preserved, and the P03 handoff contributes its explicit limitations for P04 consumption.

## Preservation and audit guarantees

- Every supplied P03 file is mapped to a cumulative destination with original size and SHA-256 in `artifacts/cumulative_state/p03_post_extension_merge_R1/SOURCE_TO_CUMULATIVE_PATH_MAP.csv`.
- Every baseline current-path byte intentionally replaced by this merge is preserved under `history/p03_merge_preimages_R1/`.
- The P03 accepted implementation is retained intact under `current/phase_03/implementation/`; functional root promotion is byte-identical except for the cumulative Layer 3 `__init__.py` non-execution compatibility shim, which preserves the repository-wide import boundary.
- Canonical P03 files and post-extension files sharing a relative name are retained as distinct scope-specific objects rather than overwriting one another.
- Root manifests, checksums, indexes, source-preservation audits, and merge validation are regenerated after integration.

## Verification

```bash
python scripts/verify_cumulative_release.py
python -m pytest -q -p no:cacheprovider
```

The prior P00→P02 cumulative README is preserved exactly at `history/p03_merge_preimages_R1/README.md`.
