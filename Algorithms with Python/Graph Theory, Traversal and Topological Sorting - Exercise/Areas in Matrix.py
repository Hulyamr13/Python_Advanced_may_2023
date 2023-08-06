def dfs(grid, visited, row, col, letter):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 0

    if visited[row][col] or grid[row][col] != letter:
        return 0

    visited[row][col] = True

    count = 1

    count += dfs(grid, visited, row - 1, col, letter)  # Up
    count += dfs(grid, visited, row + 1, col, letter)  # Down
    count += dfs(grid, visited, row, col - 1, letter)  # Left
    count += dfs(grid, visited, row, col + 1, letter)  # Right

    return count


def find_connected_areas(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    areas = {}
    total_areas = 0

    for row in range(rows):
        for col in range(cols):
            if not visited[row][col]:
                letter = grid[row][col]
                count = dfs(grid, visited, row, col, letter)
                if letter not in areas:
                    areas[letter] = 0
                areas[letter] += 1
                total_areas += 1

    return total_areas, areas



n = int(input())
m = int(input())
grid = []
for _ in range(n):
    row = input().strip()
    grid.append(row)

total_areas, areas = find_connected_areas(grid)

print("Areas:", total_areas)
for letter, count in sorted(areas.items()):
    print("Letter '{}' -> {}".format(letter, count))
