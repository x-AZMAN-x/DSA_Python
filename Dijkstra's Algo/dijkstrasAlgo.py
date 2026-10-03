# Dijkstra's Algorithm: The Shortest Path (No Heap): O(V^2)
import math

e = {
    ("A", "B", 4), ("A", "C", 2), ("B", "C", 1),
    ("B", "D", 5), ("C", "D", 8), ("C", "E", 10),
    ("D", "E", 2), ("D", "E", 6), ("E", "F", 3),
}

graph = {}

for u, v, w in e:
    graph.setdefault(u, []).append((u, w))
    graph.setdefault(v, []).append((u, w))

def dijkstraAlgo(graph, source):
    d = {node: math.inf for node in graph}          # Best Distance So Far
    d[source] = 0
    visited = set()          # Nodes Whose Distance Is Final
    
    for _ in range(len(graph)):
        # Pick The Visited Node With The Smallest Known Distance (An 0(V) Scan)
        cur = None
        for node in graph:
            if node not in visited and (cur is None or d[node] < d[cur]):
                cur = node
        if cur is None or d[cur] == math.inf:
            break          # Everything Left Is Unchangable
        visited.add(cur)

        # Relax Every Edge Leaving It
        for n, w in graph[cur]:
            if d[cur] + w < d[n]:
                d[n] = d[cur] + w
    return d

print(dijkstraAlgo(graph, "A"))