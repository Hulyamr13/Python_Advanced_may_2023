def get_salary(node, graph):
    children = graph[node]

    if not children:
        return 1

    salary = 0
    for child in children:
        salary += get_salary(child, graph)

    return salary


def read_graph(n):
    graph = [[] for _ in range(n)]

    for node in range(n):
        sequence = input()
        for i in range(len(sequence)):
            if sequence[i] == 'Y':
                graph[node].append(i)

    return graph


def calculate_salaries():
    n = int(input())
    graph = read_graph(n)

    total_salary = 0

    for node in range(n):
        salary = get_salary(node, graph)
        total_salary += salary

    print(total_salary)


calculate_salaries()