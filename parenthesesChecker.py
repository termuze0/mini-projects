class Stack:
    def __init__(self):
        self.stacks = []

    def isEmpty(self):
        return len(self.stacks) == 0

    def push(self, data):
        self.stacks.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stacks.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stacks[-1]


def is_balanced(expr):
    
    brackets = {')': '(', '}': '{', ']': '['}
    
    stack = Stack()
    
    for char in expr:
        if char in brackets.values():  
            stack.push(char)
        elif char in brackets.keys():  
            if stack.isEmpty() or stack.pop() != brackets[char]:
                return False
    
    return stack.isEmpty()  


exprs = ["(())", "{[()]}", "{[(])}", "([{}])", "(([]){})", "([]{})", "([)]"]

for expr in exprs:
    if is_balanced(expr):
        print(f"'{expr}' is balanced.")
    else:
        print(f"'{expr}' is NOT balanced.")
