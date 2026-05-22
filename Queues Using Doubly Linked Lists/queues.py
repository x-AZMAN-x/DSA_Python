# Node Class (Doubly Linked List Node)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Queue Class Using Doubly Linked List
class Queue:
    def __init__(self):
        self.front = None   # Front of Queue
        self.rear = None    # Rear of Queue
        self._size = 0

    def isEmpty(self):
        """Returns True if Queue is Empty"""
        return self.front is None

    def size(self):
        """Returns Number of Elements in Queue"""
        return self._size

    def enqueue(self, data):
        """Insert Element at Rear | O(1)"""
        new_node = Node(data)

        if self.isEmpty():
            # First Element
            self.front = self.rear = new_node
        else:
            # Link Rear <-> New Node
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

        self._size += 1
        print(f"Enqueued: {data}")

    def dequeue(self):
        """Remove Element From Front | O(1)"""
        if self.isEmpty():
            print("Queue Underflow! Queue is Empty.")
            return None

        removed_data = self.front.data

        # Move Front Forward
        self.front = self.front.next

        if self.front is not None:
            self.front.prev = None
        else:
            # Queue Became Empty
            self.rear = None

        self._size -= 1

        print(f"Dequeued: {removed_data}")
        return removed_data

    def peek(self):
        """Return Front Element Without Removing"""
        if self.isEmpty():
            print("Queue is Empty.")
            return None

        return self.front.data

    def display_forward(self):
        """Display Queue From Front to Rear"""
        if self.isEmpty():
            print("Empty Queue")
            return

        current = self.front

        print("Queue [FRONT -> REAR]: ", end="")

        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next

        print()

    def display_backward(self):
        """Display Queue From Rear to Front"""
        if self.isEmpty():
            print("Empty Queue")
            return

        current = self.rear

        print("Queue [REAR -> FRONT]: ", end="")

        while current:
            print(current.data, end=" <-> " if current.prev else "")
            current = current.prev

        print()


# Driver Code
if __name__ == "__main__":

    q = Queue()

    # Enqueue Players
    q.enqueue("PlayerALPHA")
    q.enqueue("PlayerBETA")
    q.enqueue("PlayerGAMMA")
    q.enqueue("PlayerDELTA")

    print()

    q.display_forward()
    q.display_backward()

    print(f"\nQueue Size: {q.size()}")
    print(f"Front Element: {q.peek()}")

    print("\n--- PROCESSING RESPAWN QUEUE ---")

    q.dequeue()
    q.dequeue()

    print()

    q.display_forward()
    q.display_backward()

    print(f"\nIs Queue Empty? {q.isEmpty()}")

    q.dequeue()
    q.dequeue()

    print()

    q.display_forward()

    print(f"\nIs Queue Empty? {q.isEmpty()}")

    # Underflow Test
    q.dequeue()