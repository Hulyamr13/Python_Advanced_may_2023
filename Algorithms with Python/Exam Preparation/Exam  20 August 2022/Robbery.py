from heapq import heappop, heappush


class Edge:
    def __init__(self, first, second, distance):
        self.first = first
        self.second = second
        self.distance = distance


def main():
    nodes_count = int(input())
    edges_count = int(input())

    graph = read_graph(nodes_count, edges_count)
    cameras = read_cameras(nodes_count)

    start_node = int(input())
    end_node = int(input())

    distances = [float('inf')] * nodes_count
    queue = []

    distances[start_node] = 0
    heappush(queue, (0, start_node))

    while queue:
        dist, node = heappop(queue)

        if node == end_node:
            break

        for edge in graph[node]:
            child = edge.first if edge.first != node else edge.second

            if cameras[child]:
                continue

            new_distance = distances[node] + edge.distance

            if new_distance < distances[child]:
                distances[child] = new_distance
                heappush(queue, (new_distance, child))

    print(distances[end_node])


def read_cameras(nodes_count):
    result = [False] * nodes_count

    line = input().split()

    for i in range(len(line)):
        black_or_white = line[i][1]

        if black_or_white == 'b':
            result[i] = False
        else:
            result[i] = True

    return result


def read_graph(nodes_count, edges_count):
    result = [[] for _ in range(nodes_count)]

    for _ in range(edges_count):
        edge_data = list(map(int, input().split()))
        first, second, distance = edge_data

        edge = Edge(first, second, distance)

        result[first].append(edge)
        result[second].append(edge)

    return result


if __name__ == "__main__":
    main()
