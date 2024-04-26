# Singly
# Name: Rhainer Matheuz P. Mata

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # --methods for inserting nodes--
    # ok
    def insert_before_head_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # ok
    # my code
    def insert_after_head_node(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head.next
            self.head.next = new_node

    # ok
    def insert_before_given_node(self, data, find=None):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        elif self.head.data == find:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head

            while current != None:
                if current.next == None or current.next.data == find:
                    break
                current = current.next
            
            if current.next == None:
                print("Data not in the list")
            else:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node

    # ok
    def insert_after_given_node(self, data, find=None):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        elif self.head.data == find:
            new_node = Node(data)
            self.head.next = new_node
        else:
            current = self.head
            while current != None:
                if current.data == find:
                    break
                current = current.next
            if current == None:
                print("Data not in the list")
            else:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node

    # ok
    # my code
    def insert_before_end_node(self, data=None):
        new_node = Node(data)
        
        if data == None:
            print("No data has been passed")
        elif self.head == None:
            self.head = new_node
        else:
            current = self.head
            previous = None

            while current.next != None:
                previous = current
                current = current.next
            
            new_node.next = current
            previous.next = new_node
        
    # ok
    def insert_after_end_node(self, data=None):
        new_node = Node(data)

        if data == None:
            print("No data has been passed")
        elif self.head == None:
            self.head = new_node
        else:
            current = self.head

            while current.next != None:
                current = current.next

            current.next = new_node

    # --methods for deleting nodes--
    # ok
    def delete_first_node(self):
        if self.head == None:
            print("list is empty")
        else:
            self.head = self.head.next

    # revision
    # my code
    def delete_after_first_node(self):
        if self.head == None:
            print("List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            self.head.next = self.head.next.next

    # def delete
    # revision
    def delete_before_given_node(self, find=None):
        if self.head == None:
            print("List is empty")
        else:
            current = self.head
            previous = None

            while current.next.data != find:
                previous = current
                current = current.next
                
            current.next = current.next.next

    def delete_after_given_node(self, find=None):
        if self.head == None:
            print("list is empty")
        else:
            current = self.head

            while current.data != find:
                current = current.next

            node_to_delete = current.next
            current.next = node_to_delete.next
            del node_to_delete
            
    # revision
    # my code
    def delete_before_last_node(self):
        if self.head == None:
            print("List is empty")
        elif self.head.next == None:
            self.head = None
        elif self.head.next.next == None:
            self.head.next = None
        else:
            current = self.head

            while current.next.next.next != None:
                current = current.next

            current.next = current.next.next

    # ok
    def delete_last_node(self):
        if self.head == None:
            print("List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            current = self.head

            while current.next.next != None:
                current = current.next

            current.next = None

    # ok
    def display_linked_list(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(f"{current.data} >", end=" ")
                current = current.next
            print("end")
            
LL = LinkedList()

LL.insert_before_head_node(1)
LL.insert_before_head_node(2)
LL.insert_before_head_node(3)

LL.delete_after_given_node(2)

# LL.delete_after_first_node()
# LL.delete_after_first_node()
# LL.delete_after_first_node()

LL.display_linked_list()