from math import ceil

size = 8
matrix = []
white_row, white_col = 0, 0
black_row, black_col = 0, 0

matrix_bord = []
for bord_row in range(size, 0, -1):
    value = [f'{chr(97 + x)}{bord_row}' for x in range(size)]
    matrix_bord.append(value)

for row in range(size):
    value = input().split()
    matrix.append(value)
    for col in range(size):
        if matrix[row][col] == 'b':
            black_row, black_col = row, col

        elif matrix[row][col] == 'w':
            white_row, white_col = row, col

if not abs(black_col - white_col) == 1:
    if (size - black_row) > white_row:
        print(f"Game over! White pawn is promoted to a queen at {matrix_bord[size - size][white_col]}.")

    else:
        print(f"Game over! Black pawn is promoted to a queen at {matrix_bord[size - 1][black_col]}.")


else:
    if abs(black_row - white_row) % 2 == 0:
        print(
            f"Game over! Black win, capture on {matrix_bord[black_row + ceil(abs(black_row - white_row) / 2)][white_col]}.")

    else:
        print(
            f"Game over! White win, capture on {matrix_bord[white_row - ceil(abs(black_row - white_row) / 2)][black_col]}.")