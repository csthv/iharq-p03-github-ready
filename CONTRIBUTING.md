# Contributing

## Scope and authority

This repository is the cumulative governed state through P02. Contributions must identify the controlling authority, phase/layer, canonical source, downstream consumers, and whether the change is documentary, implementation, scientific, or presentation-only.

Do not silently mutate frozen P00/P01/P02 scientific identities, results, exclusions, claim wording, post-hoc status, external revisions, or canonical/superseded state. New P03 work must begin from the P03 intake/reuse decision process rather than modifying P02 evidence in place.

## Required practice

1. State the affected phase/layer and controlling authority.
2. Classify the change as `REUSE`, `RERUN`, `EXTEND`, `IMPLEMENT`, `BLOCK`, or `N/A` where the current Build Book requires that lifecycle decision.
3. Update code, configuration, schemas, contracts, tests, manifests, handoffs, limitations, and documentation together when their interfaces change.
4. Preserve negative evidence and superseded history.
5. Keep Layer 10 read-only with respect to scientific meaning and Layer 0 claim boundaries.
6. Never commit literal credentials.

Run at minimum:

```bash
python scripts/verify_cumulative_release.py
python -m compileall -q src
python -m pytest -q -p no:cacheprovider
```

Phase-specific validators remain applicable to their preserved phase packages. The P02 replay/implementation validators live under `current/phase_02/`.
