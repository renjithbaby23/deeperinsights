"""Unit tests for pattern matcher."""

import pytest

from solution.pattern_matcher import (
    does_line_match,
    get_matching_lines,
    print_matching_line,
    print_matching_lines,
)


@pytest.fixture
def source_text():
    """Sample input."""
    return [
        "This is a test string.",
        "Another test string.",
        "This is a third test string.",
    ]


def test_does_line_match():
    """Tests for finding matching line."""
    assert does_line_match("This is a test string.", "test")
    assert does_line_match("This is a test string.", "Test")
    assert does_line_match("Another test string.", "TEST")
    assert not does_line_match("This is a test string.", "tests")
    assert not does_line_match("This is a third test string.", "foo")
    assert not does_line_match("", "foo")

    with pytest.raises(ValueError):
        does_line_match(None, "foo")

    with pytest.raises(ValueError):
        does_line_match("foo", None)

    with pytest.raises(ValueError):
        does_line_match("foo", "")


def test_get_matching_lines(source_text):
    """Tests for matching line."""
    assert get_matching_lines(source_text, "test") == [0, 1, 2]
    assert get_matching_lines(source_text, "third") == [2]
    assert get_matching_lines(source_text, "foo") == []
    assert get_matching_lines([], "test") == []
    with pytest.raises(ValueError):
        get_matching_lines(source_text, "")


def test_print_matching_line(capsys):
    """Test print output line using pytest builtin fixture 'capsys'."""
    print_matching_line("This is a test string.")
    captured = capsys.readouterr()
    assert captured.out == "[This is a test string.]\n"


def test_print_matching_lines(source_text, capsys):
    """Test print output lines using pytest builtin fixture 'capsys'."""
    print_matching_lines(source_text, [0, 2])
    captured = capsys.readouterr()
    expected_out = "[This is a test string.]\n[This is a third test string.]\n"
    assert captured.out == expected_out
