from typing import List

from scraping.utils import (
    get_all_pages,
    get_page_content,
    get_textual_content,
    prep_for_writing,
    write_entries,
)


def get_texts(
    base_url: str,
    full_url: str,
    game: str,
    content_type: str,
    category: str,
    content_prefix: str,
    header_ids: List[str],
):
    ids_to_skip = [
        "Locked",
        "Bugs",
        "Notes",
        "Trivia",
        "Related_texts",
        "Related_quest",
        "Related_quests",
        "See_also",
        "References",
        "External_links",
        "Quests",
    ]

    all_urls = get_all_pages(base_url, full_url)

    all_texts = []

    for url in all_urls:
        content = get_page_content(url)
        header = content.find("h1", class_="page-header__title").text.strip()
        title = header.replace(content_prefix, "")
        to_remove = [
            content.find_all(class_="mw-editsection"),
            content.find_all(class_="mw-editsection-bracket"),
            content.find_all(class_="mw-editsection-divider"),
            content.find_all(class_="mw-references-wrap"),
        ]
        for tags in to_remove:
            for tag in tags:
                tag.decompose()
        text_content = get_textual_content(content=content)

        for id in header_ids:
            header = text_content.find(class_="mw-headline", id=id)
            if header is not None:
                header.string.replace_with(title)
                header["id"] = title.replace(" ", "_")

        all_texts += prep_for_writing(text_content, ids_to_skip)

    write_entries(all_texts, game, content_type, category)
