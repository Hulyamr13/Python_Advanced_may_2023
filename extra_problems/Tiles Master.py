from collections import deque

white_tiles = list(map(int, input().split()))
grey_tiles = deque(map(int, input().split()))

count_of_tiles = {
    "Sink": 0,
    "Oven": 0,
    "Countertop": 0,
    "Wall": 0,
    "Floor": 0
}

while white_tiles and grey_tiles:
    if white_tiles[0] == grey_tiles[0]:
        area_of_tiles = white_tiles[0] + grey_tiles[0]

        if area_of_tiles == 40:
            count_of_tiles["Sink"] += 1
        elif area_of_tiles == 50:
            count_of_tiles["Oven"] += 1
        elif area_of_tiles == 60:
            count_of_tiles["Countertop"] += 1
        elif area_of_tiles == 70:
            count_of_tiles["Wall"] += 1
        else:
            count_of_tiles["Floor"] += 1

        white_tiles.pop(0)
        grey_tiles.popleft()
    else:
        tmp_white = white_tiles[0] // 2
        tmp_grey = grey_tiles[0]

        white_tiles.pop(0)
        grey_tiles.popleft()

        white_tiles.append(tmp_white)
        grey_tiles.append(tmp_grey)

if white_tiles:
    print(f"White tiles left: {', '.join(map(str, white_tiles))}")
else:
    print("White tiles left: none")

if grey_tiles:
    print(f"Grey tiles left: {', '.join(map(str, grey_tiles))}")
else:
    print("Grey tiles left: none")

for item in sorted(count_of_tiles.items(), key=lambda x: (-x[1], x[0])):
    if item[1] > 0:
        print(f"{item[0]}: {item[1]}")
