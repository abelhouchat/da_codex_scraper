from get_codices import get_codices, get_content, write_codices


def main():
    base_url = "https://dragonage.fandom.com/wiki/Codex:_"
    origins_subpages = ["Creatures",
                        "Items",
                        "Magic_and_Religion",
                        "Culture_and_History",
                        "Characters_(Origins)",
                        "Books_and_Songs",
                        "Notes",
                        "Quest-Related"]
    base_folder = "da1"

    for subpage in origins_subpages:
        url = f"{base_url}{subpage}"
        folder = f"{base_folder}/{subpage}"
        content = get_content(url=url)
        codices = get_codices(content=content)
        write_codices(codices=codices, folder=folder, page=subpage)


if __name__ == "__main__":
    main()
