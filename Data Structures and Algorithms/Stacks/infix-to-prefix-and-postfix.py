# Name: Rhainer Matheuz P. Mata

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
            # print("stack is empty")
            return None
        
        data_to_return = self.top.data
        self.top = self.top.next
        return data_to_return
    
    def peek(self):
        return None if self.top is None else self.top.data

    def display(self):
        current = self.top
        
        while current:
            print(current.data, end="")
            current = current.next
        print()

    def is_operator(self, character):
        return (character == "+") or (character == "-") or (character == "*") or (character == "/") or (character == "^")
    
    def get_precedence(self, operator):
        if operator == "^":
            return 3
        elif operator == "*" or operator == "/":
            return 2
        elif operator == "+" or operator == "-":
            return 1
        else:
            return 0    
    
    def reverse(self, expression):
        for character in expression:
            if character == "(":
                self.push(")")
            elif character == ")":
                self.push("(")
            else:
                self.push(character)

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

    def infix_to_prefix(self, expression):
        if not(self.is_balance(expression)):
            print("Expression is not balanced")
            return
        else:
            new_expression = self.remove_whitespace(expression)
        
        self.reverse(new_expression)
        
        stack = Stack()
        output = Stack()

        current = self.top
        
        while current:
            incoming_operator = current.data
            
            if self.is_operator(incoming_operator) and stack.top is None:
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and (self.get_precedence(incoming_operator) > stack.get_precedence(stack.peek())):
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and (self.get_precedence(incoming_operator) == stack.get_precedence(stack.peek())):
                stack.push(incoming_operator)
            
            elif self.is_operator(incoming_operator) and (self.get_precedence(incoming_operator) < stack.get_precedence(stack.peek())):
                while self.get_precedence(incoming_operator) < stack.get_precedence(stack.peek()):
                    output.push(stack.pop())
                stack.push(incoming_operator)
            
            elif incoming_operator == "(":
                stack.push(incoming_operator)
            
            elif incoming_operator == ")":
                begin = stack.top

                while begin.data != "(":
                    output.push(stack.pop())
                    begin = begin.next
                stack.pop()
            
            else:
                output.push(incoming_operator)
            
            current = current.next

        if stack.top:
            while stack.top is not None:
                output.push(stack.pop())

        output.display()

    def infix_to_postfix(self, expression):
        if not(self.is_balance(expression)):
            print("Expression is not balanced")
            return
        else:
            new_expression = self.remove_whitespace(expression)

        stack = Stack()
        initial_output = Stack()
        final_output = Stack()
        
        for incoming_operator in new_expression:
            if self.is_operator(incoming_operator) and stack.top is None:
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and self.get_precedence(incoming_operator) > (stack.get_precedence(stack.peek())):
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and self.get_precedence(incoming_operator) == (stack.get_precedence(stack.peek())):
                initial_output.push(stack.pop())
                stack.push(incoming_operator)

            elif self.is_operator(incoming_operator) and self.get_precedence(incoming_operator) < (stack.get_precedence(stack.peek())):
                initial_output.push(stack.pop())

                if self.get_precedence(incoming_operator) == stack.get_precedence(stack.peek()):
                    initial_output.push(stack.pop())
                    stack.push(incoming_operator)

                else:
                    stack.push(incoming_operator)
            
            elif incoming_operator == "(":
                stack.push(incoming_operator)

            elif incoming_operator == ")":
                begin = stack.top

                while begin.data != "(":
                    initial_output.push(stack.pop())
                    begin = begin.next
                stack.pop()

            else:
                initial_output.push(incoming_operator)

        if stack.top is not None:
            while stack.top is not None:
                initial_output.push(stack.pop())

        current = initial_output.top

        while current is not None:
            final_output.push(current.data)
            current = current.next

        # initial_output.display()
        final_output.display()

s = Stack()

# prefix
# expression = "(A+B^C)*D+E^5"      # +*+A^BCD^E5
# expression = "(p+q)*(m-n)"      # *+pq-mn
# expression = "A+B+C*(D-E*F)"      # ++AB*C-D*EF
# expression = "1+(2+3)"            # +1+23
# expression = "A+B*(C+D-E*F)+G"    # ++A*B-+CD*EFG
# expression = "1+2*3+4"            # ++1*234
expression = "a+b*c*(d+e-f)"          # +a**bc-+def

# postfix
# expression = "(A+B^C)*D+E^5"          # ABC^+D*E5^+
# expression = "K + L - M*N + (O^P) * W/U/V * T + Q"          # KL+MN*-OP^W*U/V/T*+Q+
# expression = "A+B+C*(D-E*F)"          # AB+CDEF*-*+
# expression = "a+b*c+d"                # abc*+d+
# expression = "(a+b/c*(d+e)-f)"        # abc/de+*+f-
# expression = "a+(b*c-(d/e-f)*g)*h"    # abc*de/f-g*-h*+

s.infix_to_prefix(expression)
# s.infix_to_postfix(expression)