# Returns user input as plain text without any formatting.
def format_plain():
    return input("Text: > ")

# Returns user input formatted as bold text in Markdown.
def format_bold():
    return f"**{input('Text: > ')}**"

# Returns user input formatted as italic text in Markdown.
def format_italic():
    return f"*{input('Text: > ')}*"

# Returns a Markdown-compatible line break (two spaces followed by a newline).
def format_line_break():
    return "  \n"

# Returns user input formatted as inline code in Markdown.
def format_inline_code():
    return f"`{input('Text: > ')}`"

# Prompts user for a header level (1-6) and text, then returns the formatted header in Markdown.
def format_header():
    try:
        level = int(input("Level: > "))
        if 1 <= level <= 6:
            return f"{'#' * level} {input('Text: > ')}\n"
        else:
            print("The level should be within the range of 1 to 6.")
    except ValueError:
        print("Invalid level input.")
    return ""

# Prompts user for a label and a URL, then returns the formatted Markdown hyperlink.
def format_link():
    return f"[{input('Label: > ')}]({input('URL: > ')})"

# Prompts user for the number of list items and their content.Returns an ordered or unordered list in Markdown format.
def format_list(ordered=False):
    while True:
        try:
            num_items = int(input("Number of rows: > "))
            if num_items > 0:
                break
            print("The number of rows should be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

    items = []
    for i in range(1, num_items + 1):
        item = input(f"Row #{i}: > ")
        if ordered:
            items.append(f"{i}. {item}")
        else:
            items.append(f"* {item}")

    # Start with a new line and end with a new line
    return "\n" + "\n".join(items) + "\n\n"


def format_new_line():
    return "\n\n"

FORMATTERS = {
    "plain": format_plain,
    "bold": format_bold,
    "italic": format_italic,
    "inline-code": format_inline_code,
    "header": format_header,
    "link": format_link,
    "ordered-list": lambda: format_list(ordered=True),
    "unordered-list": lambda: format_list(ordered=False),
    "new-line": format_new_line,
    "line-break": format_line_break
}
