class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None

    # displays all the data inside the linked list
    # ok
    def display_list(self):
        if self.head is None:
            print("list is empty\n")
        else:
            current = self.head
            print("Data:",end=" ")
            while True:
                if current is None:
                    break
                print(f"{current.data}", end=" ")
                current = current.next
            print("\n")

    # inserts the node at the beginning of the list
    # ok
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # inserts node at the end of the list
    # this function is only used inside the extend() method
    # ok 
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while True:
                if current is None:
                    break
                elif current.next is None:
                    break
                current = current.next
            
            if current.next is None:
                current.next = new_node
                new_node.prev = current

    # this method is only used for the delete_last_add_first() method
    def delete_end(self):
        if self.head is None:
            print("list is empty")
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            if current.next is None:
                current.prev.next = None
                
    # concatenates the current linked list data to another linked list
    # ok
    def extend(self, list=None):
        if list is None:
            print("no list has been passed")
        else:
            current = list.head

            while True:
                if current is None:
                    break
                self.insert_end(current.data)
                current = current.next

    # deletes the last node of the linked list and adds it at the beginning of the list
    # wrong ana si sir, kay ako daw gi himong circular doubly
    def delete_last_add_first(self):
        if self.head is None:
            print("list is empty")
        else:
            current = self.head
            value = 0

            while True:
                if current is None:
                    break
                elif current.next is None:
                    break
                current = current.next
            
             
            if current.next is None:

                # ari dapita sayup
                # current.next = self.head
                # self.head.prev = current
                # current.prev.next = None
                # current.prev = None
                # self.head = current
                
                value = current.data
                self.delete_end()
                self.insert_beginning(value)

    # finds the lowest value in the doubly linked list
    # ok
    def min(self):
        if self.head is None:
            print("list is empty")
        else:
            current = self.head
            lowest_value = current.data

            while current:
                if current is None:
                    break
                elif current.data < lowest_value:
                    lowest_value = current.data
                current = current.next
                
            print(f"Lowest Value : {lowest_value}")

# first doubly linked list
d1 = Doubly()

d1.insert_beginning(2)
d1.insert_beginning(-100)
d1.insert_beginning(7)
d1.insert_beginning(10)
d1.insert_beginning(10)
d1.insert_beginning(9)
d1.insert_beginning(7)
d1.insert_beginning(5)
d1.insert_beginning(6)
d1.insert_beginning(10)

print("\n<< D1 >>")
d1.display_list()

# second doubly linked list
d2 = Doubly()

d2.insert_beginning(11)
d2.insert_beginning(4)
d2.insert_beginning(2)
d2.insert_beginning(5)
d2.insert_beginning(1)

print("<< D2 >>")
d2.display_list()

print("<< Concatenate d1 and d2 >>")
d1.extend(d2)
d1.display_list()

print("<< delete_last_add_first() >>")
d1.delete_last_add_first()
d1.display_list()

print("<< min() >>")
d1.min()

# this is only for spacing
print() 