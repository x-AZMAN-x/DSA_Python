class Node:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(key, root):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(key, root.left)
        elif key > root.val:
            root.right = insert(key, root.right)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = " ")
        inorder(root.right)

def search(root, key):
    if root is None or root.val == key:
        return root
    
    if root.val < key:
        return search(root.right, key)
    if root.val > key:
        return search(root.left, key)

r = Node(10)
r = insert(5, r)
r = insert(7, r)
r = insert(2, r)
r = insert(3, r)
r = insert(4, r)
r = insert(2, r)

inorder(r)

key = int(input("\nEnter Key To Search: "))
res = search(r, key)
if res:
    print("Key Found:", res.val)
else:
    print("Key Not Found")