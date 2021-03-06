import os
import requests
from bs4 import BeautifulSoup
from get_codices import get_content, get_codices, write_codices

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
