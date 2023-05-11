n, m = map(int, input().split())
snake = input()

matrix = [[0] * m for _ in range(n)]

snake_idx = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = snake[snake_idx]
            snake_idx = (snake_idx + 1) % len(snake)
    else:
        for j in range(m-1, -1, -1):
            matrix[i][j] = snake[snake_idx]
            snake_idx = (snake_idx + 1) % len(snake)

for row in matrix:
    print("".join(row))