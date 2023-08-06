from collections import defaultdict, deque

visited_nodes = set()
sorted_nodes = deque()
cycle_nodes = set()
end_cycles = set()
is_cycle = False

graph = defaultdict(list)
# graph = {
#     0: [3],
#     1: [0],
#     2: [1, 3],
#     3: [1],
#     4: [],
# }

def main():
    read_graph()
    sorted_sticks = top_sort()

    if is_cycle:
        print("Cannot lift all sticks")
        for item in sorted_sticks:
            if item not in end_cycles:
                print(item, end=" ")
    else:
        print(' '.join(str(x) for x in sorted_sticks))

def read_graph():
    sticks = int(input())
    placings = int(input())

    for i in range(sticks):
        graph[i] = []

    for i in range(placings):
        tokens = list(map(int, input().split()))
        graph[tokens[0]].append(tokens[1])

def top_sort():
    global visited_nodes, sorted_nodes, cycle_nodes, is_cycle

    visited_nodes = set()
    sorted_nodes = deque()
    cycle_nodes = set()
    is_cycle = False

    for node in graph.keys():
        top_sort_dfs(node)

    return list(sorted_nodes)

def top_sort_dfs(node):
    global visited_nodes, sorted_nodes, cycle_nodes, is_cycle, end_cycles

    if node in cycle_nodes:
        is_cycle = True
        end_cycles.update(cycle_nodes)

    if node not in visited_nodes:
        visited_nodes.add(node)
        cycle_nodes.add(node)

        for child in graph[node]:
            top_sort_dfs(child)

        cycle_nodes.remove(node)
        sorted_nodes.appendleft(node)

if __name__ == "__main__":
    main()
