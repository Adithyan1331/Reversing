import random

# Create an empty board
board = [" " for _ in range(9)]

# Display the board
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Check winner
def check_winner(symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[pos] == symbol for pos in combo):
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Player move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
            elif board[move] != " ":
                print("That position is already taken.")
            else:
                board[move] = player
                break

        except ValueError:
            print("Please enter a valid number.")

# Computer move
def computer_move():
    print("Computer is making a move...")

    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = computer
            if check_winner(computer):
                return
            board[i] = " "

    # Block player from winning
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_winner(player):
                board[i] = computer
                return
            board[i] = " "

    # Take center
    if board[4] == " ":
        board[4] = computer
        return

    # Take corners
    corners = [0, 2, 6, 8]
    free_corners = [c for c in corners if board[c] == " "]

    if free_corners:
        board[random.choice(free_corners)] = computer
        return

    # Take any available space
    free_spaces = [i for i in range(9) if board[i] == " "]

    if free_spaces:
        board[random.choice(free_spaces)] = computer

# Show position guide
def show_positions():
    print("\nPosition Guide:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

# Main program
print("=== TIC TAC TOE ===")
show_positions()

while True:
    player = input("Choose X or O: ").upper()

    if player in ["X", "O"]:
        break

    print("Please enter only X or O.")

computer = "O" if player == "X" else "X"

print(f"\nYou are {player}")
print(f"Computer is {computer}")

# X always starts
turn = "X"

while True:
    print_board()

    if turn == player:
        player_move()
    else:
        computer_move()

    if check_winner(turn):
        print_board()

        if turn == player:
            print("🎉 Congratulations! You Win!")
        else:
            print("🤖 Computer Wins!")

        break

    if is_draw():
        print_board()
        print("🤝 Match Draw!")
        break

    turn = "O" if turn == "X" else "X"

print("\nGame Over!")