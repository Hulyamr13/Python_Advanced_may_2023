# read matrix size from input
rows = int(input())

# read matrix elements from input
matrix = []
for i in range(rows):
    row = list(map(int, input().split(', ')))
    matrix.append(row)

# create new matrix only with even numbers
even_matrix = [[num for num in row if num % 2 == 0] for row in matrix]

# print the even matrix
print(even_matrix)