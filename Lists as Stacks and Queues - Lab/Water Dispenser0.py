from collections import deque

water = int(input())
queue = deque()
command = input()

while command != "Start":
    queue.append(command)
    command = input()

while True:
    command = input()
    if command == "End":
        print(f"{water} liters left")
        break
    elif command.startswith("refill"):
        refill_liters = int(command.split()[1])
        water += refill_liters
    else:
        liters = int(command)
        if liters <= water:
            person = queue.popleft()
            print(f"{person} got water")
            water -= liters
        else:
            person = queue.popleft()
            print(f"{person} must wait")
