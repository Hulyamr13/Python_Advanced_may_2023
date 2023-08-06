class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def main():
    items = read_input()
    max_capacity = int(input())

    table = [[0 for _ in range(max_capacity + 1)] for _ in range(len(items) + 1)]
    fill_table(items, table)

    total_value = 0

    row = len(table) - 1
    col = len(table[0]) - 1

    while row > 0 and col > 0:
        if table[row][col] != table[row - 1][col]:
            selected_item = items[row - 1]
            total_value += selected_item.value
            col -= selected_item.weight

        row -= 1

    print(f"Maximum value: {total_value}")

def fill_table(items, table):
    for item_index in range(1, len(items) + 1):
        current_item = items[item_index - 1]

        for capacity in range(1, len(table[0])):
            if capacity < current_item.weight:
                table[item_index][capacity] = table[item_index - 1][capacity]
            else:
                table[item_index][capacity] = max(
                    table[item_index - 1][capacity],
                    table[item_index - 1][capacity - current_item.weight] + current_item.value
                )

def read_input():
    values = list(map(int, input().split(", ")))
    weights = list(map(int, input().split(", ")))

    return [Item(value, weight) for value, weight in zip(values, weights)]

if __name__ == "__main__":
    main()
