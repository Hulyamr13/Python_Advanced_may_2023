def find_minimum_sum(sequence):
    n = len(sequence)
    dp = [0] * n

    if n < 5:
        return min(sequence)

    dp[0:4] = sequence[0:4]

    for i in range(4, n):
        dp[i] = sequence[i] + min(dp[i - 4:i])

    return min(dp[n - 4:n])


sequence = list(map(int, input().split()))

min_sum = find_minimum_sum(sequence)

print(min_sum)
