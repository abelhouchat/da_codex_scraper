# Dragon Age Codex Scraper

Personal project to get all the codex entries from the 
[Dragon Age Wiki](https://dragonage.fandom.com/wiki/Dragon_Age_Wiki).

## Requirements
 * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Usage
Run one of the `get_da*_codices.py` files to create a folder containing all 
the codex entries for that game, with HTML files separated by section. If you 
want, you can then run `split_codices.py` to split each codex entry into its 
own HTML file.

These scripts aren't perfect. When I ran them, I could not get all the Items 
codex entries for Dragon Age II in the normal way, so I had to download the 
HTML file for that page and rerun the scraper on the downloaded file. Running 
`split_codices.py` also deletes the Grey Warden Letters codex entry from Dragon 
Age II, likely because it uses `<h2>` tags where all other Dragon Age II codex 
entries use `<h3>` tags.