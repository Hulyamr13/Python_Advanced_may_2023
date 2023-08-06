words = input().split()

n = len(words)
lengths = [1] * n
prevs = [-1] * n

best_len = 0
last_index = 0

for current in range(n):
    curr_word = words[current]

    for prev in range(current - 1, -1, -1):
        prev_word = words[prev]

        if len(prev_word) < len(curr_word) and lengths[prev] + 1 >= lengths[current]:
            lengths[current] = lengths[prev] + 1
            prevs[current] = prev

    if lengths[current] > best_len:
        best_len = lengths[current]
        last_index = current

stack = []

while last_index != -1:
    stack.append(words[last_index])
    last_index = prevs[last_index]

print(' '.join(reversed(stack)))
