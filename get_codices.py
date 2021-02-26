import os
import requests
from bs4 import BeautifulSoup, Comment


def get_content(url):
    """
    Returns a BeautifulSoup object containing the HTML content of the URL.

    Parameters
    ----------
    url : string
        URL of the page containing the codex entries.

    Returns
    -------
    content : BeautifulSoup
        BeautifulSoup object containing the content of the URL.

    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find(class_="mw-parser-output")

    return content

def get_codices(content, extra_tags=None):
    """
    Returns a BeautifulSoup object containing just the codex entry text (and 
    some formatting) contained in content.

    Parameters
    ----------
    content : BeautifulSoup
        BeautifulSoup object containing the codex entries.
    extra_tags : list of str, optional
        List containing additional tags that you want to remove from the codex 
        entry HTML.

    Returns
    -------
    content : BeautifulSoup
        BeautifulSoup object containing only the formatted codex entry text, 
        meaning no links or tables or other similar tags are included.

    """
    p_tags = content.find_all('p')
    a_tags = content.find_all('a')
    removed_tags = [content.find_all('aside'),
                    content.find_all('dl'),
                    content.find_all('div', class_='toc'),
                    content.find_all('figure'),
                    content.find_all('table'),
                    content.find_all('sup'),
                    content.find_all('div', style=["clear:both; margin: 0; padding: 0", 
                                                   "clear:right;", 
                                                   "clear:left;"]),
                    content.find_all('div', class_=["sp_banner"])
    ]
    if extra_tags is not None:
        for extra_tag in extra_tags:
            removed_tags.append(content.find_all(extra_tag))
    banner_tags = content.find_all('div', class_=["sp sp_games sp_wide sp_id_dao", "sp sp_games sp_thin sp_id_dao",
                                                  "sp sp_games sp_wide sp_id_daoa", "sp sp_games sp_thin sp_id_daoa",
                                                  "sp sp_games sp_wide sp_id_da2", "sp sp_games sp_thin sp_id_da2",
                                                  "sp sp_games sp_wide sp_id_dai", "sp sp_games sp_thin sp_id_dai",
                                                  "sp_txt"])

    for a in a_tags:
        if a.string is None:
            a.decompose()
        else:
            a.unwrap()

    for p in p_tags:
        if "Researched:" in str(p) or "Resources found here:" in str(p):
            p.decompose()

    for tags in removed_tags:
        for tag in tags:
            tag.decompose()

    for banner in banner_tags:
        banner.unwrap()

    [x.decompose() for x in content.find_all(lambda tag: (not tag.contents or len(tag.get_text(strip=True)) <= 0) and not tag.name == 'br' and not tag.name == 'hr')]

    
    for element in content(text=lambda text: isinstance(text, Comment)):
        element.extract()

    return content

def write_codices(codices, folder, page):
    """
    Writes the codex entries into a single HTML file.

    Parameters
    ----------
    codices : BeautifulSoup
        BeautifulSoup object containing the codex entries.
    folder : str
        The folder you want to write the codex HTML file into.
    page : str
        The name you want to give to the HTML file.

    Returns
    -------
    None

    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    with open(f"{folder}/{page}.html", "w") as f:
        to_write = str(codices)
        if "sp_games" in to_write or "sp_txt" in to_write or "sp_banner" in to_write:
            print("Check", page)
        f.write(to_write)