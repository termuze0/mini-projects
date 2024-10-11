def is_operator(op):
    """Check if the character is a valid operator."""
    return op in ['+', '-', '*', '/']


def evaluate_prefix(expression):
    """Evaluate the given prefix expression."""
    stack = []
    
    # Split the expression by space and process it in reverse order
    expression = expression.split()
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        if not is_operator(expression[i]):
            # If operand, push to stack
            stack.append(float(expression[i]))
        else:
            # Operator encountered, pop two operands
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            # Perform the operation
            if expression[i] == '+':
                stack.append(operand1 + operand2)
            elif expression[i] == '-':
                stack.append(operand1 - operand2)
            elif expression[i] == '*':
                stack.append(operand1 * operand2)
            elif expression[i] == '/':
                if operand2 == 0:
                    return "Error: Division by zero"
                stack.append(operand1 / operand2)
    
    # The result should be the only element in the stack
    return stack[0]


# Example Usage
if __name__ == "__main__":
    prefix_expr = "- + * 2 3 * 5 4 9"  # Example: - + (2 * 3) * (5 * 4) 9
    result = evaluate_prefix(prefix_expr)
    print(f"Result of '{prefix_expr}' is: {result}")
