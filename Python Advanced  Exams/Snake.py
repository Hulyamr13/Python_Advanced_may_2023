n = int(input())
road = [input() for _ in range(n)]
navigation = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

snake = [(i, row.index('S')) for i, row in enumerate(road) if 'S' in row][0]
food = 0

while True:
    row, col = snake
    road[row] = road[row][:col] + '.' + road[row][col+1:]
    command_pos = navigation[input()]
    snake = [row+command_pos[0], col+command_pos[1]]

    if not (0 <= snake[0] < n and 0 <= snake[1] < n):
        print("Game over!")
        break

    if road[snake[0]][snake[1]] == "B":
        road[snake[0]] = road[snake[0]][:snake[1]] + '.' + road[snake[0]][snake[1]+1:]
        snake = [(i, row.index('B')) for i, row in enumerate(road) if 'B' in row and (i, row.index('B')) != tuple(snake)][0]
    elif road[snake[0]][snake[1]] == "*":
        food += 1
    road[snake[0]] = road[snake[0]][:snake[1]] + 'S' + road[snake[0]][snake[1]+1:]

    if food == 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food}")
print('\n'.join(road))