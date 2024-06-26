# Rhainer Matheuz P. Mata
# BSIT II-1
# sayup ni

# class for node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# class for stack
class Stack:
    # initialize top to none
    def __init__(self):
        self.top = None

    # inserts a node at the top of the stack
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    # returns the top value of the stack and then deletes it
    def pop(self):
        if self.top is None:
            return None
                
        data_to_return = self.top.data
        self.top = self.top.next
        return data_to_return

    # returns the top value of the stack
    def peek(self):
        return None if self.top is None else self.top.data

    # to display the values in a stack
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current = self.top
            print("Stack :", end=" ")
            while current is not None:
                print(current.data,">", end=" ")
                current = current.next

    # method for printing 5 values before the negative value
    def backtrack(self):
        current = self.top
        begin = None
        until = None

        while True:
            if current.next.next.next.next.next is None:
                break
            elif current.next.next.next.next.next.data < 0:
                begin = current
                until = current.next.next.next.next.next
                print()
                while begin:
                    if begin == until:
                        break
                    print(begin.data, end=" ")
                    # print(self.pop())
                    begin = begin.next
                
            current = current.next

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(-1)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
s.push(-2)
s.push(11)
s.push(12)
s.push(-3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.display()
s.backtrack()