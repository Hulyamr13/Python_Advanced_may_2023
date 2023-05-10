from collections import deque

names = input().split()
n = int(input())

queue = deque(names)

while len(queue) > 1:
    queue.rotate(-n)
    print(f"Removed {queue.pop()}")

print(f"Last is {queue.pop()}")
