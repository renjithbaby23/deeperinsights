"""Unit test for content formatter."""

import pytest

from solution.content_formatter.textfile_formatter import TextContentFormatter


class TestTextContentFormatter:
    """Unit tests for text content formatter."""

    @pytest.fixture
    def formatter(self):
        """Fixture creating class instance."""
        return TextContentFormatter()

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                ["123a123Sample*7567_test123."],
                ["a Sample test"],
            ),
            ([" this 12@is34  123another"], ["this is another"]),
        ],
    )
    def test_format_with_valid_data(
        self, formatter, input_data, expected_output
    ):
        """Test with valid data."""
        res = formatter.format(input_data)
        assert res == expected_output

    def test_format_with_empty_list(self, formatter):
        """Test with empty list."""
        input_data = []
        expected_output = []
        assert formatter.format(input_data) == expected_output

    def test_format_with_invalid_data_type(self, formatter):
        """Test with invalid data types."""
        input_data = "Sample string input instead of list."
        with pytest.raises(ValueError):
            formatter.format(input_data)

    def test_format_with_invalid_data_items(self, formatter):
        """Test with invalid data types."""
        input_data = ["String1", 123, True]
        with pytest.raises(ValueError):
            formatter.format(input_data)
