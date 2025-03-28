import random


def bot_move(pencils):
    # Bot logic for losing and winning positions
    if pencils == 1:
        return 1
    elif pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:
        return random.randint(1 , 3)



def main():
    # Checking the number of pencils
    while True:
        try:
            pencils = int(input("How many pencils would you like to use:\n"))
            if pencils <= 0:
                print("The number of pencils should be positive")
                continue
            break
        except ValueError:
            print("The number of pencils should be numeric")
    # Player's choice
    while True:
        player1 = "John"
        player2 = "Jack"
        first_player = input(f"Who will be the first ({player1}, {player2}):\n")
        if first_player not in [player1, player2]:
            print(f"Choose between '{player1}' and '{player2}'")
            continue
        break

    current_player = first_player

    # Game cycle
    while pencils > 0:
        print("|" * pencils)
        print(f"{current_player}'s turn!")

        if current_player == player2:
            move = bot_move(pencils)
            print(move)
        else:
            while True:
                try:
                    move = int(input())
                    if move not in [1, 2, 3]:
                        print("Possible values: '1', '2' or '3'")
                        continue
                    if move > pencils:
                        print("Too many pencils were taken")
                        continue
                    break
                except ValueError:
                    print("Possible values: '1', '2' or '3'")

        pencils -= move

        # Check at the end of the game
        if pencils == 0:
            winner = player1 if current_player == player2 else player2
            print(f"{winner} won!")
            break

        # Switch player
        current_player = player1 if current_player == player2 else player2


if __name__ == "__main__":
    main()
