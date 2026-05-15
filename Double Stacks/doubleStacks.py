class DoubleStack:
    def __init__(self, capacity):   # Capacity Is The Size Of The Combined Array
        self.capacity = capacity   # Total Size Of The Array
        self.arr = [None] * capacity   # One Array Holding Both Stacks
        self.top1 = -1   # Stack1 Starts Empty From Left
        self.top2 = capacity   # Stack2 Starts Empty From Right

    # Stack1
    def push1(self, item):
        if self.top1 + 1== self.top2:
            raise OverflowError("Double Stack Is Full, You Can't Push Anymore.")
        self.top1 += 1
        self.arr[self.top1] = item

    def pop1(self):
        if self.top1 == -1:
            raise IndexError("Stack Is Empty.")
        item = self.arr[self.top1]
        self.arr[self.top1] = None   # Optional: Clear Reference
        self.top1 -= 1
        return item
    
    def peek1(self):
        if self.top1 == -1:
            return None
        return self.arr[self.top1]
    
    def isEmpty1(self):
        return self.top1 == self.capacity
    
    # Stack 2
    def push2(self, item):
        if self.top1 + 1== self.top2:
            raise OverflowError("Double Stack Is Full.")
        self.top2 -= 1
        self.arr[self.top2] = item

    def pop2(self):
        if self.top2 == self.capacity:
            raise IndexError("Stack 2 Is Empty.")
        item = self.arr[self.top2]
        self.arr[self.top2] = None   # Optional: Clear Reference
        self.top2 += 1
        return item
    
    def peek2(self):
        if self.top2 == self.capacity:
            return None
        return self.arr[self.top2]
    
    def isEmpty2(self):
        return self.top2 == self.capacity
    
    def display(self):
        for i in range(self.capacity):
            print(self.arr[i] if i < self.capacity else "", end= "=>")
        print()

# Driver Code
doubleStack = DoubleStack(6)

doubleStack.display()

doubleStack.push1("1")
doubleStack.push1("2")
doubleStack.push1("3")

doubleStack.display()

doubleStack.push2("a")
doubleStack.push2("b")
doubleStack.push2("c")

doubleStack.display()

doubleStack.pop1()
doubleStack.pop1()
doubleStack.pop1()

doubleStack.display()

doubleStack.pop2()
doubleStack.pop2()
doubleStack.pop2()

doubleStack.display()