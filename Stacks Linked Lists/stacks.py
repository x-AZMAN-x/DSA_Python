class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """Returns True If Stack Is Empty"""
        return self.head is None
    
    def push(self, data):
        """Push An Element Onto The Stack"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def topElement(self):
        """Returns The Top Element WIthout Removing It. Returns None If Stack Is Empty"""
        if self.isEmpty():
            return None
        return self.head.data
    
    def pop(self):
        """Remove And Return The Top Element. Returns None If Stack Is Empty"""
        if self.isEmpty():
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None   # Optional, Helps Garbage Collection
        return popped_node.data

    def display(self):
        """Print All Elements In The Stack(Top To Bottom)"""
        if self.isEmpty():
            print("Stack Is Empty.")
            return
        current = self.head
        print("Stack (Top To Bottom): ", end = " ")
        while current:
            print(current.data, end = "-->" if current.next else "")
            current = current.next
        print()

# Driver Code
stack = Stack()

print("Is The Stack Empty? ", stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("After Pushes: ")
stack.display()

print("\nTop Element: ", stack.topElement())

print("Popped Element: ", stack.pop())
print("After Pop, Top Element: ", stack.topElement())

print("Popped Element: ", stack.pop())
print("After Pop, Top Element: ", stack.topElement())

# Continue Popping Until Empty
print("Popped Element: ", stack.pop())
print("Popped Element: ", stack.pop())
print("Popped Element: ", stack.pop())

# Test Underflow
print("\nAttempt To Pop From An Empty Stack: ", stack.pop())
print("Is The Stack Empty? ", stack.isEmpty())

stack.display()