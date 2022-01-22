# Dragon Age Codex Scraper

Personal project to get all the codex entries from the 
[Dragon Age Wiki](https://dragonage.fandom.com/wiki/Dragon_Age_Wiki).

## Requirements
 * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 * [lxml](https://lxml.de/)
 * [requests](https://docs.python-requests.org/en/latest/)

## Usage
Run one of the `get_da*_codices.py` files to create a folder containing all 
the codex entries for that game, with HTML files separated by section. If you 
want, you can then run `split_codices.py` to split each codex entry into its 
own HTML file.
