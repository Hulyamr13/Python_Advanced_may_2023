def find_bridges(graph):
    n = len(graph)
    visited = [False] * n
    low = [float('inf')] * n
    parent = [-1] * n
    bridges = []

    def dfs(node):
        nonlocal time
        visited[node] = True
        low[node] = time
        time += 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                dfs(neighbor)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > low[node]:
                    bridges.append((node, neighbor))
            elif neighbor != parent[node]:
                low[node] = min(low[node], low[neighbor])

    time = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)

    return bridges


def main():
    buildings = int(input())
    streets = int(input())

    graph = [[] for _ in range(buildings)]

    for _ in range(streets):
        building1, building2 = map(int, input().split(" - "))
        graph[building1].append(building2)
        graph[building2].append(building1)

    bridges = find_bridges(graph)

    print("Important streets:")
    for bridge in bridges:
        print(f"{min(bridge)} {max(bridge)}")

main()
