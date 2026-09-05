def dfsIterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()          # Take The Most Rececntly Added Node
        visited.add(node)
        print(node, end=" ")

        for n in reversed(graph[node]):          # Reversed() Keeps Order Identical To The Recursive Version, Since  The Stack Flips The Order Back
            if n not in visited:
                stack.append(n)
    return visited

# Demo
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
    "G": ["C"],
}

dfsIterative(graph, "A")          # Output: A B D E F C G