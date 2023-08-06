from collections import deque


def shortest_path_maze(n, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    start = None
    end = None

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < n and 0 <= new_y < n and maze[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), steps + 1))
                visited.add((new_x, new_y))

    return -1



n = int(input())
maze = [input().strip() for _ in range(n)]


print(shortest_path_maze(n, maze))
