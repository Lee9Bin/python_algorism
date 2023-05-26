import sys
from collections import deque

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
cnt = 0
def bfs(x,y):
    que = deque()
    que.append((x,y))
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while que:
        nowx, nowy = que.popleft()
        
        for i in range(4):
            nextx = nowx +dx[i]
            nexty = nowy +dy[i]
            
            if nextx >= 0 and nexty>=0 and nextx<=n-1 and nexty<=m-1:
                if nextx ==0 and nexty == 0:
                    continue
                if graph[nextx][nexty] == 0:
                    graph[nextx][nexty] = graph[nowx][nowy] + 1
                    que.append((nextx,nexty))
bfs(0,0)
for i in graph:
    print(i)
