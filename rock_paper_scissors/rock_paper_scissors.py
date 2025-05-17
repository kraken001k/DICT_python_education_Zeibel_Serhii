import random

# Load player ratings from file
def load_ratings(filename="rating.txt"):
    data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, points = line.strip().split()
                data[name] = int(points)
    except FileNotFoundError:
        pass
    return data

# Save updated ratings back to file
def save_ratings(rating_data, filename="rating.txt"):
    with open(filename, "w") as file:
        for name, points in rating_data.items():
            file.write(f"{name} {points}\n")

# Generate rules of what beats what
def generate_beats_map(option_list):
    beats = {}
    for i, option in enumerate(option_list):
        rotated = option_list[i+1:] + option_list[:i]
        half = len(rotated) // 2
        beats[option] = rotated[half:]
    return beats

# --- Game Start ---
user_name = input("Enter your name:> ")
print(f"Hello, {user_name}")
print("Select the signs that will play:")
print("(rock,fire,scissors,snake,human,tree,wolf,sponge,paper,air,water,dragon,devil,lightning,gun)")

# Load and initialize ratings
all_ratings = load_ratings()
score = all_ratings.get(user_name, 0)

# Read game options
user_input = input("> ")
if user_input.strip() == "":
    game_options = ["rock", "paper", "scissors"]
else:
    game_options = user_input.strip().split(",")

print("Okay, let's start")

# Static full set of 15 options
full_15 = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf",
           "sponge", "paper", "air", "water", "dragon", "devil", "lightning", "gun"]

# Build rules
if game_options == full_15:
    beats_map = {
        "rock": ["fire", "scissors", "snake", "human", "tree", "wolf", "sponge"],
        "fire": ["scissors", "snake", "human", "tree", "wolf", "sponge", "paper"],
        "scissors": ["snake", "human", "tree", "wolf", "sponge", "paper", "air"],
        "snake": ["human", "tree", "wolf", "sponge", "paper", "air", "water"],
        "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
        "tree": ["wolf", "sponge", "paper", "air", "water", "dragon", "devil"],
        "wolf": ["sponge", "paper", "air", "water", "dragon", "devil", "lightning"],
        "sponge": ["paper", "air", "water", "dragon", "devil", "lightning", "gun"],
        "paper": ["air", "water", "dragon", "devil", "lightning", "gun", "rock"],
        "air": ["water", "dragon", "devil", "lightning", "gun", "rock", "fire"],
        "water": ["dragon", "devil", "lightning", "gun", "rock", "fire", "scissors"],
        "dragon": ["devil", "lightning", "gun", "rock", "fire", "scissors", "snake"],
        "devil": ["lightning", "gun", "rock", "fire", "scissors", "snake", "human"],
        "lightning": ["gun", "rock", "fire", "scissors", "snake", "human", "tree"],
        "gun": ["rock", "fire", "scissors", "snake", "human", "tree", "wolf"]
    }
else:
    beats_map = generate_beats_map(game_options)

# --- Game Loop ---
while True:
    try:
        user_choice = input("> ")
    except EOFError:
        print("Bye!")
        break

    if user_choice == "!exit":
        print("Bye!")
        all_ratings[user_name] = score
        save_ratings(all_ratings)
        break
    elif user_choice == "!rating":
        print(f"Your rating: {score}")
    elif user_choice not in game_options:
        print("Invalid input")
    else:
        computer_choice = random.choice(game_options)
        if user_choice == computer_choice:
            score += 50
            print(f"There is a draw ({computer_choice})")
        elif computer_choice in beats_map[user_choice]:
            score += 100
            print(f"Well done. The computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but the computer chose {computer_choice}")
