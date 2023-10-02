chess_board = []
king_position = []

for r in range(8):
    line = input().split(' ')
    chess_board.append(line)

    for c in range(8):
        if 'K' in line:
            king_position = [r, line.index('K')]

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
queens_capture = []

for move in moves:
    row, col = king_position
    next_row, next_col = move

    while True:
        if 0 <= (row + next_row) < 8 and 0 <= (col + next_col) < 8:
            row += next_row
            col += next_col

            if chess_board[row][col] == 'Q':
                queens_capture.append([row, col])
                break
        else:
            break

if queens_capture:
    [print(x) for x in reversed(queens_capture)]
else:
    print('The king is safe!')