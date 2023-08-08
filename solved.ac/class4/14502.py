import sys
import copy
from collections import deque
n ,m = map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def bfs(visited):
    que = deque()
    for i in range(n):
        for j in range(m):
            if visited[i][j]==2:
                que.append((i,j))
    
    while que:
        nowx, nowy = que.popleft()
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        for i in range(4):
            nextx = dx[i] + nowx
            nexty = dy[i] + nowy
            
            if nextx>=0 and nexty>=0 and nextx<n and nexty<m :
                if visited[nextx][nexty] == 0:
                    visited[nextx][nexty] = 2
                    que.append((nextx,nexty))
    
def back(start,cnt):
    global result
    if cnt == 3:
        visited= copy.deepcopy(graph)
        bfs(visited)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0:
                    cnt+=1
        if result < cnt:
            result = cnt
        return
    
    for i in range(n):
        for j in range(start,m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                back(start+1,cnt+1)
                graph[i][j] = 0
result = 0
back(0,0)
print(result)