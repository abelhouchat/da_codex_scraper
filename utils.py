import string
from collections import OrderedDict
from typing import List, Optional, Tuple

import requests
from bs4 import BeautifulSoup, Comment


def check_letter_existence(letter: str, url: str) -> bool:
    """
    Check if the Wiki Category page for `letter` actually contains pages
    corresponding to `letter`.

    Parameters
    ----------
    letter : str
        The letter to check.
    url : str
        The URL corresponding to that letter.

    Returns
    -------
    bool
        Whether `url` actually contains any pages corresponding to `letter`.

    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    letter_header = soup.find("div", class_="category-page__first-char")

    return letter_header.text.strip() == letter.upper()


def get_alphabetized_links(url: str) -> List[str]:
    """
    Get all Wiki Category pages that are themselves subcategories categorized by
    letter AND that actually contain pages corresponding to that letter.

    Parameters
    ----------
    url : str
        The base Category page URL to get subcategory pages from.

    Returns
    -------
    actual_alphabetized_suburls : List[str]
        List of URLs for each subcategory page that actually has pages
        corresponding to its letter.

    """
    alphabet = list(string.ascii_uppercase)
    all_alphabetized_suburls = [f"{url}?from={letter}" for letter in alphabet]
    actual_alphabetized_suburls = []

    for letter, suburl in zip(alphabet, all_alphabetized_suburls):
        if check_letter_existence(letter, suburl):
            actual_alphabetized_suburls.append(suburl)

    return actual_alphabetized_suburls


def get_letter_pages(base_url: str, letter_url: str) -> List[str]:
    """
    Get all pages that fall under a given letter category.

    Parameters
    ----------
    base_url : str
        The base URL for the Wiki.
    letter_url : str
        The URL for the letter you want to get pages for

    Returns
    -------
    letter_pages : List[str]
        List of all URLs under `letter_url`.

    """
    page = requests.get(letter_url)
    soup = BeautifulSoup(page.text, "html.parser")

    letter_pages = []

    for link in soup.find_all("a", class_="category-page__member-link"):
        suburl = str(link.get("href"))
        letter_pages.append(f"{base_url}{suburl}")

    letter_pages = list(OrderedDict.fromkeys(letter_pages))

    return letter_pages


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


def get_textual_content(
    content: BeautifulSoup, extra_tags: Optional[List[str]] = None
) -> BeautifulSoup:
    """
    Returns a BeautifulSoup object containing just the codex entry text (and
    some formatting) contained in content.

    Parameters
    ----------
    content : BeautifulSoup
        BeautifulSoup object containing the codex entries.
    extra_tags : List[str], Optional
        List containing additional tags that you want to remove from the codex
        entry HTML. Default value is None.

    Returns
    -------
    content : BeautifulSoup
        BeautifulSoup object containing only the formatted codex entry text,
        meaning no links or tables or other similar tags are included.

    """
    p_tags = content.find_all("p")
    a_tags = content.find_all("a")
    # Tags we want to remove completely from the HTML files
    removed_tags = [
        content.find_all("aside"),
        content.find_all("dl"),
        content.find_all("div", class_="toc"),
        content.find_all("figure"),
        content.find_all("table"),
        content.find_all("sup"),
        content.find_all(
            "div",
            style=["clear:both; margin: 0; padding: 0", "clear:right;", "clear:left;"],
        ),
        content.find_all("div", class_=["sp_banner"]),
    ]
    if extra_tags is not None:
        for extra_tag in extra_tags:
            removed_tags.append(content.find_all(extra_tag))
    # Tags for spoilers; we want to remove the spoiler banner but keep the text that is spoilered"
    banner_tags = content.find_all(
        "div",
        class_=[
            "sp sp_games sp_wide sp_id_dao",
            "sp sp_games sp_thin sp_id_dao",
            "sp sp_games sp_wide sp_id_daoa",
            "sp sp_games sp_thin sp_id_daoa",
            "sp sp_games sp_wide sp_id_da2",
            "sp sp_games sp_thin sp_id_da2",
            "sp sp_games sp_wide sp_id_dai",
            "sp sp_games sp_thin sp_id_dai",
            "sp_txt",
        ],
    )

    for a in a_tags:
        # Completely remove tag if there is no text content
        if a.text == "":
            a.decompose()
        # Retain only the text otherwise
        else:
            a.unwrap()

    for p in p_tags:
        # Don't want to keep error text or text that is only relevant to gameplay
        if (
            "Researched:" in str(p)
            or "Resources found here:" in str(p)
            or "mw-ext-cite-error" in str(p)
        ):
            p.decompose()

    for tags in removed_tags:
        for tag in tags:
            tag.decompose()

    for banner in banner_tags:
        banner.unwrap()

    # This (supposedly) gets rid of all other empty tags without removing important formatting tags
    [
        x.decompose()
        for x in content.find_all(
            lambda tag: (not tag.contents or len(tag.get_text(strip=True)) <= 0)
            and not tag.name == "br"
            and not tag.name == "hr"
        )
    ]

    # This gets rid of the comments at the end of each page's HTML
    for element in content(text=lambda text: isinstance(text, Comment)):
        element.extract()

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
