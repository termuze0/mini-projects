def is_operator(op):
    
    return op in ['+', '-', '*', '/']


def evaluate_postfix(expression):
    
    stack = []
    
    expression = expression.split()
    
    for token in expression:
        if not is_operator(token):
            
            stack.append(float(token))
        else:
           
            operand2 = stack.pop()  
            operand1 = stack.pop() 
            
            
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    return "Error: Division by zero"
                stack.append(operand1 / operand2)
    
    return stack[0]


if __name__ == "__main__":
    postfix_expr = "2 3 * 5 4 * + 9 -"  - 9
    result = evaluate_postfix(postfix_expr)
    print(f"Result of '{postfix_expr}' is: {result}")
