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

    def bfs(self, start):
        vis = set()
        q = deque([start])

        while q:
            node = q.popleft()

            if node not in vis:
               print(node, end=" ")
               vis.add(node)

               for neigh in self.graph[node]:
                   if neigh not in vis:
                       q.append(neigh)

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("B", "E")
g.add_edge("D", "F")

print("BFS: ")
g.bfs("A")
