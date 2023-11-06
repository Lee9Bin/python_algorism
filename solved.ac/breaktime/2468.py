import sys
from collections import deque
def bfs(height,x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while que:
        nowx, nowy = que.popleft()

        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]

            if nextx>= 0 and nexty >= 0 and nextx < n and nexty < n:
                if graph[nextx][nexty] > height and visited[nextx][nexty] == False:
                    visited[nextx][nexty] = True
                    que.append((nextx,nexty))

n = int(sys.stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

maxHeight = 0
for i in graph:
    maxHeight = max(maxHeight, max(i))

ans = 0
for i in range(maxHeight+1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    total = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y] == False and graph[x][y] > i:
                bfs(i,x,y)
                total +=1

    ans = max(ans,total)
print(ans)