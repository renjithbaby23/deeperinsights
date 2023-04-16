"""Integration tests for solution module."""

import os
import tempfile

from solution.content_formatter.textfile_formatter import TextContentFormatter
from solution.file_parser.textfile_parser import TextFileParser
from solution.pattern_matcher import get_matching_lines


def test_solution():
    """Integration test for solution."""
    # Create a temporary file with some text
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmpfile.write(b"This is some sample text.\n")
        tmpfile.write(b"Another line of text.\n")
        tmpfile.write(b"This line contains the pattern.\n")
        tmpfile.write(b"Yet another line of text.\n")
        tmpfile.write(b"And one more line of text.\n")

    # Parse the temporary file
    source_text = TextFileParser(tmpfile.name)

    # Find the matching lines
    search_term = "pattern"
    matching_indices = get_matching_lines(source_text, search_term)

    # Format the matching lines
    formatted_text = TextContentFormatter(source_text, matching_indices)

    # Assert the formatted output matches the expected result
    expected_output = "[This line contains the pattern.]"
    assert formatted_text == expected_output

    # Delete the temporary file
    os.remove(tmpfile.name)
