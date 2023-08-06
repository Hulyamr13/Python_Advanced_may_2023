from collections import deque


def dfs(node):
    visited.add(node)
    for child in graph.get(node, []):
        if child not in visited:
            dfs(child)
    result.appendleft(node)


graph = {}
visited = set()
result = deque()

while True:
    data = input().split()
    if data[0] == "End":
        break
    graph[data[0]] = data[2:]

for node in graph:
    if node not in visited:
        dfs(node)

print(' '.join(result))
