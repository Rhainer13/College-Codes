# Name : Mata, Rhainer Matheuz P.
# Date : 1-10-2024

class Node:
    def __init__(self, name, id):
        self.name = name
        self.id = id 
        self.next = None

class Double_Ended_Queue:
    def __init__(self, max=0):
        self.front = None
        self.rear = None
        self.max = max

    def count(self):
        count = 0

        current = self.front

        while current:
            count += 1
            current = current.next

        return count


    # Enroll Student:
    # Students can enroll in a course by providing their name and student ID.
    # Add the student's details to the rear of the Deque.
    def enqueue_rear(self, name, id):
        node = Node(name, id)

        if self.count() == self.max:
            self.display_status()
            
            print("Course is at max capacity")

            waitlist.enqueue_rear(name, id)
            print("Waitlist : ")
            waitlist.display_status()

        elif self.front is None and self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


    # Withdraw Student:
    # Students can withdraw from the course.
    # Remove the withdrawn student's details from the front of the Deque.
    def dequeue_front(self):
        if self.front is None and self.rear is None:
            return None

        name = self.front.name
        id = self.front.id
        
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        # self.enqueue_rear(waitlist.dequeue_front())

        return (f"Name : {name}         id : {id}")


    # View Enrollment Status:   
    # Instructors can view the current enrollment status without removing any student details.
    # Display the names and IDs of the students currently enrolled.

    # Check Waitlist Status:
    # Instructors can check the current status of the waitlist without removing any student details.
    # Display the names and IDs of the students on the waitlist.
    def display_status(self):
        if self.front is None:
            print("Empty")

        current = self.front

        while current:
            print(f"Name : {current.name}           id : {current.id}")

            current = current.next
        print()


    # Process Enrollment:
    # Process the enrollment by dequeuing students from the rear of the Deque.
    def dequeue_rear(self):
        if self.front is None and self.rear is None:
            return None
        elif self.front == self.rear:
            name = self.rear.name
            id = self.rear.id
            self.front = None
            self.rear = None

            return (f"Name : {name}         id : {id}")
        else:
            current = self.front

            while current.next != self.rear:
                current = current.next

            current.next = None
            self.rear = current

dq = Double_Ended_Queue(3)
waitlist = Double_Ended_Queue(999)

# scenario 1 : using dequeue front
# dq.enqueue_rear("Aron",1)
# dq.enqueue_rear("Brad",2)
# dq.enqueue_rear("Charlie",3)

# dq.dequeue_front()

# dq.display_status()
# waitlist.display_status()


# scenario 2 : using dequeue rear
# dq.enqueue_rear("Aron",1)
# dq.enqueue_rear("Brad",2)
# dq.enqueue_rear("Charlie",3)

# dq.dequeue_rear()

# dq.display_status()
# waitlist.display_status()


# scenario 3 : if course reaches maximum capacity
dq.enqueue_rear("Aron",1)
dq.enqueue_rear("Brad",2)
dq.enqueue_rear("Charlie",3)
dq.enqueue_rear("Don",4)