# P02 64/128/256 Extension Addendum R1

**Status:** governed post-extension addendum; canonical Stage18/G18 is unchanged.  
**Annex:** `P02_LOWLABEL_64_128_256_STAGE18S_R1_a0e2462396cf`  
**Scope:** current low-label budgets 1, 2, 4, 8, 16, 32, 64, 128, 256 plus repeated Stage18S post-hoc sensitivity.

This addendum accompanies — and does not erase — the original finalized P02 Protocol, Phase Analysis, Layer 0, Evidence Map, and Layer 10 documents already present under `final_state/through_p02/`. Those documents remain the preserved pre-extension closure record. The extension adds current numerical evidence and a governed retrieval layer without retroactively converting post-hoc Stage18S evidence into a confirmatory claim family.

## Current result surfaces

- `current/phase_02/kaggle_run_light/runtime/analysis_inputs/low_label_metric_source.csv` — 324 rows; ACC, BACC, and F1_MACRO across all nine 1→256 low-label budgets.
- `current/phase_02/kaggle_run_light/runtime/table_source_data/p02/P02_Table_low_label_BACC.csv` — 108 BACC rows across all nine budgets.
- `current/phase_02/kaggle_run_light/runtime/metrics/` — lightweight per-cell metric JSONs for the extension.
- `current/phase_02/kaggle_run_light/runtime/supplements/stage18S_balanced_sensitivity_R1/` — repeated Stage18S post-hoc sensitivity evidence.
- `final_state/through_p02/analysis/table_source_data/p02/` — curated current table mirrors, including the newly added 64/128/256 and Stage18S summary tables.

## High-budget Stage18S descriptive summary

| Budget | Mean A4 BACC | Mean ΔBACC | Median ΔBACC | Positive fraction |
|---:|---:|---:|---:|---:|
| 64 | 0.524381 | -0.003427 | -0.003472 | 0.467 |
| 128 | 0.555428 | +0.006353 | +0.008333 | 0.600 |
| 256 | 0.597537 | +0.021397 | +0.014553 | 0.778 |

The repeated sensitivity evidence remains heterogeneous and budget/repeat dependent. The 256-label anchor shows a notable positive descriptive shift, particularly in the neural longer-window condition, but this does **not** establish monotonic improvement, a new multiplicity-controlled confirmatory result, universal A4 benefit, or equivalence to FULL training.

## Heavy artifact boundary

Heavy checkpoints/prediction payloads are intentionally absent from this GitHub-ready cumulative ZIP. Exact current locations are resolved through `external_artifact_pointer_manifest.json`, `external_artifact_pointer_manifest.yaml`, and `final_state/through_p02/extension_annex/HEAVY_ARTIFACT_POINTERS.jsonl`.

## P03+ resolution order

1. Read `artifacts/handoffs/phase_02_to_phase_03/P02_64_128_256_EXTENSION_ANNEX_HANDOFF_R1.json`.
2. Resolve current lightweight files locally from this cumulative repository.
3. Resolve current heavy files from the immutable 2026-08-17 extension Hugging Face release.
4. Reuse hash-equivalent or unchanged historical artifacts only where the annex explicitly says to do so.
5. Fall back to the frozen historical P02 authorities only if the extension annex does not resolve an artifact.
