from collections import defaultdict, deque

def main():
    n = int(input())
    graph = read_graph(n)

    p = int(input())
    for _ in range(p):
        path = list(map(int, input().split()))

        if check_path(path, graph):
            print("yes")
        else:
            print("no")

def check_path(path, graph):
    for i in range(len(path) - 1):
        if not has_direct_path(path[i], path[i + 1], graph):
            return False
    return True

def has_direct_path(source, destination, graph):
    queue = deque([source])
    visited = set([source])

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    return False

def read_graph(n):
    graph = defaultdict(list)
    for i in range(n):
        graph[i] = list(map(int, input().split()))

    return graph

if __name__ == "__main__":
    main()
