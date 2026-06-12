class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def printHeightDistant(root, h):
    if root is None:
        return
    if h == 0:
        print(root.data, end= ' ')
    else:
        printHeightDistant(root.right, h - 1)
        printHeightDistant(root.left, h - 1)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    h = int(input("Enter The Value Of The Height: "))
    print(f"Nodes At Distant Of {h}: ")
    print(printHeightDistant(root, h))
    print()

if __name__ == "__main__":
    main()