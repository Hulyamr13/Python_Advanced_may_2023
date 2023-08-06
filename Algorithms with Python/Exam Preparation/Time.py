def find_correct_timeline(timeline1, timeline2):
    n = len(timeline1)
    m = len(timeline2)

    table = [[0] * (m + 1) for _ in range(n + 1)]

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if timeline1[r - 1] == timeline2[c - 1]:
                table[r][c] = table[r - 1][c - 1] + 1
            else:
                table[r][c] = max(table[r][c - 1], table[r - 1][c])

    row = n
    col = m
    lcs = []

    while row > 0 and col > 0:
        if timeline1[row - 1] == timeline2[col - 1]:
            lcs.append(timeline1[row - 1])
            row -= 1
            col -= 1
        elif table[row][col - 1] >= table[row - 1][col]:
            col -= 1
        else:
            row -= 1

    lcs.reverse()
    return lcs, len(lcs)


timeline1 = list(map(int, input().split()))
timeline2 = list(map(int, input().split()))

correct_timeline, length = find_correct_timeline(timeline1, timeline2)

print(" ".join(map(str, correct_timeline)))
print(length)