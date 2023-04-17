"""Text file parser."""
import logging

from solution.file_parser import FileParser
from solution.utils.configure_logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class TextFileParser(FileParser):
    """Concrete implementation of text file parser."""

    def __init__(self, file_path: str):
        """Init.

        Args:
            file_path: path to the input text file
        """
        super().__init__(file_path)

    def _extract_source_and_search_term(self, file_content: list) -> None:
        """Extract source and search terms."""
        # search term is the last non-empty entry in the file
        self.search_term = file_content.pop()
        self.source_text = file_content

    def _check_sanity(self, source_text) -> None:
        """Check the file contents for sanity."""
        if len(source_text) == 0:
            error = (
                f"Empty file - {self.file_path}! "
                f"Please provide valid file."
            )
            logger.error(error)
            raise ValueError(error)
        elif len(source_text) == 1:
            error = (
                f"File with only one line - {self.file_path}!"
                f"Expecting at least one line for source_text "
                f"and another line for search term."
            )
            logger.error(error)
            raise ValueError(error)

    def read_and_parse(self) -> None:
        """Implementation of read and parse."""
        with open(self.file_path, "r") as file:
            source_text = file.readlines()
            source_text = [line.strip() for line in source_text]

        self._check_sanity(source_text)

        self._extract_source_and_search_term(source_text)

        logger.debug(f"The source text is: \n{self.source_text}\n")
        logger.debug(f"The search term: '{self.search_term}'")
