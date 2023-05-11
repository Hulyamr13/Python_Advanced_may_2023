rows, cols = map(int, input().split())
matrix = [list(input()) for _ in range(rows)]
commands = list(input())
spawn_pos = ((-1, 0), (0, 1), (1, 0), (0, -1))
player_pos = next((i, j) for i in range(rows) for j in range(cols) if matrix[i][j] == "P")
dead, won, result = False, False, ""


def spread_bunnies():
    global dead, result
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                for pos in spawn_pos:
                    current_row, current_col = row + pos[0], col + pos[1]
                    if 0 <= current_row < rows and 0 <= current_col < cols:
                        if matrix[current_row][current_col] == ".":
                            matrix[current_row][current_col] = "b"
                        elif matrix[current_row][current_col] == "P" and not won and not dead:
                            dead, result = True, f"dead: {current_row} {current_col}"
                            matrix[current_row][current_col] = "b"
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "b":
                matrix[row][col] = "B"
    if won or dead:
        [print(''.join(sublist)) for sublist in matrix]
        print(result)
        raise SystemExit


def move_player(row, col):
    global player_pos, won, dead, result
    if 0 <= row < rows and 0 <= col < cols:
        if matrix[row][col] == "B":
            result = f"dead: {row} {col}"
            matrix[player_pos[0]][player_pos[1]], dead = ".", True
        else:
            matrix[player_pos[0]][player_pos[1]], player_pos = ".", (row, col)
            matrix[player_pos[0]][player_pos[1]] = "P"
    else:
        result = f"won: {player_pos[0]} {player_pos[1]}"
        matrix[player_pos[0]][player_pos[1]], won = ".", True
    spread_bunnies()


while not dead and not won:
    current_command = commands.pop(0)
    row, col = player_pos
    if current_command == "U":
        move_player(row - 1, col)
    elif current_command == "D":
        move_player(row + 1, col)
    elif current_command == "R":
        move_player(row, col + 1)
    elif current_command == "L":
        move_player(row, col - 1)
