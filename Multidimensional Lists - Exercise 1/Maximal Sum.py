rows, columns = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

max_sum = None
max_sum_row = None
max_sum_col = None

for row in range(rows - 2):
    for col in range(columns - 2):
        current_sum = sum(matrix[row][col:col+3]) + \
                      sum(matrix[row+1][col:col+3]) + \
                      sum(matrix[row+2][col:col+3])
        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum
            max_sum_row = row
            max_sum_col = col

print(f"Sum = {max_sum}")
for row in range(max_sum_row, max_sum_row+3):
    for col in range(max_sum_col, max_sum_col+3):
        print(matrix[row][col], end=' ')
    print()
