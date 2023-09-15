from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]


total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis[-1]

    if customer <= taxi:
        customers.popleft()
        taxis.pop()
        total_time += customer

    else:
        taxis.pop()


if customers:
    print(f'Not all customers were driven to their destinations\n'
          f'Customers left: {", ".join([str(x) for x in customers])}')
else:
    print(f'All customers were driven to their destinations\n'
          f'Total time: {total_time} minutes')