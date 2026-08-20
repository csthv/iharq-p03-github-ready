# Reproduction

## Accepted environment

- verified Python: 3.13.5;
- Python 3.11: unverified environment unavailable;
- Python 3.12: unverified environment unavailable;
- portable `uv.lock`: incomplete/non-authoritative and omitted.

## Commands

```bash
python -m pip install -r requirements-lock.txt
python -m pip install -e . --no-deps --no-build-isolation
python scripts/verify_runtime_lock.py
python -m iharq.cli local test
python -m iharq.cli local reproduce
python scripts/verify_publication_tree.py
```

The clean-reproduction script copies the tree to a temporary directory and runs the public suite without relying on GitHub CI.
