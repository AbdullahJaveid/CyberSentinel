"""Application configuration for CyberSentinel."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
BASELINES_DIR = DATA_DIR / "baselines"
REPORTS_DIR = DATA_DIR / "reports"
LOGS_DIR = DATA_DIR / "logs"


@dataclass(frozen=True, slots=True)
class Settings:
    """Immutable runtime settings loaded from safe environment variables."""

    app_name: str = "CyberSentinel"
    environment: str = "development"
    log_level: str = "INFO"
    log_to_file: bool = True
    max_scan_workers: int = 10
    default_scan_timeout_seconds: float = 1.0
    database_url: str = f"sqlite:///{DATA_DIR / 'cybersentinel.db'}"

    @property
    def is_development(self) -> bool:
        """Return whether the app is using development settings."""
        return self.environment.lower() == "development"


def _read_bool(name: str, default: bool) -> bool:
    """Read a boolean environment variable with safe fallback behavior."""
    value = os.getenv(name)
    if value is None:
        return default

    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False

    return default


def _read_int(name: str, default: int, minimum: int) -> int:
    """Read an integer environment variable and enforce a lower bound."""
    raw_value = os.getenv(name, str(default))
    try:
        value = int(raw_value)
    except ValueError:
        return default

    return max(value, minimum)


def _read_float(name: str, default: float, minimum: float) -> float:
    """Read a float environment variable and enforce a lower bound."""
    raw_value = os.getenv(name, str(default))
    try:
        value = float(raw_value)
    except ValueError:
        return default

    return max(value, minimum)


def ensure_data_directories() -> None:
    """Create local application directories if they do not already exist."""
    for directory in (DATA_DIR, BASELINES_DIR, REPORTS_DIR, LOGS_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def get_settings() -> Settings:
    """Build validated settings from the environment."""
    ensure_data_directories()

    return Settings(
        environment=os.getenv("CYBERSENTINEL_ENV", "development"),
        log_level=os.getenv("CYBERSENTINEL_LOG_LEVEL", "INFO").upper(),
        log_to_file=_read_bool("CYBERSENTINEL_LOG_TO_FILE", True),
        max_scan_workers=_read_int(
            "CYBERSENTINEL_MAX_SCAN_WORKERS",
            default=10,
            minimum=1,
        ),
        default_scan_timeout_seconds=_read_float(
            "CYBERSENTINEL_SCAN_TIMEOUT",
            default=1.0,
            minimum=0.1,
        ),
        database_url=os.getenv(
            "CYBERSENTINEL_DATABASE_URL",
            f"sqlite:///{DATA_DIR / 'cybersentinel.db'}",
        ),
    )
