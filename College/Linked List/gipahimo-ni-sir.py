#  copy one linked list to another
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head
            print("LINKED LIST :", end=" ")
            while current is not None:
                print(current.data,">", end=" ")
                current = current.next
            print()

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data==x:
                break
            current = current.next        
        if current.next is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node 

    def insert_after(self,data,x):
        current = self.head
        while current is not None:
            if x==current.data:
                break
            current = current.next
        if current is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    # ok
    def copy_list(self, list=None):
        current = list.head
        self.__init__()
        while True:
            if current is None:
                break
            else:
                self.insert_end(current.data)
            current = current.next

    # ok
    def count_nodes(self):
        current = self.head
        count = 0
        while current != None:
            current = current.next
            count += 1
        print("Count :", count)

# Singly Linked List 1
S1 = Singly_Linked_List()

S1.insert_end(1)
S1.insert_end(2)
S1.insert_end(3)

S1.print_linked_list()

# Singly Linked List 2
S2 = Singly_Linked_List()

S2.print_linked_list()

# copying one singly linked list to another
S2.copy_list(S1)
S2.print_linked_list()

S1.insert_end(4)
S1.insert_end(5)
S1.print_linked_list()

S2.copy_list(S1)
S2.print_linked_list()

# counting
S1.count_nodes()
S2.count_nodes()