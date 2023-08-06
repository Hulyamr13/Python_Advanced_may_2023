def main():
    nodes_count = int(input())
    separated_parts = int(input())

    graph = read_graph(nodes_count)

    depths = [0] * nodes_count
    lowpoint = [0] * nodes_count
    parent = [-1] * nodes_count
    visited = [False] * nodes_count

    articulation_points = []

    def find_articulation_point(node, depth):
        nonlocal visited
        nonlocal lowpoint
        nonlocal depths
        nonlocal parent
        nonlocal articulation_points

        visited[node] = True
        lowpoint[node] = depth
        depths[node] = depth

        child_count = 0
        is_articulation_point = False

        for child in graph[node]:
            if not visited[child]:
                parent[child] = node
                find_articulation_point(child, depth + 1)
                child_count += 1

                if lowpoint[child] >= depth:
                    is_articulation_point = True

                lowpoint[node] = min(lowpoint[node], lowpoint[child])
            elif parent[node] != child:
                lowpoint[node] = min(lowpoint[node], depths[child])

        if (parent[node] == -1 and child_count > 1) or (parent[node] != -1 and is_articulation_point):
            articulation_points.append(node)

    for node in range(len(graph)):
        if not visited[node]:
            find_articulation_point(node, 1)

    result_found = False

    def remove_articulation_point(articulation_point):
        result = [[] for _ in range(len(graph))]

        for i in range(len(graph)):
            if i != articulation_point:
                for node in graph[i]:
                    if node != articulation_point:
                        result[i].append(node)

        return result

    def topological_sorting():
        result = []
        visited = [False] * len(graph)

        def dfs(node):
            nonlocal visited
            nonlocal result

            if visited[node]:
                return

            visited[node] = True

            for child in graph[node]:
                dfs(child)

            result.append(node)

        for node in range(len(graph)):
            dfs(node)

        return result

    for articulation_point in articulation_points:
        new_graph = remove_articulation_point(articulation_point)
        sorted_nodes = topological_sorting()
        visited = [False] * nodes_count
        components = 0

        while sorted_nodes:
            node = sorted_nodes.pop()

            if visited[node]:
                continue

            component = []

            def dfs(node):
                nonlocal visited
                nonlocal component

                if visited[node]:
                    return

                visited[node] = True
                component.append(node)

                for child in new_graph[node]:
                    dfs(child)

            dfs(node)
            components += 1

        if components - 1 == separated_parts:
            result_found = True
            print(articulation_point + 1)

    if not result_found:
        print(0)


def read_graph(nodes_count):
    result = [[] for _ in range(nodes_count)]

    for i in range(1, nodes_count + 1):
        first = i - 1
        parts = list(map(int, input().split()))

        for j in range(len(parts)):
            second = parts[j] - 1

            result[first].append(second)
            result[second].append(first)

    return result


if __name__ == "__main__":
    main()
