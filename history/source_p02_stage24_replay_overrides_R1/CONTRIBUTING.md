# Contributing

## Scope

Contributions must respect the current Phase 0 boundary: repository, configuration, record-schema, validation, provenance, claim-governance, and handoff foundations. Do not introduce empirical findings or activate later-phase work through an ordinary code change.

## Required practice

1. Identify the controlling authority and affected phase/layer.
2. Use a focused branch and explain the change, downstream consumers, migrations, invalidations, and claim impact.
3. Update schemas, configurations, contracts, fixtures, tests, manifests, and documentation together when their interfaces change.
4. Run:

```bash
python scripts/verify_runtime_lock.py
python -m pytest -q -p no:cacheprovider
python scripts/verify_publication_tree.py
python scripts/run_local_reproduction.py --no-write-report
```

5. Preserve negative evidence and fail-closed behavior.
6. Do not silently change Protocol timing, claim wording, authority ownership, or current/superseded status.

## Pull requests

Use `.github/PULL_REQUEST_TEMPLATE.md`. A pull request should state the authority, phase/layer scope, tests, evidence gates, migrations, limitations, and security review. GitHub CI is not a Phase 0 evidence gate; local evidence remains controlling.
