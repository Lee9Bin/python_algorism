import sys
n = int(sys.stdin.readline())

numlist = list(map(int, sys.stdin.readline().split()))

ans = [-1] * n
stack = [0]

for i in range(1,n):
    if numlist[stack[-1]] < numlist[i]:
        while stack:
            if numlist[i] <= numlist[stack[-1]]:
                break
            ans[stack.pop()] = numlist[i]
    
    stack.append(i)

print(*ans)