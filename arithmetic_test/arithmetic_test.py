import random


# Generates a math question based on the difficulty level selected.
def generate_question(level):
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        question = f"{num1} {operation} {num2}"
        correct_answer = eval(question)
    elif level == 2:
        num1 = random.randint(11, 29)
        question = f"{num1}"
        correct_answer = num1 ** 2
    return question, correct_answer


# Prompts the user for an answer and checks if it is an integer.
def get_user_answer():
    while True:
        try:
            user_input = input("> ").strip()
            user_answer = int(user_input)
            return user_answer
        except ValueError:
            print("Wrong format! Try again.")


# Offers the user the choice of difficulty level.
def select_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        try:
            level = int(input("> ").strip())
            if level in [1, 2]:
                return level
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")


# Saves the user's result to the results.txt file.
def save_results(name, score, level):
    level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
    result_line = f"{name}: {score}/5 in level {level} ({level_description}).\n"
    with open("results.txt", "a") as file:
        file.write(result_line)
    print("The results are saved in \"results.txt\".")


# The main function of the program: starts the quiz, calculates the points and offers to save the result.
def main():
    level = select_level()
    correct_count = 0
    total_questions = 5

    for _ in range(total_questions):
        question, correct_answer = generate_question(level)
        print(question)

        user_answer = get_user_answer()
        if user_answer == correct_answer:
            print("Right!")
            correct_count += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_count}/{total_questions}.")

    print("Would you like to save the result? Enter yes or no.")
    save_input = input("> ").strip().lower()
    if save_input in ["yes", "y"]:
        print("What is your name?")
        name = input("> ").strip()
        save_results(name, correct_count, level)


if __name__ == "__main__":
    main()
