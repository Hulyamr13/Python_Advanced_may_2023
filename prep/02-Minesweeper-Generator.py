def check_next_el(matrix, row, col):
    positions = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]

    counter = 0
    for position in positions:

        potential_row = row + position[0]
        potential_col = col + position[1]

        if is_valid_bound(potential_row, potential_col, len(matrix)):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == '*':
                counter += 1
    return counter


def is_valid_bound(row, col, length):
    return 0 <= row < length and 0 <= col < length


size_matrix = int(input())
number_bombs = int(input())

matrix = []
for i in range(size_matrix):
    matrix.append([])
    for j in range(size_matrix):
        matrix[i].append(0)

for _ in range(number_bombs):
    [row, col] = map(lambda x: int(x), input()[1:][:-1].split(', '))
    matrix[row][col] = '*'

for row_idx in range(size_matrix):
    for col_idx in range(size_matrix):
        if matrix[row_idx][col_idx] != '*':
            counter = check_next_el(matrix, row_idx, col_idx)
            matrix[row_idx][col_idx] = counter

for row in matrix:
    print(' '.join([str(x) for x in row]))