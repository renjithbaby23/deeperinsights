"""Main entry point for solution."""

import argparse
import logging
import os.path
from pathlib import Path

import solution.pattern_matcher as pm
from solution.content_formatter.textfile_formatter import TextContentFormatter
from solution.file_parser.textfile_parser import TextFileParser
from solution.utils.configure_logger import configure_logger

configure_logger(level=logging.ERROR)
logger = logging.getLogger(__name__)


def main():
    """Deeperinsights solution main."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("filepath", help="Input text file path", type=str)

    args = arg_parser.parse_args()
    args.filepath = os.path.abspath(Path(args.filepath).absolute())

    # parse the file
    file_parser = TextFileParser(args.filepath)
    source_text, search_term = file_parser()

    # format the source text
    content_formatter = TextContentFormatter()
    formatted_source_text = content_formatter.format(source_text)

    # get and print the matching lines
    idx_list = pm.get_matching_lines(formatted_source_text, search_term)
    pm.print_matching_lines(formatted_source_text, idx_list)


if __name__ == "__main__":
    main()
