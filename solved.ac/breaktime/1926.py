import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

graph = []
visited = [[False for i in range(m)] for i in range(n)]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    nowArea = 1
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while que:
        nowx, nowy = que.popleft()
        
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            
            if nextx >= 0 and nexty >=0 and nextx < n and nexty < m:
                if visited[nextx][nexty] == False and graph[nextx][nexty] != 0:
                    nowArea += 1
                    visited[nextx][nexty] = True
                    graph[nextx][nexty] = graph[nowx][nowy] + 1
                    que.append((nextx,nexty))
    return nowArea
    
cnt = 0
area = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] != 0:
            cnt +=1
            area = max(area,bfs(i,j))
print(cnt)
print(area)