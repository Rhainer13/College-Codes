# Circular Queue
# Name: Mata, Rhainer Matheuz P.
# Date: 12/14/2023

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if self.front is None:
            self.front = node
            self.rear = node
            self.rear.next = self.front
        else:
            self.rear.next = node
            self.rear = node
            self.rear.next = self.front

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

    def display(self):
        if self.is_empty():
            print("\n[Queue is empty]")
        else:
            current = self.front
            
            print("\nQueue    :", end=" ")

            while current:
                print(current.data, end=" ")
                current = current.next
                if current == self.front:
                    break
            print()

    def get_front(self):
        return self.front.data if self.front else None
    
    def get_rear(self):
        return self.rear.data if self.rear else None
    
    def is_empty(self):
        return self.front is None
    
cq = Circular_Queue()

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)

cq.display()
print(cq.get_front())
print(cq.get_rear())

cq.dequeue()

cq.display()
print(cq.get_front())
print(cq.get_rear())