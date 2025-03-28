# Saves the given content to a Markdown file.Overwrites the file if it already exists.
def save_to_file(content, filename="output.md"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
