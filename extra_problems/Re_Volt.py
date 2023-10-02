def inTheMatrix(row, col, rowMatrix):
    return row >= 0 and row < rowMatrix and col >= 0 and col < rowMatrix

def changePosition(cmd, playerPos, n):
    if cmd == "up":
        if inTheMatrix(playerPos[0] - 1, playerPos[1], n):
            playerPos[0] -= 1
        else:
            playerPos[0] = n - 1
    elif cmd == "down":
        if inTheMatrix(playerPos[0] + 1, playerPos[1], n):
            playerPos[0] += 1
        else:
            playerPos[0] = 0
    elif cmd == "left":
        if inTheMatrix(playerPos[0], playerPos[1] - 1, n):
            playerPos[1] -= 1
        else:
            playerPos[1] = n - 1
    elif cmd == "right":
        if inTheMatrix(playerPos[0], playerPos[1] + 1, n):
            playerPos[1] += 1
        else:
            playerPos[1] = 0

n = int(input())
cmdCount = int(input())

matrix = []
playerPos = [0, 0]

for row in range(n):
    input_str = input().strip()
    matrix.append(list(input_str))
    for col in range(len(input_str)):
        if input_str[col] == 'f':
            playerPos[0] = row
            playerPos[1] = col

playerOldPos = [0, 0]
over = False

while cmdCount > 0:
    cmd = input().strip()

    playerOldPos[0] = playerPos[0]
    playerOldPos[1] = playerPos[1]

    matrix[playerPos[0]][playerPos[1]] = '-'
    changePosition(cmd, playerPos, n)

    if matrix[playerPos[0]][playerPos[1]] == 'B':
        changePosition(cmd, playerPos, n)

    if matrix[playerPos[0]][playerPos[1]] == 'T':
        playerPos[0] = playerOldPos[0]
        playerPos[1] = playerOldPos[1]

    if matrix[playerPos[0]][playerPos[1]] == 'F':
        matrix[playerPos[0]][playerPos[1]] = 'f'
        over = True
        break

    matrix[playerPos[0]][playerPos[1]] = 'f'
    cmdCount -= 1

if over:
    print("Player won!")
else:
    print("Player lost!")

for row in matrix:
    print(''.join(row))
