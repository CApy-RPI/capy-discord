import datetime
import logging
import logging.handlers
from pathlib import Path

from capy_discord.config import settings


def setup_logging() -> None:
    """Set up logging for the application."""
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_level = logging.getLevelNamesMapping()[settings.log_level.upper()]
    log_file = f"{datetime.datetime.now(datetime.UTC).date()}.log"

    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Root logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        log_dir / log_file,
        maxBytes=1024 * 1024 * 5,  # 5 MB
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(file_handler)
