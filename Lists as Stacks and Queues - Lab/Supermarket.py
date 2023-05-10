from collections import deque

queue = deque()

while True:
    customer = input()
    if customer == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif customer == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(customer)
