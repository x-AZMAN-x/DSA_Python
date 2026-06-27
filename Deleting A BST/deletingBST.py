class Node:
    """Represents A Single Node In The BST"""
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    """BST Implementation Using Insertion, Deletion And Traversals"""
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert A New Value Into The BST"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, root, value):
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self._insert_recursive(root.left, value)
        elif value > root.value:
            if root.right is None:
                root.right = Node(value)
            else:
                self._insert_recursive(root.right, value)
    
    def delete(self, value):
        """Delete A Value From The Given Value From The BST"""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, root, value):
        """Recursive Deletion Helper, Returns (Possibly) A New Root Of The Subtree"""
        if root is None:
            return None
        
        # Search For The Root To Delete
        if value < root.value:
            root.left = self._delete_recursive(root.left, value)
        elif value > root.value:
            root.right = self._delete_recursive(root.right, value)
        else:
            # Node Found --- Handle The Three Cases

            # Case 1 - No Childre(Leaf)
            if root.left is None and root.right is None:
                return None
            
            # Case 2 - One Child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            # Case 3 - Two Children
            # Find The Inorder Succesor
            successor = self._find_min(root.right)
            # Copy Its Value To The Current Root
            root.value = successor.value
            # Delete The Succesor From The Right Subtree
            root.right = self._delete_recursive(root.right, successor.value)

        return root
    
    def _find_min(self, root):
        """Find The Root With The Minimum Value In The Subtree"""
        while root.left is not None:
            root = root.left
        return root
    
    def inorder(self):
        """Returns A List Of Values In Order"""
        res = []
        self._inorder_recursive(self.root, res)
        return res
    
    def _inorder_recursive(self, root, res):
        if root:
            self._inorder_recursive(root.left, res)
            res.append(root.value)
            self._inorder_recursive(root.right, res)

# Demo
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Inserting Values
    values = [50, 30, 20, 40, 70, 60, 80]
    for i in values:
        bst.insert(i)

    print("Initial Binary Search Tree (In Order): ", bst.inorder())

    # Deleting A Leaf Node
    bst.delete(20)
    print("The Binary Search Tree After Deleting 20: ", bst.inorder())

    # Deleting A Root With One Child
    bst.delete(30)
    print("The Binary Search Tree After Deleting 30: ", bst.inorder())

    # Deleting A Root With Two Children
    bst.delete(50)
    print("The Binary Search Tree After Deleting 50: ", bst.inorder())

    # Deleting A Non-Existing Value
    bst.delete(100)
    print("The Binary Search Tree After Attempting To Delete 100: ", bst.inorder())