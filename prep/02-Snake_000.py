n = int(input())

snake = []
field = []
eaten_food = 0
another_burrow = []

directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

for row in range(n):
    line = [x for x in input()]
    for col in range(n):
        if line[col] == 'S':
            snake = [row, col]

    field.append(line)

while True:
    line = input()

    direction = directions[line]

    new_position = [snake[0] + direction[0], snake[1] + direction[1]]

    field[snake[0]][snake[1]] = '.'

    if new_position[0] >= len(field) or new_position[0] < 0 or new_position[1] >= len(field) or new_position[1] < 0:
        print("Game over!")
        break

    if field[new_position[0]][new_position[1]] == '*':
        eaten_food += 1
        snake = new_position
        field[snake[0]][snake[1]] = 'S'

    elif field[new_position[0]][new_position[1]] == 'B':
        field[new_position[0]][new_position[1]] = '.'

        for (y, row) in enumerate(field):
            for (x, col) in enumerate(row):
                if col == 'B':
                    another_burrow = [y, x]

        snake_out_position = another_burrow
        snake = snake_out_position
        field[snake[0]][snake[1]] = 'S'

    else:
        snake = new_position
        field[snake[0]][snake[1]] = 'S'


    if eaten_food == 10:
        print(f"You won! You fed the snake.")
        break


print(f"Food eaten: {eaten_food}")
[print("".join(row)) for row in field]