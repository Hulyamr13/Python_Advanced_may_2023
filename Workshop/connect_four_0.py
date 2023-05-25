from collections import deque


def place_circle(row=0):
    if row == rows - 1 or board[row + 1][player_col] != '0':
        board[row][player_col] = player_symbol
        return
    place_circle(row + 1)


player_one_symbol = '1'
player_two_symbol = '2'

rows, cols = 6, 7

turn = deque([[1, player_one_symbol], [2, player_two_symbol]])
board = [['0'] * cols for _ in range(rows)]

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
)

while True:
    for row in board:
        print(f"[ {' '.join(row)} ]")

    player_number, player_symbol = turn[0]

    try:
        player_col = int(input(f"\nPlayer {player_number} please choose a column: ")) - 1
    except ValueError:
        print('Select a valid number')
        continue

    if not 0 <= player_col < cols:
        print(f"Select a valid number in the range ({1} - {cols})")
        continue

    row = 0
    if board[row][player_col] != '0':
        print('No empty spaces on that column')
        continue
    place_circle()

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == player_symbol:
                for direction in directions:
                    r, c = row, col
                    count = 0
                    while True:
                        r += direction[0]
                        c += direction[1]
                        if 0 <= r < rows and 0 <= c < cols and board[r][c] == player_symbol:
                            count += 1
                            if count == 3:
                                for row in board:
                                    print(f"[ {' '.join(row)} ]")
                                print(f"The winner is player: {player_number}")
                                raise SystemExit
                        else:
                            break

    turn.append(turn.popleft())
