class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def has_cycle(self, node, parent, vis):
        vis.add(node)

        for neigh in self.graph[node]:
            if neigh not in vis:
                if self.has_cycle(neigh, node, vis):
                    return True
            elif neigh != parent:
                return True

        return False

    def cycle(self):
        vis = set()

        for node in self.graph:
            if node not in vis:
                if self.has_cycle(node, None, vis):
                    return True

        return False

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("B", "E")
g.add_edge("D", "F")

print("Cycle exists:", g.cycle())