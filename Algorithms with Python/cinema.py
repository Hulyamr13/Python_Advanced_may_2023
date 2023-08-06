def permute(names, seats, locked_seats):
    if len(names) == 0:
        print(' '.join(seats))
        return

    permute(names[1:], seats, locked_seats)

    for i in range(len(names)):
        if i > 0:
            names[0], names[i] = names[i], names[0]
        permute(names[1:], seats, locked_seats)
        if i > 0:
            names[0], names[i] = names[i], names[0]

# Read input
names = input().split(", ")
seats = [""] * len(names)
locked_seats = set()

while True:
    line = input()
    if line == "generate":
        break

    parts = line.split(" - ")
    name = parts[0]
    position = int(parts[1]) - 1

    names.remove(name)
    seats[position] = name
    locked_seats.add(position)

permute(names, seats, locked_seats)