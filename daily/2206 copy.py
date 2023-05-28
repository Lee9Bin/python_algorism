import sys
from collections import deque
# 3시00분
# 경로탐색인데 벽인 1을 하나 0으로 바꿀수 있다. -> 어떻게 처리할까?

n,m = map(int,sys.stdin.readline().split())
graph = []
result = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

def BFS(x,y):
    que = deque()
    que.append((0,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    graph[0][0] = 1
    graph[x][y] = 0
    
    while que:
        nowx,nowy = que.popleft()
        for i in range(4):
            nextx = dx[i] + nowx
            nexty = dy[i] + nowy
            
            if nextx >= 0 and nexty>=0 and nextx<=n-1 and nexty<=m-1:
                if graph[nextx][nexty] == 0:
                    graph[nextx][nexty] = graph[nowx][nowy] + 1
                    que.append((nextx,nexty))
    if graph[n-1][m-1] !=0:
        result.append(graph[n-1][m-1])

onelist = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            onelist.append((i,j))


if not result:
    print(-1)
else:
    print(min(result))