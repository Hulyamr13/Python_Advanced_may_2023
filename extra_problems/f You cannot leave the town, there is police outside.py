caught = False
dRow = -1
dCol = -1
stolen = 0
matrix = []

def changePosition(direction):
    coordinates = [0, 0]
    if direction == "up":
        coordinates[0] = dRow - 1
        coordinates[1] = dCol
    elif direction == "down":
        coordinates[0] = dRow + 1
        coordinates[1] = dCol
    elif direction == "left":
        coordinates[0] = dRow
        coordinates[1] = dCol - 1
    elif direction == "right":
        coordinates[0] = dRow
        coordinates[1] = dCol + 1
    return coordinates

def isValid(nextRow, nextCol):
    return nextRow < len(matrix) and nextRow >= 0 and nextCol < len(matrix[nextRow]) and nextCol >= 0

n = int(input())
cmd = input().split(",")

for _ in range(n):
    input_str = input().replace(" ", "")
    row = list(input_str)
    if "D" in row:
        dRow = _
        dCol = row.index("D")
    matrix.append(row)

i = 0
while i < len(cmd) and not caught:
    direction = cmd[i]
    newCoordinates = changePosition(direction)
    nextRow = newCoordinates[0]
    nextCol = newCoordinates[1]
    if not isValid(nextRow, nextCol):
        print("You cannot leave the town, there is police outside!")
        i += 1
        continue
    matrix[dRow][dCol] = '+'
    if matrix[nextRow][nextCol] == '$':
        money = nextRow * nextCol
        stolen += money
        print(f"You successfully stole {money}$.")
    elif matrix[nextRow][nextCol] == 'P':
        caught = True
        matrix[nextRow][nextCol] = '#'
        break
    dRow = nextRow
    dCol = nextCol
    matrix[dRow][dCol] = 'D'
    i += 1

if not caught:
    print(f"Your last theft has finished successfully with {stolen}$ in your pocket.")
else:
    print(f"You got caught with {stolen}$, and you are going to jail.")

for row in matrix:
    print(' '.join(row))
