from collections import deque

firework_effects = deque(int(effect) for effect in input().split(', '))
explosive_powers = [int(power) for power in input().split(', ')]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

success = False

while True:
    if not firework_effects or not explosive_powers:
        if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
            success = True
        break

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        success = True
        break

    current_effect = firework_effects[0]
    current_power = explosive_powers[-1]

    if current_effect <= 0:
        firework_effects.popleft()
        continue
    if current_power <= 0:
        explosive_powers.pop()
        continue

    result = current_effect + current_power

    if result % 3 == 0 and result % 5 != 0:
        palm_fireworks += 1
        firework_effects.popleft()
        explosive_powers.pop()
    elif result % 3 != 0 and result % 5 == 0:
        willow_fireworks += 1
        firework_effects.popleft()
        explosive_powers.pop()
    elif result % 3 == 0 and result % 5 == 0:
        crossette_fireworks += 1
        firework_effects.popleft()
        explosive_powers.pop()
    else:
        current_effect -= 1
        firework_effects.popleft()
        firework_effects.append(current_effect)

if success:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(effect) for effect in firework_effects)}")
if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(power) for power in explosive_powers)}")

print(f'Palm Fireworks: {palm_fireworks}')
print(f'Willow Fireworks: {willow_fireworks}')
print(f'Crossette Fireworks: {crossette_fireworks}')