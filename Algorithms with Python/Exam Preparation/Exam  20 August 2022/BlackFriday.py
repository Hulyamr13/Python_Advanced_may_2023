class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def main():
    nodes_count = int(input())
    edges_count = int(input())

    edges = read_edges(edges_count)

    sorted_edges = sorted(edges, key=lambda e: e.weight)

    root = [i for i in range(nodes_count)]

    total_cost = 0

    for edge in sorted_edges:
        first_root = get_root(edge.first, root)
        second_root = get_root(edge.second, root)

        if first_root != second_root:
            root[first_root] = second_root
            total_cost += edge.weight

    print(total_cost)


def get_root(node, root):
    while node != root[node]:
        node = root[node]

    return node


def read_edges(edges_count):
    result = []

    for _ in range(edges_count):
        edge_data = list(map(int, input().split()))
        first, second, weight = edge_data
        result.append(Edge(first, second, weight))

    return result


if __name__ == "__main__":
    main()
