from collections import deque

input1 = input()
input2 = input()

liquids = deque(map(int, input1.split()))
ingredients = deque(map(int, input2.split()))

food_res = {25: "Bread", 50: "Cake", 75: "Pastry", 100: "Fruit Pie"}
food = {}

while liquids and ingredients:
    first_liquid = liquids.popleft()
    first_ingredient = ingredients.pop()
    total = first_liquid + first_ingredient

    if total in food_res:
        current = food_res[total]
        food[current] = food.get(current, 0) + 1
    else:
        ingredients.append(first_ingredient + 3)

if len(food) == 4:
    print("Wohoo! You succeeded in cooking all the food!")
else:
    print("Ugh, what a pity! You didn't have enough materials to cook everything.")

if not liquids:
    print("Liquids left: none")
else:
    liquids_left = "Liquids left: " + ", ".join(map(str, liquids))
    print(liquids_left)

if not ingredients:
    print("Ingredients left: none")
else:
    ingredients_left = "Ingredients left: " + ", ".join(map(str, ingredients))
    print(ingredients_left)

print(f"Bread: {food.get('Bread', 0)}")
print(f"Cake: {food.get('Cake', 0)}")
print(f"Fruit Pie: {food.get('Fruit Pie', 0)}")
print(f"Pastry: {food.get('Pastry', 0)}")
