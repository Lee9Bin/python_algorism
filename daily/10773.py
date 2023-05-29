import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        stack.append(x)
    elif x == 0:
        stack.pop()
print(stack)