class Game:
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix
        self.my_coordinates = self.find_my_coordinates()
        self.matrix[self.my_coordinates[0]][self.my_coordinates[1]] = "-"
        self.result = False
        self.touched_opponents = 0
        self.moves_made = 0

    def find_my_coordinates(self):
        for row in range(self.n):
            for col in range(self.m):
                if self.matrix[row][col] == "B":
                    return [row, col]

    def check_my_next_position(self, my_row, my_col):
        if 0 <= my_row < len(self.matrix) and 0 <= my_col < len(self.matrix[0]):
            next_position = self.matrix[my_row][my_col]
            if next_position == "O":
                return False
            elif next_position == "-":
                return [my_row, my_col], 0
            elif next_position == "P":
                self.matrix[my_row][my_col] = "-"
                return [my_row, my_col], 1

    def play(self):
        while True:
            if self.touched_opponents == 3:
                break

            command = input()
            if command == 'Finish':
                break

            if command == 'up':
                self.result = self.check_my_next_position(self.my_coordinates[0] - 1, self.my_coordinates[1])
            elif command == 'down':
                self.result = self.check_my_next_position(self.my_coordinates[0] + 1, self.my_coordinates[1])
            elif command == 'left':
                self.result = self.check_my_next_position(self.my_coordinates[0], self.my_coordinates[1] - 1)
            elif command == 'right':
                self.result = self.check_my_next_position(self.my_coordinates[0], self.my_coordinates[1] + 1)

            if self.result:
                self.my_coordinates, touches = self.result
                self.touched_opponents += touches
                self.moves_made += 1
                self.matrix[self.my_coordinates[0]][self.my_coordinates[1]] = "-"

        print("Game over!")
        print(f"Touched opponents: {self.touched_opponents} Moves made: {self.moves_made}")


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input().split())

game = Game(n, m, matrix)
game.play()
