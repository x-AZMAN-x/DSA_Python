class Queue:
    """
    A Queue Data Structure Implemented Using A Python List.
    Follows The FIFO Principle: First In, First Out.
    """

    def __init__(self):
        self.items = []   # Our Internal List(Like Actual Storage)
    
    def enqueue(self, item):
        self.items.append(item)   # Add Items To The Rear Of The Queue
    
    def dequeue(self):
        # Remove And Return Item From The Front Of The Queue
        if self.isEmpty():
            raise IndexError("Nothing To Dequeue From An Empty Queue!")
        return self.items.pop(0)
    
    def peek(self):
        # Look At The Front Item Without Removing It
        if self.isEmpty():
            raise IndexError("Cannot Peek At An Empty Queue!")
        return self.items[0]
    
    def isEmpty(self):
        # Returns True If The Queue Has No Items
        return len(self.items) == 0
    
    def size(self):
        # Returns How Many Items Are In The Queue
        return len(self.items)
    
    def display(self):
        # Print The Queue
        if self.isEmpty():
            print("Empty Queue")
        return f"FRONT => {self.items} <= REAR"
    
    def __str__(self):
        # Called When You print() The Queue Object Directly
        return f"Queue({self.items})"
    
queue = Queue()

print("...Queuing Up Enemies...")

queue.enqueue("Goblin")
queue.enqueue("Orc")
queue.enqueue("Troll")
queue.enqueue("Dragon")

print(queue.display())

print(f"\nTotal Enemies Queued: {queue.size()}")
print(f"\nNext Enemy To Spawn: {queue.peek()}")

# Simulating Spawning Each Enemy One By One
print("...Spawing Enemies...")
while not queue.isEmpty():
    enemy = queue.dequeue()
    print(f"{enemy} Has Been Spawned!")
    print(queue.display())

print("All Enemies Have Been Spawned!")