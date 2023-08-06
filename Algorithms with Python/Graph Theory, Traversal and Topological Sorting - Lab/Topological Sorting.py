graph = {}
dependencies_by_node = {}
sorted_notes = []


for _ in range(int(input())):
    key, value = input().split(' ->')
    values = value.strip().split(', ') if value else []
    graph[key] = values


for node, children in graph.items():
    if node not in dependencies_by_node:
        dependencies_by_node[node] = 0
    for child in children:
        if child not in dependencies_by_node:
            dependencies_by_node[child] = 1
        else:
            dependencies_by_node[child] += 1


while dependencies_by_node:
    node = next((n for n, count in dependencies_by_node.items() if count == 0), None)

    if not node:
        break

    for child in graph[node]:
        dependencies_by_node[child] -= 1

    sorted_notes.append(node)
    dependencies_by_node.pop(node)


if dependencies_by_node:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_notes)}")