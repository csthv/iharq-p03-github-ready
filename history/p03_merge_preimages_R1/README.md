# IHARQ BenchGuard Stretch C — Cumulative GitHub-Ready Repository Through Phase 02, Post-Extension 64/128/256

**Current cumulative state:** `P00_P01_P02_POST_EXTENSION_MERGED_VALIDATED_READY_FOR_P03_INTAKE`

This is the professionally merged cumulative GitHub-ready state containing the full previously curated Phase 00 + Phase 01 + pre-extension Phase 02 repository **plus** the governed P02 64/128/256 low-label and repeated Stage18S extension. The merge is provenance-preserving rather than a simple concatenation: unchanged historical content is retained, changed current P02 files replace their current-path predecessors, every replaced predecessor is archived under `history/p02_pre_extension_preimages_R3/`, current heavy artifacts remain external with immutable pointers, and cumulative manifests/checksums/indexes are regenerated.

## What was added or refreshed

The complete file-level inventories are authoritative:

- `artifacts/cumulative_state/p02_post_extension_merge_R3/ADDED_FILES.csv` — every newly added current/curated file.
- `artifacts/cumulative_state/p02_post_extension_merge_R3/REPLACED_FILES.csv` — every current-path file whose content changed, with old and new SHA-256.
- `artifacts/cumulative_state/p02_post_extension_merge_R3/PREIMAGE_ARCHIVE_MANIFEST.csv` — exact preserved copies of every overwritten predecessor.
- `artifacts/cumulative_state/p02_post_extension_merge_R3/EXCLUDED_TRANSIENT_SOURCE_FILES.csv` — exact identity of two derived `__pycache__/*.pyc` delta members intentionally omitted from the GitHub-ready current tree.
- `history/source_p02_64_128_256_delta_transport_R1/metadata/DELTA_FILE_MANIFEST.jsonl` — source delta identity.
- `final_state/through_p02/extension_annex/FINAL_CROSS_REPOSITORY_LOCATION_INDEX.jsonl` — current cross-repository resolution map.

Major additions include 64/128/256 A0/A4/Stage18S lightweight metrics, manifests, diagnostics, records, analysis inputs, current table/figure-source data, the final annex handoff/audit, and extension release metadata. Current P02 table mirrors are refreshed under `final_state/through_p02/analysis/table_source_data/p02/`.

## Where the new artifacts reside

### Current lightweight / GitHub-ready evidence
`current/phase_02/kaggle_run_light/`

This includes BACC/ACC/F1 metric surfaces, low-label 1→256 analysis inputs, Stage18S repeated-sensitivity evidence, run-cell/manifests/records/diagnostics, table source data, and final extension handoffs.

### Curated final-state extension view
- Scientific addendum: `final_state/through_p02/analysis/P02_64_128_256_Extension_Addendum_R1.md`
- Current P02 table sources: `final_state/through_p02/analysis/table_source_data/p02/`
- Extension audit/pointers: `final_state/through_p02/extension_annex/`
- Preserved pre-extension PNG figures: `final_state/through_p02/analysis/figures/` (see `README_POST_EXTENSION_SCOPE.md`)

### P03 consumer handoff
`artifacts/handoffs/phase_02_to_phase_03/`

Read the extension handoff/location index **before** falling back to older P02 artifacts.

### Heavy current extension artifacts — intentionally external
Heavy checkpoint/prediction/runtime payloads are not embedded in this GitHub-ready ZIP. Their current authority is:

`Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260817t182318z`

Immutable heavy-content revision:
`7f43cf3a9ea4b2056d96b9d2135bc14eac605b90`

Resolve them through `external_artifact_pointer_manifest.json`, `external_artifact_pointer_manifest.yaml`, or `final_state/through_p02/extension_annex/HEAVY_ARTIFACT_POINTERS.jsonl`.

### Historical authorities
- Frozen whole-working P02: `Csthv/p02-phase02-final-whole-working-20260814t052120z-b890ff92@bc14961e14f2e48690e55df3577014275f9cbf30`
- Historical archival/control repo: `Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260814t051352z`
- Historical GitHub-ready repo / extension light annex: `Csthv/iharq-p02-stage24-replay-github-ready-r1-20260814t060824z`

## Scientific boundary

Canonical Stage18/G18 was **not** modified. Stage18S remains **post-hoc descriptive sensitivity evidence**. The integrated low-label axis is now 1, 2, 4, 8, 16, 32, 64, 128, 256. Do not infer a monotonic budget-response, universal A4 benefit, 256=FULL equivalence, or a new multiplicity-controlled confirmatory family from the extension.

## Preservation guarantees

- P00 and P01 source content from the validated predecessor remains present.
- Pre-extension P02 content remains present unless a current-path file is legitimately superseded; every superseded byte is archived in `history/p02_pre_extension_preimages_R3/`.
- The original delta transport metadata is preserved under `history/source_p02_64_128_256_delta_transport_R1/`.
- Heavy artifacts are not duplicated.
- Two transient Python bytecode cache files from the delta are intentionally excluded from the GitHub-ready current tree; their exact paths, sizes, hashes, and source ZIP identity are retained in `EXCLUDED_TRANSIENT_SOURCE_FILES.csv`. Their corresponding Python source is preserved and compilation/tests pass.
- Root and nested manifests/checksums are regenerated after the merge.

## P03 intake

Start with:

1. `CURRENT_PROJECT_STATUS.json`
2. `artifacts/handoffs/phase_02_to_phase_03/P02_POST_EXTENSION_INTAKE_ADDENDUM_R1.md`
3. `artifacts/handoffs/phase_02_to_phase_03/P02_64_128_256_EXTENSION_ANNEX_HANDOFF_R1.json`
4. `artifacts/handoffs/phase_02_to_phase_03/P02_64_128_256_EXTENSION_ANNEX_LOCATION_INDEX.jsonl`
5. `final_state/through_p02/analysis/P02_64_128_256_Extension_Addendum_R1.md`
6. existing Protocol / Layer 0 / Evidence Map / Layer 10 authorities under `final_state/through_p02/`
7. `external_artifact_pointer_manifest.yaml`

## Verification

```bash
python scripts/verify_cumulative_release.py
python -m pytest -q -p no:cacheprovider
```

The merge itself did not rerun scientific models or recompute heavy scientific artifacts.
