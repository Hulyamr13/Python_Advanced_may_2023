from collections import deque

names = set([input() for name in range(int(input()))])
sorted_names = sorted(names)
dq_names = deque(sorted_names)
print('\n'.join(dq_names))
