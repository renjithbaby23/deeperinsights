"""Logger configuration."""

import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import Optional


def configure_logger(
    log_path: Optional[Path] = None, level=logging.WARNING
) -> None:
    """Configure the logging."""
    handler1: logging.Handler = logging.StreamHandler()
    handlers = [handler1]
    if log_path is not None:
        handler2: logging.Handler = TimedRotatingFileHandler(
            log_path, when="D", interval=1, backupCount=3
        )

        handlers.append(handler2)

    logging.basicConfig(
        level=level,
        format="%(asctime)s.%(msecs)03d] [PID-%(process)d] "
        "[%(funcName)s-%(lineno)d]-[%(levelname)s] : %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        handlers=handlers,
    )
