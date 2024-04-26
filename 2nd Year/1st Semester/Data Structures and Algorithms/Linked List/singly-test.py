# Name: Rhainer Matheuz P. Mata
# Grade and Section: BSIT II-1

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None
    
    # inserts a node at the beginning of the list
    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # inserts a node before a given node
    def insert_before_given(self, data=None, find=None):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        elif self.head.data == find:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head

            while current:
                if current.data == find:
                    break
                current = current.next

            if current == None:
                print("data not found")
            else:
                new_node.next = current.next
                current.next = new_node

    # counts the number of duplicate data in the linked list  
    def count_duplicate(self):
        current = self.head

        # problem starts here
        # inside_current = Singly_Linked_List() 
        inside_current = self.head
        
        # --this code works--
        # while current:
        #     inside_current.insert_first(current.data)
        #     current = current.next

        duplicate = 0

        while current:
            while inside_current:
                if current.data == inside_current.data:
                    duplicate += 1
                inside_current = inside_current.next
            current = current.next  
        
        print(f"Duplicate : {duplicate}")

    # rolino code
    def count_duplicate_rolino(self): #work in progress
        current1 = self.head
        current2 = self.head
        duplicate_num_count = 0
        duplicated_numbers = []

        while current1:  
            current_number = current1.data
            count = 0

            while current2:
                if current_number in duplicated_numbers:
                    break
                if current_number == current2.data:
                    count += 1 
                current2 = current2.next 

            if count > 1:
                    duplicate_num_count += 1
                    duplicated_numbers.append(current_number)
            current1 = current1.next
            current2 = self.head 

        return duplicate_num_count

    # counts the total node in the linked list
    def count_size(self):
        current = self.head
        count = 0
        while current:
            if current == None:
                break
            count += 1
            current = current.next

        print(f"Count : {count}")

    # displays the data in each node
    def display_linked_list(self):
        current = self.head

        print("Data:", end=" ")
        while current:
            if current == None:
                break
            print(f"{current.data}", end=" ")
            current = current.next
        print()

s1 = Singly_Linked_List()

s1.insert_first(8)
s1.insert_first(10)
s1.insert_first(7)
s1.insert_first(1)
s1.insert_first(1)
s1.insert_first(1)
s1.insert_first(4)
s1.insert_first(4)
s1.insert_first(2)
s1.insert_first(10)

s1.display_linked_list()
s1.count_size()
print(s1.count_duplicate_rolino())

print()

s1.insert_before_given(7, 10)

s1.display_linked_list()
s1.count_size()
print(s1.count_duplicate_rolino())
