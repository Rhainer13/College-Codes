# Niez

class Node:
    def __init__(self, data, priority=None):
        self.data = data
        self.priority = priority
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data, priority):
        node = Node(data, priority)

        if self.rear is None:
            self.front = self.rear = node
            return
        if priority < self.front.priority:
            node.next = self.front
            self.front = node
            return
        elif priority > self.rear.priority:
            self.rear.next = node
            self.rear = node
            return
        else:
            current = self.front
            while current.next and priority > current.next.priority:
                current = current.next
            temp = current.next
            current.next = node
            node.next = temp

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        removed = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return removed

    def get_front(self):
        return self.front.data if self.front else None

    def get_rear(self):
        return self.rear.data if self.rear else None

    def display(self):
        current = self.front

        if self.front is None:
            print("Queue is empty")
        else:
            while current:
                print("Data: ", current.data, "\tPriority: ", current.priority, end="\n")
                current = current.next

q = Queue()
q.enqueue(8, 7)
q.enqueue(5, 1)
q.enqueue(6, 1)
q.enqueue(1, 5)
q.enqueue(9, 6)
q.enqueue(10, 2)
q.display()
print()
print("Front: ", q.get_front())
print("Rear: ", q.get_rear())