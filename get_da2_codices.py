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
    content = get_content(url=url)
    codices = get_codices(content=content, extra_tags=['h2'])
    write_codices(codices=codices, folder=folder, page=subpage)


item_subpage = "Items_(Dragon_Age_II)"
item_folder = f"{base_folder}/{item_subpage}"

with open('items_da2.html', 'r') as f:
    item_page = f.read()
    item_soup = BeautifulSoup(item_page, 'html.parser')
item_content = item_soup.find(class_="mw-parser-output")

item_codices = get_codices(content=item_content, extra_tags=['h2'])
write_codices(codices=item_codices, folder=item_folder, page=item_subpage)