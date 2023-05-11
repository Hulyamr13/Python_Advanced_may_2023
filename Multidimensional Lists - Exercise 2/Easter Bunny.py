import sys

rows = int(input())

field = []
eggs = []
direction = ''
max_eggs_sum = -sys.maxsize

for row in range(rows):
    columns = input().split()
    field.append(columns)

find_bunny = False

for row in range(len(field)):
    for column in range(len(field[row])):
        if field[row][column] == "B":
            bunny = [row, column]
            eggs_sum = 0
            coordinates = []

            try:
                while bunny[0] >= 1 and field[bunny[0] - 1][bunny[1]] != "X":
                    bunny[0] -= 1
                    coordinates.append([bunny[0], bunny[1]])
                    eggs_sum += int(field[bunny[0]][bunny[1]])
            except IndexError:
                pass

            if eggs_sum >= max_eggs_sum:
                eggs = coordinates
                coordinates = []
                max_eggs_sum = eggs_sum
                direction = 'up'
            else:
                coordinates = []

            bunny = [row, column]
            eggs_sum = 0
            coordinates = []

            try:
                while bunny[1] >= 1 and field[bunny[0]][bunny[1] - 1] != "X":
                    bunny[1] -= 1
                    coordinates.append([bunny[0], bunny[1]])
                    eggs_sum += int(field[bunny[0]][bunny[1]])
            except IndexError:
                pass

            if eggs_sum >= max_eggs_sum:
                eggs = coordinates
                coordinates = []
                max_eggs_sum = eggs_sum
                direction = 'left'
            else:
                coordinates = []

            bunny = [row, column]
            eggs_sum = 0
            coordinates = []

            try:
                while bunny[1] < len(field[row]) and field[bunny[0]][bunny[1] + 1] != "X":
                    bunny[1] += 1
                    coordinates.append([bunny[0], bunny[1]])
                    eggs_sum += int(field[bunny[0]][bunny[1]])
            except IndexError:
                pass

            if eggs_sum >= max_eggs_sum:
                eggs = coordinates
                coordinates = []
                max_eggs_sum = eggs_sum
                direction = 'right'
            else:
                coordinates = []

            bunny = [row, column]
            eggs_sum = 0
            coordinates = []

            try:
                while bunny[0] < len(field) and field[bunny[0] + 1][bunny[1]] != "X":
                    bunny[0] += 1
                    coordinates.append([bunny[0], bunny[1]])
                    eggs_sum += int(field[bunny[0]][bunny[1]])
            except IndexError:
                pass

            if eggs_sum >= max_eggs_sum:
                eggs = coordinates
                coordinates = []
                max_eggs_sum = eggs_sum
                direction = 'down'
            else:
                coordinates = []

            find_bunny = True
            break
    if find_bunny:
        break

if direction != '':
    print(direction)
    [print(egg) for egg in eggs]
    print(max_eggs_sum)
