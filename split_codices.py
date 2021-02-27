import os

origins_subpages = ["Creatures", "Magic_and_Religion",
                    "Characters_(Origins)", "Notes",
                    "Items", "Culture_and_History",
                    "Books_and_Songs", "Quest-Related"]
two_subpages = ["Creatures_(Dragon_Age_II)", "Items_(Dragon_Age_II)",
                "Places", "Lore",
                "Characters_(Dragon_Age_II)", "Letters_and_Notes",
                "Notes_(Dragon_Age_II)"]
inky_subpages = ["Characters_(Inquisition)", "Crafting_Materials",
                 "Creatures_(Inquisition)", "Groups",
                 "History", "Letters_%26_Notes",
                 "Magic", "Places_(Inquisition)", 
                 "Tales"]
all_subpages = [origins_subpages, two_subpages, inky_subpages]
folders = ["dao", "da2", "dai"]


if not os.path.exists("codices/"):
    os.makedirs("codices/")

for folder, subpage in zip(folders, all_subpages):
    for page in subpage:
        idx = 0
        filename = f"{folder}/{page}/{page}.html"
        with open(filename, "r") as f:
            stuffs = f.read()
            # To make it easier to clean up later, replace <hr /> and <br />
            # with tags that are functionally the same
            stuffs = stuffs.replace('<hr />', '<hr>')
            stuffs = stuffs.replace('<br />', '<br>')
            # Convert all <h2> tags to <h3> because I think it makes sense for 
            # the hierarchy to go: game - <h1>, section - <h2>, entry - <h3>
            stuffs = stuffs.replace('h2', 'h3')
            # Codex pages end with a dangling </div>, so get rid of it
            if stuffs[-6:] == "</div>":
                stuffs = stuffs[:-6]
            # Split each codex entry into its own string
            stuffs = stuffs.split('<h3>')
            # The first element is intro stuff, we ignore it
            for stuff in stuffs[1:]:
                # Skip over entries that just say "Locked" or "Bugs"
                if 'class="mw-headline" id="Locked' in stuff or 'class="mw-headline" id="Bugs"' in stuff:
                    continue
                to_write = f"<h3>{stuff}".rstrip()
                # Get rid of terminal rows and dangling </hr>, which are usually 
                # leftovers of removing gameplay-only parts of the codex entry
                if to_write[-4:] == "<hr>":
                    to_write = to_write[:-4].rstrip()
                if to_write[-5:] == "</hr>":
                    to_write = to_write[:-5].rstrip()
                name = f"{folder}_{page.split('_')[0].lower()}_{idx}.html"
                idx += 1
                with open(f"codices/{name}", "w") as f:
                    f.write(to_write)