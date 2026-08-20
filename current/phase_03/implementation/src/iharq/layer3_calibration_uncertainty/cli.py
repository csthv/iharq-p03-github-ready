"""Typer CLI for local/Kaggle parity and controlled recovery."""

from __future__ import annotations

from pathlib import Path


def build_app():
    import typer
    from .bootstrap import context_from_record
    from .orchestration import NotebookController

    app = typer.Typer(add_completion=False, no_args_is_help=True, rich_markup_mode=None)

    @app.command("run-stage")
    def run_stage(context_record: Path, stage_id: str) -> None:
        controller = NotebookController(context_from_record(context_record))
        try:
            typer.echo(controller.run_stage(stage_id))
        finally:
            controller.shutdown()

    @app.command("recover")
    def recover(context_record: Path) -> None:
        controller = NotebookController(context_from_record(context_record))
        typer.echo(controller.recover())

    return app


def main() -> None:
    build_app()()


if __name__ == "__main__":
    main()

