from get_codices import get_codices, get_content, write_codices


def main():
    base_url = "https://dragonage.fandom.com/wiki/Codex:_"
    inky_subpages = ["Characters_(Inquisition)",
                     "Crafting_Materials",
                     "Creatures_(Inquisition)",
                     "Groups",
                     "History",
                     "Letters_%26_Notes",
                     "Magic",
                     "Places_(Inquisition)",
                     "Tales"]
    base_folder = "da3"

    for subpage in inky_subpages:
        url = f"{base_url}{subpage}"
        folder = f"{base_folder}/{subpage}"
        content = get_content(url=url)
        codices = get_codices(content=content)
        write_codices(codices=codices, folder=folder, page=subpage)


if __name__ == "__main__":
    main()
