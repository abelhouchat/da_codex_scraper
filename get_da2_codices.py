from codices import get_codices


def main():
    game = "da2"
    categories = [
        "Creatures_(Dragon_Age_II)",
        "Items_(Dragon_Age_II)",
        "Places",
        "Lore",
        "Characters_(Dragon_Age_II)",
        "Letters_and_Notes",
        "Notes_(Dragon_Age_II)",
    ]

    get_codices(game=game, categories=categories)


if __name__ == "__main__":
    main()
