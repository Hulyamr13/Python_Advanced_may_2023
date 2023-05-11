def is_valid_coord(coord, rows, cols):
    row, col = coord
    return 0 <= row < rows and 0 <= col < cols

rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    if not command.startswith("swap"):
        print("Invalid input!")
        continue

    tokens = command.split()
    if len(tokens) != 5:
        print("Invalid input!")
        continue

    try:
        row1, col1, row2, col2 = map(int, tokens[1:])
        if not all(is_valid_coord(coord, rows, cols) for coord in [(row1, col1), (row2, col2)]):
            print("Invalid input!")
            continue
    except ValueError:
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
