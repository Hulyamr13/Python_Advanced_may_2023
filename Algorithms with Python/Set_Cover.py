universe = list(map(int, input().split(", ")))

num_of_sets = int(input())
sets = []
for i in range(num_of_sets):
    sets.append(list(map(int, input().split(", "))))

selected_sets = []

while len(universe) > 0:
    current_set = max(sets, key=lambda s: sum(1 for e in s if e in universe))
    selected_sets.append(current_set)
    sets.remove(current_set)

    universe_copy = universe.copy()
    for element in universe_copy:
        if element in current_set:
            universe.remove(element)

print(f"Sets to take ({len(selected_sets)}):")
for set in selected_sets:
    print(", ".join(map(str, set)))
