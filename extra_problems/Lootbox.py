first_box = list(map(int, input().split()))
second_box = list(map(int, input().split()))
claimed_items = []

while first_box and second_box:
    if (first_box[0] + second_box[-1]) % 2 == 0:
        claimed_items.append(first_box.pop(0) + second_box.pop())
    else:
        second_box.pop()

if not first_box:
    print("First lootbox is empty")
elif not second_box:
    print("Second lootbox is empty")

total_value = sum(claimed_items)
if total_value >= 100:
    print(f"Your loot was epic! Value: {total_value}")
else:
    print(f"Your loot was poor... Value: {total_value}")
