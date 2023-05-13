from collections import deque

materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])
presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic:
    current_material = materials.pop()
    current_magic_lvl = magic.popleft()
    present = current_material + current_magic_lvl

    if present < 100:
        present = current_material * 2 + current_magic_lvl * 3 if present % 2 == 0 else present * 2
    elif present > 499:
        present /= 2

    if 100 <= present <= 199:
        presents["Gemstone"] += 1
    elif 200 <= present <= 299:
        presents["Porcelain Sculpture"] += 1
    elif 300 <= present <= 399:
        presents["Gold"] += 1
    elif 400 <= present <= 499:
        presents["Diamond Jewellery"] += 1

result = ''
if all([presents.get("Gemstone", 0), presents.get("Porcelain Sculpture", 0)]) or all([presents.get("Gold", 0), presents.get("Diamond Jewellery", 0)]):
    result += "The wedding presents are made!\n"
else:
    result += "Aladdin does not have enough wedding presents.\n"

result += f"Materials left: {', '.join(map(str, materials))}\n" if materials else ""
result += f"Magic left: {', '.join(map(str, magic))}\n" if magic else ""

for gift, val in sorted(presents.items()):
    if val:
        result += f"{gift}: {val}\n"

print(result)
