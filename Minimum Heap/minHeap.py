class MinHeap:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def peek(self):
        if not self.data:
            raise IndexError("Peek From An Empty Heap")
        return self.data[0]

    def push(self, value):
        self.data.append(value)          # Add At The Next Open Leaf
        self._sift_up(len(self.data) - 1)          # Bubble It Up Into Place

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.parent[parent]:          # Child Smaller Than Parent, Then Swap
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break          # Heap Property Satisfied, Now Stop

    def __repr__(self):
        return f"MinHeap({self.data})"

h = MinHeap()
for v in [50, 30, 70, 20, 40, 60, 80]:
    h.push(v)
    print(f"Pushing({v:3}) => {h}")

print("\nPeek():", h.peak())