class Area:
    def __init__(self):
        self.Size = 0
        self.Row = 0
        self.Col = 0

def main():
    rows = int(input())
    cols = int(input())

    matrix = read_matrix(rows, cols)
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    total_areas = []

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'd':
                continue

            if visited[r][c]:
                continue

            area_size = get_area_size(matrix, r, c, visited)
            area = Area()
            area.Size = area_size
            area.Row = r
            area.Col = c
            total_areas.append(area)

    print_result(sorted(total_areas, key=lambda x: (-x.Size, x.Row, x.Col)))

def print_result(total_areas):
    print(len(total_areas))
    # print(f"Total areas found: {len(total_areas)}")
    # for i, area in enumerate(total_areas, 1):
    #     print(f"Area #{i} at ({area.Row}, {area.Col}), size: {area.Size}")

def get_area_size(matrix, row, col, visited):
    if is_outside(matrix, row, col):
        return 0

    if matrix[row][col] == 'd':
        return 0

    if visited[row][col]:
        return 0

    visited[row][col] = True

    area_size = get_area_size(matrix, row - 1, col, visited) + \
                get_area_size(matrix, row + 1, col, visited) + \
                get_area_size(matrix, row, col - 1, visited) + \
                get_area_size(matrix, row, col + 1, visited) + \
                get_area_size(matrix, row - 1, col + 1, visited) + \
                get_area_size(matrix, row - 1, col - 1, visited) + \
                get_area_size(matrix, row + 1, col + 1, visited) + \
                get_area_size(matrix, row + 1, col - 1, visited)

    return area_size + 1

def is_outside(matrix, row, col):
    return row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0])

def read_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        col_elements = input()
        matrix.append(col_elements)
    return matrix

if __name__ == "__main__":
    main()
