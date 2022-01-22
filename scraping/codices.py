from typing import List

from bs4 import BeautifulSoup

from scraping.utils import (
    ROOT_URL,
    get_page_content,
    get_textual_content,
    prep_for_writing,
    write_entries,
)


def get_codices(game: str, categories: List[str]) -> None:
    """
    Get all codices of the given categories for the given game.

    Parameters
    ----------
    game : str
        The game to get codex entries from. Assumes the games are numbered, so
        valid options are "da1", "da2", and "da3".
    categories : List[str]
        The codex categories to get. Look at the Dragon Age Wiki for appropriate
        categories for the game you want codices from.

    Returns
    -------
    None

    """
    base_url = f"{ROOT_URL}/wiki/Codex:_"

    for category in categories:
        url = f"{base_url}{category}"
        content = get_page_content(url=url)
        codices = get_textual_content(content=content)
        split_and_write_codices(codices=codices, game=game, category=category)


def split_and_write_codices(codices: BeautifulSoup, game: str, category: str) -> None:
    """
    Split codex entries from a category into individual pages and write each one
    to its own file.

    Parameters
    ----------
    codices : BeautifulSoup
        The BeautifulSoup object containing the codex entries to split and write.
    game : str
        The game to get codex entries from. Assumes the games are numbered, so
        valid options are "da1", "da2", and "da3".
    category : str
        The category that the codex entries in `codices` come from.

    Returns
    -------
    None

    """
    entries = prep_for_writing(content=codices)
    write_entries(entries=entries, game=game, content_type="codices", category=category)
