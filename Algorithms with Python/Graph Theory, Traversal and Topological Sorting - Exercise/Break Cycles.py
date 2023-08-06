from collections import deque


class Edge:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f"{self.first} - {self.second}"

    def reversed(self):
        return Edge(self.second, self.first)


def has_path(source, destination, graph):
    queue = deque()
    queue.append(source)

    visited = set([source])

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for child in graph[node]:
            if child in visited:
                continue

            visited.add(child)
            queue.append(child)

    return False


def process_input(n):
    graph = {}
    edges = []

    for _ in range(n):
        parts = input().split(" -> ")
        node = parts[0]
        children = parts[1].split()

        if node not in graph:
            graph[node] = []

        for child in children:
            graph[node].append(child)
            edges.append(Edge(node, child))

    return edges, graph


def main():
    n = int(input())

    edges, graph = process_input(n)

    edges = sorted(edges, key=lambda e: (e.first, e.second))

    removed_edges = []
    blacklisted = set()

    for edge in edges:
        first = edge.first
        second = edge.second

        graph[first].remove(second)

        if has_path(first, second, graph):
            if str(edge) in blacklisted:
                continue

            removed_edges.append(edge)
            blacklisted.add(str(edge.reversed()))
        else:
            graph[first].append(second)

    print(f"Edges to remove: {len(removed_edges)}")
    for edge in removed_edges:
        print(edge)


main()
