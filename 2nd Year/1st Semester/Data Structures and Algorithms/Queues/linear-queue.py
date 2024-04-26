# Linear Queue
# Name: Mata, Rhainer Matheuz
# Date: 12/13/2023

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linear_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # inserts a node in the end
    def enqueue(self, data):
        node = Node(data)

        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    # removes the first node
    def dequeue(self):
        if self.front is None:
            # print("Queue is empty")
            return None
        else:
            removed_data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed_data

    def display(self):
        if self.is_empty():
            print("\n[Queue is empty]")
        else:
            current = self.front
            
            print("\nQueue    :", end=" ")

            while current:
                print(current.data, end=" ")
                current = current.next
            print()

    def get_front(self):
        return self.front.data if self.front else None
    
    def get_rear(self):
        return self.rear.data if self.rear else None
    
    def is_empty(self):
        return self.front is None
    
    def reverse(self):
        prev = None
        current = self.front
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.front = prev

        self.display()
            
q = Linear_Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.display()
q.reverse()

# q.display()
# print("Front    :", q.get_front())
# print("Rear     :", q.get_rear())

# print("\nData removed :", q.dequeue(), end="")
# q.display()
# print("Front    :", q.get_front())
# print("Rear     :", q.get_rear())