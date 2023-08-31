import sys
from collections import deque
# 다시 풀어보기

n,m = map(int,sys.stdin.readline().split())
graph = []
visited = [[[0 for i in range(2)] for i in range(m)] for i in range(n)]

for i in range(n):
    graph.append(list((sys.stdin.readline().rstrip())))

def BFS(x,y):
    global result
    que = deque()
    que.append((x,y,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    graph[x][y] = 1
    visited[x][y][0] = 1
    
    while que:
        nowx,nowy,block = que.popleft()
        if nowx == n-1 and nowy == m-1:
            return visited[nowx][nowy][block]
        for i in range(4):
            nextx = dx[i] + nowx
            nexty = dy[i] + nowy
            
            if nextx >= 0 and nexty>=0 and nextx<=n-1 and nexty<=m-1:
                if graph[nextx][nexty] == '1' and block == 0:
                    visited[nextx][nexty][block+1] = visited[nowx][nowy][block]+1
                    que.append((nextx,nexty,block+1))
                elif graph[nextx][nexty] == '0' and visited[nextx][nexty][block] == 0:
                    visited[nextx][nexty][block] = visited[nowx][nowy][block]+1
                    que.append((nextx,nexty,block))
    return -1
print(BFS(0,0))