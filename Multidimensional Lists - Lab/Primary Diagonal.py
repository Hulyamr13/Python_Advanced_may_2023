# read matrix size from input
n = int(input())

# read matrix elements from input
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# calculate the sum of the primary diagonal and print it
diagonal_sum = sum(matrix[i][i] for i in range(n))
print(diagonal_sum)