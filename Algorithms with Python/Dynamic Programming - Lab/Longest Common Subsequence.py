str1 = input()
str2 = input()

table = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for r in range(1, len(table)):
    for c in range(1, len(table[0])):
        if str1[r - 1] == str2[c - 1]:
            table[r][c] = table[r - 1][c - 1] + 1
        else:
            table[r][c] = max(table[r - 1][c], table[r][c - 1])

print(table[len(str1)][len(str2)])
