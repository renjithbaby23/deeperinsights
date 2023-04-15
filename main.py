"""Main entry point for finding match."""

import argparse
import logging

import pattern_matcher as pm
from content_formatter.textfile_formatter import TextContentFormatter
from file_parser.textfile_parser import TextFileParser
from utils.configure_logger import configure_logger
from utils.utils import get_abs_path

configure_logger(level=logging.ERROR)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("filepath", help="Input text file path", type=str)

    args = arg_parser.parse_args()
    # args.filepath = "sample4.txt"
    args.filepath = get_abs_path(args.filepath, __file__)

    # parse the file
    file_parser = TextFileParser(args.filepath)
    source_text, search_term = file_parser()

    # format the source text
    content_formatter = TextContentFormatter()
    formatted_source_text = content_formatter.format(source_text)

    # get and print the matching lines
    idx_list = pm.get_matching_lines(formatted_source_text, search_term)
    pm.print_matching_lines(formatted_source_text, idx_list)
