from collections import deque
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

    def node_count(self):
        return len(self.graph)

    def isconnected(self, start):
        def bfs():
            vis = set()
            q = deque([start])

            while q:
                node = q.popleft()
                vis.add(node)

                for neigh in self.graph[node]:
                    if neigh not in vis:
                        q.append(neigh)
            return len(vis)

        return self.node_count() == bfs()

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("B", "E")
g.add_edge("D", "F")
g.add_edge(0, 1)

print(g.isconnected("A"))
