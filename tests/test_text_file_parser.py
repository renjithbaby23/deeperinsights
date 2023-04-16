"""Test for text file_parser."""

import os
import tempfile

import pytest

from solution.file_parser.textfile_parser import TextFileParser


class TestTextFileParser:
    """Tests for TextFileParser class."""

    def write_to_temp_file(self, content):
        """Utility function to write to temporary file."""
        self.tmp_file.write(content)
        self.tmp_file.close()

    def setup_method(self):
        """Setup."""
        self.tmp_file = tempfile.NamedTemporaryFile(delete=False)

    def teardown_method(self):
        """Teardown."""
        os.unlink(self.tmp_file.name)

    @pytest.mark.parametrize(
        "content, expected_result",
        [
            (
                b"Sample123Entry   _here212!\n\nsearchterm",
                (["Sample123Entry   _here212!"], "searchterm"),
            ),
            (
                b"Sample123Entry_here212!\n"
                b"Another123Entry   _here212!\n\nsearchterm",
                (
                    [
                        "Sample123Entry_here212!",
                        "Another123Entry" "   _here212!",
                    ],
                    "searchterm",
                ),
            ),
        ],
    )
    def test_read_and_parse(self, content, expected_result):
        """Read and parse on a valid entry."""
        self.write_to_temp_file(content)

        fp = TextFileParser(self.tmp_file.name)
        fp.read_and_parse()
        assert fp.source_text == expected_result[0]
        assert fp.search_term == expected_result[1]

    @pytest.mark.parametrize(
        "content, expected_result",
        [
            (
                b"Sample123Entry   _here212!\n\nsearchterm",
                (["Sample123Entry   _here212!"], "searchterm"),
            ),
            (
                b"Sample123Entry_here212!\n"
                b"Another123Entry   _here212!\n\nsearchterm",
                (
                    ["Sample123Entry_here212!", "Another123Entry   _here212!"],
                    "searchterm",
                ),
            ),
        ],
    )
    def test_call(self, content, expected_result):
        """Test the class call function on a valid entry."""
        self.write_to_temp_file(content)

        fp = TextFileParser(self.tmp_file.name)
        result = fp()
        assert result == expected_result

    def test_call_with_empty_file(self):
        """Test the class call function on an empty file."""
        fp = TextFileParser(self.tmp_file.name)
        with pytest.raises(
            ValueError, match=f"Empty file - {self.tmp_file.name}"
        ):
            fp()

    def test_call_with_oneline_file(self):
        """Test the class call function on a file without source_text."""
        content = b"searchterm"
        self.write_to_temp_file(content)
        fp = TextFileParser(self.tmp_file.name)
        with pytest.raises(
            ValueError, match=f"No content found - {self.tmp_file.name}"
        ):
            fp()
