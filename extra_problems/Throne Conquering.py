energy = int(input())
rows = int(input())

matrix = []
p_row = 0
p_col = 0
helen_is_here = False

for i in range(rows):
    array = input()
    matrix.append(list(array))

for i in range(rows):
    for j in range(len(matrix[i])):
        current_char = matrix[i][j]
        if current_char == 'P':
            p_row = i
            p_col = j

while energy > 0:
    command, e_row, e_col = input().split()
    e_row, e_col = int(e_row), int(e_col)

    matrix[e_row][e_col] = 'S'
    energy -= 1

    if command == 'up' and p_row - 1 != -1:
        matrix[p_row][p_col] = '-'
        p_row -= 1
        if matrix[p_row][p_col] == 'S':
            energy -= 2
            if energy <= 0:
                matrix[p_row][p_col] = 'X'
            else:
                matrix[p_row][p_col] = '-'
        elif matrix[p_row][p_col] == 'H':
            helen_is_here = True
            matrix[p_row][p_col] = '-'
            break

    elif command == 'down' and p_row + 1 < rows:
        matrix[p_row][p_col] = '-'
        p_row += 1
        if matrix[p_row][p_col] == 'S':
            energy -= 2
            if energy <= 0:
                matrix[p_row][p_col] = 'X'
            else:
                matrix[p_row][p_col] = '-'
        elif matrix[p_row][p_col] == 'H':
            helen_is_here = True
            matrix[p_row][p_col] = '-'
            break

    elif command == 'left' and p_col - 1 >= 0:
        matrix[p_row][p_col] = '-'
        p_col -= 1
        if matrix[p_row][p_col] == 'S':
            energy -= 2
            if energy <= 0:
                matrix[p_row][p_col] = 'X'
            else:
                matrix[p_row][p_col] = '-'
        elif matrix[p_row][p_col] == 'H':
            helen_is_here = True
            matrix[p_row][p_col] = '-'
            break

    elif command == 'right' and p_col + 1 < len(matrix[p_row]):
        matrix[p_row][p_col] = '-'
        p_col += 1
        if matrix[p_row][p_col] == 'S':
            energy -= 2
            if energy <= 0:
                matrix[p_row][p_col] = 'X'
            else:
                matrix[p_row][p_col] = '-'
        elif matrix[p_row][p_col] == 'H':
            helen_is_here = True
            matrix[p_row][p_col] = '-'
            break

    if helen_is_here:
        break

    if energy <= 0:
        matrix[p_row][p_col] = 'X'

if helen_is_here:
    print(f"Paris has successfully abducted Helen! Energy left: {energy}")
else:
    print(f"Paris died at {p_row};{p_col}.")

for row in matrix:
    print("".join(row))