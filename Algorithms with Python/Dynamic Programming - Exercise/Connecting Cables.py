def find_max_pairs(cables):
    n = len(cables)

    # Create a list to store the LIS lengths
    lis = [1] * n

    # Compute the LIS lengths
    for i in range(1, n):
        for j in range(i):
            if cables[i] > cables[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Find the maximum LIS length
    max_pairs = max(lis)

    return max_pairs

# Read the input cables as a list of integers
cables = list(map(int, input().split()))

# Find the maximum number of pairs we can connect
max_pairs = find_max_pairs(cables)

# Print the result
print("Maximum pairs connected:", max_pairs)
