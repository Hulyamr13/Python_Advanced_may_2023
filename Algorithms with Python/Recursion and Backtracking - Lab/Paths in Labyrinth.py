def read_lab():
    rows = int(input())
    cols = int(input())
    labyrinth = []

    for _ in range(rows):
        row_elements = input()
        labyrinth.append(list(row_elements))

    return labyrinth


def find_paths(row, col, direction, labyrinth, path):
    rows = len(labyrinth)
    cols = len(labyrinth[0])

    def is_in_bounds(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def is_exit(row, col):
        return labyrinth[row][col] == 'e'

    def is_visited(row, col):
        return labyrinth[row][col] == 'v'

    def is_free(row, col):
        return labyrinth[row][col] == '-'

    def mark(row, col):
        labyrinth[row][col] = 'v'

    def unmark(row, col):
        labyrinth[row][col] = '-'

    def print_path():
        print(''.join(path))

    if not is_in_bounds(row, col):
        return

    if direction != 'S':
        path.append(direction)

    if is_exit(row, col):
        print_path()
    elif not is_visited(row, col) and is_free(row, col):
        mark(row, col)
        find_paths(row, col + 1, 'R', labyrinth, path)
        find_paths(row + 1, col, 'D', labyrinth, path)
        find_paths(row, col - 1, 'L', labyrinth, path)
        find_paths(row - 1, col, 'U', labyrinth, path)
        unmark(row, col)

    if path:
        path.pop()


labyrinth = read_lab()
find_paths(0, 0, 'S', labyrinth, [])
