# Required Kaggle inputs — R5 HF-enabled package

Before the actual governed run, attach the following.

## Required Kaggle inputs

1. **P02 R5 implementation package**
   - file: `IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R5.zip`
   - role: code/config/contracts/notebook support
   - required: YES

2. **Cumulative P00+P01 repository ZIP**
   - file: `IHARQ_Cumulative_GitHub_Ready_Through_P01_R1.zip`
   - SHA-256: `dc2708ab70e7746499ae09760456825b54efcf587cae3db3410e6f72b0024542`
   - role: current authority/project state and P01→P02 handoff

3. **P01 core derived-window Kaggle Dataset**
   - handle: `csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473`
   - provider version: 2
   - logical revision: 1
   - manifest SHA-256: `dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1`
   - expected core windows: 12,910

4. **P01 A4 R2 Kaggle Dataset**
   - handle: `csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108`
   - provider version: 1
   - logical revision: 2
   - manifest SHA-256: `29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305`
   - expected matched parents: 12,910 / 12,910
   - expected A4 WindowRecords: 51,640

## Hugging Face conditional assets

A separate checkpoint Kaggle Dataset is **not required** for the normal R5 run.

Stage 03 can retrieve scientifically eligible governed Hugging Face assets from their exact immutable repositories/revisions and verify hashes before admission. The previous `IHARQ_P02_CONDITIONAL_MODEL_ASSETS.json` mechanism remains an optional offline fallback.

## Hugging Face token

- preferred unattended source: private Kaggle Secret named `HF_TOKEN`
- interactive fallback: hidden `getpass()` cell before Stage 03
- blank is allowed for public eligible assets such as the current CBraMod checkpoint
- token values are memory-only, never serialized, and cleared immediately after Stage 03
- authentication never overrides scientific/license/corpus-overlap/input/resource gates

## Required runtime settings

- Internet ON for governed HF retrieval and exact dependency installation if required
- GPU accelerator for the full run
- one complete notebook execution lineage; no alternative scientific mode
