# Circular Singly
# Name: Rhainer Matheuz P. Mata

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Circular_Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def display_list(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            print("Data :", end=" ")
            while True:
                print(f"{current.data}", end=" ")
                current = current.next
                if current is self.head:
                    break
            print("\n")
            print(f"Head        : {self.head.data}\n"
                  f"Tail        : {self.tail.data}\n"
                  f"Tail Next   : {self.tail.next.data}")

    def insert_begin(self, data=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def insert_before_given_node(self, data=None, find=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        elif self.head.data == find:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        else:
            current = self.head
            while True:
                if current.next.data == find:
                    break
                # sugod ari wako kasabot pero ni gana ang code
                elif current.next == self.head:
                    break
                
                current = current.next
            
            if current.next == self.head:
                print(f"value {find} not found")
            else:
                new_node.next = current.next
                current.next = new_node

    def insert_after_given_node(self, data=None, find=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail =new_node
            self.tail.next = self.head
        elif self.head.data == find:
            new_node.next = self.head.next
            self.head.next = new_node
            # new_node.next = self.head
            # self.head = new_node
            # self.tail.next = self.head
        else:
            current = self.head
            
            while True:
                if current.data == find:
                    break
                elif current.next == self.head:
                    break
                current = current.next
            
            if current.data == find:
                if self.tail.data == find:
                    # mugana rapud ni
                    # self.insert_end(data)

                    self.tail.next = new_node
                    self.tail = new_node
                    self.tail.next = self.head
                else:
                    new_node.next = current.next
                    current.next = new_node    
            elif current.next == self.head:
                print(f"value {find} not found")

    def insert_end(self, data=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node 
            self.tail.next = self.head

    def delete_first_node(self):
        if self.head is None:
            print("List is empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

    def delete_given_node(self, find=None):
        if self.head is None:
            print("List is empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head.data == find:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            current = self.head

            while True:
                if current.next.data == find:
                    break
                elif current.next == self.head:
                    break
                current = current.next

            if current.next.data == find:
                self.tail = current
                self.tail.next = self.head

    def delete_last_node(self):
        if self.head is None:
            print("List is empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while True:
                if current.next.next == self.head:
                    break
                elif current.next == self.head:
                    break
                current = current.next
            
            if current.next.next == self.head:
                self.tail = current
                self.tail.next = self.head
            
cll = Circular_Singly_Linked_List()

cll.insert_end(1)
cll.insert_end(2)
cll.insert_end(3)

# cll.insert_begin(4)
# cll.insert_begin(5)
# cll.insert_begin(6)

# cll.insert_before_given_node(0, 1)
# cll.insert_before_given_node(00, 3)

# cll.insert_after_given_node(99,1)
# cll.insert_after_given_node(999,2)
# cll.insert_after_given_node(999,3)

# cll.delete_first_node()
# cll.delete_first_node()
# cll.delete_first_node()

# cll.delete_last_node()
# cll.delete_last_node()
# cll.delete_last_node()

# cll.delete_given_node(1)
# cll.delete_given_node(2)
# cll.delete_given_node(3)

cll.display_list()