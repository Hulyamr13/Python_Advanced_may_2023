from collections import deque

liquids = deque(map(int, input().split()))
ingredients = deque(map(int, input().split()))

food_res = {25: "Biscuit", 50: "Cake", 75: "Pastry", 100: "Pie"}
food = {}

while liquids and ingredients:
    first_liquid = liquids.popleft()
    first_ingredient = ingredients.pop()
    total = first_liquid + first_ingredient

    if total in food_res:
        food_name = food_res[total]
        food[food_name] = food.get(food_name, 0) + 1
    else:
        ingredients.append(first_ingredient + 3)

if len(food) == 4:
    print("Great! You succeeded in cooking all the food!")
else:
    print("What a pity! You didn't have enough materials to cook everything.")

if not liquids:
    print("Liquids left: none")
else:
    liquids_left = ", ".join(str(x) for x in reversed(liquids))
    print(f"Liquids left: {liquids_left}")

if not ingredients:
    print("Ingredients left: none")
else:
    ingredients_left = ", ".join(str(x) for x in ingredients)
    print(f"Ingredients left: {ingredients_left}")

print("Biscuit:", food.get("Biscuit", 0))
print("Cake:", food.get("Cake", 0))
print("Pie:", food.get("Pie", 0))
print("Pastry:", food.get("Pastry", 0))
