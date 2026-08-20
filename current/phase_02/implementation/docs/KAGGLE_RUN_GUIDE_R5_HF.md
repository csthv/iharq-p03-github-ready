# IHARQ Phase 02 — Final Kaggle Run Guide R5 (Hugging Face Conditional Assets)

## What to run

Use exactly one scientific notebook:

`IHARQ_Phase_02_Complete_Execution_and_Analysis_R4_HF_R1.ipynb`

Attach the matching implementation input package:

`IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R5.zip`

Do not edit model, training-policy, A0/A4, seed, metric, statistical, record, gate, or artifact settings. P02 retains 678 A0 cells + 1,218 A4 slots = 1,896 official phase-owned ablation cells. The separate EEGNet S&R challenger remains diagnostic and outside A-number accounting.

---

## 1. Create/import the Kaggle notebook

1. Open Kaggle Notebooks.
2. Import `IHARQ_Phase_02_Complete_Execution_and_Analysis_R4_HF_R1.ipynb`.
3. Keep the notebook unchanged.

## 2. Configure runtime

1. Select a GPU accelerator.
2. Turn Internet **ON**. The notebook needs network access for exact pinned Python-package installation when necessary and for governed Hugging Face asset retrieval.
3. Do not substitute package versions if the exact environment cannot be materialized. Stage 01 is fail-closed.

## 3. Attach the P02 implementation package

Create/attach a **private Kaggle Dataset** containing exactly:

`IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R5.zip`

Suggested Kaggle Dataset title: `IHARQ P02 L2 Implementation R5`

The notebook finds this exact ZIP under `/kaggle/input`, checks ZIP safety/CRC, extracts it to `/kaggle/working`, and verifies the package `checksums.sha256` before project imports.

Do not attach R4 and R5 implementation packages simultaneously.

## 4. Attach cumulative P00+P01 repository

Attach a private Kaggle Dataset containing:

`IHARQ_Cumulative_GitHub_Ready_Through_P01_R1.zip`

Required SHA-256:

`dc2708ab70e7746499ae09760456825b54efcf587cae3db3410e6f72b0024542`

Suggested Kaggle Dataset title: `IHARQ Cumulative P00 P01 R1`

Do not extract/repack the ZIP. Renaming the file to the canonical filename is acceptable only if its bytes remain unchanged.

## 5. Attach P01 core Dataset

Attach:

`csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473`

Expected contract:

- provider version: 2
- logical immutable revision: 1
- manifest: `IHARQ_P01_L1_DERIVED_WINDOW_DATASET_MANIFEST.json`
- manifest SHA-256: `dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1`
- core windows: 12,910

## 6. Attach P01 A4 R2 Dataset

Attach:

`csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108`

Expected contract:

- provider version: 1
- logical revision: 2
- manifest: `IHARQ_P01_L1_A4_DERIVED_WINDOW_DATASET_MANIFEST.json`
- manifest SHA-256: `29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305`
- matched parents: 12,910 / 12,910
- A4 WindowRecords: 51,640

## 7. Hugging Face authentication — no checkpoint Dataset required

You no longer need to create a separate Kaggle Dataset containing CBraMod/REVE weights.

### Preferred path: Kaggle Secret

For unattended **Save & Run All**:

1. Create a Hugging Face user access token with read-only/fine-grained read access sufficient for the governed repositories you are authorized to access.
2. In the Kaggle notebook, open **Add-ons / Secrets** (UI wording can vary).
3. Add a secret named exactly:

   `HF_TOKEN`

4. Give the notebook permission to use that secret.

The notebook's Hugging Face preflight cell reads `HF_TOKEN` through Kaggle's secret provider. The token value is never printed or written into IHARQ configuration, logs, manifests, stage artifacts, checkpoints, or the final execution bundle.

### Interactive fallback

If no Kaggle Secret is available, run the notebook interactively. Immediately before Stage 03, the notebook executes a hidden `getpass()` prompt. Paste your Hugging Face token there. It is not echoed.

You may submit a blank value. CBraMod's governed repository is public, so its current P02 checkpoint can be retrieved without authentication. A token is needed only for a future branch/repository that is both scientifically eligible and access-gated.

### Token lifetime

The credential is held in memory only for Stage 03 conditional-asset resolution. After Stage 03 succeeds, the notebook calls `SESSION.clear_hf_token()` and sets its notebook token variable to `None`.

The implementation deliberately does **not** call persistent Hugging Face `login()`.

## 8. What Hugging Face retrieval does in this P02 run

### CBraMod

Current P02 automatically resolves the maintained Braindecode checkpoint from:

`braindecode/cbramod-pretrained`

at the exact immutable revision recorded in `configs/phase_02/models/huggingface_assets.yaml`.

The required `model.safetensors` SHA-256 is independently checked before branch admission. The package uses the maintained Braindecode CBraMod implementation through the IHARQ adapter and retains all existing license, corpus-overlap, input-compatibility, resource and checkpoint-reload gates.

### REVE

The implementation supports gated Hugging Face authentication operationally, but **current P02 does not download or admit REVE**. Its current frozen branch state is blocked by the project's pretraining-corpus-overlap gate. Authentication cannot override a scientific gate.

Therefore, do not interpret possession of a REVE token/access grant as permission to execute REVE in this run.

### Offline fallback

The prior `IHARQ_P02_CONDITIONAL_MODEL_ASSETS.json` mechanism remains supported. If a verified pre-attached asset is supplied, it is considered before Hugging Face retrieval. This is an offline fallback, not a requirement for the normal R5 run.

## 9. Start the governed run

After inputs, Internet, GPU and (optionally) `HF_TOKEN` are configured:

1. For an interactive sanity start, execute from the top.
2. For the actual long run, use Kaggle's **Save Version / Save & Run All** once configuration is correct.
3. Do not launch two concurrent copies of the same scientific run.

The HF cell appears after Stage 02 and before Stage 03. If you configured `HF_TOKEN` as a Kaggle Secret, no interaction is required during Save & Run All.

## 10. Preflight 00–07

Do not bypass failures. These stages verify authorities, environment/resources, cumulative state, P01 pointers/HF assets, immutable P01 inputs, scientific freeze/training-policy amendment, import/schema integrity and role firewall.

If Stage 03 reports a CBraMod download/checksum/network failure, preserve the exact status. Do not replace the checkpoint with an arbitrary model file. A conditional branch can be visibly blocked without changing the mandatory P02 baseline floor.

## 11. Scientific stages

The notebook then follows the unchanged governed sequence:

- 08 sanity/negative controls
- 09 classical anchors
- 10 Riemannian anchors
- 11 compact neural + training-policy challenger
- 12 conditional deep/SSL branches, including eligible CBraMod
- 13 checkpoint/model-registry closure
- 14 PredictionRecord closure
- 15 A0 + training-policy closure
- 16 low-label curves
- 17 participant/session profiles
- 18 A4 C0–C5 + C4/C5 strongest-constituent inference
- 18U additional-ablation authority check
- 19 failure/negative/diagnostic evidence
- 20 downstream readiness
- 21 figure/table source data
- 22 Protocol/Phase-Analysis/Layer0/EvidenceMap/Layer10/P03 handoffs
- 23 evidence sufficiency
- 24 final checksummed execution bundle

## 12. Final output

On Stage 24 success, retrieve:

`/kaggle/working/IHARQ_P02_L2_Phase_Execution_Bundle_<RUN_ID>.zip`

Keep the completed Kaggle notebook/version/logs with that ZIP.

The execution bundle contains provenance for any admitted external checkpoint (repository, revision, hashes and governed status) but **not** your Hugging Face token and not a redistributed gated REVE checkpoint.

## 13. What you need to attach — final checklist

Required Kaggle inputs:

1. `IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R5.zip`
2. `IHARQ_Cumulative_GitHub_Ready_Through_P01_R1.zip`
3. P01 core derived-window Dataset
4. P01 A4 R2 Dataset

Runtime settings:

5. GPU
6. Internet ON
7. Optional but recommended `HF_TOKEN` Kaggle Secret for unattended authenticated HF access

**No separate conditional-model checkpoint Dataset is required for the normal R5 run.**
