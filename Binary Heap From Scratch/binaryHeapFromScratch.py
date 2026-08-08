class BinaryHeapFromScratch:
    """
    A Hand-Built Binary Min-Heap, Stored In A Plain Python List.
    The Key Idea:- A Binary Heap Is A Binary Tree, But Instead Of Storing It With Node Objects And Pointers, We Store It Flat In A List And Use Arithmetic To Find Parent/Child Relationships.
    
    The Only Rule The Heap Enforces:- Every Parent Must Be <= Both Its Children (The "Min-Heap Property"). It Does Not Keep The Whole List Fully Sorted - Only That one Local Store Rule - Which Is Exactly What Makes push/pop O(log n) instead of O(n log n)
    """
    def __init__(self):
        self._heap = []          # List Of (priority, item) Tuples

    def isEmpty(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)

    def push(self, item, priority):
        self._heap.append((priority, item))
        self._siftUp(len(self._heap) - 1)

    def pop(self):
        if not self._heap:
            raise IndexError("Pop From An Emty Priority Queue")
        
        top = self._heap[0]

        # Move From The Last Item To The Root, Then Let It Sink Down To Wherever The Min-Heap Property Says It Belongs.

        last = self._heap.pop()
        if self._heap:
            self._heap[0] = last
            self._siftDown(0)

        return top[1]

    def _siftUp(self, i):
        """
        A Newly pushed Item Might Be Smaller Than It's Parent - Bubble It Up
        """
        while i > 0:
            parent = (i - 1) // 2
            if self._heap[i][0] < self._heap[parent][0]:
                self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
                i = parent
            else:
                break

    def _siftDown(self, i):
        """
        The New Root Might Be Greater Than Its Children - Push It Down
        """
        n = len(self._heap)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i

            if left < n and self._heap[left][0] < self._heap[smallest][0]:
                smallest = left
            if right < n and self._heap[right][0] < self._heap[smallest][0]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]

# Demo
if __name__ == "__main__":
    # Lower Number = Higher Priority - Like An ER: 1 = Critical, 5 = Minor
    tasks = [
        ("Check Vitals", 3)
        ("Gunshot Wound", 1)
        ("Refill Water", 5)
        ("Chest Pain", 1)
        ("Broken Arm", 2)
    ]
for name, cls in [
    ("BinaryHeapFromScratch", BinaryHeapFromScratch)
]:
    print(f"\n--- {name} ---")
    pq = cls()
    for item, priority in tasks:
        pq.push(item, priority)

        # Note:- Two Tasks Share Priority, 1. Only HeapqPriorityQueue Gurantees Insertion Order Is Preserved For Ties (Thanks To The Counter). The Other Two May Break Ties Differently - That's A Real, Common Difference Between Implementation, Not A Bug.
        
        while not pq.isEmpty():
            print(pq.pop())