import sys
from collections import deque

n = int(sys.stdin.readline())
balloons = list(map(int,sys.stdin.readline().split()))

que = deque()
for i in range(1,n+1):
    que.append((balloons[i-1],i))

ans = []

while que:
    nowBalloon, order = que.popleft()
    ans.append(order)
    
    if not que:
        continue
    
    if nowBalloon > 0:
        for i in range(nowBalloon-1):
            ballon = que.popleft()
            que.append(ballon)
    else:
        for i in range(abs(nowBalloon)):
            ballon = que.pop()
            que.appendleft(ballon)
print(*ans)