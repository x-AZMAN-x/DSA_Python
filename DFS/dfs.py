def dfsRecursive(graph, node, visited = None):
    if visited is None:
        visited = set()
    
    visited.add(node)          # Mark This Node As Visited
    print(node, end=" ")          #  Print It

    for n in graph[nodes]:
        if n not in visited:
            dfsRecursive(graph, n, visited)          # Go Deeper
    return visited

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
    "G": ["C"]
}

dfsRecursive(graph, "A")          # Output: A B D E F C G