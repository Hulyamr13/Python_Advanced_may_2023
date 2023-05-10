from queue import Queue

queue = Queue()

while True:
    customer = input()
    if customer == "Paid":
        while not queue.empty():
            print(queue.get())
        continue
    elif customer == "End":
        remaining_customers = queue.qsize()
        print(f"{remaining_customers} people remaining.")
        break
    queue.put(customer)