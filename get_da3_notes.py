from scraping.texts import get_texts
from scraping.utils import ROOT_URL


def main():
    game = "da3"
    url = f"{ROOT_URL}/wiki/Category:Dragon_Age:_Inquisition_texts"
    content_prefix = "Note: "
    content_type = "texts"
    category = "Notes"
    header_ids = ["Note_text", "Note_texts", "Text"]

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
