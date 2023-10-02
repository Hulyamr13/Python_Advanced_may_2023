def change_position(command, player_pos, n):
    if command == "up" and in_matrix(player_pos[0] - 1, player_pos[1], n):
        player_pos[0] -= 1
    elif command == "down" and in_matrix(player_pos[0] + 1, player_pos[1], n):
        player_pos[0] += 1
    elif command == "left" and in_matrix(player_pos[0], player_pos[1] - 1, n):
        player_pos[1] -= 1
    elif command == "right" and in_matrix(player_pos[0], player_pos[1] + 1, n):
        player_pos[1] += 1


def in_matrix(row, col, n):
    return 0 <= row < n and 0 <= col < n


n = int(input())
commands = input().split(",")
matrix = [input().split() for _ in range(n)]
player_pos = [0, 0]
bomb_number = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "s":
            player_pos = [row, col]
            matrix[player_pos[0]][player_pos[1]] = "+"
        elif matrix[row][col] == "B":
            bomb_number += 1

end = False
bombs_found = False

for s in commands:
    change_position(s, player_pos, n)

    if matrix[player_pos[0]][player_pos[1]] == "B":
        print("You found a bomb!")
        bomb_number -= 1
        if bomb_number == 0:
            bombs_found = True
            break
        matrix[player_pos[0]][player_pos[1]] = "+"

    if matrix[player_pos[0]][player_pos[1]] == "e":
        end = True
        break

if bombs_found:
    print("Congratulations! You found all bombs!")
elif end:
    print(f"END! {bomb_number} bombs left on the field")
else:
    print(f"{bomb_number} bombs left on the field. Sapper position: ({player_pos[0]},{player_pos[1]})")