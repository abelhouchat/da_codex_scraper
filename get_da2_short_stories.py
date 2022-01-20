from get_codices import get_codices, get_content, write_codices


def main():
    base_url = "https://dragonage.fandom.com/wiki/"
    pages = [
        "Anders_(short_story)",
        "Aveline_(short_story)",
        "Fenris_(short_story)",
        "Isabela_(short_story)",
        "Merrill_(short_story)",
        "Sebastian_(short_story)",
        "Varric_(short_story)",
    ]
    story_urls = [f"{base_url}{page}" for page in pages]

    for url, page in zip(story_urls, pages):
        folder = "da2/short_stories"
        content = get_content(url=url)
        codices = get_codices(content=content)
        write_codices(codices=codices, folder=folder, page=page)


if __name__ == "__main__":
    main()
