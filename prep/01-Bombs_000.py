from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

bombs = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
maked_bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}

succeeded_bomb_pouch = False

while bomb_effects and bomb_casings:
    bomb_effect = bomb_effects[0]
    bomb_casing = bomb_casings[-1]

    result = bomb_effect + bomb_casing

    if result in bombs:
        bomb_effects.popleft()
        bomb_casings.pop()
        bomb = bombs[result]
        maked_bombs[bomb] += 1

    else:
        bomb_casings.append(bomb_casings.pop() - 5)

    if (maked_bombs['Datura Bombs'] >= 3 and maked_bombs['Cherry Bombs']) >= 3 and (maked_bombs['Smoke Decoy Bombs']) >= 3:
        succeeded_bomb_pouch = True
        break

if succeeded_bomb_pouch:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effects])}')
else:
    print(f"Bomb Effects: empty")

if bomb_casings:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casings])}')
else:
    print(f"Bomb Casings: empty")


for bomb, value in sorted(maked_bombs.items()):
    print(f"{bomb}: {value}")
