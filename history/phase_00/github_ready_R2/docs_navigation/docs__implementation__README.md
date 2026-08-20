# Implementation guide

The directly browsable implementation is under `src/iharq/`, with machine interfaces in `schemas/`, `configs/`, and `contracts/`.

The current Build Book distribution is [../phase_00/final_documents/01_IHARQ_Master_Implementation_Build_Book_Current.md](../phase_00/final_documents/01_IHARQ_Master_Implementation_Build_Book_Current.md). The Phase 0 implementation/finalization annex is [../phase_00/final_documents/02_IHARQ_Phase_0_Implementation_and_Finalization_Annex_Current.md](../phase_00/final_documents/02_IHARQ_Phase_0_Implementation_and_Finalization_Annex_Current.md).

Local verification:

```bash
python -m pip install -r requirements-lock.txt
python -m pip install -e . --no-deps --no-build-isolation
python -m pytest -q -p no:cacheprovider
python scripts/verify_publication_tree.py
```
