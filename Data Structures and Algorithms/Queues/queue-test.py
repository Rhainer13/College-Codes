# Queue Test
# Name: Mata, Rhainer Matheuz P.
# Date: 12/15/2023

# Problem: Customer Service Queue

# You are tasked with simulating a customer service queue using a linear queue. Each customer service request is represented by customer_id, 
# issue_description, where customer_id is a unique identifier (an integer), and issue_description is a string describing the customer's issue.
# Write a program that implements a linear queue to manage customer service requests. The class should have the following methods:

# Enqueue Request:
# Add a customer service request to the end of the queue.

# Dequeue Request:
# Remove and return the customer service request from the front of the queue.
# If the queue is empty, return None.

# Display Queue Length:
# Return the current length of the queue.

# Display Customer Requests:
# Print the customer service requests in the queue, showing the customer identifiers and issue descriptions

class Node:
    def __init__(self, customer_id, issue_description):
        self.customer_id = customer_id
        self.issue_description = issue_description
        self.next = None

# class for linear queue
class Linear_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # method for inserting a request at the end of a queue
    def enqueue_request(self, customer_id, issue_description):
        node = Node(customer_id, issue_description)
        
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    # method for removing the first/front request in a queue
    def dequeue_request(self):
        if self.front is None:
            return None
        else:
            removed_customer_id = self.front.customer_id
            removed_issue_description = self.front.issue_description

            self.front = self.front.next

            if self.front is None:
                self.rear = None
            
            return f"Customer Id : {removed_customer_id}    Issue Description : {removed_issue_description}"

    # returns the current length of the queue
    def queue_length(self):
        current = self.front
        length = 0

        while current:
            length += 1
            current = current.next
            
        return length

    # method to display the customer id and customer issue of each element in a queue
    def display(self):
        if self.front is None:
            print("\n[Queue is empty]")
        else:
            current = self.front
            
            print("\n--Customer Requests--")
            while current:
                print(f">> Customer Id : {current.customer_id}     Customer Issue : {current.issue_description}")
                current = current.next
            print()

pq = Linear_Queue()

# we are adding and displaying three(3) customer requests
# we also displayed the current number of customer requests
pq.enqueue_request(101, "Phone is broken")
pq.enqueue_request(102, "Computer is broken")
pq.enqueue_request(103, "Console is broken")
pq.display()
print(f"Queue Length : {pq.queue_length()}\n")


# we are removing an issue from the front of the queue one at a time until the queue is empty
print(f"REMOVED : {pq.dequeue_request()}")
pq.display()
print(f"Queue Length : {pq.queue_length()}\n")

print(f"REMOVED : {pq.dequeue_request()}")
pq.display()
print(f"Queue Length : {pq.queue_length()}\n")

print(f"REMOVED : {pq.dequeue_request()}")
pq.display()
print(f"Queue Length : {pq.queue_length()}\n")


# if the queue is already empty and we try to dequeue a request, it simply shows None
print(f"REMOVED : {pq.dequeue_request()}")
pq.display()
print(f"Queue Length : {pq.queue_length()}\n")