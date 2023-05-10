queue = []

while True:
    customer = input()
    if customer == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif customer == "Paid":
        for name in queue:
            print(name)
        queue.clear()
    else:
        queue.append(customer)