import sys
from collections import deque
a, b = map(str,sys.stdin.readline().split())

que = deque()
que.append((1,a))
result = 0
while que:
    cnt, nownum = que.popleft()
    if nownum == b:
        result = cnt
        break
    for i in (str((int(nownum)*2)),(nownum+"1")):
        if int(i) <= int(b):
            que.append((cnt+1,i))
if result == 0:
    print(-1)
else:
    print(result)