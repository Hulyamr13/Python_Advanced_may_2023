def make_a_move(row_, col_, matrix):
    found_hazelnuts = 0
    if not (0 <= row_ < len(matrix) and 0 <= col_ < len(matrix)):
        print("The squirrel is out of the field.")
        return
    if matrix[row_][col_] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        return
    if matrix[row_][col_] == 'h':
        found_hazelnuts += 1
    matrix[row_][col_] = '*'
    return found_hazelnuts, matrix

rows = int(input())
commands = input().split(", ")
field = [list(input()) for _ in range(rows)]
hazelnuts = 0

squirrel_position = [(row, col) for row in range(rows) for col in range(rows) if field[row][col] == 's'][0]
field[squirrel_position[0]][squirrel_position[1]] = "*"

for command in commands:
    if command == 'left':
        squirrel_position = (squirrel_position[0], squirrel_position[1]-1)
    elif command == 'right':
        squirrel_position = (squirrel_position[0], squirrel_position[1]+1)
    elif command == 'down':
        squirrel_position = (squirrel_position[0]+1, squirrel_position[1])
    elif command == 'up':
        squirrel_position = (squirrel_position[0]-1, squirrel_position[1])
    result = make_a_move(*squirrel_position, field)
    if not result:
        print("Game over!")
        break
    count_hazelnuts, field = result
    hazelnuts += count_hazelnuts
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if hazelnuts < 3:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")
