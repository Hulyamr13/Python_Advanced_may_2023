from heapq import heappop, heappush


def prim(node, edges_by_node, forest):
    forest.add(node)
    queue = []

    for edge in edges_by_node[node]:
        heappush(queue, (edge.weight, edge))

    while queue:
        weight, edge = heappop(queue)

        non_tree_node = get_non_tree_node(edge.first, edge.second, forest)

        if non_tree_node == -1:
            continue

        print(f"{edge.first} - {edge.second}")

        forest.add(non_tree_node)
        for adj_edge in edges_by_node[non_tree_node]:
            heappush(queue, (adj_edge.weight, adj_edge))


def get_non_tree_node(first, second, forest):
    non_tree_node = -1

    if first in forest and second not in forest:
        non_tree_node = second
    elif second in forest and first not in forest:
        non_tree_node = first

    return non_tree_node


def read_graph(e):
    edges_by_node = {}

    for _ in range(e):
        edge_data = [int(x) for x in input().split(", ")]

        first = edge_data[0]
        second = edge_data[1]
        weight = edge_data[2]

        if first not in edges_by_node:
            edges_by_node[first] = []
        if second not in edges_by_node:
            edges_by_node[second] = []

        edge = Edge(first, second, weight)

        edges_by_node[first].append(edge)
        edges_by_node[second].append(edge)

    return edges_by_node


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


edges = int(input())
edges_by_node = read_graph(edges)
forest = set()

for node in edges_by_node.keys():
    if node not in forest:
        prim(node, edges_by_node, forest)
