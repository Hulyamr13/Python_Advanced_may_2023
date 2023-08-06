from collections import deque
from queue import PriorityQueue


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]

    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []

    graph[source].append((source, destination, weight))

start = int(input())
target = int(input())

max_node = max(graph.keys())

distances = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distances[start] = 0

pq = PriorityQueue()  # Always returns smallest
pq.put((0, start))  # sorts by first param

while not pq.empty():
    min_distance, node = pq.get()

    if node == target:
        break

    for edge in graph[node]:
        source, destination, weight = edge
        new_distance = min_distance + weight

        if new_distance < distances[destination]:
            distances[destination] = new_distance
            parent[destination] = node
            pq.put((new_distance, destination))

if distances[target] == float('inf'):
    print("There is no such path.")
else:
    path = deque()
    node = target

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(distances[target])
    print(*path, sep=' ')
