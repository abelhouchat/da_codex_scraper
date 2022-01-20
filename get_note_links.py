import os
import string
from collections import OrderedDict

import requests
from bs4 import BeautifulSoup

from get_codices import get_codices, get_content, write_codices
from split_codices import remove_last_chars, replace_substrings


base_url = "https://dragonage.fandom.com"

dai_url = f"{base_url}/wiki/Category:Dragon_Age:_Inquisition_texts"
alphabet = list(string.ascii_uppercase)
dai_urls = [f"{dai_url}?from={a}" for a in alphabet]

note_urls = []

print("Getting urls")
for url in dai_urls:
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")

    for link in soup.find_all("a"):
        suburl = str(link.get("href"))
        if "/wiki/Note:" in suburl:
            note_urls.append(f"{base_url}{suburl}")

note_urls = list(OrderedDict.fromkeys(note_urls))
print("Got urls")

note_names = []
for url in note_urls:
    note_name = url[40:]
    note_names.append(note_name)
    print("Getting", note_name)
    folder = "dai/notes_(non-codex)"
    content = get_content(url=url)
    to_remove = [
        content.find_all(class_="mw-editsection"),
        content.find_all(class_="mw-editsection-bracket"),
        content.find_all(class_="mw-editsection-divider"),
        content.find_all(class_="mw-references-wrap"),
    ]
    for tags in to_remove:
        for tag in tags:
            tag.decompose()
    codices = get_codices(content=content, extra_tags=["ul"])
    write_codices(codices=codices, folder=folder, page=note_name)


# To make it easier to clean up later, replace <hr /> and <br /> with tags that
# are functionally the same. We also want to convert all <h2> tags to <h3>
# because I think it makes sense for the hierarchy to go:
# game - <h1>, section - <h2>, entry - <h3>
replacements = [
    ("<hr />", "<hr>"),
    ("<hr/>", "<hr>"),
    ("<br />", "<br>"),
    ("<br/>", "<br>"),
    ("h2", "h3"),
]
folder = "dai"

if not os.path.exists("notes_(non-codex)/"):
    os.makedirs("notes_(non-codex)/")

for page in note_names:
    idx = 0
    filename = f"{folder}/notes_(non-codex)/{page}.html"
    with open(filename, "r") as f:
        stuffs = f.read().rstrip()
        stuffs = replace_substrings(input_string=stuffs, replacements=replacements)
        # Codex pages end with a dangling </div>, so get rid of it
        stuff = remove_last_chars(input_string=stuffs, last_chars="</div>")
        # Skip over entries that just say "Locked" or "Bugs"
        if (
            'class="mw-headline" id="Locked' in stuff
            or 'class="mw-headline" id="Bugs"' in stuff
        ):
            continue
        to_write = stuff.rstrip()
        # Get rid of terminal rows and dangling </hr>, which are usually
        # leftovers of removing gameplay-only parts of the codex entry
        to_write = remove_last_chars(input_string=to_write, last_chars="<hr>")
        to_write = remove_last_chars(input_string=to_write, last_chars="</hr>")
        name = f"{folder}_{page}.html"
        idx += 1
        with open(f"notes_(non-codex)/{name}", "w") as f:
            f.write(to_write)
