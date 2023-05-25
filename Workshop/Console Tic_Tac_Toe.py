import math

# Global Variables
player_one = None
player_two = None
board = [[' ' for _ in range(3)] for _ in range(3)]
loop = True

# Setup function
def setup():
    global player_one, player_two
    player_one = [input("Player 1, enter your name: "), '']
    player_one[1] = input(f"{player_one[0]}, choose your sign (X/O): ").upper()
    player_two = [input("Player 2, enter your name: "), 'O' if player_one[1] == 'X' else 'X']

    print("\nGame Rules:")
    print("-----------")
    print("To make a move, enter the number corresponding to the position on the board.\n")

# Function to draw the board
def draw_board(board):
    for row in board:
        print('|', end='')
        for label in row:
            print(label, end='|')
        print('\n-------')

# Function to check if a player has won
def check_if_won(current, board):
    global loop
    won = False

    # Check rows
    for row in board:
        if row.count(current[1]) == 3:
            won = True

    # Check columns
    for col in range(3):
        if board[0][col] == current[1] and board[1][col] == current[1] and board[2][col] == current[1]:
            won = True

    # Check diagonals
    if (board[0][0] == current[1] and board[1][1] == current[1] and board[2][2] == current[1]) or \
       (board[0][2] == current[1] and board[1][1] == current[1] and board[2][0] == current[1]):
        won = True

    if won:
        draw_board(board)
        print(f"{current[0]} wins!")
        loop = False

# Function to play the game
def play():
    global loop
    current = player_one
    other = player_two

    while loop:
        draw_board(board)
        choice = int(input(f"{current[0]}, choose a position (1-9): "))

        row = math.ceil(choice / 3) - 1
        col = (choice - 1) % 3

        if board[row][col] == ' ':
            board[row][col] = current[1]
            check_if_won(current, board)
            current, other = other, current
        else:
            print("Invalid move. Try again.")

# Main Logic
def main():
    setup()
    play()

# Start the game
main()
