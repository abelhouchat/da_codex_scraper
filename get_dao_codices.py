import os
import requests
from bs4 import BeautifulSoup
from get_codices import get_content, get_codices, write_codices


base_url = "https://dragonage.fandom.com/wiki/Codex:_"
origins_subpages = ["Creatures", "Magic_and_Religion",
                    "Characters_(Origins)", "Notes",
                    "Items", "Culture_and_History",
                    "Books_and_Songs", "Quest-Related"]
base_folder = "dao"

for subpage in origins_subpages:
    url = f"{base_url}{subpage}"
    folder = f"{base_folder}/{subpage}"
    content = get_content(url=url)
    codices = get_codices(content=content)
    write_codices(codices=codices, folder=folder, subpage=subpage)