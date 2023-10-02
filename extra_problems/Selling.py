def main():
    n = int(input())

    matrix = [[0] * n for _ in range(n)]
    player_pos = [0, 0]
    pillar_c = [[0] * 2 for _ in range(2)]
    out_pastry = [0]

    fill_matrix(matrix, player_pos, pillar_c)

    money = 0

    while money < 50:
        input_str = input()
        matrix[player_pos[0]][player_pos[1]] = '-'
        change_position(input_str, player_pos, n, out_pastry)

        if out_pastry[0] == 1:
            break

        if str(matrix[player_pos[0]][player_pos[1]]).isdigit():
            money += int(str(matrix[player_pos[0]][player_pos[1]]))

        if matrix[player_pos[0]][player_pos[1]] == 'O':
            matrix[player_pos[0]][player_pos[1]] = '-'
            if player_pos[0] == pillar_c[0][0] and player_pos[1] == pillar_c[0][1]:
                player_pos[0] = pillar_c[1][0]
                player_pos[1] = pillar_c[1][1]
            else:
                player_pos[0] = pillar_c[0][0]
                player_pos[1] = pillar_c[0][1]
        matrix[player_pos[0]][player_pos[1]] = 'S'

    if out_pastry[0] == 1:
        print("Bad news, you are out of the bakery.")
    else:
        print("Good news! You succeeded in collecting enough money!")
    print(f"Money: {money}")
    for row in matrix:
        print("".join(row))


def change_position(input_str, player_pos, n, out_pastry):
    if input_str == "up":
        if in_matrix(player_pos[0]-1, player_pos[1], n):
            player_pos[0] -= 1
        else:
            out_pastry[0] = 1
    elif input_str == "down":
        if in_matrix(player_pos[0]+1, player_pos[1], n):
            player_pos[0] += 1
        else:
            out_pastry[0] = 1
    elif input_str == "left":
        if in_matrix(player_pos[0], player_pos[1]-1, n):
            player_pos[1] -= 1
        else:
            out_pastry[0] = 1
    elif input_str == "right":
        if in_matrix(player_pos[0], player_pos[1]+1, n):
            player_pos[1] += 1
        else:
            out_pastry[0] = 1


def in_matrix(row, col, n):
    return row >= 0 and row < n and col >= 0 and col < n


def fill_matrix(matrix, player_pos, pillar_c):
    pillar_r = 0
    for row in range(len(matrix)):
        input_str = input()
        for col in range(len(input_str)):
            matrix[row][col] = input_str[col]
            if input_str[col] == 'S':
                player_pos[0] = row
                player_pos[1] = col
            if input_str[col] == 'O':
                pillar_c[pillar_r][0] = row
                pillar_c[pillar_r][1] = col
                pillar_r += 1


if __name__ == '__main__':
    main()
