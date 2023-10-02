steel_input = input().split()
carbon_input = input().split()

steel = []
carbon = []

for s in steel_input:
    steel.append(int(s))

for c in carbon_input:
    carbon.append(int(c))

swords = {
    "Sabre": 0,
    "Katana": 0,
    "Shamshir": 0,
    "Gladius": 0
}

while len(steel) > 0 and len(carbon) > 0:
    first_st = steel.pop(0)
    first_carb = carbon.pop()

    if first_carb + first_st == 70:
        swords["Gladius"] += 1
    elif first_carb + first_st == 80:
        swords["Shamshir"] += 1
    elif first_carb + first_st == 90:
        swords["Katana"] += 1
    elif first_carb + first_st == 110:
        swords["Sabre"] += 1
    else:
        carbon.append(first_carb + 5)

sum_swords = sum(swords.values())

if sum_swords > 0:
    print("You have forged {} swords.".format(sum_swords))
else:
    print("You did not have enough resources to forge a sword.")

if len(steel) == 0:
    print("Steel left: none")
else:
    steel_left = ", ".join(str(s) for s in steel)
    print("Steel left: {}".format(steel_left))

if len(carbon) == 0:
    print("Carbon left: none")
else:
    carbon_left = ", ".join(str(c) for c in reversed(carbon))
    print("Carbon left: {}".format(carbon_left))

for sword, count in swords.items():
    if count > 0:
        print("{}: {}".format(sword, count))
