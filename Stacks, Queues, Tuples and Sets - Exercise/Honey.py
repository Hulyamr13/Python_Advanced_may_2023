from collections import deque

working_bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
process = deque(input().split())

total_honey = 0

while working_bees and nectar:

    current_bee = working_bees[0]
    current_nectar = nectar[-1]

    if current_bee <= current_nectar:

        if process[0] == "*":
            total_honey += abs(current_bee * current_nectar)

        elif process[0] == "/" and current_nectar > 0:
            total_honey += abs(current_bee / current_nectar)

        elif process[0] == "+":
            total_honey += abs(current_bee + current_nectar)

        elif process[0] == "-":
            total_honey += abs(current_bee - current_nectar)

        working_bees.popleft()
        nectar.pop()
        process.popleft()

    elif current_bee > current_nectar:
        nectar.pop()
        continue

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")