s = 8
board = []
king_pos = []
queens_pos = []
for row in range(s):
    line = input().split()
    if 'K' in line:
        king_pos = [row, line.index('K')]
    board.append(line)

# Diagonal
for row_delta, col_delta in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
    for i in range(s):
        row = king_pos[0] + row_delta*i
        col = king_pos[1] + col_delta*i
        if not 0 <= col < s or not 0 <= row < s:
            break
        if board[row][col] == 'Q':
            queens_pos.append([row, col])
            break

# Horizontal and vertical
for row_delta, col_delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    for i in range(s):
        row = king_pos[0] + row_delta*i
        col = king_pos[1] + col_delta*i
        if not 0 <= col < s or not 0 <= row < s:
            break
        if board[row][col] == 'Q':
            queens_pos.append([row, col])
            break

if queens_pos:
    print(*queens_pos, sep='\n')
else:
    print('The king is safe!')
