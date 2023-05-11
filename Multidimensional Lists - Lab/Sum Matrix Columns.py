# read matrix size from input
rows, columns = map(int, input().split(', '))

# read matrix elements from input
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# calculate the sum for each column and print it on separate lines
for j in range(columns):
    col_sum = sum(matrix[i][j] for i in range(rows))
    print(col_sum)