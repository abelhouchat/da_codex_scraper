from scraping.texts import get_texts
from scraping.utils import ROOT_URL


def main():
    game = "da2"
    url = f"{ROOT_URL}/wiki/Category:Dragon_Age_II_letters"
    content_prefix = "Letter: "
    content_type = "texts"
    category = "Letters"
    header_ids = ["Letter"]

    get_texts(
        url=url,
        game=game,
        content_type=content_type,
        category=category,
        content_prefix=content_prefix,
        header_ids=header_ids,
    )


if __name__ == "__main__":
    main()
