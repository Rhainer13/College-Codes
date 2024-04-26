# Mata, Rhainer Matheuz P.
# BSIT II-1
# Test on Stack 
# Score 30/35

# class for Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class for Stack
class Stack:
    def __init__(self):
        self.top = None

    # inserts a new node at the top of the stack
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    # returns the top data and deletes it after
    def pop(self):
        data_to_return = self.top.data
        self.top = self.top.next
        return data_to_return
    
    # shows the top value of the stack
    def peek(self):
        return None if self.top is None else self.top.data
    
    # used to display all the nodes in a stack
    def display(self):
        current = self.top
        print(f"Stack :",end=" ")
        while current:
            print(f"{current.data} >",end=" ")
            current = current.next
        print()

    # note: Dont use lists mao gisulti ni sir
        
    # method for checking if an expression is balanced or not
    # def is_balanced(self, expression=None):
    #     # this is only used for storing braces to be compared
    #     open = ["(","[","{"]
    #     close = [")","]","}"]

    #     stack = Stack()

    #     if expression is None:
    #         return False
    #     else:
    #         # the first for loop is to push all the opening braces into the stack
    #         for character in expression:
    #             if character in open:
    #                 stack.push(character)

    #         # the second for loop is for checking for brace pairs and if there is then pop the brace in the stack
    #         for character in expression:
    #             if character in close:
    #                 if character and stack.peek():
    #                     stack.pop()
    #                 elif stack.top is None:
    #                     return False

    #     # if the stack is empty return True which means the expression is balanced otherwise return false which means the expression is not balanced
    #     return True if stack.top is None else False


    # kani sakto na function
    def is_balance(self, expression):
        for character in expression:
            if character == "(" or character == "{" or character == "[":
                self.push(character)
            
        for character in expression:
            if character == ")" or character == "}" or character == "]":
                if self.peek() == "(" and character == ")" or self.peek() == "{" and character == "}" or self.peek() == "[" and character == "]":
                    self.pop()
            
                else:
                    return False
        
        return False if self.top else True

s = Stack()

# sample expressions
expression = "1(2+3)/(5-4)"
# expression = "((]))"
# expression = "((][))"
# expression = None

print(f"\nIs the expression {expression} balanced ?"
      f"\nAnswer : {s.is_balance(expression)}\n")


# Name: Rolino Ongco
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# class Stack:
#     def __init__(self):
#         self.top = None

#     def push(self, data):
#         node = Node(data)

#         node.next = self.top
#         self.top  = node

#     def pop(self):
#         if self.top is None:
#             return 

#         value = self.top.data
#         self.top = self.top.next
#         return value

#     def peek(self):
#         return self.top.data if self.top else None
    
#     def is_balance(self, expression):
#         #loop to check for the (, [, and { characters
#         for i in expression:

#             #if i is one of these three
#             if i == '(' or i == '[' or i == '{': 
                
#                 #we push i to the stack
#                 self.push(i)        

#         #loop to check for the ), ], and } character
#         for i in expression:
            
#             #we check to see if i is one these three characters
#             if i == ')' or i == ']' or i == '}': 

#                 #we then check to see if the top character of the stack is a pair to i
#                 if self.peek() == '(' and i == ')' or self.peek() == '[' and i == ']' or self.peek() == '{' and i == '}':

#                     #if true, we the program then performs the pop() function
#                     self.pop()   

#                 #if the top character is not a pair to the i, we then return False. Meaning 
#                 #the expression is unbalanced.       
#                 else:
#                     return False    

#         #return false if stack is not empty, meaning the expression is unbalance, else true
#         return False if self.top else True
        
#     def display(self):
#         if self.top is None:
#             return
        
#         current = self.top
#         while current:
#             print(current.data, end=' ')
#             current = current.next

#         print()
    
# s = Stack()
# print(s.is_balance('(())'))


# Name: Sean Anino
# def is_balance(self, str1):
#         for i in str1:
#             if i == '(' or i == '[' or i == '{':
#                 self.push(i)
#             elif i == ')' or i == ']' or i == '}':
#                 if self.peek() is None:
#                     return False
#                 data = self.pop()
#                 if (i == ')' and data != '(') or (i==']' and data != '[') or (i=='}' and data!='{'):
#                     return False  
#         return self.top is None