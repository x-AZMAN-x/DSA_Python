class Graph:
    # Undirected, weighted graph stored as an adjacency list
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def addNode(self, node):
        self.nodes.add(node)

    def addEdges(self, node1, node2 , weight = 1):
        if node2 not in self.nodes:
            self.addNode(node1)
        if node2 not in self.nodes:
            self.addNode(node2)
        if node1 not in self.edges:
            self.edges[node1] = set()
        self.edges[node1].add((node2, weight))
        if node2 not in self.edges:
            self.edges[node2] = set()
        self.edges[node2].add((node1, weight))

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges

    def __repr__(self):
        return f"Graph (Nodes = {self.nodes}), edges = {self.edges}"

if __name__ == "__main__":
    # Driver Code
    g = Graph()

    g.addNode("A")
    g.addNode("B")
    g.addNode("C")

    g.addEdges("A", "B")          # Default Weight = 1
    g.addEdges("A", "C")
    g.addEdges("B", "C")

    print(g)