# Linked List useful functions cheat sheet

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return (f"Data : {self.data} || Next : {self.next}")

class LinkedList:
    def __init__(self):
        self.head = None

    # linked list traversal
    def print_linked_list(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head
            print("LINKED LIST :", end=" ")
            while current is not None:
                print(current.data,">", end=" ")
                current = current.next

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

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

# deletion methods
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head=self.head.next

    # chatgpt
    def delete_node_by_value(self, value):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == value:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        # If the value is not present in the linked list
        if not current:
            print(f"Node with value {value} not found.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None


    def delete_by_value(self, x):
        if self.head is None:
            print("can't delete LL is empty")
            return
        if x==self.head.data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if x==current.next.data:
                break
            current = current.next
        if current.next is None:
            print("Node is not present!")
        else:
            current.next = current.next.next

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

    # gi add ni bles ug jumao as
    def count_nodes(self):
        current = self.head
        count = 0
        while current != None:
            current = current.next
            count += 1
        print("Count :", count)

LL = LinkedList()

for i in range(0, 3):
    LL.insert_beginning(i)

LL.insert_after(99, 4)

LL.print_linked_list()