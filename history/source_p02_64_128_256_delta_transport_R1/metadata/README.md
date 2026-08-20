# IHARQ P02 64/128/256 GitHub-ready delta transport

Annex ID: `P02_LOWLABEL_64_128_256_STAGE18S_R1_a0e2462396cf`

This ZIP is **not** a replacement for the previously finalized cumulative
P00+P01+P02 GitHub-ready package. It is a deterministic delta package intended
to be supplied **alongside** that frozen baseline for a later full cumulative
merge and re-audit.

## Frozen baseline expected later

- Canonical ZIP name: `IHARQ_Cumulative_GitHub_Ready_Through_P02_Final_R2.zip`
- Supplied ZIP SHA-256: `8f24fdbf11971fbecb886ff214b30b8241d32e7f0baef6dd9f6cf75817fe824b`
- Root manifest SHA-256: `10df9886ae4c31b61499142a5f79981f61c6935a6b1b6311ac70cb070f488c4b`
- Root manifest file count: `30824`

The later merge must fail closed if those identities do not match.

## What is physically inside this delta ZIP

1. `overlay/` — all verified current lightweight/control files that are new or
   changed, placed at their proposed cumulative-repository target paths.
2. `metadata/DELTA_FILE_MANIFEST.jsonl` — exact SHA-256/size/path identity for
   every embedded payload file.
3. `metadata/DELTA_TARGET_PATH_INDEX.csv` — deterministic overlay targets.
4. `metadata/HEAVY_ARTIFACT_POINTERS.jsonl` — exact pointers for current heavy
   artifacts. **No heavy bytes are embedded.**
5. `metadata/BASELINE_HASH_REUSE_POINTERS.jsonl` — exact historical reuse
   pointers for byte-identical artifacts that should not be duplicated.
6. final annex handoff/audit/location index and Stage24/G24 receipt evidence.
7. `metadata/MERGE_CONTRACT.json` — required later synthesis/regeneration rules.

## Current repository roles

### Current lightweight annex
`Csthv/iharq-p02-stage24-replay-github-ready-r1-20260814t060824z`

Annex content revision:
`c7504a1719ca7af9e44d849c0802a732099ed365`

Annex pointer revision:
`84201e72d1ff8ffdd14b17cbbceec2857a14b436`

### Current heavy extension authority
`Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260817t182318z`

Heavy-content revision:
`7f43cf3a9ea4b2056d96b9d2135bc14eac605b90`

Latest verified release revision:
`1abb59c6d8b6002d86ef72571bed46d9af028569`

### Historical archival authority
`Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260814t051352z`

### Frozen whole-working baseline
`Csthv/p02-phase02-final-whole-working-20260814t052120z-b890ff92@bc14961e14f2e48690e55df3577014275f9cbf30`

## Non-duplication policy

- unchanged historical files are not included;
- baseline-hash-equivalent files are represented by pointers;
- heavy current artifacts are represented by immutable HF pointers;
- only current lightweight/control bytes plus post-annex control metadata are
  embedded.

## Important later-merge requirement

Overlaying these files is only the first step. The final cumulative repository
must regenerate root manifests/checksums/current indexes and reconcile curated
`final_state/through_p02` mirrors from the changed source artifacts. Historical
P00/P01 content must remain byte-preserved unless a governed cross-phase pointer
or index legitimately needs regeneration.

Scientific boundary: canonical Stage18/G18 remains unchanged; Stage18S remains
`POST_HOC_SENSITIVITY_DESCRIPTIVE`.
