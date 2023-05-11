n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
while True:
    command = input().split()
    if command[0] == "Add":
        i, j, v = map(int, command[1:])
        if 0 <= i < n and 0 <= j < n:
            matrix[i][j] += v
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        i, j, v = map(int, command[1:])
        if 0 <= i < n and 0 <= j < n:
            matrix[i][j] -= v
        else:
            print("Invalid coordinates")
    else:
        break

for row in matrix:
    print(" ".join(str(x) for x in row))