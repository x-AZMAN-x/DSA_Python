from collections import deque

class Stack:
    def __init__(self):
        # q1 Is The Main Queue(Always Holds Elements In The FIFO Order)
        # q2 Is The Temporary Auxilary Queue
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):   # O(1)
        self.q2.append(x)
    
    def pop(self):   # O(n)
        if not self.q1:
            return
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
            self.q1.popleft()
            self.q1, self.q2 = self.q2, self.q1

    def top(self):   # O(n)
        # Peek At Front Without Removing
        if self.q1:
            return None
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        top = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return top
    
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