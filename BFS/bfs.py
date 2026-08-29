from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return order

graph = {
    "A": ["B", "C"],
    "B": ["A", "E", "D"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["F", "B"],
    "F": ["E", "C"]
}

print("Graph:", bfs(graph, 'A'))