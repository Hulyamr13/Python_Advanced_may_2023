n = int(input())

matrix = [[''] * n for i in range(n)]
mirrors = [[0, 0], [0, 0]]

rO, cO = -1, -1
m_row = 0
gold = 0

def in_the_matrix(row, col, row_matrix, col_matrix):
    return row >= 0 and row <= row_matrix - 1 and col >= 0 and col <= col_matrix - 1

for i in range(n):
    input_str = input()
    for j in range(len(input_str)):
        matrix[i][j] = input_str[j]
        if input_str[j] == 'A':
            rO, cO = i, j
        if input_str[j] == 'M':
            mirrors[m_row][0], mirrors[m_row][1] = i, j
            m_row += 1

while gold < 65:
    direction = input()
    oldRO, oldCO = rO, cO

    if direction == 'up':
        rO -= 1
    elif direction == 'down':
        rO += 1
    elif direction == 'right':
        cO += 1
    elif direction == 'left':
        cO -= 1

    matrix[oldRO][oldCO] = '-'

    if in_the_matrix(rO, cO, n, n):
        if matrix[rO][cO].isdigit():
            gold += int(matrix[rO][cO])

        if matrix[rO][cO] == 'M':
            if rO == mirrors[0][0] and cO == mirrors[0][1]:
                rO, cO = mirrors[1][0], mirrors[1][1]
                matrix[mirrors[0][0]][mirrors[0][1]] = '-'
            else:
                rO, cO = mirrors[0][0], mirrors[0][1]
                matrix[mirrors[1][0]][mirrors[1][1]] = '-'

        matrix[rO][cO] = 'A'
    else:
        break

if in_the_matrix(rO, cO, n, n):
    print('Very nice swords, I will come back for more!')
else:
    print('I do not need more swords!')

print(f'The king paid {gold} gold coins.')

for row in matrix:
    for col in row:
        print(col, end='')
    print()
