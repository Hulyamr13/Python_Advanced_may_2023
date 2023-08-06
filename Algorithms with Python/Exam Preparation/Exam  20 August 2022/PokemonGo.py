class Street:
    def __init__(self, name, value, length):
        self.name = name
        self.value = value
        self.length = length


def main():
    max_fuel = int(input())
    streets = read_input()

    table = [[0 for _ in range(max_fuel + 1)] for _ in range(len(streets) + 1)]
    fill_table(streets, table)

    selected_streets = set()
    used_fuel = 0
    total_value = 0

    row = len(table) - 1
    col = len(table[0]) - 1

    while row > 0 and col > 0:
        if table[row][col] != table[row - 1][col]:
            selected_item = streets[row - 1]

            selected_streets.add(selected_item.name)
            used_fuel += selected_item.length
            total_value += selected_item.value

            col -= selected_item.length

        row -= 1

    if selected_streets:
        print(" -> ".join(selected_streets))
    print(f"Total Pokemon caught -> {total_value}")
    print(f"Fuel Left -> {max_fuel - used_fuel}")


def fill_table(streets, table):
    for item_index in range(1, len(table)):
        current_item = streets[item_index - 1]

        for capacity in range(1, len(table[0])):
            if capacity < current_item.length:
                table[item_index][capacity] = table[item_index - 1][capacity]
            else:
                table[item_index][capacity] = max(
                    table[item_index - 1][capacity],
                    table[item_index - 1][capacity - current_item.length] + current_item.value
                )


def read_input():
    result = []

    while True:
        line = input()

        if line == "End":
            break

        name, value, length = line.split(", ")
        value, length = int(value), int(length)

        result.append(Street(name, value, length))

    return result


if __name__ == "__main__":
    main()
