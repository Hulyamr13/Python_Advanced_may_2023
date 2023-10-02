from collections import deque
from decimal import Decimal

input1 = input()
input2 = input()

milk = deque(map(Decimal, input1.split()))
cocoa = deque(map(Decimal, input2.split()))

ready = {}

while milk and cocoa:
    first_milk = milk[0]
    first_cocoa = cocoa[0]

    percentage = (first_cocoa / (first_milk + first_cocoa)) * 100

    if percentage == Decimal('30'):
        ready.setdefault("Milk Chocolate", 0)
        ready["Milk Chocolate"] += 1
        milk.popleft()
        cocoa.popleft()
    elif percentage == Decimal('50'):
        ready.setdefault("Dark Chocolate", 0)
        ready["Dark Chocolate"] += 1
        milk.popleft()
        cocoa.popleft()
    elif percentage == Decimal('100'):
        ready.setdefault("Baking Chocolate", 0)
        ready["Baking Chocolate"] += 1
        milk.popleft()
        cocoa.popleft()
    else:
        cocoa.popleft()
        increase = milk[0] + Decimal('10')
        milk.popleft()
        milk.append(increase)

print("It’s a Chocolate Time. All chocolate types are prepared.") if len(ready) == 3 else print(
    "Sorry, but you didn't succeed to prepare all types of chocolates.")

for key, value in ready.items():
    print("#", key, "-->", value)
