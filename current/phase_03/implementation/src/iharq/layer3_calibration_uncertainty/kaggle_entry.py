"""Thin notebook entry points; all scientific behavior remains in package stages."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable
import sys

from .bootstrap import create_execution_context, discover_companion_package, prepare_working_repository, validate_bundled_repository_base
from .orchestration import NotebookController


def bootstrap_kaggle(
    *,
    input_roots: Iterable[str | Path] = ("/kaggle/input",),
    working_root: str | Path = "/kaggle/working/iharq_p03_l3",
    protocol_filename: str = "P03_EXECUTION_FREEZE.yaml",
) -> NotebookController:
    input_roots = list(input_roots)
    companion = discover_companion_package(input_roots)
    base_receipt = validate_bundled_repository_base(companion)
    cumulative = Path(base_receipt["base_root"])
    working_root = Path(working_root)
    repository = working_root / "repository"
    prepare_working_repository(cumulative, companion, repository)

    # C5: make the reconstructed cumulative working repository the package search
    # root for inherited Layer-2 adapters.  The notebook initially imports this
    # entrypoint from the additive companion overlay, which is a namespace-only
    # Layer-3 source.  Extending the already-imported parent package here prevents
    # the C4 failure where `iharq.layer2_decoders` was invisible to the persistent
    # scientific worker, without mutating any P01/P02 source bytes.
    working_src = (repository / "src").resolve()
    working_iharq = (working_src / "iharq").resolve()
    if str(working_src) not in sys.path:
        sys.path.insert(0, str(working_src))
    parent = sys.modules.get("iharq")
    if parent is not None and hasattr(parent, "__path__"):
        package_paths = list(parent.__path__)
        if str(working_iharq) not in package_paths:
            parent.__path__.append(str(working_iharq))

    config = repository / "configs" / "phases" / "p03.yaml"
    protocol_candidates = list(Path(root).rglob(protocol_filename) for root in input_roots if Path(root).exists())
    flattened = [path for group in protocol_candidates for path in group]
    if len(flattened) != 1:
        raise RuntimeError(f"P03_EXECUTION_FREEZE_EXPECTED_ONE: found={len(flattened)} candidates={[path.as_posix() for path in flattened]}")
    protocol = flattened[0]
    context = create_execution_context(repository_root=repository, package_root=companion, working_root=working_root, config_path=config, protocol_path=protocol, authoring_fixture=False)
    return NotebookController(context)
