def main():
    dimensions = list(map(int, input().split()))
    rows = dimensions[0]
    columns = dimensions[1]

    field = read_field(rows)
    directions = read_directions()
    players_positions = find_players_position(field)
    player_x_position = players_positions[0]
    player_y_position = players_positions[1]

    moves = []

    for direction in directions:
        if direction == "up":
            if player_x_position - 1 >= 0 and field[player_x_position - 1][player_y_position] != "T":
                player_x_position -= 1
                moves.append(direction)
        elif direction == "down":
            if player_x_position + 1 < rows and field[player_x_position + 1][player_y_position] != "T":
                player_x_position += 1
                moves.append(direction)
        elif direction == "left":
            if player_y_position - 1 >= 0 and field[player_x_position][player_y_position - 1] != "T":
                player_y_position -= 1
                moves.append(direction)
        elif direction == "right":
            if player_y_position + 1 < columns and field[player_x_position][player_y_position + 1] != "T":
                player_y_position += 1
                moves.append(direction)

        if check_position(field, player_x_position, player_y_position, moves):
            return

    print("The map is fake!")


def check_position(field, player_x_position, player_y_position, moves):
    if field[player_x_position][player_y_position] == "X":
        print(f"I've found the treasure!\nThe right path is {', '.join(moves)}")
        return True
    return False


def find_players_position(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == "Y":
                return [i, j]
    return [0]


def read_directions():
    directions = []
    while True:
        command = input()
        if command == "Finish":
            break
        directions.append(command)
    return directions


def read_field(rows):
    field = []
    for i in range(rows):
        row = input().replace(" ", "")
        field.append(list(row))
    return field


if __name__ == "__main__":
    main()
