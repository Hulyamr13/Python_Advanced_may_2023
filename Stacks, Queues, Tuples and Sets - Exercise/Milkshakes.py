chocolates = list(map(int, input().split(", ")))
milk_cups = list(map(int, input().split(", ")))

shakes_made = 0

while chocolates and milk_cups and shakes_made < 5:
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.pop(0)
        continue
    if chocolates[-1] == milk_cups[0]:
        chocolates.pop()
        milk_cups.pop(0)
        shakes_made += 1
    else:
        milk_cups.append(milk_cups.pop(0))
        chocolates[-1] -= 5

if shakes_made == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {'empty' if not chocolates else ', '.join(map(str, chocolates))}")
print(f"Milk: {'empty' if not milk_cups else ', '.join(map(str, milk_cups))}")
