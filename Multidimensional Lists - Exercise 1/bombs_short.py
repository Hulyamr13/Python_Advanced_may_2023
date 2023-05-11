n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = [tuple(map(int, coord.split(','))) for coord in input().split()]

for bomb in bombs:
    row, col = bomb
    bomb_damage = matrix[row][col]
    if bomb_damage > 0:
        matrix[row][col] = 0
        for row_pos, col_pos in ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)):
            if 0 <= row + row_pos < n and 0 <= col + col_pos < n and matrix[row + row_pos][col + col_pos] > 0:
                matrix[row + row_pos][col + col_pos] -= bomb_damage

alive_cells = [num for row in matrix for num in row if num > 0]
print(f"Alive cells: {len(alive_cells)}\nSum: {sum(alive_cells)}")
for row in matrix:
    print(" ".join(str(cell) for cell in row))