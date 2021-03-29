from get_codices import get_content, get_codices, write_codices


base_url = "https://dragonage.fandom.com/wiki/"
pages = ["Short_Story:_Paper_%26_Steel",
         "Short_Story:_Paying_the_Ferryman",
         "Short_Story:_The_Riddle_of_Truth"
]
story_urls = [f"{base_url}{page}" for page in pages]

for url, page in zip(story_urls, pages):
    folder = "dai/short_stories"
    content = get_content(url=url)
    codices = get_codices(content=content)
    write_codices(codices=codices, folder=folder, page=page)