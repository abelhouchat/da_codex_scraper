import os
import requests
from bs4 import BeautifulSoup

base_url = "https://dragonage.fandom.com/wiki/Codex:_"
inky_subpages = ["Characters_(Inquisition)", "Crafting_Materials",
                 "Creatures_(Inquisition)", "Groups",
                 "History", "Letters_%26_Notes",
                 "Magic", "Places_(Inquisition)", 
                 "Tales"]

for subpage in inky_subpages:
    url = base_url + subpage
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(class_="mw-parser-output")
    p_tags = results.find_all('p')
    a_tags = results.find_all('a')
    other_tags = [results.find_all('aside'),
                  results.find_all('dl'),
                  results.find_all('div', class_='toc'),
                  results.find_all('figure'),
                  results.find_all('div', style=["clear:both; margin: 0; padding: 0", "clear:right;", "clear:left;"]),
                  results.find_all('div', class_=["sp_banner"])
    ]
    banner_tags = results.find_all('div', class_=["sp sp_games sp_wide sp_id_dao", "sp sp_games sp_wide sp_id_da2", "sp sp_games sp_wide sp_id_dai",
                                                  "sp sp_games sp_wide sp_id_daoa", "sp sp_games sp_thin sp_id_daoa"
                                                  "sp sp_games sp_thin sp_id_dao", "sp sp_games sp_thin sp_id_da2", "sp sp_games sp_thin sp_id_dai",
                                                  "sp_txt"])

    for a in a_tags:
        if a.string is None:
            a.decompose()
        else:
            a.unwrap()

    for p in p_tags:
        if 'Researched:' in str(p):
            p.decompose()

    for tags in other_tags:
        for tag in tags:
            tag.decompose()

    for banner in banner_tags:
        banner.unwrap()


    folder = f"dai/{subpage}"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    with open(f"{folder}/{subpage}.html", "w") as f:
        to_write = str(results)
        if "sp_games" in to_write:
            print("Check", subpage)
        f.write(to_write)