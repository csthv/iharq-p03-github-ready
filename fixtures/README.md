# Fixture index

Fixtures are engineering validation inputs, not empirical research results.

- `valid/`: accepted canonical examples;
- `integrated/`: cross-layer, cross-phase, and handoff chains;
- `invalid/`: malformed cases expected to fail closed.

The invalid filename generally names the violated invariant. The associated public tests under `tests/` verify rejection. The complete internal fixture and adversarial corpus remains preserved in the R5 release-assets archive; this clean tree retains every distinct category required by the public operational suite.
