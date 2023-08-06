def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


def check_acyclic():
    graph = {}
    line = input().strip()

    while line != "End":
        start, end = line.split("-")

        if start not in graph:
            graph[start] = []

        if end not in graph:
            graph[end] = []

        graph[start].append(end)

        line = input().strip()

    acyclic = not has_cycle(graph)
    print("Acyclic: " + ("Yes" if acyclic else "No"))


check_acyclic()
