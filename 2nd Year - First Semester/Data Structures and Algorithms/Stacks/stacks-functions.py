# Name: Rhainer Mata
# note: katu paning introduction

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            # print("stack is empty")
            return None
        
        data_to_return = self.top.data
        self.top = self.top.next
        
        return data_to_return
    
    def peek(self):
        
        # if self.top is None:
        #     return None
        # return self.top.data

        return None if self.top is None else self.top.data

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current = self.top

            while current is not None:
                print(current.data, end="")
                current = current.next
                
    # Shane code
    # def display_stack(self):
    #     if self.top is None:
    #         return print("Empty list")

    #     current = self.top
    #     while current:
    #         print(current.data, end=" ")
    #         current = current.next

    # Noel
    def palindrome(self, word):        
        for letter in word:
            self.push(letter)

        for letter in word:
            if letter == self.peek():
                self.pop()

        return True if self.top is None else False

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
    
    def remove_whitespace(self, expression):
        new_expression = ""

        for character in expression:
            if character != " ":
                new_expression += character

        return new_expression

stack = Stack()

# print(stack.is_balance(stack.remove_whitespace("a+(b+c)")))
# stack.pop()


# print(stack.palindrome("civil"))
# print(f"Topmost value : {stack.peek()}")
# stack.display()



# ka noel ni nga code

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = next

# class Stack:
#     def __init__(self):
#         self.top = None

#     def push(self, data):
#         node = Node(data)
#         node.next = self.top
#         self.top = node

#     def pop(self):
#         if self.top is None:
#             return
        
#         returned_data = self.top.data
#         self.top = self.top.next
#         return returned_data
        
#     def peek(self):
#         return None if self.top is None else self.top.data

#     def is_palindrome(self, str1):
#         for char in str1:
#             self.push(char)

#         for char in str1:
#             if char == self.peek():
#                 self.pop()
            
#         return True if self.top is None else False


#     def display(self):
#         current = self.top

#         if self.top is None:
#             return
        
#         while current is not None:
#             print(current.data, '', end='')
#             current = current.next


# s = Stack()


# print(s.is_palindrome('civil'))
# print('Topmost Value: ',s.peek())
# s.display()