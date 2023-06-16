import sys
from collections import deque
que = deque()
n = int(sys.stdin.readline())

for i in range(1,n+1):
    que.append(i)
    

while len(que) >2:
    que.popleft()
    last = que.popleft()
    que.append(last)
    if len(que) == 2:
        break
print(que[-1])