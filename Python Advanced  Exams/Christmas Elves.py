from collections import deque

energy = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])
toys_made = 0
used_energy = 0
counter = 1

while energy and materials:
    if energy[0] < 5:
        energy.popleft()
        continue

    current_elf, current_material = energy.popleft(), materials.pop()
    toys, nrg_needed = (1, current_material) if counter % 3 != 0 else (2, current_material * 2)

    if current_elf >= nrg_needed:
        current_elf -= nrg_needed
        if counter % 5 != 0:
            toys_made += toys
            current_elf += 1

        energy.append(current_elf)
        used_energy += nrg_needed
    else:
        materials.append(current_material)
        current_elf = current_elf * 2
        energy.append(current_elf)

    counter += 1

print(f"Toys: {toys_made}")
print(f"Energy: {used_energy}")

if energy:
    print(f"Elves left: {', '.join(str(x) for x in energy)}")

if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
