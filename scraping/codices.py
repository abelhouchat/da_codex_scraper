from typing import List

from bs4 import BeautifulSoup

from scraping.utils import (
    get_page_content,
    get_textual_content,
    prep_for_writing,
    write_entries,
)


def get_codices(game: str, categories: List[str]) -> None:
    base_url = "https://dragonage.fandom.com/wiki/Codex:_"

    for category in categories:
        url = f"{base_url}{category}"
        content = get_page_content(url=url)
        codices = get_textual_content(content=content)
        split_and_write_codices(codices=codices, game=game, category=category)


def split_and_write_codices(
    codices: BeautifulSoup,
    game: str,
    category: str,
) -> None:
    ids_to_skip = ["Locked", "Bugs"]

    entries = prep_for_writing(codices, ids_to_skip)
    write_entries(entries, game, "codices", category)
