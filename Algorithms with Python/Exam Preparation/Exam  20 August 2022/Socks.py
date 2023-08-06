def main():
    left_socks = list(map(int, input().split()))
    right_socks = list(map(int, input().split()))

    table = [[0 for _ in range(len(right_socks) + 1)] for _ in range(len(left_socks) + 1)]

    for r in range(1, len(table)):
        for c in range(1, len(table[0])):
            if left_socks[r - 1] == right_socks[c - 1]:
                table[r][c] = table[r - 1][c - 1] + 1
            else:
                table[r][c] = max(table[r][c - 1], table[r - 1][c])

    row = len(left_socks)
    col = len(right_socks)

    lcs_count = 0

    while row > 0 and col > 0:
        if left_socks[row - 1] == right_socks[col - 1]:
            lcs_count += 1
            row -= 1
            col -= 1
        elif table[row][col - 1] >= table[row - 1][col]:
            col -= 1
        else:
            row -= 1

    print(lcs_count)

if __name__ == "__main__":
    main()
