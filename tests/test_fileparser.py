"""Test for file_parser."""

import os
import tempfile

import pytest

from file_parser import FileParser


class ConcreteFileParser(FileParser):
    """Dummy concrete class of FileParser."""

    def read_and_parse(self):
        """Dummy implementation."""
        pass


class TestFileParser:
    def setup_method(self):
        """Test setup."""
        # creates a dummy file for test
        self.tmp_file = tempfile.NamedTemporaryFile(delete=False)
        self.tmp_file.write(b"Sample11\ncontent for test4343 !\n")
        self.tmp_file.close()
        assert os.path.isfile(
            self.tmp_file.name
        ), f"Couldn't create temp file at {self.tmp_file.name}"

    def teardown_method(self):
        """Test teardown."""
        # delete the temp file created
        os.unlink(self.tmp_file.name)

    def test_valid_file(self):
        """Test with a valid file."""
        file_parser = ConcreteFileParser(self.tmp_file.name)
        assert file_parser._validate_path() is None

    def test_invalid_file(self):
        """Test with an invalid file."""
        with pytest.raises(FileNotFoundError):
            file_parser = ConcreteFileParser("invalid_file.txt")
            file_parser._validate_path()

    def test_call(self):
        """Test call method."""
        file_parser = ConcreteFileParser(self.tmp_file.name)
        result = file_parser()
        # expect the results to be default values
        assert result == ([], "")

    def test_call_with_source_text(self):
        """Test call with overridden source_text."""
        file_parser = ConcreteFileParser(self.tmp_file.name)
        file_parser.source_text = ["Hello"]
        result = file_parser()
        assert result == (["Hello"], "")

    def test_call_with_search_term(self):
        """Test call with overridden search_term."""
        file_parser = ConcreteFileParser(self.tmp_file.name)
        file_parser.search_term = "world"
        result = file_parser()
        assert result == ([], "world")
