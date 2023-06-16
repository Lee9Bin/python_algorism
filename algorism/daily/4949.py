import sys
result= []
while True:
    stack = []
    senten = sys.stdin.readline().rstrip()
    if senten == '.':
        break
    
    for i in senten:
        if i =='(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if len(stack) == 0:
                stack.append(i)
                break
            else:
                if i == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
                        break
                if i == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(i)
    if len(stack)>0:
        print("no")
    else:
        print('yes')