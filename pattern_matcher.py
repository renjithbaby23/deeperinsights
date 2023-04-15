"""Pattern matching."""

from typing import List


def does_line_match(source_line: str, search_term: str) -> bool:
    """Check if a source line has a matching search_term."""
    return search_term.lower() in source_line.lower()


def get_matching_lines(source_text: List[str], search_term) -> List[int]:
    """Get the matching line indices."""
    result_idx = []
    for idx, text in enumerate(source_text):
        if does_line_match(text, search_term):
            result_idx.append(idx)
    return result_idx


def print_matching_line(text):
    """Print the matching lines in desired format."""
    words = text.split()
    formatted_text = "[" + " ".join(words) + "]"
    print(formatted_text)


def print_matching_lines(source_text: List[str], idx_list: List[int]):
    """Print all the matching lines from the list of lines."""
    _ = [
        print_matching_line(text)
        for idx, text in enumerate(source_text)
        if idx in idx_list
    ]
