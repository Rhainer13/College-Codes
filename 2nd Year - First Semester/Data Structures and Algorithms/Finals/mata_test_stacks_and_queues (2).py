# Name : Mata, Rhainer Matheuz P.
# Date : 1-04-2024

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class Stack_and_Queue:
    def __init__(self):
        self.top = None

        self.front = None
        self.rear = None

    # 1) Inbox (Queue) : all new applications go into a queue, like a line of customers waiting to be served
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
            return None
        
        data_to_return = self.front.name
        self.front = self.front.next

        return data_to_return

    def queue_display(self):
        current = self.front
        print("Queue:")
        while current:
            print(f"> {current.name}")
            current = current.next
        print()

    # 2) Reviewing Stack: When youre ready to review, pull applications from the queue and stack them on your desk. you cann review them in any order, focusing on the ones that seem most promising
    def review_stack(self):
        node = Node(self.dequeue())

        if self.top is None:
            self.top = node
        else:
            node.next = self.top 
            self.top = node

    # 3) Interview Queue: once you shortlist some candidates, move them to a separate queue for interview scheduling
    def interview_queue(self):
        interview.enqueue(applications.pop())

    # 4) Schedule Interviews: take candidates from the interview queue and schedule meetings based on your and their availability. send interview details and reminders.
    def schedule_interview(self):
        schedule.push(interview.dequeue())

    # 5) Hiring Decision: as interviews progress, move promising candidates through the "stack" until you make a final hiring decision
    def hiring_decision(self):
        final.enqueue(schedule.pop())

    def pop(self):
        if self.top is None:
            return None

        data_to_return = self.top.name
        self.top = self.top.next
        return data_to_return
    
    def stack_display(self):
        current = self.top
        print("Stack:")
        while current:
            print(f"> {current.name}")
            current = current.next
        print()
    
applications = Stack_and_Queue()
interview = Stack_and_Queue()
schedule = Stack_and_Queue()
final = Stack_and_Queue()

print("---INBOX---")
applications.enqueue("Aaron")
applications.enqueue("Bob")
applications.enqueue("Charlie")
applications.queue_display()
print()

print("---REVIEW STACK---")
applications.review_stack()
applications.review_stack()
applications.queue_display()
applications.stack_display()
print()

print("---INTERVIEW QUEUE---")
applications.interview_queue()
applications.queue_display()
applications.stack_display()
interview.queue_display()

# print("---SCHEDULE INTERVIEWS---")
# applications.schedule_interview()
# applications.queue_display()
# applications.stack_display()
# schedule.queue_display()

# print("---HIRING DECISION---")
# applications.schedule_interview()
# applications.queue_display()
# applications.stack_display()
# interview.queue_display()