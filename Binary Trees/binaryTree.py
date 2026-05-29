#   A Single Node: One Value + Two Links
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # Left Child: Smaller Values Live Here
        self.right = None   # Right Child: Larger Values Live Here

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:   # Found An Empty Spot (Land Here)
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node
    
    # Inorder
    def inOrder(self, node, out):
        if node:
            self.inOrder(node.left, out)
            out.append(node.value)
            self.inOrder(node.right, out)
        return out
    
    # Level Order
    def levelOrder(self):
        from collections import deque
        if self.root is None:
            return []
        out, queue = [], deque([self.root])
        while queue:
            node = queue.popleft()   # Taken From The FRONT (FIFO)
            out.append(node.value)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return out
    
# Demo --> Build The Tree And Walk It
tree = BinaryTree()
for v in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(v)

print("In Order: ", tree.inOrder(tree.root, []))   # [20, 30, 40, 50, 60,70, 80]
print("Level Order: ", tree.levelOrder())   # [50, 30, 70, 20, 40, 60, 80]