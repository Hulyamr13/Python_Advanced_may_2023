from pyfiglet import Figlet
import speech_recognition as sr


def get_name(player_number):
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(f"Player {player_number}, say your name")

            try:
                audio_data = r.record(source, duration=3)
                print("Recognizing...")
                return r.recognize_google(audio_data)
            except sr.UnknownValueError:
                print("Please say your name again")
            except sr.RequestError as e:
                print(f"Speech recognition request error: {str(e)}")


def validate_sign(sign):
    if sign not in ['X', 'O']:
        raise ValueError("Invalid sign! Please choose 'X' or 'O'.")


def validate_position(position):
    if not 1 <= position <= len(board) * len(board):
        raise ValueError("Invalid position! Please choose a number from 1 to 9.")


def validate_free_space(position):
    row, col = (position - 1) // 3, (position - 1) % 3
    if board[row][col] != ' ':
        raise ValueError("Selected position is not free!")


def check_for_win():
    player_name, player_symbol = players[0]
    size = len(board)

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - 1 - i] == player_symbol for i in range(size)])

    row_win = any([all(True if pos == player_symbol else False for pos in row) for row in board])
    col_win = any([all(True if board[r][c] == player_symbol else False for r in range(size)) for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")
        raise SystemExit


def place_symbol(position):
    row, col = (position - 1) // 3, (position - 1) % 3

    board[row][col] = players[0][1]

    check_for_win()

    print_board()
    choose_position()


def choose_position():
    while True:
        try:
            position = int(input(f"{players[0][0]}, choose a free position [1-9]: "))
            validate_position(position)
            validate_free_space(position)
            place_symbol(int(position))
            break
        except ValueError as e:
            print(str(e))
            continue


def print_board(begin=False):
    if begin:
        print("This is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first!")

        for row in range(len(board)):
            for col in range(len(board)):
                board[row][col] = ' '
    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    figlet = Figlet(font='big')
    print(figlet.renderText("Tic-Tac-Toe"))

    player_one_name = get_name("one")
    player_two_name = get_name("two")

    while True:
        player_one_symbol = input(f"{player_one_name}, would you like to play with 'X' or 'O'? ").upper()
        try:
            validate_sign(player_one_symbol)
        except ValueError as e:
            print(str(e))
            continue

        player_two_symbol = "O" if player_one_symbol == "X" else "X"

        players.append([player_one_name, player_one_symbol])
        players.append([player_two_name, player_two_symbol])

        print_board(begin=True)
        choose_position()


players = []
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

start()

