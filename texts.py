from utils import (
    get_alphabetized_links,
    get_letter_pages,
    get_page_content,
    get_textual_content,
)


def get_texts():
    base_url = "https://dragonage.fandom.com"
    full_url = f"{base_url}/wiki/Category:Dragon_Age:_Inquisition_texts"

    alphabetical_links = get_alphabetized_links(full_url)

    all_urls = []

    for link in alphabetical_links:
        all_urls += get_letter_pages(base_url, link)

    for url in all_urls:
        content = get_page_content(url)
        to_remove = [
            content.find_all(class_="mw-editsection"),
            content.find_all(class_="mw-editsection-bracket"),
            content.find_all(class_="mw-editsection-divider"),
            content.find_all(class_="mw-references-wrap"),
        ]
        for tags in to_remove:
            for tag in tags:
                tag.decompose()
        texts = get_textual_content(content=content, extra_tags=["ul"])
