from collections import deque

dimensions = input().split(',')
n = int(dimensions[0].strip())
m = int(dimensions[1].strip())

matrix = [list(input().strip()) for _ in range(n)]

mouse_position = None
cheese_count = sum(row.count('C') for row in matrix)

for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        if cell == 'M':
            mouse_position = (i, j)
            break

directions = []
while True:
    direction = input().strip()
    if direction == 'danger':
        break
    directions.append(direction)

directions = deque(directions)

for direction in directions:
    if direction == 'danger':
        print("Mouse will come back later!")
        matrix[mouse_position[0]][mouse_position[1]] = 'M'
        break

    row, col = mouse_position
    if direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1

    if not (0 <= row < n and 0 <= col < m):
        print("No more cheese for tonight!")
        break

    if matrix[row][col] == '@':
        continue

    if matrix[row][col] == 'T':
        print("Mouse is trapped!")
        matrix[mouse_position[0]][mouse_position[1]] = '*'
        matrix[row][col] = 'M'
        break

    if matrix[row][col] == 'C':
        cheese_count -= 1
        if cheese_count == 0:
            matrix[row][col] = '*'
            print("Happy mouse! All the cheese is eaten, good night!")
        else:
            matrix[row][col] = 'M'

    matrix[mouse_position[0]][mouse_position[1]] = '*'
    matrix[row][col] = 'M'
    mouse_position = (row, col)

for row in matrix:
    print(''.join(row))
