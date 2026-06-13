class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def traverse(root, tilt):
    if (not root):          # Same As 'if root is None:'
        return 0
    
    left = traverse(root.left, tilt)
    right = traverse(root.right, tilt)

    tilt[0] += abs(left - right)

    return left + right + root.data

def tilt(root):
    tilt = [0]
    traverse(root, tilt)
    return tilt[0]

if __name__ == "__main__":
    root = None
    root = Node(4)
    root.left = Node(2)
    root.right = Node(9)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.right.right = Node(7)

    print("The Tilt Of The Whole Tree Is:", tilt(root))