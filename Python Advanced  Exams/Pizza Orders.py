pizza_orders = []
for x in input().split(', '):
    if 0 < int(x) <= 10:
        pizza_orders.append(int(x))

employees = []
for x in input().split(', '):
    employees.append(int(x))

total_pizzas = 0

while len(pizza_orders) > 0 and len(employees) > 0:
    order = pizza_orders.pop(0)
    employee = employees.pop()
    if order <= employee:
        total_pizzas += order
    elif order > employee:
        order -= employee
        total_pizzas += employee
        pizza_orders.insert(0, order)

if len(pizza_orders) == 0:
    print("All orders are successfully completed!\nTotal pizzas made: {}\nEmployees: {}".format(total_pizzas, ', '.join(str(x) for x in employees)))
else:
    print("Not all orders are completed.\nOrders left: {}".format(', '.join(str(x) for x in pizza_orders)))
