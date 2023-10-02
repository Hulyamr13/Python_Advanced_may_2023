from collections import deque

milk_values = list(map(float, input().split()))
cacao_values = list(map(float, input().split()))
chocolates = {"Milk Chocolate": 0, "Dark Chocolate": 0, "Baking Chocolate": 0}

milk_values_queue = deque(milk_values)
cacao_values_stack = deque(cacao_values)

while milk_values_queue and cacao_values_stack:
    current_milk_value = milk_values_queue[0]
    current_cacao = cacao_values_stack[-1]
    cacao_percentage = (current_cacao / (current_milk_value + current_cacao)) * 100

    if cacao_percentage == 30:
        chocolates["Milk Chocolate"] += 1
        milk_values_queue.popleft()
        cacao_values_stack.pop()

    elif cacao_percentage == 50:
        chocolates["Dark Chocolate"] += 1
        milk_values_queue.popleft()
        cacao_values_stack.pop()

    elif cacao_percentage == 100:
        chocolates["Baking Chocolate"] += 1
        milk_values_queue.popleft()
        cacao_values_stack.pop()

    else:
        cacao_values_stack.pop()
        current_milk_value += 10
        milk_values_queue.popleft()
        milk_values_queue.append(current_milk_value)

if 0 in chocolates.values():
    print("Sorry, but you didn't succeed to prepare all types of chocolates.")
else:
    print("It's a Chocolate Time. All chocolate types are prepared.")

for chocolate_type, amount in sorted(chocolates.items()):
    if amount > 0:
        print(f"# {chocolate_type} --> {amount}")
