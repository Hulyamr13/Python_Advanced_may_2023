n = int(input())
m = int(input())
bombs = [tuple(map(int, input()[1:-1].split(', '))) for _ in range(m)]

field = [[0] * n for _ in range(n)]
for r, c in bombs:
    field[r][c] = '*'
    for i in range(max(0, r-1), min(n, r+2)):
        for j in range(max(0, c-1), min(n, c+2)):
            if field[i][j] != '*':
                field[i][j] += 1

for row in field:
    print(' '.join(map(str, row)))
