customers = input().split(', ')
taxis = input().split(', ')
for i in range(len(customers)):
    customers[i] = int(customers[i])
for i in range(len(taxis)):
    taxis[i] = int(taxis[i])

total_time = 0
while customers and taxis:
    customer = customers[0]
    taxi = taxis[-1]

    if customer <= taxi:
        customers.pop(0)
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
