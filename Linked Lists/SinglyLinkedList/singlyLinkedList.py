class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None #Address Of The Next Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Swap() Will Swap The Given Two Nodes
    def swap(self, n1, n2):
        prevNode1 = None;
        prevNode2 = None;
        node1 = self.head;
        node2 = self.head;
    
        if (self.head == None):
            return;
        
        #If n1 And n2 Are Equal, Then List Will Create The Same
        if (n1 == n2):
            return;
        
        #Pointer: It Is The Memory Address Of A Node
        #Search For node1
        while (node1 != None and node1.data != n1):
            prevNode1 = node1;
            node1 = node1.next;
        
        #Search For node2
        while (node2 != None and node2.data != n1):
            prevNode2 = node2;
            node2 = node2.next;
        
        if(node1 == None and node2 != None):
            #If Previous Node To node1 Is Not None, Then It Will Point To node2
            if(prevNode1 != None):
                prevNode1.next = node2;
            else:
                self.head = node2;
            #If Previous Node To node2 Is Not None, Then It Will Point To node1
            if (prevNode2 != None):
                prevNode2.next = node1;
            else:
                self.head = node1;
            #Swap The Next Nodes Of node1 And node2
            tempo = node1.next;
            node1.next = node2.next;
            node2.next = tempo;
        else:
            print("Swapping is Not Possible!");
    
    def display(self):
        if(self.head == None):
            print("List Is Empty")
        else:
            tempo = self.head
            while tempo:
                print(tempo.data, "--", end = " ")
                tempo = tempo.next

l = SinglyLinkedList()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
l.display()
print()
l.swap(10, 30)
l.display()