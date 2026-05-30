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
    def insert(self,data):
        new_node = Node(data)
    
        # If Tree Is Emoty, New Node Becomes The Root
        if self.root is None:
            self.root = new_node
            return
        
        # Use A Queue To Scan Level By Level
        queue = [self.root]

        while queue:
            current = queue.pop[0]          # Take The Front Node

        # Try To Attach The Left Child First
        if current.left is None:
            current.left = new_node
            return
        else:
            queue.append(current.left)

        # Then Try The Right Child
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
        
        queue = self.root
        while queue:
            current = queue.pop(0)
            if current.data == target:          # Target Found
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
    def disply(self):
        if self.root is None:
            print("Tree Is Empty.")
            return
        queue = [self.root]
        level = 1

        while queue:
            level_size = len(queue)
            print(f"Level {level}: ", end= "")