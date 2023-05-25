class InvalidColumnError(Exception):
    pass


def print_matrix(m):
    [print(el) for el in m]


def validate_col(col, max_cols):
    if not (0 <= col <= max_cols):
        raise InvalidColumnError
    return False


# Creating the matrix
rows = 6
cols = 7
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Print current state
print_matrix(matrix)

player_num = 1
while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        # Read column choice from input and verify if the number is correct
        column_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_col(column_num, cols - 1)
    except InvalidColumnError:
        print(f"This column is not valid. Please select a "
              f"number between {1} and {cols}")
        continue
    except ValueError:
        print(f"Please select a valid digit!")
        continue
    player_num += 1
    print_matrix(matrix)
