def in_the_matrix(row, col, row_matrix):
    return 0 <= row < row_matrix and 0 <= col < row_matrix


def create_matrix(matrix, bee_position):
    for i in range(len(matrix)):
        row = input()
        for j in range(len(row)):
            matrix[i][j] = row[j]
            if row[j] == 'B':
                bee_position[0], bee_position[1] = i, j


n = int(input())

matrix = [[None] * n for _ in range(n)]
bee_position = [0, 0]
out = [0]
create_matrix(matrix, bee_position)

flowers = 0
bonus_found = False

while True:
    command = input()
    if command == "End":
        break

    matrix[bee_position[0]][bee_position[1]] = '.'

    if command == "up":
        if in_the_matrix(bee_position[0] - 1, bee_position[1], n):
            bee_position[0] -= 1
        else:
            out[0] = 1
            break
    elif command == "down":
        if in_the_matrix(bee_position[0] + 1, bee_position[1], n):
            bee_position[0] += 1
        else:
            out[0] = 1
            break
    elif command == "left":
        if in_the_matrix(bee_position[0], bee_position[1] - 1, n):
            bee_position[1] -= 1
        else:
            out[0] = 1
            break
    elif command == "right":
        if in_the_matrix(bee_position[0], bee_position[1] + 1, n):
            bee_position[1] += 1
        else:
            out[0] = 1
            break

    if matrix[bee_position[0]][bee_position[1]] == 'O':
        bonus_found = True
        matrix[bee_position[0]][bee_position[1]] = '.'
        if command == "up":
            if in_the_matrix(bee_position[0] - 1, bee_position[1], n):
                bee_position[0] -= 1
            else:
                out[0] = 1
                break
        elif command == "down":
            if in_the_matrix(bee_position[0] + 1, bee_position[1], n):
                bee_position[0] += 1
            else:
                out[0] = 1
                break
        elif command == "left":
            if in_the_matrix(bee_position[0], bee_position[1] - 1, n):
                bee_position[1] -= 1
            else:
                out[0] = 1
                break
        elif command == "right":
            if in_the_matrix(bee_position[0], bee_position[1] + 1, n):
                bee_position[1] += 1
            else:
                out[0] = 1
                break

    if matrix[bee_position[0]][bee_position[1]] == 'f':
        flowers += 1

    matrix[bee_position[0]][bee_position[1]] = 'B'

if out[0] == 1:
    print("The bee got lost!")
    print(f"Great job, the bee manage to pollinate {flowers} flowers!")
else:
    needed_flowers = 5 - flowers
    print(f"The bee couldn't pollinate the flowers, she needed {5 - flowers} flowers more")

for row in matrix:
    print(''.join(row))

