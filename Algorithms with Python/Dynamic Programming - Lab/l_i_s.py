from collections import deque

def find_lis(sequence):
    n = len(sequence)

    # Array to store the length of LIS ending at each index
    lis_length = [1] * n

    # Array to store the index of the previous element in the LIS
    previous_index = [-1] * n

    # Variables to keep track of the length and ending index of the longest subsequence
    max_length = 1
    max_index = 0

    # Calculate LIS at each index
    for i in range(1, n):
        for j in range(i):
            if sequence[j] < sequence[i] and lis_length[j] + 1 > lis_length[i]:
                lis_length[i] = lis_length[j] + 1
                previous_index[i] = j

        # Update the length and ending index of the longest subsequence found so far
        if lis_length[i] > max_length:
            max_length = lis_length[i]
            max_index = i

    # Recover the LIS
    lis = deque()
    while max_index != -1:
        lis.appendleft(sequence[max_index])
        max_index = previous_index[max_index]

    return lis

sequence = list(map(int, input().split()))

lis = find_lis(sequence)
print(" ".join(map(str, lis)))
