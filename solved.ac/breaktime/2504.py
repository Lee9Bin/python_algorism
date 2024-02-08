import sys
opers = sys.stdin.readline().rstrip()

stack = []

result = 0
temp = 1
for i in range(len(opers)):

    if opers[i] in ("[", "("):
        stack.append(opers[i])
        if opers[i] == "[":
            temp *= 3
        else:
            temp *= 2
    
    elif opers[i] == ")":
        if not stack or stack[-1] != "(":
            result = 0
            break
        if opers[i-1] == "(":
            result += temp
        stack.pop()
        temp = temp//2

    elif opers[i] == "]":
        if not stack or stack[-1] != "[":
            result = 0
            break
        if opers[i-1] == "[":
            result += temp
        stack.pop()
        temp = temp//3


if stack:
    print(0)
else:
    print(result)