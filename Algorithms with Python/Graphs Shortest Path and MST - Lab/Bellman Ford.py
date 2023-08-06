from collections import deque

nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(' ')]
    graph.append((source, destination, weight))


start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0
parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False
    for edge in graph:
        source, destination, weight = edge
        if distance[source] == float('inf'):
            continue

        new_distance = distance[source] + weight

        if new_distance < distance[destination]:
            distance[destination] = new_distance
            parent[destination] = source
            updated = True
    if not updated:
        break

for edge in graph:
    source, destination, weight = edge
    new_distance = distance[source] + weight
    if new_distance < distance[destination]:
        print('Negative Cycle Detected')
        break
else:
    path = deque()
    node = target

    while node:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=' ')
    print(distance[target])