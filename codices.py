import os
from typing import List, Optional

from bs4 import BeautifulSoup, Comment

from utils import get_page_content, remove_last_chars, replace_substrings


def get_codex_categories(
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


def get_codices(game: str, categories: List[str]) -> None:
    base_url = "https://dragonage.fandom.com/wiki/Codex:_"

    for category in categories:
        url = f"{base_url}{category}"
        content = get_page_content(url=url)
        codices = get_codex_categories(content=content)
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
