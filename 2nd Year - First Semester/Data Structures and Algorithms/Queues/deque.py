# Deque or Double Ended Queue
# Name: Mata, Rhainer Matheuz
# Date: 12/14/2023

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue_front(self, data):
        node = Node(data)

        if self.front is None:
            self.front = node
            self.rear = node
        else:
            node.next = self.front
            self.front = node

    def dequeue_front(self):
        if self.front is None:
            print("Queue is empty")
        else:
            removed_data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed_data

    def enqueue_rear(self, data):
        node = Node(data)

        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue_rear(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front == self.rear:
            removed_data = self.rear.data
            self.front = None
            self.rear = None

            return removed_data
        else:
            current = self.front
            
            while current.next != self.rear:
                current = current.next

            removed_data = self.rear.data
            current.next = None
            self.rear = current
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
    
q = Deque()
q.enqueue_front(5)
q.enqueue_front(2)
q.enqueue_front(3)
#q.enqueue_front(1)
#q.enqueue_front(0)
q.enqueue_rear(6)
q.enqueue_rear(7)
q.enqueue_rear(8)
q.display()
print()
print('Front: ', q.get_front())
print('Rear: ', q.get_rear())
print()
q.dequeue_front()
q.dequeue_rear()
q.display()
print()
print('Front: ', q.get_front())
print('Rear: ', q.get_rear())