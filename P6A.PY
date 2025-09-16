def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return 0


def infix_to_postfix(expression):
    stack = []     
    postfix = ""   
    
    for char in expression:
     
        if char.isalnum():  
            postfix = postfix + char
       
        elif char == '(':
            stack.append(char)
       
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix = postfix + stack.pop()
            stack.pop()  # remove '(' from stack
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix = postfix + stack.pop()
            stack.append(char)
    while stack:
        postfix = postfix + stack.pop()

   
    return postfix

infix = input("Enter an infix expression: ")  
postfix = infix_to_postfix(infix)
print("Postfix expression:", postfix)
