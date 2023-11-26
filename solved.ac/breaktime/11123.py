import sys
from collections import deque
def bfs(x,y):
    que = deque()
    que.append((x,y))
    graph[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while que:
        nowx, nowy = que.popleft()
        
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            
            if nextx>= 0 and nexty >= 0 and nextx < n and nexty < m:
                if graph[nextx][nexty] == "#":
                    graph[nextx][nexty] = True
                    que.append((nextx,nexty))

T = int(sys.stdin.readline())
result = []
for i in range(T):
    n, m = map(int, sys.stdin.readline().split())

    graph = []

    for k in range(n):
        graph.append(list(map(str, sys.stdin.readline().rstrip())))
    
    cnt = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == "#":
                cnt += 1
                bfs(x,y)
    result.append(cnt)
    
for i in result:
    print(i)