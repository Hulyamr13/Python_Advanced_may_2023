def change_position(input, player_pos, n, out_pastry):
    if input == "up":
        if in_matrix(player_pos[0] - 1, player_pos[1], n):
            player_pos[0] -= 1
        else:
            out_pastry[0] = 1
    elif input == "down":
        if in_matrix(player_pos[0] + 1, player_pos[1], n):
            player_pos[0] += 1
        else:
            out_pastry[0] = 1
    elif input == "left":
        if in_matrix(player_pos[0], player_pos[1] - 1, n):
            player_pos[1] -= 1
        else:
            out_pastry[0] = 1
    elif input == "right":
        if in_matrix(player_pos[0], player_pos[1] + 1, n):
            player_pos[1] += 1
        else:
            out_pastry[0] = 1

def in_matrix(row, col, n):
    return row >= 0 and row < n and col >= 0 and col < n

n = int(input())
matrix = [None] * n
player_pos = [0, 0]
pillar_c = [[0, 0], [0, 0]]
out_pastry = [0]

for i in range(n):
    matrix[i] = list(input())
    for j in range(n):
        if matrix[i][j] == "S":
            player_pos[0], player_pos[1] = i, j
        elif matrix[i][j] == "P":
            if pillar_c[0][0] == 0 and pillar_c[0][1] == 0:
                pillar_c[0][0], pillar_c[0][1] = i, j
            else:
                pillar_c[1][0], pillar_c[1][1] = i, j

money = 0

while money < 50:
    input_line = input()
    matrix[player_pos[0]][player_pos[1]] = "-"
    change_position(input_line, player_pos, n, out_pastry)

    if out_pastry[0] == 1:
        break

    if matrix[player_pos[0]][player_pos[1]].isdigit():
        money += int(matrix[player_pos[0]][player_pos[1]])

    if matrix[player_pos[0]][player_pos[1]] == "P":
        matrix[player_pos[0]][player_pos[1]] = "-"
        if player_pos[0] == pillar_c[0][0] and player_pos[1] == pillar_c[0][1]:
            player_pos[0], player_pos[1] = pillar_c[1][0], pillar_c[1][1]
        else:
            player_pos[0], player_pos[1] = pillar_c[0][0], pillar_c[0][1]
    matrix[player_pos[0]][player_pos[1]] = "S"

if out_pastry[0] == 1:
    print("Bad news! You are out of the pastry shop.")
else:
    print("Good news! You succeeded in collecting enough money!")
print(f"Money: {money}")

for row in matrix:
    print("".join(row))
