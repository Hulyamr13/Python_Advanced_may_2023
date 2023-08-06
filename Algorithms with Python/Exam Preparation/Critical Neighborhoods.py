from collections import defaultdict

def dijkstra(graph, start, end):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    previous = {}
    visited = set()

    while graph:
        min_city = min(graph, key=lambda city: distances[city])
        for neighbor, distance in graph[min_city].items():
            if distances[min_city] + distance < distances[neighbor]:
                distances[neighbor] = distances[min_city] + distance
                previous[neighbor] = min_city

        visited.add(min_city)
        graph.pop(min_city)

    path = []
    city = end
    while city != start:
        path.append(city)
        city = previous[city]
    path.append(start)
    path.reverse()
    return path, distances[end]

def main():
    r = int(input())
    graph = defaultdict(dict)

    for _ in range(r):
        road = input().split(" - ")
        city1, city2, distance = road[0], road[1], int(road[2])
        graph[city1][city2] = distance
        graph[city2][city1] = distance

    closed_roads = input().split(",")
    for road in closed_roads:
        city1, city2 = road.split("-")
        if city1 in graph and city2 in graph[city1]:
            del graph[city1][city2]
            del graph[city2][city1]

    start_city = input()
    end_city = input()

    path, total_distance = dijkstra(graph, start_city, end_city)

    print(" - ".join(path))
    print(total_distance)

if __name__ == "__main__":
    main()
