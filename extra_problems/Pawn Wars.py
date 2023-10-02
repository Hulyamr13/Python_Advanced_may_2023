def main():
    matrix = []
    w_row, w_col, b_row, b_col = -1, -1, -1, -1

    for row in range(8):
        arr = list(input().strip())
        matrix.append(arr)

        for col in range(len(arr)):
            if arr[col] == 'w':
                w_row, w_col = row, col
            elif arr[col] == 'b':
                b_row, b_col = row, col

    is_hit = False

    while w_row != 0 and b_row != 7 and not is_hit:
        if white_pawn_hit_black(w_row, w_col, b_row, b_col):
            coordinates = find_coordinates(b_row, b_col)
            print(f"Game over! White capture on {coordinates}.")
            is_hit = True

        w_row -= 1

        if black_pawn_hit_white(b_row, b_col, w_row, w_col):
            coordinates = find_coordinates(w_row, w_col)
            print(f"Game over! Black capture on {coordinates}.")
            is_hit = True

        b_row += 1

    if not is_hit:
        if w_row == 0:
            print(f"Game over! White pawn is promoted to a queen at {find_coordinates(w_row, w_col)}.")
        else:
            print(f"Game over! Black pawn is promoted to a queen at {find_coordinates(b_row, b_col)}.")


def find_coordinates(row, col):
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = ['8', '7', '6', '5', '4', '3', '2', '1']
    return cols[col] + rows[row]


def black_pawn_hit_white(b_row, b_col, w_row, w_col):
    return b_row + 1 == w_row and (b_col + 1 == w_col or b_col - 1 == w_col)


def white_pawn_hit_black(w_row, w_col, b_row, b_col):
    return w_row - 1 == b_row and (w_col + 1 == b_col or w_col - 1 == b_col)


if __name__ == '__main__':
    main()
