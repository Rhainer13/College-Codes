# rolino

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head

            while current:
                if current.next is None:
                    current.next = new_node
                    new_node.prev = current
                    return
                
                current = current.next
    def extend(self, list_to_extend):
        current = list_to_extend.head

        while current:
            self.insert_end(current.data)
            current = current.next

    def delete_last_add_first(self):
        last_number = None

        current = self.head

        while current:
            if current.next is None:
                last_number = current.data
            current = current.next

        self.delete_end()
        self.insert_beginning(last_number)

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        
        else:
            self.head = self.head.next
            return

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        
        else:
            current = self.head

            while current:
                if current.next is None:
                    current.prev.next = None
                    return
                current = current.next
    def min(self):
        if self.head is None:
            print("List is empty")
            return
        
        else:
            current = self.head
            smallest_number = current.data

            while current:

                if current.data < smallest_number:
                    smallest_number = current.data
                current = current.next

            print(smallest_number)

    def display(self):
        if self.head is None:
            print("List is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next

        print()

d1 = Doubly()

d1.insert_beginning(2)
d1.insert_beginning(1)
d1.insert_beginning(7)
d1.insert_beginning(10)
d1.insert_beginning(10)
d1.insert_beginning(9)
d1.insert_beginning(7)
d1.insert_beginning(5)
d1.insert_beginning(6)
d1.insert_beginning(10)
print("d1: ", end='')
d1.display()

d2 = Doubly()

d2.insert_beginning(11)
d2.insert_beginning(4)
d2.insert_beginning(2)
d2.insert_beginning(-5)
d2.insert_beginning(1)
print("d2: ", end='')
d2.display()

d1.extend(d2)
print("d1 + d2: ", end='')
d1.display()

print("Smallest number of d1: ", end='')
d1.min()

print("Delete last node, then add it to the first node: ", end='')
d1.delete_last_add_first()
d1.display()
