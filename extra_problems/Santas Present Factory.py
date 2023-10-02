from collections import deque

materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

present = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while materials and magic_level:
    if materials[0] == 0:
        materials.popleft()
        continue
    if magic_level[0] == 0:
        magic_level.popleft()
        continue

    first_m = materials.popleft()
    first_ml = magic_level.popleft()
    sum = first_m * first_ml

    if sum == 150:
        present["Doll"] += 1
    elif sum == 250:
        present["Wooden train"] += 1
    elif sum == 300:
        present["Teddy bear"] += 1
    elif sum == 400:
        present["Bicycle"] += 1
    else:
        if sum < 0:
            materials.append(first_m + first_ml)
        else:
            materials.append(first_m + 15)

if (present["Doll"] > 0 and present["Wooden train"] > 0) or (present["Teddy bear"] > 0 and present["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for name, count in present.items():
    if count > 0:
        print(f"{name}: {count}")
