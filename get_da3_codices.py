from codices import get_codices


def main():
    game = "da3"
    categories = [
        "Characters_(Inquisition)",
        "Crafting_Materials",
        "Creatures_(Inquisition)",
        "Groups",
        "History",
        "Letters_%26_Notes",
        "Magic",
        "Places_(Inquisition)",
        "Tales",
    ]

    get_codices(game=game, categories=categories)


if __name__ == "__main__":
    main()
