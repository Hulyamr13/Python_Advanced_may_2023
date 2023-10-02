def in_the_matrix(row, col, row_matrix):
    return row >= 0 and row < row_matrix and col >= 0 and col < row_matrix

def change_position(cmd, player_pos, n):
    if cmd == "up":
        if in_the_matrix(player_pos[0] - 1, player_pos[1], n):
            player_pos[0] -= 1
        else:
            player_pos[0] = n - 1
    elif cmd == "down":
        if in_the_matrix(player_pos[0] + 1, player_pos[1], n):
            player_pos[0] += 1
        else:
            player_pos[0] = 0
    elif cmd == "left":
        if in_the_matrix(player_pos[0], player_pos[1] - 1, n):
            player_pos[1] -= 1
        else:
            player_pos[1] = n - 1
    elif cmd == "right":
        if in_the_matrix(player_pos[0], player_pos[1] + 1, n):
            player_pos[1] += 1
        else:
            player_pos[1] = 0

n = int(input())
cmd_count = int(input())

matrix = [['.' for col in range(n)] for row in range(n)]
player_pos = [0, 0]

for row in range(n):
    input_str = input()
    for col in range(len(input_str)):
        matrix[row][col] = input_str[col]
        if input_str[col] == 'P':
            player_pos = [row, col]

player_old_pos = [0, 0]
race_over = False

while cmd_count > 0:
    cmd = input()

    player_old_pos[0] = player_pos[0]
    player_old_pos[1] = player_pos[1]

    matrix[player_pos[0]][player_pos[1]] = '.'
    change_position(cmd, player_pos, n)

    if matrix[player_pos[0]][player_pos[1]] == 'B':
        change_position(cmd, player_pos, n)
    elif matrix[player_pos[0]][player_pos[1]] == 'T':
        player_pos[0] = player_old_pos[0]
        player_pos[1] = player_old_pos[1]
    elif matrix[player_pos[0]][player_pos[1]] == 'F':
        matrix[player_pos[0]][player_pos[1]] = 'P'
        race_over = True
        break

    matrix[player_pos[0]][player_pos[1]] = 'P'
    cmd_count -= 1

if race_over:
    print("Well done, the player won first place!")
else:
    print("Oh no, the player got lost on the track!")

for row in range(n):
    print(''.join(matrix[row]))
