"""Logging configuration."""

import logging

from rich.logging import RichHandler


def get_logger(name: str, log_file: str | None = None) -> logging.Logger:
    """Configure and return a logger with rich console output.

    Args:
        name: Logger name (usually module __name__).
        log_file: Optional file path to also write logs.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        console = RichHandler(rich_tracebacks=True)
        console.setFormatter(logging.Formatter("%(message)s", datefmt="[%X]"))
        logger.addHandler(console)

        if log_file:
            fh = logging.FileHandler(log_file, encoding="utf-8")
            fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
            logger.addHandler(fh)

    return logger
