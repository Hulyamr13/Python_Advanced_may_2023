from queue import PriorityQueue

class Edge:
    def __init__(self, from_node, to_node, distance):
        self.from_node = from_node
        self.to_node = to_node
        self.distance = distance

def main():
    nodes_count = int(input())
    edges_count = int(input())

    start_node = int(input())

    graph = read_graph(nodes_count, edges_count)

    distances = [float('inf')] * nodes_count
    distances[start_node] = 0

    queue = PriorityQueue()
    queue.put((0, start_node))

    visited_nodes = {start_node}

    while not queue.empty():
        current_distance, node = queue.get()
        visited_nodes.add(node)

        if node == start_node:
            break

        for edge in graph[node]:
            child = edge.to_node

            if distances[child] == float('inf'):
                queue.put((edge.distance, child))

            new_distance = distances[node] + edge.distance

            if new_distance < distances[child]:
                distances[child] = new_distance
                queue.put((distances[child], child))

    if distances[start_node] == float('inf'):
        print(len(visited_nodes))
    else:
        print(distances[start_node])

def read_graph(nodes_count, edges_count):
    graph = [[] for _ in range(nodes_count)]

    for i in range(edges_count):
        from_node, to_node, distance = map(int, input().split())
        graph[from_node].append(Edge(from_node, to_node, distance))

    return graph

if __name__ == "__main__":
    main()
