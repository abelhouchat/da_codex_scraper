import os
import requests
from bs4 import BeautifulSoup
from get_codices import get_content, get_codices, write_codices

base_url = "https://dragonage.fandom.com/wiki/Codex:_"
inky_subpages = ["Characters_(Inquisition)", "Crafting_Materials",
                 "Creatures_(Inquisition)", "Groups",
                 "History", "Letters_%26_Notes",
                 "Magic", "Places_(Inquisition)", 
                 "Tales"]
base_folder = "dai"

for subpage in inky_subpages:
    url = f"{base_url}{subpage}"
    folder = f"{base_folder}/{subpage}"
    content = get_content(url=url)
    codices = get_codices(content=content)
    write_codices(codices=codices, folder=folder, subpage=subpage)