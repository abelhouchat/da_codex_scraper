from scraping.texts import get_texts


def main():
    game = "da2"
    base_url = "https://dragonage.fandom.com"
    full_url = f"{base_url}/wiki/Category:Dragon_Age_II_letters"
    content_prefix = "Letter: "
    content_type = "texts"
    category = "Letters"
    header_ids = ["Letter"]

    get_texts(
        base_url, full_url, game, content_type, category, content_prefix, header_ids
    )


if __name__ == "__main__":
    main()
