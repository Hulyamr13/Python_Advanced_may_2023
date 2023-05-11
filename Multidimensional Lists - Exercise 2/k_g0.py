board_size = int(input())
removed_knights = 0
matrix = [list(input()) for row in range(board_size)]
knight = "K"

kn_move = ((-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1,2), (1,-2), (1,2))

knights = {}

while True:
    knights = {}
    number_of_good_knights = 0
    for row in range(board_size):
        for col in range(board_size):
            if matrix[row][col] == knight:
                for m_row, m_col in kn_move:
                    knight_row, knight_col = row + m_row, col + m_col
                    if 0 <= knight_row < board_size and 0 <= knight_col < board_size:
                        if matrix[knight_row][knight_col] == knight:
                            number_of_good_knights += 1
                            if f"{row} {col}" not in knights.keys():
                                knights[f"{row} {col}"] = 1
                            else:
                                knights[f"{row} {col}"] += 1
    if number_of_good_knights == 0:
        break
    best_knight = [-1, -1]
    best_knight_attacks = 0
    for m_knight, attacks in knights.items():
        if attacks > best_knight_attacks:
            best_knight[0], best_knight[1] = map(int, m_knight.split())
            best_knight_attacks = attacks
    if best_knight[0] >= 0 and best_knight[1] >= 0:
        matrix[best_knight[0]][best_knight[1]] = '0'
        removed_knights += 1

print(removed_knights)
