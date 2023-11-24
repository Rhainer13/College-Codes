# my version doubly linked list

class Node:
    def __init__(self, data=None):
        self.previous = None
        self.data = data
        self.next = None
    
class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def display_linked_list(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            print("Data:", end=" ")
            while current is not None:
                print(f"{current.data}", end=" ")
                current = current.next
            print()

    def insert_beginning(self, data=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
    
    def insert_before_given(self, data=None, find=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif self.head.data == find:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        else:
            current = self.head
            while True:
                if current is None:
                    break
                elif current.data == find:
                    break
                current = current.next

            if current is None:
                print(f"value {find} not in the list")
            elif current.data == find:
                new_node.next = current
                new_node.previous = current.previous
                current.previous.next = new_node
                current.previous = new_node

    def insert_after_given(self, data=None, find=None):
        new_node =Node(data)
        if self.head is None:
            self.head = new_node
        # elif self.head.data == find:
        #     self.head.next = new_node
        #     new_node.previous = self.head
        else:
            current = self.head
            while True:
                if current is None:
                    break
                elif current.data == find:
                    break
                current = current.next

            if current is None:
                print(f"value {find} not in the list")
            elif current.data == find:
                new_node.next = current.next
                new_node.previous = current
                if current.next is not None:
                    current.next.previous = new_node
                current.next = new_node

    def insert_end(self, data=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node
            new_node.previous = current

    def delete_first_node(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None

    def delete_given(self, find=None):
        if self.head is None:
            print("list is empty")
        elif self.head.data == find:
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
        else:
            current = self.head
            while True:
                if current.data == find:
                    break
                elif current is None:
                    break
                current = current.next
            
            if current.data == find:
                current.previous.next = current.next
                if current.next is not None:
                    current.next.previous = current.previous
            else:
                print(f"value {find} is not in the list")
                            
    def deleting_last_node(self):
        if self.head is None:
            print("list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while True:
                if current.next.next is None:
                    break
                current = current.next
            
            current.next = None  

dll = Doubly_Linked_List()

dll.insert_beginning(1)
dll.insert_beginning(2)
dll.insert_beginning(3)
dll.insert_beginning(4)
dll.insert_beginning(5)

# dll.insert_before_given(3)
# dll.insert_before_given(8,3)
# dll.insert_before_given(9,1)

# dll.insert_after_given(999999999999,1)
# dll.insert_after_given(2,1)
# dll.insert_after_given(3,2)

# dll.insert_end(4)
# dll.insert_end(5)
# dll.insert_end(6)

# dll.delete_first_node()
# dll.delete_first_node()
# dll.delete_first_node()

dll.delete_given(1)
dll.delete_given(2)
dll.delete_given(3)
dll.delete_given(4)
dll.delete_given(5)

# dll.deleting_last_node()
# dll.deleting_last_node()
# dll.deleting_last_node()

dll.display_linked_list()