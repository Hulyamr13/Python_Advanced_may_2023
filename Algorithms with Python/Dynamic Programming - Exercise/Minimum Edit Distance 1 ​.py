def calculate_edit_distance(s1, s2, replace_cost, insert_cost, delete_cost):
    m = len(s1)
    n = len(s2)

    # Create a 2D table to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i * delete_cost
    for j in range(n + 1):
        dp[0][j] = j * insert_cost

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                replace = dp[i - 1][j - 1] + replace_cost
                insert = dp[i][j - 1] + insert_cost
                delete = dp[i - 1][j] + delete_cost
                dp[i][j] = min(replace, insert, delete)

    return dp[m][n]

# Read the input costs and strings
replace_cost = int(input())
insert_cost = int(input())
delete_cost = int(input())
s1 = input()
s2 = input()

# Calculate the minimum edit distance
min_edit_distance = calculate_edit_distance(s1, s2, replace_cost, insert_cost, delete_cost)

# Print the result
print("Minimum edit distance:", min_edit_distance)
