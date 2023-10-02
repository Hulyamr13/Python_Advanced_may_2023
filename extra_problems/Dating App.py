from collections import deque

males = deque(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males and females:
    current_male = males[-1]
    current_female = females[0]

    if current_male <= 0:
        males.pop()
    elif current_female <= 0:
        females.popleft()
    elif current_male % 25 == 0:
        males.pop()
        if males:
            males.pop()
    elif current_female % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
    elif current_male == current_female:
        males.pop()
        females.popleft()
        matches += 1
    else:
        males[-1] -= 2
        females.popleft()

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(m) for m in reversed(males))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(str(f) for f in females)}")
else:
    print("Females left: none")
