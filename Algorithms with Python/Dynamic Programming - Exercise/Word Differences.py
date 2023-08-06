def find_min_operations(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D table to store the lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The minimum number of deletions and insertions
    deletions = m - dp[m][n]
    insertions = n - dp[m][n]

    return deletions, insertions

# Read the input strings
str1 = input()
str2 = input()

# Find the minimum number of deletions and insertions
min_deletions, min_insertions = find_min_operations(str1, str2)

# Print the result
print("Deletions and Insertions:", min_deletions + min_insertions)
