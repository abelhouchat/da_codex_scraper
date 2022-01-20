from get_codices import get_codices, get_content, write_codices


def main():
    base_url = "https://dragonage.fandom.com/wiki/"
    pages = [
        "Short_Story:_Minrathous_Shadows",
        "Short_Story:_The_Next_One",
        "Short_Story:_Ruins_of_Reality",
        "Short_Story:_The_Wake",
        "Short_Story:_Won't_Know_When",
        "Short_Story:_The_Eternal_Flame",
    ]
    story_urls = [f"{base_url}{page}" for page in pages]

    for url, page in zip(story_urls, pages):
        folder = "da4/short_stories"
        content = get_content(url=url)
        codices = get_codices(content=content)
        write_codices(codices=codices, folder=folder, page=page)


if __name__ == "__main__":
    main()
