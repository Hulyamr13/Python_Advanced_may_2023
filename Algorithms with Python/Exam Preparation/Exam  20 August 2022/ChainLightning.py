from heapq import heappush, heappop


class Edge:
    def __init__(self, first, second, distance):
        self.first = first
        self.second = second
        self.distance = distance


def main():
    nodes = int(input())
    edges = int(input())
    lightnings = int(input())

    graph = read_graph(nodes, edges)
    tree_by_node = {}
    damage_by_node = {}

    for _ in range(lightnings):
        lightning_data = list(map(int, input().split()))
        node = lightning_data[0]
        damage = lightning_data[1]

        if node not in tree_by_node:
            tree_by_node[node] = prim(node, graph)

        tree = tree_by_node[node]

        for neighbor, depth in tree.items():
            current_damage = calculate_damage(damage, depth)

            if neighbor not in damage_by_node:
                damage_by_node[neighbor] = 0

            damage_by_node[neighbor] += current_damage

    max_damaged_node = max(damage_by_node.values())

    print(max_damaged_node)


def calculate_damage(damage, depth):
    for i in range(depth - 1):
        damage //= 2

    return damage


def prim(start_node, graph):
    tree = {start_node: 1}
    queue = []

    for edge in graph[start_node]:
        heappush(queue, (edge.distance, edge))

    while queue:
        distance, edge = heappop(queue)

        non_tree_node = get_non_tree_node(tree, edge)

        if non_tree_node == -1:
            continue

        tree_node = get_tree_node(tree, edge)

        tree[non_tree_node] = tree[tree_node] + 1

        for neighbor_edge in graph[non_tree_node]:
            heappush(queue, (neighbor_edge.distance, neighbor_edge))

    return tree


def get_tree_node(tree, edge):
    if edge.first in tree:
        return edge.first
    else:
        return edge.second


def get_non_tree_node(tree, edge):
    if edge.first in tree and edge.second not in tree:
        return edge.second

    if edge.second in tree and edge.first not in tree:
        return edge.first

    return -1


def read_graph(nodes, edges):
    graph = [[] for _ in range(nodes)]

    for _ in range(edges):
        first, second, distance = map(int, input().split())
        graph[first].append(Edge(first, second, distance))
        graph[second].append(Edge(second, first, distance))

    return graph


if __name__ == "__main__":
    main()
