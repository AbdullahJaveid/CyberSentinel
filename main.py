"""CyberSentinel command-line entry point."""

from __future__ import annotations

import platform
import sys
from typing import Annotated

import typer

from app import __version__
from app.config import Settings, get_settings
from app.core.logger import configure_logging, get_logger


app = typer.Typer(
    name="cybersentinel",
    help=(
        "CyberSentinel is a defensive cybersecurity assessment platform for "
        "localhost, systems you own, and explicitly authorized networks."
    ),
    no_args_is_help=True,
    add_completion=False,
)

logger = get_logger(__name__)


def _settings() -> Settings:
    """Load settings and configure logging for a CLI command."""
    settings = get_settings()
    configure_logging(settings)
    return settings


@app.callback()
def main_callback(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            help="Show the CyberSentinel version and exit.",
            is_eager=True,
        ),
    ] = False,
) -> None:
    """CyberSentinel defensive assessment commands."""
    if version:
        typer.echo(f"CyberSentinel {__version__}")
        raise typer.Exit()


@app.command()
def status() -> None:
    """Show application readiness and non-sensitive runtime configuration."""
    settings = _settings()

    logger.info(
        "status_check_completed environment=%s python=%s",
        settings.environment,
        platform.python_version(),
    )

    typer.echo("CyberSentinel status")
    typer.echo("─" * 24)
    typer.echo("Status: READY")
    typer.echo(f"Version: {__version__}")
    typer.echo(f"Environment: {settings.environment}")
    typer.echo(f"Python: {platform.python_version()}")
    typer.echo(f"Platform: {platform.system()} {platform.release()}")
    typer.echo(f"Maximum scan workers: {settings.max_scan_workers}")
    typer.echo(
        f"Default scan timeout: {settings.default_scan_timeout_seconds:.1f} seconds"
    )
    typer.echo("")
    typer.echo("Authorized use only: localhost, your own systems, or systems")
    typer.echo("for which you have explicit permission to assess.")


@app.command()
def system() -> None:
    """Show a placeholder for the Phase 3 local-system assessment command."""
    _settings()
    typer.echo(
        "The system assessment command will be implemented in Phase 3 "
        "(Network Information)."
    )


@app.command("network-info")
def network_info() -> None:
    """Show a placeholder for the Phase 3 network-information command."""
    _settings()
    typer.echo("Network information gathering will be implemented in Phase 3.")


@app.command()
def scan() -> None:
    """Show a placeholder for the Phase 4 authorized TCP scanner command."""
    _settings()
    typer.echo(
        "The authorized TCP scanner will be implemented in Phase 4. "
        "It will only support targets you own or are explicitly authorized "
        "to assess."
    )


@app.command()
def password() -> None:
    """Show a placeholder for the Phase 2 local password analyzer command."""
    _settings()
    typer.echo(
        "The local-only password analyzer will be implemented in Phase 2. "
        "Passwords will never be logged, stored, or uploaded."
    )


@app.command()
def integrity() -> None:
    """Show a placeholder for the Phase 5 file-integrity command."""
    _settings()
    typer.echo(
        "File-integrity baseline and verification commands will be "
        "implemented in Phase 5."
    )


if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        logger.info("application_interrupted_by_user")
        typer.echo("\nOperation cancelled.", err=True)
        sys.exit(130)
