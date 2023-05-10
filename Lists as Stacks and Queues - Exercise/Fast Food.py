from collections import deque

# Read quantity of food
quantity_of_food = int(input())

# Read orders
orders = deque(map(int, input().split()))

# Find biggest order
biggest_order = max(orders)

# Serve customers
while orders:
    order = orders.popleft()
    if order <= quantity_of_food:
        quantity_of_food -= order
    else:
        orders.appendleft(order)
        break

# Print results
print(biggest_order)
if not orders:
    print("Orders complete")
else:
    orders_left = " ".join(str(order) for order in orders)
    print(f"Orders left: {orders_left}")
