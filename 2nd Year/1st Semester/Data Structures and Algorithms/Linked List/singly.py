#Name: Rolino Ongco

#Errors trapped:
    #Using insert_begenning when list is empty.
    #Using insert_end when list is empty.
    #Using insert_before_node when list is empty.
    #Using insert_after_node when list is empty.
    #Using the delete functions when list is empty.
    #Using the delete_given to delete the head node.
    #Using copy_list when list is empty.
    #Using display when list is empty.
    #Passing non-existent node to insert_before_node.
    #Passing non-existent node to insert_after_node.
    #Passing non-existent node to delete_given.
    

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None: #check if list is empty
            self.head = new_node
        else:
            new_node.next = self.head #set new node next as the head
            self.head = new_node #set new node as the head

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None: #check if list is empty
            self.head = new_node
        else:
            current = self.head
            
            #traverse the linked list
            while current.next:
                current = current.next

            current.next = new_node

    def insert_before_node(self, key_value, data):
        new_node = Node(data)
    
        if self.head is None: #Checks if list is empty. If true, throw error.
            print("Key value not found")
            #self.insert_beginning(data)
            return
        
        current = self.head
        pre_current = None
        
        while current.data != key_value:
            pre_current = current
            current = current.next
        
            if current is None: #Checks if the key value is not found. If true, throw error.
                print("Key value not found.")
                return

        if pre_current is None:
            self.insert_beginning(data)
        else:
            pre_current.next = new_node
            new_node.next = current
        
    def insert_after_node(self, key_value, data):
        new_node = Node(data)

        if self.head is None: #Checks if list is empty. If true, throw error.
            print("Key value not found.")
            return
        
        current = self.head
        post_current = current.next

        while current.data != key_value:
            current = post_current
            post_current = post_current.next
            
            if post_current is None: #Checks if the key value is not found. If true, throw error.
                print("Key value not found.")
                return
            
        current.next = new_node
        new_node.next = post_current

    def delete_beginning(self):
        if self.head is None: #Checks if list is empty. If true, throw error.
            print("List is empty.")
            return
        
        self.head = self.head.next

    def delete_end(self):
        if self.head is None: #Checks if list is empty. If true, throw error.
            print("List is empty.")
            return
        
        current = self.head
        pre_current = None

        while current:
            pre_current = current
            current = current.next
            
            if current.next is None:
                pre_current.next = None
                return
            
    def delete_given(self, data_to_delete):
        if self.head is None: #Checks if list is empty. If true, throw error.
            print("List is empty.")
            return
        if data_to_delete == self.head.data: #If data to delete is the head, call delete_beginning function.
            self.delete_beginning()
            return
            
        current = self.head
        post_current = current.next
        pre_current = None

      
        while current.data != data_to_delete:
            pre_current = current
            current = post_current
            post_current = current.next

            if current.data == data_to_delete:
                pre_current.next = post_current

            elif current.next is None:
                print("Data not found.")
                return
                

    def count_list(self):
        current = self.head
        
        count = 0
        while current:
            current = current.next
            count += 1
        
        return count

    def copy_list(self, list_to_copy):
        if list_to_copy.head is None: #Check if list to copy is empty. If true, throw error.
            print("List to copy is empty.")
            return
        
        self.__init__()

        current = list_to_copy.head
        while current:
            
            self.insert_end(current.data)
            current = current.next
        
    def display(self):
        current = self.head

        if self.head is None:
            print("List is empty.", end="")
        else:
            while current:
                print(current.data, end=" ")
                current = current.next
                
        print()

sll = Singly()

sll.display()
sll.insert_before_node("m", "j")
sll.insert_after_node("m", "j")
sll.delete_beginning()
sll.delete_end()
sll.delete_given('d')
print(sll.count_list())
print()

sll.insert_beginning("a")
sll.insert_beginning("b")
sll.insert_beginning("c")
sll.insert_end("g")
sll.display()

sll.insert_before_node("q", "j")

sll.insert_before_node("c", "m")
sll.insert_after_node("m", "r")
sll.insert_before_node("m", "n")
sll.display()

sll.insert_after_node("z", "o")


print(f"The length of the list is: {sll.count_list()}")

sll.delete_given("c")
sll.delete_given("n")
sll.delete_given('p')
sll.display()

print(f"The length of the list is: {sll.count_list()}")
print()

sll2 = Singly()

sll2.copy_list(sll)

sll2.insert_beginning("q")
sll2.insert_beginning("j")

sll2.display()


