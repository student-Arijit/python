class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] =[]
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, vis=None):
        if vis is None:
            vis = set()

        if node not in vis:
            print(node, end=" ")
            vis.add(node)

            for neigh in self.graph[node]:
                self.dfs(neigh, vis)

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("B", "E")
g.add_edge("D", "F")

print("DFS:")
g.dfs("A")
