# 1) Inbox (Queue) : all new applications go into a queue, like a line of customers waiting to be served

# 2) Reviewing Stack: When youre ready to review, pull applications from the queue and stack them on your desk.
#    you cann review them in any order, focusing on the ones that seem most promising

# 3) Interview Queue: once you shortlist some candidates, move them to a separate queue for interview scheduling

# 4) Schedule Interviews: take candidates from the interview queue and schedule meetings based on your and their availability.
#    send interview details and reminders.

# 5) Hiring Decision: as interviews progress, move promising candidates through the "stack" until you make a final hiring decision

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class Stack_and_Queue:
    def __init__(self):
        self.top = None
        self.front = None
        self.rear = None

    def enqueue(self, name):
        node = Node(name)

        if self.front is None and self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None and self.rear is None:
            print("Empty")
        else:
            name = self.front.name
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            
            return name

    def push(self, name):
        node = Node(name)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        
        name = self.top.name
        self.top = self.top.next

        return name