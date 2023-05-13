BOARD_SIZE = 6

# Read in the board matrix from user input
board = [input().split() for _ in range(BOARD_SIZE)]

# Initialize the total points to 0
total_points = 0

# Allow the player to throw the ball three times
for _ in range(3):
    # Read in the row and column of the current throw
    row, col = map(int, input().strip('()').split(', '))

    # Check that the row and column are valid indices on the board
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
        # Check if the current position is a bucket (marked with 'B')
        if board[row][col] == 'B':
            # If it is, mark it as hit with 'X'
            board[row][col] = 'X'

            # Add the sum of the current column's points to the total score
            for r in range(BOARD_SIZE):
                if board[r][col].isdigit():
                    total_points += int(board[r][col])

# Determine the prize based on the total score
if total_points >= 300:
    prize = "Lego Construction Set"
elif 200 <= total_points <= 299:
    prize = "Teddy Bear"
elif 100 <= total_points <= 199:
    prize = "Football"
else:
    points_needed = 100 - total_points
    print(f"Sorry! You need {points_needed} points more to win a prize.")
    # Exit the program if the player did not win a prize
    exit()

# If the player won a prize, print out the total points and the prize name
print(f"Good job! You scored {total_points} points, and you've won {prize}.")
