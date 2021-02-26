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
subpages = [origins_subpages, two_subpages, inky_subpages]
folders = ["dao", "da2", "dai"]


if not os.path.exists("codices/"):
    os.makedirs("codices/")

for folder, subpage in zip(folders, subpages):
    for page in subpage:
        idx = 0
        filename = f"{folder}/{page}/{page}.html"
        with open(filename, "r") as f:
            # Convert all <h2> tags to <h3> because I think it makes sense for 
            # the hierarchy to go: game - <h1>, section - <h2>, entry - <h3>
            stuffs = f.read().replace('h2', 'h3').split('<h3>')
            for stuff in stuffs[1:]:
                to_write = f"<h3>{stuff}"
                name = f"{folder}_{page.split('_')[0].lower()}_{idx}.html"
                idx += 1
                with open(f"codices/{name}", "w") as f:
                    f.write(to_write)