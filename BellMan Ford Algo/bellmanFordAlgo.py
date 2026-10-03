class Graph:

    def __init__ (self, vertices):
        self.V = vertices          # Number Of Vertices
        self.graph = []
    
    # Function To Add An Edge To Graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    # Utility Function Used To Print The Solution
    def printArr(self, d):
        print("Vertex Distance From Source")
        for i in range(self.V):
            print(f"{i}\t\t{d[i]}")
    
    # The Main Function That Finds The Shortest Distance From Source To All Other Vertices Using Bell-Man Ford Algorithm. The Function Also Detects Negative Weight Cycle
    def bellManFord(self, src):
        
        # Initialize Distances From Source To All Other Vertices As Infinite
        d = [float("Inf")] * self.V
        d[src] = 0

        # Relax All Edges [V] - 1 Times. A Simple Shortest Path Source To Any Other Vertex Can Have At Most [V] - 1 Edges
        for _ in range(self.V - 1):
            
            # Update Distance Value And Parent Index Of The Adjacent Vertices Of The Picked Vertex. Consider Only Those Vertices Which Are Still In Queue
            for u, v, w in self.graph:
                if d[u] != float("Inf") and d[u] + w < d[v]:
                    d[v] = d[u] + w
        
        # Check For Negative-Weighted Cycles. The Above Step Gurantees Shortest Distances If Graph Doesn't Contain Negative Weight Cycle. If We Get A Shorter Path, Then There Is A Cycle.
        for u, v, w in self.graph:
            if d[u] != float("Inf") and d[u] + w < d[v]:
                print("Grpah Contains Negative Weight Cycle")
                return
        
        # Print All Distance
        self.printArr(d)

# Demo
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    # Function Call
    g.bellManFord(0)