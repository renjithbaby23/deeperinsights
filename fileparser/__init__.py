"""Initialise file parser."""
import logging
from abc import ABC, abstractmethod
from pathlib import Path

from utils.configure_logger import configure_logger

configure_logger(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class FileParser(ABC):
    """Abstract class for file parsers."""

    def __init__(self, file_path: str):
        """Init for the abstract class."""
        self.file_path: Path = Path(file_path)
        self.source_text: list = list()
        self.search_term: str = ""

    def _validate_path(self) -> None:
        """Check if the path given is valid."""
        if self.file_path.is_file():
            logger.info(f"File '{self.file_path}' is a valid file.")
            return
        else:
            error = f"File '{self.file_path}' doesn't exist!"
            logger.warning(error)
            raise FileNotFoundError(error)

    @abstractmethod
    def read_and_parse(self) -> None:
        """Abstract method definition."""
        pass

    def __call__(self):
        """Do the file parsing."""
        self._validate_path()
        self.read_and_parse()
        return self.source_text, self.search_term
