from collections import deque

input1 = input()

input2 = input()

ingredients = deque(map(int, input1.split()))
fresh_level = list(map(int, input2.split()))

cocktails = {}

while ingredients and fresh_level:
    if ingredients[0] == 0:
        ingredients.popleft()
        continue

    first_ingredient = ingredients.popleft()
    first_level = fresh_level.pop()

    if first_ingredient * first_level == 150:  # Pear Sour
        cocktails["Pear Sour"] = cocktails.get("Pear Sour", 0) + 1
    elif first_ingredient * first_level == 250:  # The Harvest
        cocktails["The Harvest"] = cocktails.get("The Harvest", 0) + 1
    elif first_ingredient * first_level == 300:  # Apple Hinny
        cocktails["Apple Hinny"] = cocktails.get("Apple Hinny", 0) + 1
    elif first_ingredient * first_level == 400:  # High Fashion
        cocktails["High Fashion"] = cocktails.get("High Fashion", 0) + 1
    else:
        ingredients.append(first_ingredient + 5)

print("It's party time! The cocktails are ready!" if len(cocktails) == 4 else "What a pity! You didn't manage to prepare all cocktails.")
if ingredients:
    print("Ingredients left:", sum(ingredients))
for cocktail, count in cocktails.items():
    print(f" # {cocktail} --> {count}")