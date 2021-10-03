import os


def replace_substrings(input_string, replacements):
    """
    Replace multiple substrings in a string.

    Parameters
    ----------
    input_string : string
        The string to perform replacement on.
    replacements : list of tuple of str
        List of pairs of substrings to replace and replace with. The 
        first element in each tuple is the substring to replace, and 
        the second is the substring to replace the first element with.

    Returns
    -------
    input_string : string
        The input string with all replacements.

    """
    for replaced, replacer in replacements:
        input_string = input_string.replace(replaced, replacer)

    return input_string


def remove_last_chars(input_string, last_chars):
    """
    If the last characters in a string are known to be certain characters, 
    remove these last characters and any trailing whitespace.

    Parameters
    ----------
    input_string : string
        The string to remove the last characters from.
    last_chars : string
        The characters to remove from the end of input_string.

    Returns
    -------
    input_string : string
        The input string with the last characters and trailing whitespace removed.

    """
    length = len(last_chars)
    assert length < len(input_string), "last_chars is longer than input_string"
    if input_string[-length:] == last_chars:
        input_string = input_string[:-length].rstrip()

    return input_string


if __name__ == "__main__":
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

    # To make it easier to clean up later, replace <hr /> and <br /> with tags that
    # are functionally the same. We also want to convert all <h2> tags to <h3>
    # because I think it makes sense for the hierarchy to go:
    # game - <h1>, section - <h2>, entry - <h3>
    replacements = [('<hr />', '<hr>'), ('<br />', '<br>'), ('h2', 'h3')]

    if not os.path.exists("codices/"):
        os.makedirs("codices/")

    for folder, subpage in zip(folders, all_subpages):
        for page in subpage:
            idx = 0
            filename = f"{folder}/{page}/{page}.html"
            with open(filename, "r") as f:
                stuffs = f.read().rstrip()
                stuffs = replace_substrings(
                    input_string=stuffs, replacements=replacements)
                # Codex pages end with a dangling </div>, so get rid of it
                stuffs = remove_last_chars(
                    input_string=stuffs, last_chars="</div>")
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
                    to_write = remove_last_chars(
                        input_string=to_write, last_chars="<hr>")
                    to_write = remove_last_chars(
                        input_string=to_write, last_chars="</hr>")
                    name = f"{folder}_{page.split('_')[0].lower()}_{idx}.html"
                    idx += 1
                    with open(f"codices/{name}", "w") as f:
                        f.write(to_write)
