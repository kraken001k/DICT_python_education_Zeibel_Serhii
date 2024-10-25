import random
import string

def play_game():


    words = ['python', 'java', 'script', 'php']

    word_to_guess = random.choice(words)

    current_word = ['-' for _ in word_to_guess]

    word_letters = set(word_to_guess)

    guessed_letters = set()
    lives = 8

    while lives > 0:
        print(''.join(current_word))

        guess = input("Input a letter: > ")

        if len(guess) != 1:
            print("You should input a single letter")
            continue
        if guess not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
            continue
        if guess in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:

            current_word = [letter if letter in guessed_letters else '-' for letter in word_to_guess]
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

        if ''.join(current_word) == word_to_guess:
            print(f"You guessed the word {word_to_guess}!\nYou survived!")
            break

    else:
        print(f"You lost! The word was: {word_to_guess}")


def menu():
    print("HANGMAN\nThe game will be available soon")


    while True:
        choice = input('Type "play" to play the game, "exit" to quit: > ')
        if choice == "play":
            play_game()
        elif choice == "exit":
            break
        else:
            print('Please type "play" to start the game or "exit" to quit.')


menu()
