rows = int(input())
commands = input().split(", ")
field = []
hazelnuts = 0
die = False

for _ in range(rows):
    field.append(list(input()))

squirrel_position = []
for row in range(rows):
    for col in range(rows):
        if field[row][col] == 's':
            squirrel_position = [row, col]

field[squirrel_position[0]][squirrel_position[1]] = "*"

found_hazelnuts = 0
if not (0 <= squirrel_position[0] < len(field) and 0 <= squirrel_position[1] < len(field)):
    print("The squirrel is out of the field.")
    die = True
elif field[squirrel_position[0]][squirrel_position[1]] == 't':
    print("Unfortunately, the squirrel stepped on a trap...")
    die = True
elif field[squirrel_position[0]][squirrel_position[1]] == 'h':
    found_hazelnuts += 1
field[squirrel_position[0]][squirrel_position[1]] = '*'
hazelnuts += found_hazelnuts

for command in commands:
    if command == 'left':
        squirrel_position[1] -= 1
    elif command == 'right':
        squirrel_position[1] += 1
    elif command == 'down':
        squirrel_position[0] += 1
    elif command == 'up':
        squirrel_position[0] -= 1

    found_hazelnuts = 0
    if not (0 <= squirrel_position[0] < len(field) and 0 <= squirrel_position[1] < len(field)):
        print("The squirrel is out of the field.")
        die = True
        break
    elif field[squirrel_position[0]][squirrel_position[1]] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        die = True
        break
    elif field[squirrel_position[0]][squirrel_position[1]] == 'h':
        found_hazelnuts += 1
    field[squirrel_position[0]][squirrel_position[1]] = '*'
    hazelnuts += found_hazelnuts
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if not die and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
