class Edge:
    def __init__(self, fr, to, weight):
        self.from_node = fr
        self.to_node = to
        self.weight = weight


def main():
    nodes_count = int(input())
    edges_count = int(input())

    edges = read_edges(edges_count)

    source = int(input())
    destination = int(input())

    distances = [float('inf')] * (nodes_count + 1)
    distances[source] = 0

    prev = [-1] * (nodes_count + 1)

    for _ in range(nodes_count - 1):
        updated = False

        for edge in edges:
            if distances[edge.from_node] == float('inf'):
                continue

            new_distance = distances[edge.from_node] + edge.weight
            if new_distance < distances[edge.to_node]:
                distances[edge.to_node] = new_distance
                prev[edge.to_node] = edge.from_node

                updated = True

        if not updated:
            break

    for edge in edges:
        if distances[edge.from_node] == float('inf'):
            continue

        new_distance = distances[edge.from_node] + edge.weight
        if new_distance < distances[edge.to_node]:
            print("Undefined")
            return

    path = reconstruct_path(prev, destination)

    print(" ".join(str(node) for node in path))
    print(distances[destination])


def reconstruct_path(prev, destination):
    path = []
    node = destination

    while node != -1:
        path.append(node)
        node = prev[node]

    return path[::-1]


def read_edges(edges_count):
    result = []

    for _ in range(edges_count):
        edge_data = list(map(int, input().split()))
        from_node = edge_data[0]
        to_node = edge_data[1]
        weight = edge_data[2]

        result.append(Edge(from_node, to_node, weight))

    return result


if __name__ == "__main__":
    main()
