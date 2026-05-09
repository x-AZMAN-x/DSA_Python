# Stack class using array/list implementation
class Stack:
    """Array-Based Implementation"""
    # Constructor to initialize the stack
    def __init__(self, capacity = 10):
        # Create an array of fixed size filled with None
        self.items = [None] * capacity
        # 'top' stores the index of the top element
        # -1 means the stack is empty
        self.top = -1 
        # Store the current maximum capacity of the stack
        self.capacity = capacity

    # Function to push/add an element into the stack
    def push(self, value):
        # Check if stack is full
        if self.isfull():
            # Increase stack size if full
            self.resize()
        # Move top pointer one step forward
        self.top += 1
        # Insert the new value at top position
        self.items[self.top] = value

    # Function to remove and return the top element
    def pop(self):
        # Check if stack is empty
        if self.isempty():
            # Raise error if trying to pop from empty stack
            raise IndexError("Stack Underflow: Cannot Pop From An Empty Stack!")
        # Store the top element temporarily
        value = self.items[self.top]
        # Move top pointer one step backward
        self.top -= 1
        # Return removed element
        return value

    # Function to return the top element without removing it
    def peek(self):
        # Check if stack is empty
        if self.isempty():
            # Raise error if no element exists
            raise IndexError("Stack Underflow: There Is No Element Inside The Stack!")
        # Return top element
        return self.items[self.top]

    # Function to check whether stack is empty
    def isempty(self):
        # Stack is empty if top index is -1
        return self.top == -1

    # Function to check whether stack is full
    def isfull(self):
        # Stack is full when top reaches last index
        return self.top == self.capacity - 1

    # Function to return number of elements in stack
    def size(self):
        # Since indexing starts at 0, size is top + 1
        return self.top + 1

    # Function to increase stack capacity dynamically
    def resize(self):
        # Double the current capacity
        self.capacity *= 2
        # Create a new larger array
        new_items = [None] * self.capacity
        # Copy old elements into new array
        for i in range(self.top + 1):
            # Copy each element
            new_items[i] = self.items[i]
        # Replace old array with new resized array
        self.items = new_items

    # Special function to display stack nicely
    def __str__(self):  # Visualising The Stack
        # Return only active elements as a list
        return str([self.items[i] for i in range(self.top + 1)])
    

# Driver Code
# Create a stack object
stack = Stack()

# Print empty stack
print(stack)

# Push elements into stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Print stack after pushes
print("Stack After Pushes: ", stack)

# Show top element
print("Top Element: ", stack.peek())

# Pop top element
print("Popped Elements: ", stack.pop())

# Print updated stack
print(stack)

# Print current size of stack
print("Stack Size: ", stack.size())