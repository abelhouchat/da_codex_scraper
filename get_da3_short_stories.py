from scraping.texts import get_texts


def main():
    game = "da3"
    base_url = "https://dragonage.fandom.com"
    full_url = f"{base_url}/wiki/Category:Dragon_Age:_Inquisition_short_stories"
    content_prefix = "Short Story: "
    content_type = "texts"
    category = "Short Stories"
    header_ids = ["Story"]

    get_texts(
        base_url, full_url, game, content_type, category, content_prefix, header_ids
    )


if __name__ == "__main__":
    main()
