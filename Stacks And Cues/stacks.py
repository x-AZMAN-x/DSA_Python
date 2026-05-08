class Stack:
    """Array-Based Implementation"""
    def __init__(self, capacity = 10):
        self.items = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, value):
        if self.isfull():
            self.resize()
        self.top += 1
        self.items[self.top] = value

    def pop(self):
        if self.isempty():
            raise IndexError("Stack Underflow: Cannot Pop From An Empty Stack!")
        value = self.items[self.top]
        self.top -= 1
        return value
    
    def peek(self):
        if self.isempty():
            raise IndexError("Stack Underflow: There Is No Element Inside The Stack!")
        return self.items[self.top]
    
    def isempty(self):
        return self.top == -1
    
    def isfull(self):
        return self.top == self.capacity - 1
    
    def size(self):
        return self.top + 1
    
    def resize(self):
        self.capacity *= 2
        new_items = [None] * self.capacity
        for i in range(self.top + 1):
            new_items[i] = self.items[i]
            self.items = new_items

    def __str__(self): # Visualising The Stack
        return str([self.items[i] for i in range(self.top + 1)])
    
# Create A Stack
stack = Stack()
print(stack)

# Push Elements
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print("Stack After Pushes: ", stack)

# Peek At Top
print("Top Element: ", stack.peek())

# Pop Elements
print("Popped Elements: ", stack.pop())

print(stack)
print("Stack Size: ", stack.size())