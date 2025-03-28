#Displays the playing field on the screen
def print_board(board):
    print("---------")
    for row in board:
        print(f"| {' '.join(row)} |")
    print("---------")


#Checks if there is a winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return board[0][2]
    return None


#Checks if there is a tie (all cells are filled)
def is_draw(board):
    for row in board:
        if "_" in row:
            return False
    return True


#Checks whether a move to the given cell is possible
def is_valid_move(board, x, y):
    return 0 <= x < 3 and 0 <= y < 3 and board[x][y] == "_"


#Main function
def main():

    board = [["_" for _ in range(3)] for _ in range(3)]
    print_board(board)

    current_player = "X"


    while True:
        try:
            #Input of coordinates by the player
            coordinates = input(f"Enter the coordinates for {current_player}: ").split()

            #Check for correct input
            if len(coordinates) != 2 or not all(c.isdigit() for c in coordinates):
                print("You should enter numbers!")
                continue

            #We convert the entered coordinates into a numerical format
            x, y = map(int, coordinates)

            #Checking the coordinate range
            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Coordinates should be from 1 to 3!")
                continue

            #We convert the coordinates into the format for the array
            x, y = x - 1, y - 1

            #Check if the cell is not busy
            if not is_valid_move(board, x, y):
                print("This cell is occupied! Choose another one!")
                continue

            #Making a move
            board[x][y] = current_player
            print_board(board)

            #Check for victory
            winner = check_winner(board)
            if winner:
                print(f"{winner} wins")
                break

            #Checking for a draw
            if is_draw(board):
                print("Draw")
                break

            #change of player
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input. Please try again.")


#Starting the program
if __name__ == "__main__":
    main()
