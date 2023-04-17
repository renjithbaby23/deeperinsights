"""Initialise file parser."""
import logging
import os
from abc import ABC, abstractmethod
from pathlib import Path

from solution.utils.configure_logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class FileParser(ABC):
    """Abstract class for file parsers."""

    def __init__(self, file_path: str):
        """Init for the abstract class."""
        self.file_path: Path = Path(file_path)
        self.source_text: list = list()
        self.search_term: str = ""
        self._validate_path()

    def _validate_path(self) -> None:
        """Check if the path given is valid.

        Raises:
            IsADirectoryError
            FileNotFoundError
            PermissionError
        """
        if self.file_path.is_dir():
            error = f"'{self.file_path}' is a directory! " f"Expecting a file."
            raise IsADirectoryError(error)
        if self.file_path.is_file():
            logger.debug(f"File '{self.file_path}' is a valid file.")
        else:
            error = f"Invalid path! File '{self.file_path}' doesn't exist!"
            logger.error(error)
            raise FileNotFoundError(error)
        if not os.access(self.file_path, os.R_OK):
            error = (
                f"File '{self.file_path}' has no read permission! "
                f"Please provide read access."
            )
            logger.error(error)
            raise PermissionError(error)

    @abstractmethod
    def read_and_parse(self) -> None:
        """Abstract method definition."""
        pass

    def __call__(self):
        """Do the file parsing."""
        self.read_and_parse()
        return self.source_text, self.search_term
