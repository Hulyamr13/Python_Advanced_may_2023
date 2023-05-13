rows, cols = list(map(int, input().split(', ')))

workshop = []
my_pos = []

total_items = {
    'D': 0,
    'G': 0,
    'C': 0,
}

collected_items = {
    'D': 0,
    'G': 0,
    'C': 0,
}

for row in range(rows):
    line = input().split()
    if 'Y' in line:
        my_pos = [row, line.index('Y')]
    if 'C' in line:
        total_items['C'] += line.count('C')
    if 'G' in line:
        total_items['G'] += line.count('G')
    if 'D' in line:
        total_items['D'] += line.count('D')
    workshop.append(line)

merry_christmas = False
while True:
    command = input()
    if command == 'End':
        break
    direction, steps = command.split('-')
    steps = int(steps)
    r, c = my_pos[0], my_pos[1]
    workshop[r][c] = 'x'
    for _ in range(steps):
        if direction == 'right':
            if c + 1 == cols:
                c = -1
            c += 1
            if workshop[r][c] in total_items:
                total_items[workshop[r][c]] -= 1
                collected_items[workshop[r][c]] += 1
            workshop[r][c] = 'x'
        elif direction == 'left':
            if c - 1 < 0:
                c = cols
            c -= 1
            if workshop[r][c] in total_items:
                total_items[workshop[r][c]] -= 1
                collected_items[workshop[r][c]] += 1
            workshop[r][c] = 'x'
        elif direction == 'up':
            if r - 1 < 0:
                r = rows
            r -= 1
            if workshop[r][c] in total_items:
                total_items[workshop[r][c]] -= 1
                collected_items[workshop[r][c]] += 1
            workshop[r][c] = 'x'
        elif direction == 'down':
            if r + 1 == rows:
                r = -1
            r += 1
            if workshop[r][c] in total_items:
                total_items[workshop[r][c]] -= 1
                collected_items[workshop[r][c]] += 1
            workshop[r][c] = 'x'
        if not any(total_items.values()):
            merry_christmas = True
            workshop[r][c] = 'Y'
            break
    my_pos[0], my_pos[1] = r, c
    workshop[my_pos[0]][my_pos[1]] = 'Y'
    if merry_christmas:
        print("Merry Christmas!")
        break

print("You've collected:")
print(f"- {collected_items['D']} Christmas decorations\n"
      f"- {collected_items['G']} Gifts\n"
      f"- {collected_items['C']} Cookies")
for row in workshop:
    print(*row)
