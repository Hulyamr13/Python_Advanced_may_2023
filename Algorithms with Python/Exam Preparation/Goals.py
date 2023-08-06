def best_increasing_subsequence(goals):
    n = len(goals)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if goals[i] >= goals[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_length = max(dp)
    max_idx = dp.index(max_length)

    subsequence = []
    while max_idx != -1:
        subsequence.append(goals[max_idx])
        max_idx = prev[max_idx]

    return subsequence[::-1]


input_sequence = input().split(", ")
goals = [int(x) for x in input_sequence]

result = best_increasing_subsequence(goals)
print(" ".join(map(str, result)))
