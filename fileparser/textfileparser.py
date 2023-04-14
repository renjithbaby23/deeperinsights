"""Text file parser."""
import logging

from fileparser import FileParser
from utils.configure_logger import configure_logger

configure_logger(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TextFileParser(FileParser):
    """Concrete implementation of text file parser."""

    def __init__(self, file_path: str):
        """Init."""
        super().__init__(file_path)

    def _extract_source_and_search_term(self, file_content: list):
        """Extract source and search terms."""
        # search term is the last non-empty entry in the file
        self.search_term = file_content.pop()
        self.source_text = file_content

    def _check_sanity(self, source_text):
        """Check the file contents for sanity."""
        if len(source_text) == 0:
            error = f"Empty file - {self.file_path}"
            logger.error(error)
            raise ValueError(error)
        elif len(source_text) == 1:
            error = f"No content found - {self.file_path}"
            logger.error(error)
            raise ValueError(error)

    def read_and_parse(self) -> None:
        """Implementation of read and parse."""
        with open(self.file_path, "r") as file:
            source_text = file.readlines()
            source_text = [
                line.strip() for line in source_text if line.strip() != ""
            ]

        self._check_sanity(source_text)

        self._extract_source_and_search_term(source_text)

        logger.debug(f"The source text is: \n{self.source_text}\n")
        logger.info(f"The search term: '{self.search_term}'")
