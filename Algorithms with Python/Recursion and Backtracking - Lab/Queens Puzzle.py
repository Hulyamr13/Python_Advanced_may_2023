class Program:
    attacked_rows = set()
    attacked_cols = set()
    attacked_left_diagonals = set()
    attacked_right_diagonals = set()

    @staticmethod
    def main():
        board = [[False] * 8 for _ in range(8)]
        Program.put_queens(board, 0)

    @staticmethod
    def put_queens(board, row):
        if row == len(board):
            Program.print_board(board)
            return

        for col in range(len(board[0])):
            if not Program.is_attacable(row, col):
                board[row][col] = True
                Program.attacked_rows.add(row)
                Program.attacked_cols.add(col)
                Program.attacked_left_diagonals.add(row - col)
                Program.attacked_right_diagonals.add(row + col)

                Program.put_queens(board, row + 1)

                board[row][col] = False
                Program.attacked_rows.remove(row)
                Program.attacked_cols.remove(col)
                Program.attacked_left_diagonals.remove(row - col)
                Program.attacked_right_diagonals.remove(row + col)

    @staticmethod
    def is_attacable(row, col):
        return row in Program.attacked_rows \
            or col in Program.attacked_cols \
            or (row - col) in Program.attacked_left_diagonals \
            or (row + col) in Program.attacked_right_diagonals

    @staticmethod
    def print_board(board):
        for row in board:
            for cell in row:
                if cell:
                    print("* ", end="")
                else:
                    print("- ", end="")
            print()
        print()

Program.main()
