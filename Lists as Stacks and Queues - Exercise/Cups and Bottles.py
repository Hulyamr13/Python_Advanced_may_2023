cups_input = input()
cups = [int(cup) for cup in cups_input.split()]

bottles_input = input()
bottles = [int(bottle) for bottle in bottles_input.split()]

wasted_water = 0

while len(cups) > 0 and len(bottles) > 0:
    current_cup = cups.pop(0)
    current_bottle = bottles.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        while current_cup > 0 and len(bottles) > 0:
            current_bottle = bottles.pop()
            if current_bottle >= current_cup:
                wasted_water += current_bottle - current_cup
                current_cup = 0
            else:
                current_cup -= current_bottle

if len(cups) == 0:
    print(f"Bottles: {' '.join(map(str, bottles[::-1]))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")
