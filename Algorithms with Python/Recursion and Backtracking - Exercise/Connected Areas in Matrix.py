class Area:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.size = 0

    def __lt__(self, other):
        if self.size == other.size:
            if self.row == other.row:
                return self.col < other.col
            return self.row < other.row
        return self.size > other.size

def find_connected_areas(matrix, rows, cols):
    visited = [[False] * cols for _ in range(rows)]
    areas = []
    area_count = 0

    for row in range(rows):
        for col in range(cols):
            if not visited[row][col] and matrix[row][col] == '-':
                area = Area(row, col)
                dfs(matrix, rows, cols, visited, row, col, area)
                areas.append(area)
                area_count += 1

    return area_count, areas

def dfs(matrix, rows, cols, visited, row, col, area):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return

    if visited[row][col] or matrix[row][col] != '-':
        return

    visited[row][col] = True
    area.size += 1


    dfs(matrix, rows, cols, visited, row - 1, col, area)
    dfs(matrix, rows, cols, visited, row + 1, col, area)
    dfs(matrix, rows, cols, visited, row, col - 1, area)
    dfs(matrix, rows, cols, visited, row, col + 1, area)


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    row = input().strip()
    matrix.append(list(row))


area_count, areas = find_connected_areas(matrix, rows, cols)


areas.sort()


print("Total areas found:", area_count)
for i, area in enumerate(areas):
    print(f"Area #{i+1} at ({area.row}, {area.col}), size: {area.size}")
