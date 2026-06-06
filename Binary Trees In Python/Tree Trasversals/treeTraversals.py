class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
    
def inorder(root):
    # (Left, Root, Right)
    if root is None:
        return
    inorder(root.left)
    print(root.data, end = ' ')
    inorder(root.right)

def postorder(root):
    # (Left, Right, Root)
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end = ' ')

def preorder(root):
    # (Root, Left, Right)
    if root is None:
        return
    print(root.data, end = ' ')
    preorder(root.left)
    preorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder: Left -> Root -> Right")
print(inorder(root))
print()

print("Preorder: Root -> Left -> Right")
print(preorder(root))
print()

print("Postorder: Left -> Right -> Root")
print(postorder(root))
print()