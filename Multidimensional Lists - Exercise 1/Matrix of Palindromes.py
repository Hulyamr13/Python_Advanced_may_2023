r, c = map(int, input().split())

for i in range(r):
    row = ""
    for j in range(c):
        middle_letter = chr(ord('a') + i + j)
        row += chr(ord('a') + i) + middle_letter + chr(ord('a') + i)
        if j != c - 1:
            row += " "
    print(row)