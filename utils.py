from typing import List, Tuple

import requests
from bs4 import BeautifulSoup


def get_page_content(url: str, parser: str = "html.parser") -> BeautifulSoup:
    """
    Returns a BeautifulSoup object containing the HTML content of the URL.

    Parameters
    ----------
    url : str
        URL of the page containing the codex entries.
    parser : str
        HTML parser to use.

    Returns
    -------
    content : BeautifulSoup
        BeautifulSoup object containing the content of the URL.

    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, parser)
    # Actual codex content is located under the "mw-parser-output" div
    content = soup.find(class_="mw-parser-output")

    return content


def remove_last_chars(input_string: str, last_chars: str) -> str:
    """
    If the last characters in a string are known to be certain characters,
    remove these last characters and any trailing whitespace.

    Parameters
    ----------
    input_string : str
        The string to remove the last characters from.
    last_chars : str
        The characters to remove from the end of input_string.

    Returns
    -------
    input_string : str
        The input string with the last characters and trailing whitespace removed.

    """
    length = len(last_chars)
    assert length < len(input_string), "last_chars is longer than input_string"
    if input_string[-length:] == last_chars:
        input_string = input_string[:-length].rstrip()

    return input_string


def replace_substrings(input_string: str, replacements: List[Tuple[str]]) -> str:
    """
    Replace multiple substrings in a string.

    Parameters
    ----------
    input_string : str
        The string to perform replacement on.
    replacements : list of tuple of str
        List of pairs of substrings to replace and replace with. The
        first element in each tuple is the substring to replace, and
        the second is the substring to replace the first element with.

    Returns
    -------
    input_string : str
        The input string with all replacements.

    """
    for replaced, replacer in replacements:
        input_string = input_string.replace(replaced, replacer)

    return input_string
