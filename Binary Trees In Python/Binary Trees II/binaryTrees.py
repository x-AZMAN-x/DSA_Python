# Node Class
# A Node Is One Box In The Tree. It Holds A Value To A Point To A Left And A Right Child.

class Node:
    def __init__(self, data):
        self.data = data          # Value Stored
        self.left = None          # Left Child (Empty At First)
        self.right = None          # Right Child (Empty At First)

# Binary Tree Class
# The Tree Itself, It Only Needs To Remember The Root (Top Node). Every Other Node Is Reachable From The Root.
class BinaryTree:
    def __init__(self):
        self.root = None          # Empty Tree To Start
    
    # Insert
    # Adds A New Value To The Tree
    # Strategy: It Scans Level By Level (Left To Right) And Places The Node In The First Empty Spot Found. This Keeps The Tree Complete And Balanced.
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    # Search
    # Looks For A Specific Value Everywhere In The Tree. Scans Every Node Level By Level Until Found. Returns True If Found, False If Not.
    def search(self, target):
        if self.root is None:
            return False

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.data == target:         # Target Found
                return True

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            return False          # Target Not Found After Checking Every Node
    
    # Delete
    # Removes A Value From The Tree.
    # Strategy: Find The Node To Delete. Find The Deepest Rightmost Node In The Tree. Copy The Deepest Node's Value Into The Target Node. Remove The Deepest Node. This Keeps The Tree Connected Without Restructing it.
    def delete(self, target):
        if self.root is None:
            print("Tree Is Empty.")
            return
        
        # Special Case: Only One Node In The Tree
        if (self.root.left is None and self.root.right is None):
            if self.root.data == target:
                self.root = None
            else:
                print(f"{target} Not Found In The Tree.")
            return

        # Scan Level By Level To Find a) The Node Whose Data Matches Target. b) The Deepest Rightmost Node (Last Node Visited).
        target_node = None
        last_node = None
        last_parent = None
        queue = [self.root]

        while queue:
            last_node = queue.pop(0)
            if last_node.data == target:
                target_node = last_node
            
            if last_node.left:
                last_parent = last_node
                queue.append(last_node.left)

            if last_node.right:
                last_parent = last_node
                queue.append(last_node.right)

        if target_node is None:
            print(f"{target} Not Found In The Tree.")

            # Copy Deepest Node's Value Into The Target's Node
            target_node.data = last_node.data

            # Remove The Deepest Node From Its Parent
            if last_parent:
                if last_parent.right is last_node:
                    last_parent.right = None
                else:
                    last_parent.left = None
            else:
                # The Deepest Node Is The Root (Single Node Edge Case)
                self.root = None

    # Display 
    # Prints The Tree Level By Level So You Can See Its Shape
    def display(self):
        if self.root is None:
            print("Tree Is Empty.")
            return
        queue = [self.root]
        level = 1

        while queue:
            level_size = len(queue)
            print(f"Level {level}: ", end= "")

            for _ in range(level_size):
                node = queue.pop(0)
                print(node.data, end = " ")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()          # A New Line After Each Level
            level += 1
    
    def countNodes(self):
        return self._countNodes(self.root)
    
    def _countNodes(self, node):
        if not node: return 0
        return 1 + self._countNodes(node.left) + self._countNodes(node.right)
    
    def height(self):
        return self._height(self.root)
    def _height(self, node):
        if not node: return -1
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def countLeaves(self):
        return self._countLeaves(self.root)
    def _countLeaves(self, node):
        if not node: return 0
        if not node.left and not node.right: return 1
        return self._countLeaves(node.left) + self._countLeaves(node.right)
    
    def treeSum(self):
        return self._treeSum(self.root)
    def _treeSum(self, node):
        if not node: return 0
        return node.data + self._treeSum(node.left) + self._treeSum(node.right)
    
    def maxElement(self):
        return self._maxElement(self.root)
    def _maxElement(self, node):
        if node is None:
            return float('-inf')
        left_max = self._maxElement(node.left)
        right_max = self._maxElement(node.right)
        return max(node.value, left_max, right_max)
# Demo
if __name__ == "__main__":
    tree = BinaryTree()

    # Insert Values
    print("Inserting: 1, 2, 3, 4, 5, 6, 7")
    for value in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert(value)

    print("\nTree After Inserting: ")
    tree.display()

    # # Search
    # print("\nSearching For 5...")
    # print("\n",tree.search(5))

    # print("\nSearching For 9...")
    # print("\n",tree.search(9))

    # # Delete
    # print("\nDeleting '2'...")
    # tree.delete(2)
    # print("\nTree After Deleting '2':")
    # tree.display()

    # print("\nDeleting '10'...")
    # tree.delete(10)

    for v in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(v)

    print("Height Of The Tree: ",{tree.height()})
    print("Total Count Of The Leaves From The Tree: ",{tree.countLeaves()})
    print("Total Node's Data From The Tree: ",{tree.treeSum()})
    print("Maximum Value Of The Nodes From The Tree: ",{tree.maxElement()})