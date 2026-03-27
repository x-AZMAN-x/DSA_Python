class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        print(f"Inserted {data} At The Beginning.")

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        print(f"Inserted {data} At The End.")

    def insertAfter(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if current == None:
            print(f"Node With Value {prev_data} Not Found.")
            return
        
        newNode = Node(data)
        newNode.next = current.next
        current.next = newNode
        print(f"Inserted Data {data} After {prev_data}.")

    def display(self):
        if self.head is None:
            print(f"List Is Empty.")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" => ".join(elements))

if __name__ == "__main__":
    ll = LinkedList()
    print("--- INSERTIONS ---")
    ll.insertAtEnd(10)
    ll.insertAtEnd(20)
    ll.insertAtEnd(30)
    ll.display()

    ll.insertAtBeginning(5)
    ll.display()

    ll.insertAfter(20, 25)
    ll.display()