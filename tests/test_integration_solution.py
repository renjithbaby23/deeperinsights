"""Integration tests for solution module."""

import os
import tempfile

import solution.pattern_matcher as pm
from solution.content_formatter.textfile_formatter import TextContentFormatter
from solution.file_parser.textfile_parser import TextFileParser


def test_solution(capsys):
    """Integration test for solution."""
    # Create a temporary file with some text
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmpfile.write(b"This is some sample text.\n")
        tmpfile.write(b"Another line of text.\n")
        tmpfile.write(b"This line contains the pattern.\n")
        tmpfile.write(b"Yet another line of text with patt ern.\n")
        tmpfile.write(b"123And one456more line&^% of text.\n")
        tmpfile.write(b"1@This #$line also4$contains! the 1#pattern#@.\n")
        tmpfile.write(b"pattern\n")

    expected_output = (
        "[This line contains the pattern]\n"
        "[This line also contains the pattern]\n"
    )

    # Parse the temporary file
    file_parser = TextFileParser(tmpfile.name)
    source_text, search_term = file_parser()

    # Format the matching lines
    content_formatter = TextContentFormatter()
    formatted_source_text = content_formatter.format(source_text)

    idx_list = pm.get_matching_lines(formatted_source_text, search_term)
    pm.print_matching_lines(formatted_source_text, idx_list)

    # Assert the formatted output matches the expected result
    captured = capsys.readouterr()
    assert captured.out == expected_output

    # Cleanup - delete the temporary file
    os.remove(tmpfile.name)
