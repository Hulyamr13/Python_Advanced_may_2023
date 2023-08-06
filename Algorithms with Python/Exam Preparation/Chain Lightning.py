from heapq import heappop, heappush


class Edge:
    def __init__(self, first, second, distance):
        self.first = first
        self.second = second
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


def main():
    nodes = int(input())
    edges = int(input())
    lightnings = int(input())

    graph = read_graph(nodes, edges)
    tree_by_node = {}
    damage_by_node = {}

    for _ in range(lightnings):
        lightning_data = [int(x) for x in input().split()]
        node = lightning_data[0]
        damage = lightning_data[1]

        if node not in tree_by_node:
            tree_by_node[node] = prim(node, graph)

        tree = tree_by_node[node]

        for key, value in tree.items():
            current_damage = calculate_damage(damage, value)

            if key not in damage_by_node:
                damage_by_node[key] = 0

            damage_by_node[key] += current_damage

    max_damaged_node = max(damage_by_node.values())
    print(max_damaged_node)


def calculate_damage(damage, depth):
    for _ in range(depth - 1):
        damage //= 2

    return damage


def prim(start_node, graph):
    tree = {start_node: 1}
    queue = []
    for edge in graph[start_node]:
        heappush(queue, edge)

    while queue:
        edge = heappop(queue)
        non_tree_node = get_non_tree_node(tree, edge)

        if non_tree_node == -1:
            continue

        tree_node = get_tree_node(tree, edge)

        tree[non_tree_node] = tree[tree_node] + 1

        for next_edge in graph[non_tree_node]:
            heappush(queue, next_edge)

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
        edge_data = [int(x) for x in input().split()]
        first = edge_data[0]
        second = edge_data[1]
        distance = edge_data[2]

        edge = Edge(first, second, distance)

        graph[first].append(edge)
        graph[second].append(edge)

    return graph


if __name__ == "__main__":
    main()
