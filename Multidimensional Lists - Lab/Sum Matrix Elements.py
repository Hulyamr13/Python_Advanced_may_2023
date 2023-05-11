# read matrix size from input
rows, columns = map(int, input().split(', '))

# read matrix elements from input and calculate total sum
matrix = []
total_sum = 0
for i in range(rows):
    row = list(map(int, input().split(', ')))
    matrix.append(row)
    total_sum += sum(row)

# print the total sum and the matrix
print(total_sum)
print(matrix)