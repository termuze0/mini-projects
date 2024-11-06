class InfixToPostfixConverter:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # Precedence of operators
        self.stack = []  # Stack to hold operators and parentheses
        self.result = []  # List to store the postfix expression

    def is_operator(self, char):
        return char in {'+', '-', '*', '/', '^'}

    def is_operand(self, char):
        return char.isalnum()  # Operand is a letter or a digit

    def precedence_of(self, operator):
        return self.precedence.get(operator, 0)

    def convert(self, infix):
        for char in infix:
            if self.is_operand(char):
                self.result.append(char)
            elif char == '(':
                self.stack.append(char)
            elif char == ')':
                # Pop from stack to result until we find the matching '('
                while self.stack and self.stack[-1] != '(':
                    self.result.append(self.stack.pop())
                self.stack.pop()  # Pop the '(' from the stack
            elif self.is_operator(char):
                # Pop operators from the stack to result if they have higher or equal precedence
                while (self.stack and self.stack[-1] != '(' and
                       self.precedence_of(self.stack[-1]) >= self.precedence_of(char)):
                    self.result.append(self.stack.pop())
                self.stack.append(char)

        # Pop all remaining operators from the stack
        while self.stack:
            self.result.append(self.stack.pop())

        return ''.join(self.result)

# Example usage
infix_expression = input("Enter an infix expression: ")
converter = InfixToPostfixConverter()
postfix_expression = converter.convert(infix_expression)
print(f"Postfix Expression: {postfix_expression}")
