"""Main entry point for finding match."""

import argparse
import logging

from fileparser.textfileparser import TextFileParser
from utils.configure_logger import configure_logger
from utils.utils import get_abs_path

configure_logger(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("filepath", help="Input text file path", type=str)

    args = arg_parser.parse_args()
    args.filepath = get_abs_path(args.filepath, __file__)

    file_parser = TextFileParser(args.filepath)
    source_text, search_term = file_parser()

    # logger.debug(f"The source text is: \n{source_text}\n")
    # logger.info(f"The search term: '{search_term}'")
