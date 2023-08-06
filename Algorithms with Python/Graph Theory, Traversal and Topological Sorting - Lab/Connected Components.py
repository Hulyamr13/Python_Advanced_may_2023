class Program:
    graph = []
    visited = []

    @staticmethod
    def main():
        Program.graph = Program.read_graph()
        Program.find_graph_connected_components()

    @staticmethod
    def read_graph():
        n = int(input())
        graph = [[] for _ in range(n)]
        for i in range(n):
            graph[i] = list(map(int, input().split()))
        return graph

    @staticmethod
    def find_graph_connected_components():
        Program.visited = [False] * len(Program.graph)

        for start_node in range(len(Program.graph)):
            if not Program.visited[start_node]:
                print("Connected component:", end=" ")
                Program.dfs(start_node)
                print()

    @staticmethod
    def dfs(vertex):
        if not Program.visited[vertex]:
            Program.visited[vertex] = True
            for child in Program.graph[vertex]:
                Program.dfs(child)

            print(vertex, end=" ")


Program.main()
