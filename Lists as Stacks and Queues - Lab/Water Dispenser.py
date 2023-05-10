from queue import Queue

water_dispenser = int(input())
people_queue = Queue()

while True:
    command = input()
    if command == "Start":
        break
    people_queue.put(command)

while True:
    command = input()
    if command == "End":
        break
    elif command.startswith("refill"):
        liters = int(command.split()[1])
        water_dispenser += liters
    else:
        liters = int(command)
        if liters <= water_dispenser and not people_queue.empty():
            person = people_queue.get()
            print(f"{person} got water")
            water_dispenser -= liters
        elif not people_queue.empty():
            person = people_queue.get()
            print(f"{person} must wait")

print(f"{water_dispenser} liters left")