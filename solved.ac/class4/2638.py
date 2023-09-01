import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph =[]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
ans = 0

def dfs(x,y):
    que = deque()
    que.append((x,y))
    cntvisited = [[0 for i in range(m)] for i in range(n)]
    fire =[]
    visited = [[False for i in range(m)] for i in range(n)]
    while que:
        nowx,nowy = que.popleft()
        
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            
            if nextx >= 0 and nexty >=0 and nextx < n and nexty<m:
                if graph[nextx][nexty] == 0 and visited[nextx][nexty] == False:
                    visited[nextx][nexty] = True
                    que.append((nextx,nexty))
                elif graph[nextx][nexty] == 1 and visited[nextx][nexty] == False:
                    cntvisited[nextx][nexty] += 1
    for i in range(n):
        for j in range(m):
            if cntvisited[i][j] >=2:
                fire.append((i,j))
                
    for a,b in fire:
        graph[a][b] = 0
        
while True:
    cnt = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt +=1
    if cnt == 0:
        break
    ans +=1
    dfs(0,0)
print(ans)