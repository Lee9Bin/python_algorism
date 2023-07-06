import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
graph = []
visited = [[False for i in range(m)] for i in range(n)]

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    
def bfs(x,y):
        graph[x][y] = 0
        visited[x][y] = True
        que = deque()
        que.append((x,y))
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        while que:
            nowx, nowy = que.popleft()
            for i in range(4):
                nextx = nowx + dx[i]
                nexty = nowy + dy[i]
                
                if nextx >= 0 and nexty >= 0 and nextx <= n-1 and nexty <= m-1:
                    if graph[nextx][nexty] !=0 and visited[nextx][nexty] == False:
                        graph[nextx][nexty] = graph[nowx][nowy] + 1
                        visited[nextx][nexty] = True
                        que.append((nextx,nexty))

# 2인 지점 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x,y = i,j
bfs(x,y)
# 탐색 후 0이 아니고 아직 방문을 못했다는건 갈 수 없다는 것
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] != 0:
            graph[i][j] = -1
for i in graph:
    print(*i)