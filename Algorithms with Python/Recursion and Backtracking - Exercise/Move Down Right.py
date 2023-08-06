def unique_paths(m, n):
    grid = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        grid[i][1] = 1
    for j in range(1, n+1):
        grid[1][j] = 1

    for i in range(2, m+1):
        for j in range(2, n+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[m][n]


m = int(input())
n = int(input())

paths = unique_paths(m, n)
print(paths)
