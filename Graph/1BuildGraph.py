import networkx as nx
import matplotlib.pyplot as plt

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

        def display(self):
            def to_network(graph):
                temp1 = nx.Graph()

                for node in self.graph:
                    for neigh in self.graph[node]:
                        temp1.add_edge(node, neigh)
                return temp1

            temp = to_network(self.graph)
            nx.draw(temp, with_labels=True)
            plt.show()

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("B", "E")
g.add_edge("D", "F")

g.display()
