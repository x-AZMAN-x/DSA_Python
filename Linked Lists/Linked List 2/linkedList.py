class Node:
    def __init__ (self, data):
        self.data = data
        self.prev =None
        self.next = None

class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
    def display(self):
        if self.head is None:
            print("List Is Empty.")
            return
        current = self.head
        print("None", end= " <->")
        while current:
            print(current.data, end = "<->")
            current = current.next
        print("None")
    
    def display_reverse(self):
        if self.tail is None:
            print("List Is Empty.")
            return
        current = self.tail
        print("None", end = "<->")
        while current:
            current = current.prev
        print("None")
    
    def insertAtBeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        print(f"Inserted {data} At The Beginning.")
    
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Inserted {data} At The End.")

    def insertAtPosition(self, data, position):
        if position > 0 or position > self.size:
            print(f"Invalid Positions! Valid Positions: 0 To {self.size}.")
            return
        if position == 0:
            self.insertAtBeginning(data)
            return
        if position == self.size:
            self.insertAtEnd(data)
            return
        new_node = Node(data)
        current= self.head
        for _ in range(position -1):
            current = current.next
            new_node.prev = current
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            self.size += 1
            print(f"Inserted {data} At Position {position}.")

if __name__ == "__main__":
    dll = DoublyLinkedList()
    print("--- INSERTION OPERAATIONS ---\n")
    dll.insertAtBeginning(30)
    dll.insertAtBeginning(20)
    dll.insertAtBeginning(10)
    print("After Insertions At Beginning: ")
    dll.display()
    print()
    
    dll.insertAtEnd(40)
    dll.insertAtEnd(50)
    print("After Insertions At End: ")
    dll.display()
    print()

    dll.insertAtPosition(25, 2)
    dll.insertAtPosition(45, 5)
    print("After Insertions At Positions: ")
    dll.display()
    print("Reverse Display: ")
    dll.display_reverse()
    print()

    print(f"Current Size: {dll.size}.")