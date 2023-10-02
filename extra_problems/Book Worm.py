initial_string = input()
size = int(input())
field = []
player_pos = None

for row in range(size):
    current_row = list(input())
    if "P" in current_row:
        player_pos = (row, current_row.index("P"))
    field.append(current_row)

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

result_string = initial_string

while True:
    command = input()
    if command == "end":
        break

    move_row, move_col = moves[command]
    new_row, new_col = player_pos[0] + move_row, player_pos[1] + move_col

    if new_row < 0 or new_row >= size or new_col < 0 or new_col >= size:
        if result_string:
            result_string = result_string[:-1]
    else:
        if field[new_row][new_col] != "-":
            result_string += field[new_row][new_col]

        field[new_row][new_col] = "P"
        field[player_pos[0]][player_pos[1]] = "-"
        player_pos = (new_row, new_col)

print(result_string)
for row in field:
    print("".join(row))
