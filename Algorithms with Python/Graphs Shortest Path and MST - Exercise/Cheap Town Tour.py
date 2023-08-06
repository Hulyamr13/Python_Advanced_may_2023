class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


def main():
    nodes_count = int(input())
    edges_count = int(input())

    graph = []
    parent = [num for num in range(nodes_count)]
    total_cost = 0

    for _ in range(edges_count):
        first, second, weight = [int(x) for x in input().split(' - ')]
        graph.append((first, second, weight))

    for first, second, weight in sorted(graph, key=lambda x: x[2]):
        first_node_root = find_root(parent, first)
        second_node_root = find_root(parent, second)

        if first_node_root == second_node_root:
            continue

        parent[first_node_root] = second_node_root
        total_cost += weight

    print(f"Total cost: {total_cost}")


if __name__ == "__main__":
    main()
