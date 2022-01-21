from scraping.texts import get_texts


def main():
    game = "da3"
    base_url = "https://dragonage.fandom.com"
    full_url = f"{base_url}/wiki/Category:Dragon_Age:_Inquisition_texts"
    content_prefix = "Note: "
    content_type = "texts"
    category = "Notes"
    header_ids = ["Note_text", "Note_texts", "Text"]

    get_texts(
        base_url, full_url, game, content_type, category, content_prefix, header_ids
    )


if __name__ == "__main__":
    main()
