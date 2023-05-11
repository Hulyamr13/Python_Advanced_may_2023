n = int(input())
matrix = [input() for _ in range(n)]
symbol = input()

for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            break
    else:
        continue
    break
else:
    print(f"{symbol} does not occur in the matrix")