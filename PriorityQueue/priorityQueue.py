import heapq
import itertools

class PriorityQueue:
    """
    A Stable Property Queue:- A Lower Priority Number - Served First. Uses An Insertion Counter So Ties Break By Arrival Order, And So heapq Never Has To Compare Two Task Objects Directly.
    """
    def __init__(self):
        self._heap = []
        self._counter = itertools.count()

    def push(self, priority, task):
        count = next(self._counter)
        heapq.heappush(self._heap, (priority, count, task))

    def pop(self):
        priority, count, task = heapq.heappop(self._heap)
        return task

    def __len__(self):
        return len(self._heap)

pq = PriorityQueue()
pq.push(3, "Send Weekly Report")
pq.push(1, "Send Production Outrage")
pq.push(2, "Reply To Customer Email")
pq.push(1, "Patch Security Hole")          # Same Priority As An Earlier Task

print("Processing Tasks In Priority Order: ")
while pq:
    print(" -", pq.pop())          # Serving The Element From teh Queue