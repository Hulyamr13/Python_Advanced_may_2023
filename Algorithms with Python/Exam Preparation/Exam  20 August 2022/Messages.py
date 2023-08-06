from collections import defaultdict, deque

def main():
    command = input()[7:]
    people = [person for person in command.split() if person]

    command = input()[12:]
    connections = [connection for connection in command.split(',') if connection]

    command = input()[6:]
    startNodes = [node for node in command.split() if node]

    graph = defaultdict(list)
    distances = {}
    queue = deque()
    peopleByDistance = defaultdict(list)

    for person in people:
        graph[person] = []

    for connection in connections:
        start, end = connection.split('-')
        graph[start].append(end)
        graph[end].append(start)

    peopleByDistance[0] = startNodes

    for person in startNodes:
        distances[person] = 0
        queue.append(person)

    max_distance = 0

    while queue:
        current = queue.popleft()

        for child in graph[current]:
            if child not in distances:
                new_distance = distances[current] + 1
                distances[child] = new_distance

                peopleByDistance[new_distance].append(child)
                queue.append(child)

                if new_distance > max_distance:
                    max_distance = new_distance

    non_reachable = sorted(node for node in graph.keys() if node not in distances)

    if non_reachable:
        print("Cannot reach:", ", ".join(sorted(non_reachable)))
    else:
        people_on_last_step = sorted(peopleByDistance[max_distance])
        print(f"All people reached in {max_distance} steps")
        print("People at last step:", ", ".join(people_on_last_step))

if __name__ == "__main__":
    main()
