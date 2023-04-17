"""Pattern matching."""

import logging
from typing import List

from solution.utils.configure_logger import configure_logger

configure_logger(level=logging.ERROR)
logger = logging.getLogger(__name__)


def does_line_match(source_line: str, search_term: str) -> bool:
    """Check if a source line has a matching search_term.

    Args:
        source_line: source text lines
        search_term: query used for pattern matching

    Returns:
        bool: True if the search term is found in the source_line
    """
    if not isinstance(source_line, str):
        error = f"Invalid input text encountered - {source_line}"
        raise ValueError(error)
    if not isinstance(search_term, str):
        error = f"Invalid search term encountered - {search_term}"
        raise ValueError(error)
    elif len(search_term) < 1:
        error = "Empty search term encountered!"
        raise ValueError(error)
    return search_term.lower() in source_line.lower()


def get_matching_lines(source_text: List[str], search_term: str) -> List[int]:
    """Get the matching line indices.

    Args:
        source_text: input text formatted
        search_term: search term
    Returns:
        object:
    """
    result_idx = []
    for idx, text in enumerate(source_text):
        if does_line_match(text, search_term):
            result_idx.append(idx)
    return result_idx


def print_matching_line(text: str) -> None:
    """Print the matching lines in desired format."""
    words = text.split()
    formatted_text = "[" + " ".join(words) + "]"
    print(formatted_text)


def print_matching_lines(source_text: List[str], idx_list: List[int]) -> None:
    """Print all the matching lines from the list of lines."""
    for idx, text in enumerate(source_text):
        if idx in idx_list:
            print_matching_line(text)
