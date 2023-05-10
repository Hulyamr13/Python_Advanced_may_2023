from collections import deque

kids = input().split()
n = int(input())

queue = deque(kids)

while len(queue) > 1:
    for i in range(n-1):
        queue.append(queue.popleft())
    print(f"Removed {queue.popleft()}")

print(f"Last is {queue[0]}")