# Dragon Age Codex Scraper

Personal project to get all the codex entries from the 
[Dragon Age Wiki](https://dragonage.fandom.com/wiki/Dragon_Age_Wiki).

## Requirements
 * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 * [lxml](https://lxml.de/)
 * [requests](https://docs.python-requests.org/en/latest/)

## Usage
To get all codex entries and snippets of in-game text (okay not all of them, but
a lot of them), run `get_all.sh`. This script just calls all of the `get_da*.py`
files, so if you only wanted one type of text from one game in particular, you
could run the individual Python scripts instead.

The scripts will store each codex entry or piece of text in its own HTML file.
The files will be stored in folders first by game and then by type of text
(codex or general text).

The functions that perform all the scraping, formatting, and writing are located
in the `scraping` directory.
