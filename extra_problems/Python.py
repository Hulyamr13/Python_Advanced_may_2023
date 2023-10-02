def main():
    n = int(input())
    commands = input().split(", ")

    matrix = []
    python_pos = [0, 0, 0]

    fill_matrix(n, matrix, python_pos)

    python_length = 1
    is_dead = False

    for command in commands:
        change_positions(command, python_pos, n)
        if matrix[python_pos[0]][python_pos[1]] == "f":
            python_length += 1
            python_pos[2] -= 1
        if matrix[python_pos[0]][python_pos[1]] == "e":
            is_dead = True
            break

    if python_pos[2] == 0:
        print(f"You win! Final python length is {python_length}")
    elif is_dead:
        print("You lose! Killed by an enemy!")
    else:
        print(f"You lose! There is still {python_pos[2]} food to be eaten.")

def change_positions(command, python_pos, row_matrix):
    if command == "up":
        if in_the_matrix(python_pos[0] - 1, python_pos[1], row_matrix):
            python_pos[0] -= 1
        else:
            python_pos[0] = row_matrix - 1
    elif command == "down":
        if in_the_matrix(python_pos[0] + 1, python_pos[1], row_matrix):
            python_pos[0] += 1
        else:
            python_pos[0] = 0
    elif command == "left":
        if in_the_matrix(python_pos[0], python_pos[1] - 1, row_matrix):
            python_pos[1] -= 1
        else:
            python_pos[1] = row_matrix - 1
    elif command == "right":
        if in_the_matrix(python_pos[0], python_pos[1] + 1, row_matrix):
            python_pos[1] += 1
        else:
            python_pos[1] = 0

def in_the_matrix(row, col, row_matrix):
    return row >= 0 and row < row_matrix and col >= 0 and col < row_matrix

def fill_matrix(row_matrix, matrix, python_pos):
    for i in range(row_matrix):
        row = input().split()
        matrix.append(row)
        for j in range(len(row)):
            if row[j] == "s":
                matrix[i][j] = "*"
                python_pos[0] = i
                python_pos[1] = j
            if row[j] == "f":
                python_pos[2] += 1

if __name__ == '__main__':
    main()
