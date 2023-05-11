n, m = map(int, input().split())

matrix = [list(input().split()) for _ in range(n)]

while True:
    command = input().split()

    if command[0] == "swap" and len(command) == 5:
        r1, c1, r2, c2 = map(int, command[1:])
        if 0 <= r1 < n and 0 <= r2 < n and 0 <= c1 < m and 0 <= c2 < m:
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for row in matrix:
                print(" ".join(row))
        else:
            print("Invalid input!")
    elif command[0] == "END":
        break
    else:
        print("Invalid input!")
