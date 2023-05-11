def get_input():
    field_size = int(input())
    commands = input().split()
    field = []
    for _ in range(field_size):
        row = input().split()
        field.append(row)
    return field_size, commands, field


def move_miner(command, miner_pos, field_size):
    row, col = miner_pos
    if command == 'left' and col > 0:
        col -= 1
    elif command == 'right' and col < field_size - 1:
        col += 1
    elif command == 'up' and row > 0:
        row -= 1
    elif command == 'down' and row < field_size - 1:
        row += 1
    return row, col


def play_game(field_size, commands, field):
    miner_pos = None
    coal_count = 0
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] == 's':
                miner_pos = (i, j)
            elif field[i][j] == 'c':
                coal_count += 1

    for command in commands:
        miner_pos = move_miner(command, miner_pos, field_size)
        row, col = miner_pos
        if field[row][col] == 'c':
            coal_count -= 1
            field[row][col] = '*'
            if coal_count == 0:
                print(f"You collected all coal! ({row}, {col})")
                return
        elif field[row][col] == 'e':
            print(f"Game over! ({row}, {col})")
            return

    print(f"{coal_count} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")


field_size, commands, field = get_input()
play_game(field_size, commands, field)