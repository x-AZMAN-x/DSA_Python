class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

def printSingleChildNodes(root):
    if root is None:
        return
    if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        print(root.data)

    printSingleChildNodes(root.left)
    printSingleChildNodes(root.right)

if __name__  == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.right.left = Node(7)

    print("Nodes With Single Childs (Preorder): ")
    print(printSingleChildNodes(root))