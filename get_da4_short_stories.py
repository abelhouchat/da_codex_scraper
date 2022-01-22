from scraping.texts import get_texts
from scraping.utils import ROOT_URL


def main():
    game = "da4"
    url = f"{ROOT_URL}/wiki/Category:Dragon_Age_4_short_stories"
    content_prefix = "Short Story: "
    content_type = "texts"
    category = "Short Stories"
    header_ids = ["Story"]

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
