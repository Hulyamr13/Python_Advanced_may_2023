edges = int(input())
max_node = float('-inf')
graph = []
forest = []

def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


for _ in range(edges):
    first, second, weight = map(int, input().split(", "))
    graph.append((first, second, weight))
    max_node = max(first, second, max_node)

parent = list(range(max_node + 1))

for edge in sorted(graph, key=lambda x: x[2]):
    first_node_root = find_root(parent, edge[0])
    second_node_root = find_root(parent, edge[1])

    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest.append(edge)

for edge in forest:
    print(f"{edge[0]} - {edge[1]}")