from collections import deque

males_stack = deque(map(int, input().split()))
females_queue = deque(map(int, input().split()))
matches_counter = 0

while males_stack and females_queue:
    male = males_stack[-1]
    female = females_queue[0]

    if male <= 0:
        males_stack.pop()
        continue

    if female <= 0:
        females_queue.popleft()
        continue

    if female % 25 == 0:
        females_queue.popleft()
        females_queue.popleft()
        continue

    if male % 25 == 0:
        males_stack.pop()
        males_stack.pop()
        continue

    if male != female:
        male -= 2
        males_stack.pop()
        females_queue.popleft()
        males_stack.append(male)
    else:
        matches_counter += 1
        males_stack.pop()
        females_queue.popleft()

print(f"Matches: {matches_counter}")
print(f"Males left: {', '.join(map(str, reversed(males_stack))) if males_stack else 'none'}")
print(f"Females left: {', '.join(map(str, females_queue)) if females_queue else 'none'}")