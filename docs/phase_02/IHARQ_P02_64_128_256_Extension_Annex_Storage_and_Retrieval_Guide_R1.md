# IHARQ Phase 02 — 64/128/256 Extension Annex
## Storage, Provenance, Retrieval, and Future-Phase Use Guide

**Document status:** FINAL / POST-ANNEX CLOSURE  
**Phase:** P02  
**Extension scope:** low-label budgets **64, 128, 256 labels/class** plus associated Stage18S repeated sensitivity and downstream regenerated presentation/control artifacts  
**Annex ID:** `P02_LOWLABEL_64_128_256_STAGE18S_R1_a0e2462396cf`  
**Final annex status:** `PASS`  
**Primary purpose of this document:** explain, in one place, what existed before the extension, what changed, what was intentionally *not* duplicated, where every class of current artifact now resides, and how P03+ or any future consumer should resolve P02 artifacts.

---

# 1. Executive Summary

Phase 02 had already been completed and published before the 64/128/256-label extension work.

The extension did **not** replace the original P02 release and did **not** rebuild or duplicate the entire repository family.

Instead, the extension was handled as a **delta annex**:

1. compare the current integrated P02 working tree against the frozen historical P02 authorities;
2. identify which files are unchanged, byte-equivalent, changed, or entirely new;
3. **do not re-upload unchanged files**;
4. **do not re-upload current heavy artifacts that were already successfully uploaded**;
5. upload only the genuinely changed/new lightweight and control artifacts into a dedicated annex in the existing GitHub-ready Hugging Face repository;
6. add only a small control/pointer annex to the historical archival/heavy repository;
7. keep the current heavy 64/128/256 artifacts in the already-created current extension release repository;
8. create a cross-repository location index so future phases can resolve the newest valid artifact without guessing.

The resulting storage model is therefore:

```text
Historical GitHub-ready repository
    + NEW lightweight/current delta annex
    + README / manifests / location index

Historical archival/heavy repository
    + NEW control/pointer annex only
    + historical R2 manifest preserved unchanged

Current 64/128/256 extension release repository
    + current heavy artifacts already uploaded
    + no duplicate heavy upload performed by the annex

Frozen original whole-working baseline
    + remains read-only and unmodified
```

---

# 2. What Existed Before the 64/128/256 Extension

There are three historical authorities that must be distinguished.

## 2.1 Frozen whole-working P02 baseline — read-only authority

Repository:

```text
Csthv/p02-phase02-final-whole-working-20260814t052120z-b890ff92
```

Frozen revision:

```text
bc14961e14f2e48690e55df3577014275f9cbf30
```

Role:

- original finalized whole-working P02 authority;
- used as a historical baseline for identity and provenance checks;
- **not modified by the extension annex**;
- future consumers may fall back to it only when the extension annex does not supersede or redirect an artifact.

Write policy:

```text
READ_ONLY_IMMUTABLE_BASELINE
```

---

## 2.2 Historical archival/heavy P02 repository

Repository:

```text
Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260814t051352z
```

Role before the extension:

- historical P02 archival/release authority;
- contained the historical release/control metadata and external-artifact mappings;
- represented the already-completed pre-extension P02 state.

The extension did **not** overwrite the historical R2 pointer manifest and did **not** turn this repository into a second copy of the new heavy release.

---

## 2.3 Historical GitHub-ready P02 repository

Repository:

```text
Csthv/iharq-p02-stage24-replay-github-ready-r1-20260814t060824z
```

Historical repository-tree baseline revision:

```text
c805487d24ab9727d86b63be74efb68b6b392476
```

Historical remote repository-tree manifest:

```text
github_ready/CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json
```

Manifest SHA-256:

```text
a6694a3d550e33c7bcbbff2f22b0beddc878ae403bb8646aa9c5ca7afb69c8ce
```

Manifest ID:

```text
IHARQ-GITHUB-READY-THROUGH-P02-STAGE24-REPLAY-R1
```

Files represented by that manifest:

```text
27,080
```

Role before the extension:

- clean/lightweight GitHub-ready derivative;
- code, documents, manifests, tables, configs, pointers, and other repository-friendly content;
- not intended to duplicate the entire heavy runtime/checkpoint payload.

---

# 3. A Manifest Distinction That Must Be Preserved

Two valid historical manifests have the same basename but describe **different scopes**.

Do not treat them as the same artifact.

## 3.1 Remote GitHub-ready repository-tree manifest

```text
Path:
github_ready/CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json

SHA-256:
a6694a3d550e33c7bcbbff2f22b0beddc878ae403bb8646aa9c5ca7afb69c8ce

Manifest ID:
IHARQ-GITHUB-READY-THROUGH-P02-STAGE24-REPLAY-R1

Files:
27,080
```

This is the correct historical authority for determining what already existed in the GitHub-ready Hugging Face repository.

## 3.2 Separate finalized cumulative P02 R2 ZIP root manifest

```text
SHA-256:
10df9886ae4c31b61499142a5f79981f61c6935a6b1b6311ac70cb070f488c4b
```

Role:

```text
SEPARATE_CUMULATIVE_ZIP_AUTHORITY
```

It is a valid historical cumulative-package manifest, but it is **not** the same object as the remote GitHub-ready repository-tree manifest above.

This distinction was explicitly preserved in the final annex workflow to prevent future manifest-resolution mistakes.

---

# 4. What the 64/128/256 Extension Added

The extension expanded the low-label axis from the historical:

```text
1, 2, 4, 8, 16, 32
```

to the integrated current axis:

```text
1, 2, 4, 8, 16, 32, 64, 128, 256
```

It also incorporated the associated current Stage18S repeated sensitivity products and regenerated downstream tables/manifests required to represent the integrated 1→256 state.

Important governance boundaries remain:

```text
Canonical Stage18 / G18:
UNCHANGED

Stage18S:
POST_HOC_SENSITIVITY_DESCRIPTIVE

No new confirmatory test family was created by the annex.
```

Useful current Stage18S identity counts:

```text
planned cells:                    324
groups:                           108
SUCCESS:                          270
INPUT_INCOMPATIBLE:                54
member receipts:                  432
successful member receipts:       378
incompatible member receipts:      54
combined successful effect rows:  315
three-repeat anchor trajectories:  90
nine-budget MR00 trajectories:     15
```

These counts are useful for verifying that a future consumer has reached the integrated current P02 extension rather than an older Stage18S state.

---

# 5. Why a Delta Annex Was Used

A complete re-upload would have been wasteful and would have made the repositories harder to interpret.

The extension workflow therefore classified every current file by identity.

Final comparison:

```text
Current files considered:                 21,504

Changed or new:                            4,496
Baseline-hash reuse / no upload:              51
Unchanged / no upload:                    16,957
```

Byte-level result:

```text
Changed/new total:                     2.748507 GiB
Heavy changed/new already remote:      2.535035 GiB
Lightweight changed/new uploaded:      0.213472 GiB
Unchanged bytes intentionally avoided: 9.241335 GiB
```

Changed/new split:

```text
Heavy artifacts already uploaded:         758 files
Lightweight/control annex uploads:       3,738 files
```

This accounting closes exactly:

```text
758 + 3,738 = 4,496 changed/new files
```

and:

```text
2.535035 GiB + 0.213472 GiB
= 2.748507 GiB changed/new data
```

---

# 6. Where the New / Current Artifacts Now Reside

This is the most important operational section.

---

## 6.1 Current lightweight / GitHub-ready delta

Repository:

```text
Csthv/iharq-p02-stage24-replay-github-ready-r1-20260814t060824z
```

Annex ID:

```text
P02_LOWLABEL_64_128_256_STAGE18S_R1_a0e2462396cf
```

Annex content revision:

```text
c7504a1719ca7af9e44d849c0802a732099ed365
```

Current annex pointer revision:

```text
84201e72d1ff8ffdd14b17cbbceec2857a14b436
```

What was added here:

- the **3,738 genuinely new/changed lightweight or control files**;
- current CSV/JSON/JSONL/table/analysis/control products where changed;
- Stage18S lightweight analysis outputs and summaries where changed/new;
- manifests and location indexes;
- annex README/instructions;
- handoff/control information;
- current annex pointers.

What was deliberately **not** added here:

```text
heavy bytes reuploaded:      0
unchanged bytes reuploaded:  0
```

This repository is therefore the primary location for the **current lightweight P02 extension view**.

---

## 6.2 Historical archival/heavy repository — control annex only

Repository:

```text
Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260814t051352z
```

Annex ID:

```text
P02_LOWLABEL_64_128_256_STAGE18S_R1_a0e2462396cf
```

Control-annex revision:

```text
1bb0d70013fddf5e475468b7925e0dd636602e59
```

Current control-pointer revision:

```text
d2de83414bd5a3c452bcab7820d126999c5ff661
```

What was added here:

- annex/control README;
- annex manifests;
- artifact-location index / pointer overlay;
- instructions telling future consumers where the current extension artifacts actually live.

What was deliberately **not** done:

```text
historical R2 pointer manifest overwritten: false
heavy bytes reuploaded:                     0
unchanged bytes reuploaded:                 0
```

This repository remains the historical archival authority while gaining a small, truthful overlay describing the extension.

---

## 6.3 Current heavy 64/128/256 extension artifacts

Repository:

```text
Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260817t182318z
```

Current verified latest revision at annex closure:

```text
1abb59c6d8b6002d86ef72571bed46d9af028569
```

Verified heavy-content revision:

```text
7f43cf3a9ea4b2056d96b9d2135bc14eac605b90
```

Role:

- current heavy-artifact authority for the integrated extension;
- stores the heavy/checkpoint/runtime payload that had already been successfully uploaded during the Stage24 low-disk release;
- the annex **references** these current heavy bytes instead of uploading them again.

At verification time:

```text
heavy remote package/object groups verified: 47
GitHub-ready package objects verified:         4
cumulative package objects verified:           4
```

The **758 changed/new heavy logical files** are represented through the already-uploaded current heavy release rather than duplicated into the other two repositories.

---

# 7. What the Annex Manifest / Location Index Does

Every relevant current artifact is classified and resolved.

Typical disposition classes include:

```text
UNCHANGED_BASELINE_SAME_LOGICAL_PATH
UPLOAD_CHANGED_CURRENT
UPLOAD_NEW_CURRENT
REUSE_BASELINE_HASH_EQUIVALENT
```

The location index records enough information for a later phase to identify the authoritative copy, including fields such as:

```text
logical path
category
size / bytes
SHA-256
change class / disposition
resolution kind
repository ID
immutable revision
remote path
archive member, when applicable
```

The important design principle is:

> A filename alone is not considered sufficient identity.  
> Resolution uses logical path, SHA-256, repository role, and immutable revision.

---

# 8. Mandatory Future Lookup Precedence

**P03 and all later consumers should use the following resolution order.**

```text
STEP 1
Read the P02 extension-annex handoff / current annex pointer.

        ↓

STEP 2
Read the annex README and annex location index.

        ↓

STEP 3
Resolve the requested artifact according to the annex:

    A. Current lightweight / repository-friendly artifact
       → use the GitHub-ready extension annex.

    B. Current heavy artifact
       → use the current 2026-08-17 extension release repository.

    C. Byte-identical / baseline-hash-equivalent artifact
       → reuse the exact historical artifact identified by the annex.

    D. Explicitly unchanged historical artifact
       → reuse the historical location; do not create another copy.

        ↓

STEP 4
Only if the extension annex does not resolve the requested artifact:
fall back to the frozen historical P02 whole-working / archival authorities.
```

In compact form:

```text
ANNEX FIRST
    ↓
current light → GitHub-ready annex
current heavy → current extension release
same bytes     → historical hash-equivalent pointer
unchanged      → historical location
    ↓
historical P02 fallback only if unresolved
```

This order is mandatory because an older P02 repository may contain a valid historical file with the same or similar name but an older scientific scope, for example a pre-64/128/256 table or an older Stage18S surface.

---

# 9. Local Handoff Files Produced for Future Phases

The completed annex audit wrote the following current handoff files in the integrated working run:

```text
/kaggle/working/iharq_p02_integrated_1_256_R1/runtime/handoffs/
P02_64_128_256_EXTENSION_ANNEX_HANDOFF_R1.json
```

and:

```text
/kaggle/working/iharq_p02_integrated_1_256_R1/runtime/handoffs/
P02_64_128_256_EXTENSION_ANNEX_LOCATION_INDEX.jsonl
```

These are the preferred machine-readable local entry points when the integrated P02 working state is available.

If those local files are unavailable, use the repository annex pointer/README/location index described above.

---

# 10. Stage24 Receipt Repair and Why It Does Not Mean the Release Failed

The low-disk Stage24 release successfully completed its governed science/release handler and remote upload work.

Verified state:

```text
Stage24 = SUCCESS
G24     = PASS
```

A later local receipt-construction line failed because a boolean Stage24-acceptance result was incorrectly treated like a dictionary.

That error occurred **after** the large remote release objects had already been uploaded.

The annex workflow therefore:

- did not rerun Stage24 science;
- did not redo the heavy upload;
- verified the existing remote release;
- wrote a post-hoc repaired receipt describing the true completed release state.

Repaired local receipt:

```text
/kaggle/working/iharq_p02_integrated_1_256_R1/runtime/manifests/
P02_STAGE24_TRANSPORT_SUCCESSOR_POSTHOC_RECEIPT_R4_FIX1.json
```

The repaired receipt explicitly represents a transport/receipt repair, not a new scientific execution.

---

# 11. Final Cross-Repository Audit

Final annex audit:

```text
ANNEX-04 — FINAL CROSS-REPOSITORY AUDIT — PASS
```

Final resolved counts:

```text
changed/new files resolved:          4,496
baseline-hash reuse files resolved:     51
unchanged files not uploaded:       16,957
```

Storage efficiency:

```text
unchanged bytes not uploaded:  9.241335 GiB
heavy bytes reuploaded:        0.000000 GiB
light bytes uploaded:          0.213472 GiB
```

Historical preservation:

```text
baseline whole-working mutated:             false
historical R2 pointer manifest overwritten: false
```

Final trusted markers:

```text
IHARQ_P02_EXTENSION_ANNEX_FINAL_PASS
IHARQ_P02_64_128_256_ARTIFACT_RESOLUTION_READY_FOR_P03
```

These markers indicate that the P02 extension artifact-resolution layer is closed and ready for future-phase consumption.

---

# 12. Repository Role Summary

| Repository | Role after extension | What is new there | What is intentionally not duplicated |
|---|---|---|---|
| `Csthv/p02-phase02-final-whole-working-20260814t052120z-b890ff92` | Frozen whole-working baseline | Nothing | Everything; read-only |
| `Csthv/iharq-p02-stage24-replay-github-ready-r1-20260814t060824z` | Historical GitHub-ready + current light annex | 3,738 changed/new lightweight/control artifacts, annex README/manifests/index | Heavy current payload; unchanged historical bytes |
| `Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260814t051352z` | Historical archival authority + control annex | README, control manifests, pointer/location overlay | Current heavy payload; current light payload; unchanged bytes |
| `Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260817t182318z` | Current extension heavy-artifact authority | Already-uploaded current 64/128/256 heavy/runtime content | No annex-driven duplicate upload |

---

# 13. What Future Maintainers Must Not Do

Do **not**:

1. assume the historical repository is automatically the newest authority for a same-named file;
2. overwrite the historical R2 pointer manifest with the extension state;
3. re-upload all historical heavy artifacts just to make the extension self-contained;
4. duplicate the 758 changed/new heavy logical files into the GitHub-ready repository;
5. re-upload the 16,957 unchanged files;
6. treat the GitHub-ready remote repository-tree manifest (`a669...`) as the same file as the separate cumulative R2 ZIP root manifest (`10df...`);
7. modify the frozen whole-working baseline repository;
8. claim that Stage18S became confirmatory or that canonical Stage18/G18 was changed;
9. rerun P02 model training merely to recover these release/pointer artifacts.

---

# 14. Minimal Instructions for P03+

A future P03+ notebook can use this checklist:

```text
1. Locate:
   P02_64_128_256_EXTENSION_ANNEX_HANDOFF_R1.json
   or the current remote extension-annex pointer.

2. Read:
   annex README
   annex location index

3. For every requested P02 input:
   resolve by SHA-256 + logical path + repository revision.

4. Prefer:
   current annex location over historical same-name artifacts.

5. Heavy current artifact:
   retrieve from:
   Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260817t182318z

6. Lightweight current artifact:
   retrieve from the annex in:
   Csthv/iharq-p02-stage24-replay-github-ready-r1-20260814t060824z

7. Historical unchanged/hash-equivalent artifact:
   reuse the historical location named by the annex.

8. Fall back to the frozen P02 historical authorities only when the annex does
   not provide a resolution.
```

---

# 15. One-Paragraph Portable Explanation

Phase 02 was originally completed and released before the 64/128/256 low-label extension. Rather than replacing or re-uploading the entire original P02 repository family, the extension was published as a SHA-256-governed delta annex. Of 21,504 current files, 16,957 were unchanged and were not uploaded again, 51 were resolved through byte-identical historical reuse, and 4,496 were genuinely changed or new. Of those, 758 heavy logical files (about 2.535 GiB) were already present in the current 2026-08-17 extension release and were therefore referenced rather than duplicated, while only 3,738 changed/new lightweight and control files (about 0.213 GiB) were added to a dedicated annex in the existing GitHub-ready Hugging Face repository. The historical archival/heavy repository received only a small control/pointer annex, with its original R2 manifest preserved unchanged. A cross-repository location index now tells future phases exactly where the authoritative current or historical copy of each artifact resides. P03 and later phases must therefore consult the P02 extension annex first, resolve current lightweight artifacts from the GitHub-ready annex, current heavy artifacts from the 2026-08-17 extension release, and only then fall back to historical P02 repositories for unchanged or explicitly reused artifacts.

---

# 16. Canonical Locator Block

```yaml
phase: P02
extension:
  budgets_added: [64, 128, 256]
  annex_id: P02_LOWLABEL_64_128_256_STAGE18S_R1_a0e2462396cf
  status: PASS
  claim_scope: POST_HOC_SENSITIVITY_DESCRIPTIVE
  canonical_stage18_g18_modified: false

frozen_whole_working:
  repo: Csthv/p02-phase02-final-whole-working-20260814t052120z-b890ff92
  revision: bc14961e14f2e48690e55df3577014275f9cbf30
  policy: READ_ONLY_IMMUTABLE_BASELINE

github_ready:
  repo: Csthv/iharq-p02-stage24-replay-github-ready-r1-20260814t060824z
  historical_tree_revision: c805487d24ab9727d86b63be74efb68b6b392476
  historical_tree_manifest:
    path: github_ready/CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json
    sha256: a6694a3d550e33c7bcbbff2f22b0beddc878ae403bb8646aa9c5ca7afb69c8ce
    manifest_id: IHARQ-GITHUB-READY-THROUGH-P02-STAGE24-REPLAY-R1
    files_count: 27080
  annex_content_revision: c7504a1719ca7af9e44d849c0802a732099ed365
  annex_pointer_revision: 84201e72d1ff8ffdd14b17cbbceec2857a14b436
  changed_new_light_files: 3738
  light_uploaded_gib: 0.213472
  heavy_bytes_reuploaded: 0
  unchanged_bytes_reuploaded: 0

historical_archival:
  repo: Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260814t051352z
  annex_control_revision: 1bb0d70013fddf5e475468b7925e0dd636602e59
  annex_pointer_revision: d2de83414bd5a3c452bcab7820d126999c5ff661
  historical_r2_pointer_manifest_overwritten: false
  heavy_bytes_reuploaded: 0
  unchanged_bytes_reuploaded: 0

current_extension_heavy_release:
  repo: Csthv/iharq-p02-phase02-r2-P02-L2-OFFICIAL-RUN-R4DY-20260817t182318z
  latest_verified_revision: 1abb59c6d8b6002d86ef72571bed46d9af028569
  heavy_content_revision: 7f43cf3a9ea4b2056d96b9d2135bc14eac605b90
  heavy_logical_files_resolved: 758
  heavy_changed_new_gib: 2.535035
  verified_heavy_remote_objects: 47

delta_accounting:
  current_files_considered: 21504
  changed_or_new_files: 4496
  baseline_hash_reuse_no_upload: 51
  unchanged_not_uploaded: 16957
  unchanged_bytes_not_uploaded_gib: 9.241335
  heavy_bytes_reuploaded_gib: 0.0
  light_bytes_uploaded_gib: 0.213472

future_resolution_order:
  - extension_annex
  - annex_location_index
  - current_light_in_github_ready_annex
  - current_heavy_in_extension_release
  - exact_historical_hash_reuse
  - historical_fallback

final_markers:
  - IHARQ_P02_EXTENSION_ANNEX_FINAL_PASS
  - IHARQ_P02_64_128_256_ARTIFACT_RESOLUTION_READY_FOR_P03
```

---

# 17. Final Status

The P02 64/128/256 extension publication is **closed**.

The final storage model is reuse-first, non-destructive, hash-addressed, and annex-first:

```text
No scientific rerun required.
No historical baseline mutation.
No historical R2 manifest overwrite.
No unchanged-file re-upload.
No heavy-artifact duplicate upload.
Current corrected lightweight files published.
Current heavy files resolved to the existing extension release.
Future P03+ lookup contract established.
```

**Final status: READY FOR P03+ CONSUMPTION THROUGH THE EXTENSION-ANNEX RESOLUTION CONTRACT.**
