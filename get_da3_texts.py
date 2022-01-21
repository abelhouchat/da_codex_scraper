from other.other import get_alphabetized_links, get_letter_pages


def main():

    full_url = f"{base_url}/Category:Dragon_Age_4_short_stories"

    folder = "da4"
    content_type = "short_stories"

    alph_links = get_alphabetized_links(full_url)

    all_texts = []

    for link in alph_links:
        all_texts.append(get_letter_pages(base_url, link))

    for text in all_texts:
        print(text)

    note_names = []
    for letter_texts in all_texts:
        for url in letter_texts:
            note_name = url[40:]
            note_names.append(note_name)
            print("Getting", note_name)
            content_path = f"{folder}/{content_type}"
            content = get_page_content(url=url)
            to_remove = [
                content.find_all(class_="mw-editsection"),
                content.find_all(class_="mw-editsection-bracket"),
                content.find_all(class_="mw-editsection-divider"),
                content.find_all(class_="mw-references-wrap"),
            ]
            for tags in to_remove:
                for tag in tags:
                    tag.decompose()
            codices = get_codices(content=content, extra_tags=["ul"])
            write_codices(codices=codices, folder=content_path, page=note_name)

    # To make it easier to clean up later, replace <hr /> and <br /> with tags that
    # are functionally the same. We also want to convert all <h2> tags to <h3>
    # because I think it makes sense for the hierarchy to go:
    # game - <h1>, section - <h2>, entry - <h3>
    replacements = [
        ("<hr />", "<hr>"),
        ("<hr/>", "<hr>"),
        ("<br />", "<br>"),
        ("<br/>", "<br>"),
        ("h2", "h3"),
    ]

    split_and_write(folder, note_names, content_type, replacements)


if __name__ == "__main__":
    main()
