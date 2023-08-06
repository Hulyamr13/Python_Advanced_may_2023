rows = int(input())
cols = int(input())

numbers = []

for r in range(rows):
    elements = list(map(int, input().split()))
    numbers.append(elements)

sums = [[0] * cols for _ in range(rows)]
sums[0][0] = numbers[0][0]

# First row
for c in range(1, cols):
    sums[0][c] = sums[0][c - 1] + numbers[0][c]

# First column
for r in range(1, rows):
    sums[r][0] = sums[r - 1][0] + numbers[r][0]

for r in range(1, rows):
    for c in range(1, cols):
        upperCell = sums[r - 1][c]
        leftCell = sums[r][c - 1]
        sums[r][c] = max(upperCell, leftCell) + numbers[r][c]

# Find Path
row = rows - 1
col = cols - 1

path = []
path.append(f"[{row}, {col}]")


while row > 0 and col > 0:
    upper = sums[row - 1][col]
    left = sums[row][col - 1]

    if upper > left:
        row -= 1
    else:
        col -= 1

    path.append(f"[{row}, {col}]")


while row > 0:
    row -= 1
    path.append(f"[{row}, {col}]")

while col > 0:
    col -= 1
    path.append(f"[{row}, {col}]")

print(" ".join(path[::-1]))
