import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

numlist = deque()
for i in range(1, n + 1):
    numlist.append(i)
result = []
while numlist:
    for i in range(m):
        if i < m - 1:
            nown = numlist.popleft()
            numlist.append(f"{nown}")
        else:
            result.append(numlist.popleft())
print("<", end="")
print(*result, sep=", ", end="")
print(">")
# 1 2 3 4 5 6 7
