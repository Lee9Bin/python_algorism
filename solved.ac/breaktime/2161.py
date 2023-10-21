import sys
from collections import deque
result = []
n = int(sys.stdin.readline())
numlist = deque()
for i in range(1,n+1):
    numlist.append(i)

while numlist:
    result.append(numlist.popleft())
    if len(numlist) == 0:
        break 
    nowx = numlist.popleft()
    numlist.append(nowx)
    
print(*result)
    