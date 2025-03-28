from text_formatter import FORMATTERS
from file_handler import save_to_file
from helpers import print_help

# Main function that runs the Markdown editor. Allows users to choose formatters and apply them to text.Saves the final result when the user enters "!done".
def main():
    markdown = ""
    special_commands = {"!help", "!done"}

    while True:
        user_input = input("Choose a formatter: > ")

        if user_input in special_commands:
            if user_input == "!help":
                print_help()
            elif user_input == "!done":
                save_to_file(markdown)
                break
        elif user_input in FORMATTERS:
            markdown += FORMATTERS[user_input]()
            print(markdown)
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()
