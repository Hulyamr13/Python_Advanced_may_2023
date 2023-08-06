def main():
    songs = list(map(int, input().split(',')))
    start = int(input())
    max_val = int(input())
    current_max = start

    matrix = initialize_matrix(len(songs) + 1, max_val + 1)

    matrix[0][start] = start

    for row in range(len(songs)):
        current_value = songs[row]
        for col in range(max_val + 1):
            if matrix[row][col] != -1:
                new_increment = matrix[row][col] + current_value
                new_decrement = matrix[row][col] - current_value

                if new_increment <= max_val:
                    matrix[row + 1][new_increment] = new_increment

                if new_decrement >= 0:
                    matrix[row + 1][new_decrement] = new_decrement

    result = get_max(matrix)
    print(result)

def get_max(matrix):
    last_row = len(matrix) - 1
    for col in range(len(matrix[0]) - 1, -1, -1):
        if matrix[last_row][col] != -1:
            return matrix[last_row][col]

    return -1

def initialize_matrix(rows, cols):
    return [[-1 for _ in range(cols)] for _ in range(rows)]

if __name__ == "__main__":
    main()
