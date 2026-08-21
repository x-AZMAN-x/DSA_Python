class Graph:          # Graph Class

    def __init__(self):          # Set Nodes And The Edges As Blank
        self.nodes = set()
        self.edges = {}

    def addNodes(self, nodes):          # Adding The Nodes
        self.nodes.add(nodes)

    def addEdge(self, node1, node2, weight):          # Adiing The Edges
        weight = 1
        if node1 not in self.nodes:
            self.node.add(node1)
        if node2 not in self.nodes:
            self.node.add(node2)
        if node1 not in self.edges:
            self.edges[node1] = set()
        self.edges[node1].add((node2, weight))
        if node2 not in self.edges:
            self.edges[node2] = set()
        self.edges[node2].add((node1, weight))

    def getNodes(self):          # Returns The Nodes
        return self.nodes

    def getEdges(self):          # Returns The Edges
        return self.edges

    def __repr__(self):
        return self.edges

    def __repr__(self):
        return str(self.nodes) + " => " + str(self.edges)

# Create A Graph
graph = Graph()

# Add Nodes
graph.addNodes("A")
graph.addNodes("B")
graph.addNodes("C")

# Add Edges
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("B", "C")

# Print The Graph
print(graph)