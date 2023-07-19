import sys
from collections import deque
t = int(sys.stdin.readline())

for i in range(t):
    visited = [False] * 10000
    a, b = map(int,sys.stdin.readline().split())
    
    que = deque()
    que.append((a,""))
    visited[a] = True
    while que:
        
        nowx, nowc = que.popleft()
        if nowx == b:
            print(nowc)
            break
        for k in ("D","S","L","R"):
            if k == "D":
                nextn = nowx*2 % 10000
                if visited[nextn] == False:
                    visited[nextn] = True
                    que.append((nextn,nowc+"D"))
            if k == "S":
                if nowx == 0:
                    nextn = 9999
                else:
                    nextn = nowx-1
                if visited[nextn] == False:
                    visited[nextn] = True
                    
                    que.append((nextn,nowc+"S"))
            if k == "L":
                nextn = nowx // 1000 + (nowx % 1000)*10
                if visited[nextn] == False:
                    visited[nextn] = True
                    que.append((nextn,nowc+"L"))
            if k == "R":
                nextn = nowx // 10 + (nowx % 10) * 1000
                if visited[nextn] == False:
                    visited[nextn] = True
                    que.append((nextn,nowc+"R"))
