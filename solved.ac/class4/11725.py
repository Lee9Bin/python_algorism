import sys
from collections import deque

n = int(sys.stdin.readline())
visited = [0] * (n+1)
graph = [[]for i in range(n+1)]

for i in range(n-1):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(start,parents):
    que = deque()
    que.append((start,parents))
    visited[start] = parents
    
    while que:
        nowv,parents = que.popleft()
        visited[nowv] = parents
        
        for i in graph[nowv]:
            if visited[i] == 0:
                que.append((i,nowv))                
bfs(1,1)
for i in range(2,n+1):
    print(visited[i])