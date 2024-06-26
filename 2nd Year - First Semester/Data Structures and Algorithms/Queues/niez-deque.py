# Niez

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue_front(self, data):
        node = Node(data)
        if self.front is None:
            self.front = node
            self.rear = self.front
        else:
            node.next = self.front
            self.front = node

    def dequeue_front(self):
        if self.front is None:
            print('Queue is Empty')
            return
        self.front = self.front.next

    def enqueue_rear(self, data):
        node = Node(data)
        if self.rear is None:
            self.rear = node
            self.front = self.rear
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def dequeue_rear(self):
        current = self.front
        pre_node = None
        if self.rear is None:
            print('Queue is Empty')
            return
        else:
            while current.next is not None:
                pre_node = current
                current = current.next
            if pre_node is not None:
                pre_node.next = None
                self.rear = pre_node
            else:
                self.front = self.rear = None

    def getfront(self):
        return self.front.data if self.front else None

    def getrear(self):
        return self.rear.data if self.rear else None

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        if self.is_empty() is None:
            print('empty')
            return
        else:
            while current is not None:
                print(current.data, '', end='')
                current = current.next


q = Queue()
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
print('Front: ', q.getfront())
print('Rear: ', q.getrear())
print()
q.dequeue_front()
q.dequeue_rear()
q.display()
print()
print('Front: ', q.getfront())
print('Rear: ', q.getrear())