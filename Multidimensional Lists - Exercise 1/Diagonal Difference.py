n = int(input())

matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_sum = sum(matrix[i][i] for i in range(n))
secondary_sum = sum(matrix[i][n-1-i] for i in range(n))

diff = abs(primary_sum - secondary_sum)
print(diff)