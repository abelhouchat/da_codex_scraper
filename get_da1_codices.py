from scraping.codices import get_codices


def main():
    game = "da1"
    categories = [
        "Creatures",
        "Items",
        "Magic_and_Religion",
        "Culture_and_History",
        "Characters_(Origins)",
        "Books_and_Songs",
        "Notes",
        "Quest-Related",
    ]

    get_codices(game=game, categories=categories)


if __name__ == "__main__":
    main()
