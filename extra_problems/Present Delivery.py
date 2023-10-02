def give_present(matrix, row_mutator, col_mutator):
    global presents, all_nice_kids, nice_kids, santa_row, santa_col
    if matrix[santa_row + row_mutator][santa_col + col_mutator] == 'X':
        presents -= 1
        all_nice_kids += 1
    elif matrix[santa_row + row_mutator][santa_col + col_mutator] == 'V':
        presents -= 1
        nice_kids -= 1
        all_nice_kids += 1
    matrix[santa_row + row_mutator][santa_col + col_mutator] = '-'

def in_the_matrix(row_mutator, col_mutator, row_matrix):
    global santa_row, santa_col
    return 0 <= santa_row + row_mutator < row_matrix and 0 <= santa_col + col_mutator < row_matrix

def change_position(command):
    global santa_row, santa_col
    matrix[santa_row][santa_col] = '-'
    if command == 'up' and in_the_matrix(-1, 0, row_matrix):
        santa_row -= 1
    elif command == 'down' and in_the_matrix(1, 0, row_matrix):
        santa_row += 1
    elif command == 'left' and in_the_matrix(0, -1, row_matrix):
        santa_col -= 1
    elif command == 'right' and in_the_matrix(0, 1, row_matrix):
        santa_col += 1

def print_matrix():
    for row in matrix:
        print(' '.join(row))

presents = int(input())
row_matrix = int(input())

matrix = []
santa_row, santa_col = -1, -1
nice_kids, all_nice_kids = 0, 0

for i in range(row_matrix):
    row = input().split()
    matrix.append(row)
    for j in range(len(row)):
        if matrix[i][j] == 'S':
            santa_row, santa_col = i, j
            matrix[i][j] = '-'
        elif matrix[i][j] == 'V':
            nice_kids += 1

command = None
while presents > 0 and command != 'Christmas morning':
    command = input()
    change_position(command)
    if matrix[santa_row][santa_col] == 'V':
        presents -= 1
        nice_kids -= 1
        all_nice_kids += 1
    elif matrix[santa_row][santa_col] == 'X':
        matrix[santa_row][santa_col] = '-'
    elif matrix[santa_row][santa_col] == 'C':
        give_present(matrix, 1, 0)
        give_present(matrix, -1, 0)
        give_present(matrix, 0, 1)
        give_present(matrix, 0, -1)

if presents == 0:
    print('Santa ran out of presents!')
print_matrix()
if nice_kids == 0:
    print(f'Good job, Santa! {all_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids} nice kid/s.')
