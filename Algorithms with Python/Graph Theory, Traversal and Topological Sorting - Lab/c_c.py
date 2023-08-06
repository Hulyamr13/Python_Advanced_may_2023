def read_graph():
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, input().split()))
    return graph


def find_graph_connected_components(graph):
    visited = [False] * len(graph)

    for start_node in range(len(graph)):
        if not visited[start_node]:
            print("Connected component:", end=" ")
            dfs(graph, start_node, visited)
            print()


def dfs(graph, vertex, visited):
    if not visited[vertex]:
        visited[vertex] = True
        for child in graph[vertex]:
            dfs(graph, child, visited)

        print(vertex, end=" ")


graph = read_graph()
find_graph_connected_components(graph)
