import os
from typing import List

from bs4 import BeautifulSoup

from utils import get_page_content, remove_last_chars, replace_substrings


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
    folder = f"{game}/codices"
    if not os.path.exists(folder):
        os.makedirs(folder)

    replacements = [
        ("<hr />", "<hr>"),
        ("<hr/>", "<hr>"),
        ("<br />", "<br>"),
        ("<br/>", "<br>"),
        ("h2", "h3"),
    ]

    idx = 0

    codices_str = str(codices)
    stuffs = codices_str.rstrip()
    stuffs = replace_substrings(input_string=stuffs, replacements=replacements)
    # Codex pages end with a dangling </div>, so get rid of it
    stuffs = remove_last_chars(input_string=stuffs, last_chars="</div>")
    # Split each codex entry into its own string
    stuffs = stuffs.split("<h3>")
    # The first element is intro stuff, we ignore it
    for stuff in stuffs[1:]:
        # Skip over entries that just say "Locked" or "Bugs"
        if (
            'class="mw-headline" id="Locked' in stuff
            or 'class="mw-headline" id="Bugs"' in stuff
        ):
            continue
        to_write = f"<h3>{stuff}".rstrip()
        # Get rid of terminal rows and dangling </hr>, which are usually
        # leftovers of removing gameplay-only parts of the codex entry
        to_write = remove_last_chars(input_string=to_write, last_chars="<hr>")
        to_write = remove_last_chars(input_string=to_write, last_chars="</hr>")
        name = f"{game}_{category.split('_')[0].lower()}_{idx}.html"
        idx += 1
        with open(f"{folder}/{name}", "w") as f:
            f.write(to_write)
