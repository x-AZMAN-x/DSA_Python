"""
Queue Implementation Using Linked Lists - Python
Each Node Holds Data + A Pointer To The Next Node
FRONT Is Where The Elements Leave (Dequeue)
REAR Is Where The Elements Enter (Enqueue)
"""

# Node Class
class Node:
    def __init__(self, data):
        self.data = data   # Value Stored In This Node
        self.next = None   # Pointer To The Next Node

# Queue Class
class Queue:
    def __init__(self):
        self.front = None   # Points To The FRONT Node (Dequeue Here)
        self.rear = None   # Points To The REAR Node (Enqueue Here)
        self._size = 0

    def isEmpty(self):
        """Returns True If The Queue Has No Elements"""
        return self.front is None
    
    def size(self):
        """Returns The Number Of Elements Currently In The Queue"""
        return self._size
    
    def enqueue(self, data):
        """Insert An Element At The Rear Of The Queue | O(1)"""
        new_node = Node(data)   # Create A New Node

        if self.isEmpty():
            # If The Queue Is Empty, FRONT And REAR Both Points To The Next Node
            self.front = new_node
            self.rear = new_node
        else:
            # Link Current Rear To New Node, Then Advance Rear
            self.rear.next = new_node
            self.rear = new_node
        
        self._size += 1   # Increment _size Counter
        print(f"Enqueued Data: {data}")

    def dequeue(self):
        """Remove And Return The FRONT Element | O(1)"""
        if self.isEmpty():
            print("Queue Underflow! Cannot Dequeue From An Empty Queue.")
            return None
        
        removed_data = self.front.data   # Save Front's Data
        self.front = self.front.next   # Move Front Pointer Forward

        if self.front is None:
            # Queue Is Now Empty - Also Resets Rear To None
            self.rear = None
        
        self._size -= 1   # Decrement _size Counter
        print(f"Dequeued {removed_data}")
        return removed_data
    
    def peek(self):
        """Return The Front Element Without Removing It | O(1)"""
        if self.isEmpty():
            print("Queue Is Empty - Nothing To Peek At!")
            return None
        return self.front.data
    
    def display(self):
        """Print All Elements From Front To Rear | O(n)"""
        if self.isEmpty():
            print("Empty Queue")
            return
        
        current = self.front
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Queue [FRONT -> REAR]:", " -> ".join(elements))

# Driver Code
if __name__ == "__main__":
    q = Queue()

    # Enqueue Players Into A Respawn Queue
    q.enqueue("PlayerALPHA")
    q.enqueue("PlayerBETA")
    q.enqueue("PlayerGAMMA")
    q.enqueue("PlayerDELTA")

    q.display()
    print(f"Queue Size: {q.size()}")
    print(f"Top Element In The Queue: {q.peek()}")

    print("\n --- PROCESSING RESPAWN QUEUE ---")
    
    q.dequeue()
    q.dequeue()

    q.display()

    print(f"\n Checking If Queue Is Empty...\n{q.isEmpty()} ")

    q.dequeue()
    q.dequeue()

    q.display()
    
    print(f"\n Checking If Queue Is Empty...\n{q.isEmpty()} ")

    q.dequeue()
    q.dequeue()   # The Queue Is Empty Now

    q.display()

    q.dequeue()   # Since The Queue Is Empty, This Will Trigger The Underflow Message