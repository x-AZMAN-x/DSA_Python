# Node Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function To Create A New BST Node
def newNode(item):
    node = Node(item)
    node.key = item
    node.left = node.right = None
    return node

# Function To Create A New Node With A Given Key In BST
def insert(node, key):
    # If The Tree Is Empty, Return A New Node
    if node is None:
        return newNode(key)
    
    # Otherwise, Recursion
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    
    # Return The Node Pointer
    return node

# Function To Do Inorder Traversal Of BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end = " ")
        inorder(root.right)
    
# Driver Code
if __name__ == "__main__":
    # The BST
    #            50
    #          /    \
    #         30     70
    #       /   \   /  \
    #      20   40  60  80
    
    root = None

    # Creating The BST In The Terminal
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    # Calling The Function
    inorder(root)