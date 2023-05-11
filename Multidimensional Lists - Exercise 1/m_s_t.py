n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
max_sum = max(sum(matrix[i][j:j+3]) + sum(matrix[i+1][j:j+3]) + sum(matrix[i+2][j:j+3])
              for i in range(n-2) for j in range(m-2))
print(f"Sum = {max_sum}")
for i in range(n-2):
    for j in range(m-2):
        if sum(matrix[i][j:j+3]) + sum(matrix[i+1][j:j+3]) + sum(matrix[i+2][j:j+3]) == max_sum:
            print(*matrix[i][j:j+3])
            print(*matrix[i+1][j:j+3])
            print(*matrix[i+2][j:j+3])
            exit()