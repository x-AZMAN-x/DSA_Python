class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        print("None", end=" <-> ")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    def display_reverse(self):
        if self.tail is None:
            print("List is empty")
            return
        
        current = self.tail
        print("None", end=" <-> ")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
        print(f"Inserted {data} at the beginning")
    
    def insert_at_end(self, data):
        new_node = Node(data)       
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        print(f"Inserted {data} at the end")
    
    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            print(f"Invalid position! Valid positions: 0 to {self.size}")
            return
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        if position == self.size:
            self.insert_at_end(data)
            return
        
        new_node = Node(data)
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        new_node.prev = current
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node
        
        self.size += 1
        print(f"Inserted {data} at position {position}")
        
    def delete_from_beginning(self):
        if self.head is None:
            print("Cannot delete from empty list")
            return None
        
        deleted_data = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        print(f"Deleted {deleted_data} from the beginning")
        return deleted_data
    
    def delete_from_end(self):
        if self.tail is None:
            print("Cannot delete from empty list")
            return None
        
        deleted_data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        print(f"Deleted {deleted_data} from the end")
        return deleted_data
    
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return None
        
        if position < 0 or position >= self.size:
            print(f"Invalid position! Valid positions: 0 to {self.size - 1}")
            return None
        
        if position == 0:
            return self.delete_from_beginning()
        
        if position == self.size - 1:
            return self.delete_from_end()
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        current.prev.next = current.next
        current.next.prev = current.prev
        
        deleted_data = current.data
        self.size -= 1
        print(f"Deleted {deleted_data} from position {position}")
        return deleted_data
    


if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    print("=== INSERTION OPERATIONS ===\n")
    
    dll.insert_at_beginning(30)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(10)
    print("After insertions at beginning:")
    dll.display()
    print()
    
    dll.insert_at_end(40)
    dll.insert_at_end(50)
    print("After insertions at end:")
    dll.display()
    print()
    
    dll.insert_at_position(25, 2)  # Insert 25 at position 2
    dll.insert_at_position(45, 5)  # Insert 45 at position 5
    print("After insertions at positions:")
    dll.display()
    print("Reverse display:")
    dll.display_reverse()
    print()

    print(f"Current size: {dll.size}\n")
    
    print("=== DELETION OPERATIONS ===\n")
    
    dll.delete_from_beginning()
    print("After deletion from beginning:")
    dll.display()
    print()
    
    dll.delete_from_end()
    print("After deletion from end:")
    dll.display()
    print()
    
    dll.delete_at_position(2)
    print("After deletion at position 2:")
    dll.display()
    print()

    print(f"Final size: {dll.size}")