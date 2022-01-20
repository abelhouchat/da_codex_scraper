from get_codices import get_codices, get_content, write_codices


def main():
    base_url = "https://dragonage.fandom.com/wiki/Codex:_"
    two_subpages = ["Creatures_(Dragon_Age_II)",
                    "Items_(Dragon_Age_II)",
                    "Places",
                    "Lore",
                    "Characters_(Dragon_Age_II)",
                    "Letters_and_Notes",
                    "Notes_(Dragon_Age_II)"]
    base_folder = "da2"

    for subpage in two_subpages:
        url = f"{base_url}{subpage}"
        folder = f"{base_folder}/{subpage}"
        content = get_content(url=url, parser='lxml')
        codices = get_codices(content=content, extra_tags=['h2'])
        write_codices(codices=codices, folder=folder, page=subpage)


if __name__ == "__main__":
    main()
