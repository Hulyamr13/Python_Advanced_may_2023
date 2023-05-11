rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
max_sum = None
max_row, max_col = None, None

for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum
            max_row, max_col = row, col

top_left = matrix[max_row][max_col:max_col + 2]
bottom_left = matrix[max_row + 1][max_col:max_col + 2]

print(top_left[0], top_left[1])
print(bottom_left[0], bottom_left[1])
print(max_sum)