# Priority Queue
# Name: Mata, Rhainer Matheuz P.
# Date: 12/14/2023

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class Priority_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # inserts a node in the end
    def enqueue(self, data, priority):
        node = Node(data, priority)

        if self.front is None:
            self.front = node
            self.rear = node
        elif priority < self.front.priority:
            node.next = self.front
            self.front = node
        elif priority > self.rear.priority:
            self.rear.next = node
            self.rear = node
        else:
            current = self.front

            while current and priority >= current.next.priority:
                current = current.next

            node.next = current.next
            current.next = node
            
    # removes the first node
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
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
            
            print()
            while current:
                print(f"Data : {current.data}\tPriority : {current.priority}")
                current = current.next
            print()

    def get_front(self):
        return self.front.data if self.front else None
    
    def get_rear(self):
        return self.rear.data if self.rear else None
    
    def is_empty(self):
        return self.front is None
    
pq = Priority_Queue()

# pq.enqueue(8, 7)
# pq.enqueue(5, 1)
# pq.enqueue(6, 1)
# pq.enqueue(1, 5)
# pq.enqueue(9, 6)
# pq.enqueue(10, 2)

pq.enqueue(1,1)
pq.enqueue(2,2)
pq.enqueue(3,4)
pq.enqueue(4,5)

pq.enqueue(2,4)

pq.display()

print(f"Front   : {pq.get_front()}")
print(f"Rear    : {pq.get_rear()}")