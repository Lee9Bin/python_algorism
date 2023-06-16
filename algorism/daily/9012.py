import sys
n = int(sys.stdin.readline())
ans = []
for i in range(n):
    senten = sys.stdin.readline().rstrip()
    stack =[]
    for i in senten:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) <= 0:
                stack.append(i)
                break
            else:
                stack.pop()
    if len(stack) >0:
        ans.append('NO')
    else:
        ans.append("YES")
for i in ans:
    print(i)