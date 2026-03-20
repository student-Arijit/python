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

    def has_node(self, node):
        return node in self.graph

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("B", "E")
g.add_edge("D", "F")

print(g.has_node("R"))
