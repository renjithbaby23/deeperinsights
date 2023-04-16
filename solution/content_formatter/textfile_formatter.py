"""Content formatter init."""

import logging
from typing import List

from solution.content_formatter import ContentFormatter
from solution.utils.configure_logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class TextContentFormatter(ContentFormatter):
    """Text content formatter.

    Usage:
    >> input_text = ["12abc", "1abc def 123", "123", "abc"]
    >> content_formatter = TextContentFormatter()
    >> content_formatter.format(input_text)
       ["abc", "abc def", "", "abc"]
    """

    def __init__(self):
        """Init for the abstract class."""
        super().__init__()
        self.accepted_chars = (
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )

    @staticmethod
    def _validate_data(input_data: List[str]) -> None:
        """Check if the given data is valid."""
        if isinstance(input_data, list) and all(
            isinstance(item, str) for item in input_data
        ):
            logger.debug(f"Source text is valid with length {len(input_data)}")
            return
        else:
            error = "Source data received is not list of strings!"
            logger.error(error)
            raise ValueError(error)

    def _format_text(self, text: str) -> str:
        """Format the given text to text with only alphabets."""
        words = []
        current_word = ""
        for char in text:
            # If the character is an accepted character,
            # add it to the current word
            if char in self.accepted_chars:
                current_word += char
            # else add the current_word to the list of words
            elif current_word:
                words.append(current_word)
                current_word = ""

        # add the last word to the list of words
        if current_word:
            words.append(current_word)

        # Join the words into a single string with spaces between them
        formatted_text = " ".join(words)

        return formatted_text

    def format(self, input_data: List[str]) -> List[str]:
        """Format the input list of texts."""
        self._validate_data(input_data)
        formatted_data = [self._format_text(item) for item in input_data]
        return formatted_data
