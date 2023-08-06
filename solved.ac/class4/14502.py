import sys
from collections import deque
n ,m = map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def dfs(x,y):
    que = deque()
    que.append((x,y))
    visited= [[0 for i in range(m)] for i in range(n)]
    
    while que:
        nowx, nowy = que.popleft()
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        for i in range(4):
            nextx = dx[i] + nowx
            # nexty = dy[i] + nowy
            
            # if nextx>=0 and nexty>=0 and nextx<n and nexty<0:
            #     if visited[nextx][nexty]
        
def back(x,y,cnt):
    if cnt == 3:
        print(graph)
        return
    
    for i in range(x,m):
        if i == x:
            for j in range(y+1,m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    back(i,j,cnt+1)
                    graph[i][j] = 0
        else:
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    back(i,j,cnt+1)
                    graph[i][j] = 0
  
back(0,1,1)              
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             back(i,j,1)
#             print(graph)