# Read the input
num_rows = int(input())
matrix = [input().split() for _ in range(num_rows)]
num_cols = len(matrix[0])

# Initialize variables
score = [0]
movement = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

# Check if Alice can make a movement
def check_movement(row, col):
    if 0 <= row < num_rows and 0 <= col < num_cols and matrix[row][col] != "R":
        return True

    print("Alice didn't make it to the tea party.")

    rabbit_row, rabbit_col = find_position("R", False)

    if rabbit_row + rabbit_col == row + col:
        matrix[row][col] = "*"

    show_result()
    exit()

# Find the position of a symbol in the matrix
def find_position(symbol, alice=True):
    for row in range(num_rows):
        if symbol in matrix[row]:
            col = matrix[row].index(symbol)
            if alice:
                matrix[row][col] = "*"
            return row, col

# Move Alice
def move_alice(row, col, movement_pos):
    move_row, move_col = row + movement[movement_pos][0], col + movement[movement_pos][1]

    if check_movement(move_row, move_col):
        if matrix[move_row][move_col][-1].isdigit():
            score[0] += int(matrix[move_row][move_col])

        matrix[move_row][move_col] = "*"

    return move_row, move_col

# Show the resulting matrix
def show_result():
    for row in matrix:
        print(" ".join(row))

# Find the position of Alice in the matrix
alice_row, alice_col = find_position("A")

# Move Alice until she reaches the tea party or gets stuck
while score[0] < 10:
    move = input()
    alice_row, alice_col = move_alice(alice_row, alice_col, move)

# Print the final result
print("She did it! She went to the party.")
show_result()
