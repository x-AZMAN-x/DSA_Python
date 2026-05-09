# Node class represents a single element in the linked list
class Node:
    # Constructor to initialize the node with data
    def __init__(self, data):
        # Store the value/data in the node
        self.data = data
        # Pointer to the next node, initially None
        self.next = None

# Stack class implementation using linked list
class Stack:
    # Constructor to initialize an empty stack
    def __init__(self):
        # Head points to the top element of the stack
        self.head = None

    # Function to check whether the stack is empty
    def isEmpty(self):
        """Returns True If Stack Is Empty"""
        return self.head is None
    
    # Function to push/add an element onto the stack
    def push(self, data):
        """Push An Element Onto The Stack"""
        # Create a new node with the given data
        new_node = Node(data)
        # New node points to current head
        new_node.next = self.head
        # Move head to the new node
        self.head = new_node

    # Function to return the top element without removing it
    def topElement(self):
        """Returns The Top Element Without Removing It. Returns None If Stack Is Empty"""
        # Check if stack is empty
        if self.isEmpty():
            # Return None if empty
            return None
        # Return the data of the head node
        return self.head.data
    
    # Function to remove and return the top element
    def pop(self):
        """Remove And Return The Top Element. Returns None If Stack Is Empty"""
        # Check if stack is empty
        if self.isEmpty():
            # Return None if stack is empty
            return None
        # Store the current head node temporarily
        popped_node = self.head
        # Move head to the next node
        self.head = self.head.next
        # Disconnect popped node from the list (optional)
        popped_node.next = None
        # Return the data of the removed node
        return popped_node.data

    # Function to display all elements in the stack
    def display(self):
        """Print All Elements In The Stack (Top To Bottom)"""
        # Check if stack is empty
        if self.isEmpty():
            # Print message if empty
            print("Stack Is Empty.")
            # Exit the function
            return
        # Start traversing from the head node
        current = self.head
        # Print heading
        print("Stack (Top To Bottom): ", end=" ")
        # Traverse through the linked list
        while current:
            # Print current node data
            # Print "-->" if next node exists
            print(current.data, end="-->" if current.next else "")
            # Move to next node
            current = current.next
        # Move to next line after printing stack
        print()


# Driver code
# Create an empty stack object
stack = Stack()

# Check if stack is initially empty
print("Is The Stack Empty? ", stack.isEmpty())

# Push elements into the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# Display stack after pushing elements
print("After Pushes: ")
stack.display()

# Show top element
print("\nTop Element: ", stack.topElement())

# Pop top element
print("Popped Element: ", stack.pop())

# Show new top element after pop
print("After Pop, Top Element: ", stack.topElement())

# Pop another element
print("Popped Element: ", stack.pop())

# Show new top element again
print("After Pop, Top Element: ", stack.topElement())

# Continue popping remaining elements
print("Popped Element: ", stack.pop())
print("Popped Element: ", stack.pop())
print("Popped Element: ", stack.pop())

# Try popping from an empty stack (Underflow condition)
print("\nAttempt To Pop From An Empty Stack: ", stack.pop())

# Check whether stack is empty now
print("Is The Stack Empty? ", stack.isEmpty())

# Display Final Stack
stack.display()