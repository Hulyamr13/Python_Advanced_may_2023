# read matrix size from input
rows = int(input())

# read matrix elements from input
matrix = []
for i in range(rows):
    row = list(map(int, input().split(', ')))
    matrix.append(row)

# flatten the matrix into a list
flattened_matrix = [num for row in matrix for num in row]

# print the flattened matrix
print(flattened_matrix)