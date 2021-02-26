import os
import requests
from bs4 import BeautifulSoup


def get_content(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find(class_="mw-parser-output")

    return content

def get_codices(content):
    p_tags = content.find_all('p')
    a_tags = content.find_all('a')
    removed_tags = [content.find_all('aside'),
                    content.find_all('dl'),
                    content.find_all('div', class_='toc'),
                    content.find_all('figure'),
                    content.find_all('div', style=["clear:both; margin: 0; padding: 0", "clear:right;", "clear:left;"]),
                    content.find_all('div', class_=["sp_banner"])
    ]
    banner_tags = content.find_all('div', class_=["sp sp_games sp_wide sp_id_dao", "sp sp_games sp_wide sp_id_da2", "sp sp_games sp_wide sp_id_dai",
                                                  "sp sp_games sp_wide sp_id_daoa", "sp sp_games sp_thin sp_id_daoa",
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

    for tags in removed_tags:
        for tag in tags:
            tag.decompose()

    for banner in banner_tags:
        banner.unwrap()

    [x.decompose() for x in content.find_all(lambda tag: (not tag.contents or len(tag.get_text(strip=True)) <= 0) and not tag.name == 'br' )]
    
    return content

def write_codices(codices, folder, subpage):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    with open(f"{folder}/{subpage}.html", "w") as f:
        to_write = str(codices)
        if "sp_games" in to_write or "sp_txt" in to_write or "sp_banner" in to_write:
            print("Check", subpage)
        f.write(to_write)