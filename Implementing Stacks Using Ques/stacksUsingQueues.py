from collections import deque

class Stack:
    def __init__(self):
        # q1 Is The Main Queue(Always Holds Elements In The FIFO Order)
        # q2 Is The Temporary Auxilary Queue
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):   # O(n)
        # Enqueue A New Element Into Empty q2
        self.q2.append(x)
        # Move All Of q1 Into q2
        # New Element Is Now Added To The FRONT Of q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap Names --> q1 Has Now Correct LIFO Order
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):   # O(1)
        # Front Of q1 Is Always The Stack Top - Just Dequeue It
        if self.q1:
            self.q1.popleft()

    def top(self):   # O(1)
        # Peek At Front Without Removing
        if self.q1:
            return self.q1[0]
        return None
    
    def size(self):   # O(1)
        return len(self.q1)
    
    def isEmpty(self):   # O(1)
        return len(self.q1) == 0
    
# Driver Code
if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    print("Current Size:", s.size())
    print("Top Element:", s.top())

    s.pop()
    print("Top Element:", s.top())

    s.pop()
    print("Top Element:", s.top())

    print("Current Size:", s.size())

    print("Is It Empty?", s.isEmpty())