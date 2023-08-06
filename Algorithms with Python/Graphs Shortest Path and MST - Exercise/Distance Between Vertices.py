from collections import deque


def get_shortest_path(source, destination, graph):
    queue = deque()
    queue.append(source)

    steps = {source: 0}

    while queue:
        node = queue.popleft()

        if node == destination:
            return steps[node]

        for child in graph[node]:
            if child in steps:
                continue

            queue.append(child)
            steps[child] = steps[node] + 1

    return -1


def read_graph(n):
    graph = {}

    for _ in range(n):
        parts = input().split(':')

        node = int(parts[0])

        if len(parts) == 1:
            graph[node] = []
        else:
            children = list(map(int, parts[1].split()))
            graph[node] = children

    return graph


n = int(input())
p = int(input())
graph = read_graph(n)

for _ in range(p):
    pair = input().split('-')
    source = int(pair[0])
    destination = int(pair[1])

    steps = get_shortest_path(source, destination, graph)

    print(f"{{{source}, {destination}}} -> {steps}")
