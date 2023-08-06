from collections import defaultdict, deque

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Read the input
num_nodes = int(input())
num_edges = int(input())

graph = defaultdict(list)
for _ in range(num_edges):
    destination, source = map(int, input().split(" "))
    graph[destination].append(source)
    graph[source].append(destination)

start_node = int(input())
end_node = int(input())

# Find the shortest path
path = shortest_path(graph, start_node, end_node)

# Print the result
if path:
    print(f"Shortest path length is: {len(path) - 1}")
    print(" ".join(str(node) for node in path))
else:
    print("No path found")
