from heapq import heappush, heappop

class Edge:
    def __init__(self, first, second, time_in_seconds):
        self.first = first
        self.second = second
        self.time_in_seconds = time_in_seconds


def main():
    rooms_count = int(input())
    exit_rooms = list(map(int, input().split()))

    best_exit_time = [0.0 if i in exit_rooms else float('inf') for i in range(rooms_count)]
    rooms_by_exit = {exit_room: set() for exit_room in exit_rooms}

    edges_count = int(input())

    graph = read_graph(rooms_count, edges_count)

    max_time = get_time_in_seconds(input())

    queue = []

    for exit_room in exit_rooms:
        heappush(queue, (0, exit_room))

        for room in range(rooms_count):
            while queue:
                dist, node = heappop(queue)
                rooms_by_exit[exit_room].add(node)

                if node == room:
                    break

                for edge in graph[node]:
                    child = edge.first if edge.second == node else edge.second

                    if child not in rooms_by_exit[exit_room]:
                        heappush(queue, (best_exit_time[child], child))

                    new_distance = best_exit_time[node] + edge.time_in_seconds

                    if new_distance < best_exit_time[child]:
                        best_exit_time[child] = new_distance
                        heappush(queue, (best_exit_time[child], child))

    for room in range(len(best_exit_time)):
        if best_exit_time[room] != 0:
            if best_exit_time[room] == float('inf'):
                print(f"Unreachable {room} (N/A)")
            elif best_exit_time[room] > max_time:
                print(f"Unsafe {room} ({get_time_string_from_seconds(int(best_exit_time[room]))})")
            else:
                print(f"Safe {room} ({get_time_string_from_seconds(int(best_exit_time[room]))})")


def get_time_string_from_seconds(seconds):
    return f"{seconds // 3600:02}:{seconds // 60 % 60:02}:{seconds % 60:02}"


def read_graph(nodes, edges):
    result = [[] for _ in range(nodes)]

    for _ in range(edges):
        edge_data = input().split()
        first = int(edge_data[0])
        second = int(edge_data[1])
        time_in_seconds = get_time_in_seconds(edge_data[2])

        edge = Edge(first, second, time_in_seconds)

        result[first].append(edge)
        result[second].append(edge)

    return result


def get_time_in_seconds(time_string):
    time_data = list(map(int, time_string.split(":")))
    minutes = time_data[0]
    seconds = time_data[1]

    time_in_seconds = minutes * 60 + seconds

    return time_in_seconds


if __name__ == "__main__":
    main()
