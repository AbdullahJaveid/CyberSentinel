"""Safe application logging utilities."""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler

from app.config import LOGS_DIR, Settings


LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"


def configure_logging(settings: Settings) -> None:
    """
    Configure application logging once.

    Passwords, tokens, credentials, and file contents must never be passed
    into log messages by calling code.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level)

    if root_logger.handlers:
        return

    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    if settings.log_to_file:
        log_path = LOGS_DIR / "cybersentinel.log"
        file_handler = RotatingFileHandler(
            log_path,
            maxBytes=1_000_000,
            backupCount=3,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    """Return a named logger for a CyberSentinel module."""
    return logging.getLogger(name)
