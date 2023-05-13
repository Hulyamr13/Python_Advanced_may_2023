def navigate_submarine(matrix, start_row, start_col):
    ROWS, COLS = len(matrix), len(matrix[0])
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    submarine_row, submarine_col = start_row, start_col
    mines_hit = 0
    cruisers_destroyed = 0

    while True:
        command = input()
        next_row, next_col = submarine_row + directions[command][0], submarine_col + directions[command][1]

        if not (0 <= next_row < ROWS and 0 <= next_col < COLS):
            continue  # ignore invalid moves

        if matrix[next_row][next_col] == '-':
            matrix[submarine_row][submarine_col] = '-'
            submarine_row, submarine_col = next_row, next_col
        elif matrix[next_row][next_col] == '*':
            mines_hit += 1
            matrix[submarine_row][submarine_col] = '-'
            matrix[next_row][next_col] = 'S'
            submarine_row, submarine_col = next_row, next_col
            if mines_hit == 3:
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_row}, {submarine_col}]!")
                break
        elif matrix[next_row][next_col] == 'C':
            cruisers_destroyed += 1
            matrix[submarine_row][submarine_col] = '-'
            matrix[next_row][next_col] = 'S'
            submarine_row, submarine_col = next_row, next_col
            if cruisers_destroyed == 3:
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                break

    for row in matrix:
        print(''.join(row))


# read input
n = int(input())
matrix = [list(input()) for _ in range(n)]

# find submarine start position
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'S':
            submarine_row, submarine_col = row, col
            break

# navigate submarine through the battlefield
navigate_submarine(matrix, submarine_row, submarine_col)
