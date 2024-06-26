# Name: Rhainer Matheuz P. Mata
# note: mao niy improved version sa stacks-functions.py tas sagol ang katung prefix og postfix

class Node:
    def __init__(self, data):
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
            return None
        
        data_to_return = self.top.data
        self.top = self.top.next

        return data_to_return
    
    def peek(self):
        return None if self.top is None else self.top.data
    
    def display(self):
        if self.top is None:
            return None
        else:
            current = self.top

            while current:
                print(current.data, end="")
                current = current.next

            print()

    def is_palindrome(self, word):
        for letter in word:
            self.push(letter)

        for letter in word:
            if letter == self.peek():
                self.pop()

        return True if self.top is None else False
    
    def remove_whitespace(self, expression):
        new_expression = ""

        for character in expression:
            if character != " ":
                new_expression += character

        return new_expression
    
    def is_balance(self, expression):
        for character in expression:
            if character == "(" or character == "[" or character == "{":
                self.push(character)

        for character in expression:
            if character == ")" or character == "]" or character == "}":
                if self.peek() == "(" and character == ")" or self.peek() == "[" and character == "]" or self.peek() == "{" and character == "}":
                    self.pop()
                else:
                    return False
        
        return True if self.top is None else False
    
    def reverse(self, expression):
        for character in expression:
            if character == "(":
                self.push(")")
            elif character == ")":
                self.push("(")
            else:
                self.push(character)

    def get_precedence(self, character):
        if character == "^":
            return 3
        elif character == "*" or character == "/":
            return 2
        elif character == "+" or character == "-":
            return 1
        else:
            return 0

    def is_operator(self, character):
        return (character == "+") or (character == "-") or (character == "*") or (character == "/") or (character == "^")

    def infix_to_prefix(self, expression):
        if self.is_balance(expression) is False:
            print("Expression is not balanced")
            return
        else:
            new_expression = self.remove_whitespace(expression)
            # reversed_expression = self.reverse(self.remove_whitespace(expression))
        
        self.reverse(new_expression)

        stack = Stack()
        output = Stack()

        current = self.top

        while current:
            incoming_operator = current.data

            if self.is_operator(incoming_operator) and stack.peek() is None:
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and self.get_precedence(incoming_operator) > stack.get_precedence(stack.peek()):
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and self.get_precedence(incoming_operator) == stack.get_precedence(stack.peek()):
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and self.get_precedence(incoming_operator) < stack.get_precedence(stack.peek()):
                while self.get_precedence(incoming_operator) < stack.get_precedence(stack.peek()):
                    output.push(stack.pop())
                stack.push(incoming_operator)

            elif incoming_operator == "(":
                stack.push(incoming_operator)

            elif incoming_operator == ")":
                stack_current = stack.top

                while stack_current.data != "(":
                    output.push(stack.pop())
                    stack_current = stack_current.next
                stack.pop()

            else:
                output.push(incoming_operator)

            current = current.next

        if stack.top:
            while stack.top is not None:
                output.push(stack.pop())
            
        output.display()

    def infix_to_postfix(self, expression):
        if self.is_balance(expression) is False:
            return "Expression is not balanced"
        
        new_expression = self.remove_whitespace(expression)

        stack = Stack()
        initial_output = Stack()
        final_output = Stack()

        for incoming_operator in new_expression:
            if self.is_operator(incoming_operator) and stack.peek() is None:
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and self.get_precedence(incoming_operator) > stack.get_precedence(stack.peek()):
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and self.get_precedence(incoming_operator) == stack.get_precedence(stack.peek()):
                # while self.get_precedence(incoming_operator) == stack.get_precedence(stack.peek()):
                #     initial_output.push(stack.pop())
                initial_output.push(stack.pop())
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and self.get_precedence(incoming_operator) < stack.get_precedence(stack.peek()):
                while self.get_precedence(incoming_operator) < stack.get_precedence(stack.peek()) or self.get_precedence(incoming_operator) == stack.get_precedence(stack.peek()):    
                    initial_output.push(stack.pop())
                stack.push(incoming_operator)

            elif incoming_operator == "(":
                stack.push(incoming_operator)

            elif incoming_operator == ")":
                stack_current = stack.top

                while stack_current.data != "(":
                    initial_output.push(stack.pop())
                    stack_current = stack_current.next
                stack.pop()

            else:
                initial_output.push(incoming_operator)

        if stack.top:
            while stack.top is not None:
                initial_output.push(stack.pop())

        current = initial_output.top

        while current:
            final_output.push(initial_output.pop())
            current = current.next

        final_output.display()

s = Stack()

# prefix
# expression = "(A+B^C)*D+E^5"      # +*+A^BCD^E5
# expression = "(p+q)*(m-n)"      # *+pq-mn
# expression = "A+B+C*(D-E*F)"      # ++AB*C-D*EF
# expression = "1+(2+3)"            # +1+23
# expression = "A+B*(C+D-E*F)+G"    # ++A*B-+CD*EFG
# expression = "1+2*3+4"            # ++1*234
# expression = "a+b*c*(d+e-f)"          # +a**bc-+def

# postfix
# expression = "(A+B^C)*D+E^5"          # ABC^+D*E5^+
# expression = "K+L-M*N+(O^P)*W/U/V*T+Q"          # KL+MN*-OP^W*U/V/T*+Q+
# expression = "A+B+C*(D-E*F)"          # AB+CDEF*-*+
# expression = "a+b*c+d"                # abc*+d+
# expression = "(a+b/c*(d+e)-f)"        # abc/de+*+f-
# expression = "a+(b*c-(d/e-f)*g)*h"    # abc*de/f-g*-h*+

# s.infix_to_prefix(expression)
# s.infix_to_postfix(expression)

# using the push method
# s.push(1)
# s.push(2)
# s.push(3)
# s.display()

# using the pop method
# print(s.pop())
# s.display()

# using the peek method
# print(s.peek())

# using the is_palindrome() method
# print(s.is_palindrome("civic"))

# using the is_palindrome() method with the remove_whitespace()
# print(s.is_palindrome(s.remove_whitespace("civil")))

# using is_balance()
# expression = "1(2+3)/(5-4)"
# expression = "(())"
# expression = "((][))"
# expression = None

# print(s.is_balance(expression))