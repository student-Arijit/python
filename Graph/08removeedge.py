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

    def del_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def display(self):
            def to_network():
                temp1 = nx.Graph()

                for node in self.graph:
                    temp1.add_node(node)

                for node in self.graph:
                    for neigh in self.graph[node]:
                        temp1.add_edge(node, neigh)
                return temp1

            temp = to_network()
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

try:
    g.del_edge("B", "E")
    g.del_edge("D", "E")
    g.display()
except ValueError:
    print("The Edge doesn't exist.")
