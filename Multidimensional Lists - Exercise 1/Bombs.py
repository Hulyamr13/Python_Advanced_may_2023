n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = [tuple(map(int, coord.split(','))) for coord in input().split()]


def explode(r, c, value):
    if matrix[r][c] <= 0:
        return

    damage = matrix[r][c]
    matrix[r][c] = 0

    for i in range(max(0, r-1), min(n, r+2)):
        for j in range(max(0, c-1), min(n, c+2)):
            if matrix[i][j] > 0:
                matrix[i][j] -= damage

    return


for bomb in bombs:
    row, col = bomb
    value = matrix[row][col]
    explode(row, col, value)

alive_cells = 0
sum_of_cells = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
            alive_cells += 1
            sum_of_cells += matrix[i][j]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")
for row in matrix:
    print(" ".join(str(cell) for cell in row))
