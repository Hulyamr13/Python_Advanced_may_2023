ROWS = 6
COLS = 7
EMPTY_SLOT = ' '
PLAYER1_PIECE = 'X'
PLAYER2_PIECE = 'O'

board = [[EMPTY_SLOT] * COLS for _ in range(ROWS)]


def display_board():
    for row in board:
        print('|', end='')
        for slot in row:
            print(slot, end='|')
        print()
    print('-' * (COLS * 2 + 1))


def take_turn(player):
    while True:
        try:
            col = int(input(f"Player {player}, choose a column (0-{COLS-1}): "))
            if col < 0 or col >= COLS:
                raise ValueError
            if board[0][col] != EMPTY_SLOT:
                raise ValueError
            break
        except ValueError:
            print("Invalid column choice. Try again.")

    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY_SLOT:
            board[row][col] = PLAYER1_PIECE if player == 1 else PLAYER2_PIECE
            break


def check_win(player):
    piece = PLAYER1_PIECE if player == 1 else PLAYER2_PIECE


    for row in range(ROWS):
        for col in range(COLS - 3):
            if (
                board[row][col] == piece and
                board[row][col + 1] == piece and
                board[row][col + 2] == piece and
                board[row][col + 3] == piece
            ):
                return True


    for row in range(ROWS - 3):
        for col in range(COLS):
            if (
                board[row][col] == piece and
                board[row + 1][col] == piece and
                board[row + 2][col] == piece and
                board[row + 3][col] == piece
            ):
                return True


    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (
                board[row][col] == piece and
                board[row + 1][col + 1] == piece and
                board[row + 2][col + 2] == piece and
                board[row + 3][col + 3] == piece
            ):
                return True


    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if (
                board[row][col] == piece and
                board[row - 1][col + 1] == piece and
                board[row - 2][col + 2] == piece and
                board[row - 3][col + 3] == piece
            ):
                return True

    return False


def check_draw():
    for row in board:
        if EMPTY_SLOT in row:
            return False
    return True


def play_game():
    current_player = 1

    while True:
        display_board()
        take_turn(current_player)

        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break

        if check_draw():
            display_board()
            print("The game ends in a draw!")
            break

        current_player = 2 if current_player == 1 else 1


play_game()


