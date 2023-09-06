import sys
senten = sys.stdin.readline().rstrip()
stack = []
result = []
for i in range(len(senten)):
    if senten[i] not in ("+","-","*","/","(",")"):
        result.append(senten[i])
        
    if senten[i] == "(":
        stack.append(senten[i])
        
    if senten[i] == ")":
        while stack:
            a = stack.pop()
            if a == "(" :
                break
            result.append(a)
    
    if senten[i] == "*" or senten[i] == "/":
        while stack and stack[-1] != "(" and (stack[-1] == "*" or stack[-1] == "/"):
            a = stack.pop()
            result.append(a)
        stack.append(senten[i])
    
    if senten[i] == "+" or senten[i] == "-":
        while stack:
            a = stack.pop()
            if a =="(":
                break
            result.append(a)
        stack.append(senten[i])
while stack:
    result.append(stack.pop())
print(''.join(result))