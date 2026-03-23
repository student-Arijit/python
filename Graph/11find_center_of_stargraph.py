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

    def degree(self, node):
        return len(self.graph[node])
        
    def findcenter(self, start):
        for node in self.graph:
        	if self.degree(node) == self.node_count():
        		return node

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("A", "E")
g.add_edge("A", "F")

print(g.findcenter("A"))