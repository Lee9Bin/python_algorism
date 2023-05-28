import sys
from collections import deque
def DFS(v):
    if visited[v] == False:
        print(v,end=' ')
    visited[v] = True
    for i in range(1,n+1):
        if graph[v][i] == 1 and visited[i]==False:
            graph[v][i] = -1
            DFS(i)

def BFS(v):
    que = deque()
    que.append(v)
    while que:
        nowv = que.popleft()
        if Bvisited[nowv] == False:
            print(nowv,end=' ')
        Bvisited[nowv] = True
        for i in range(1,n+1):
            if Bgraph[nowv][i] == 1 and Bvisited[i] == False:
                Bgraph[nowv][i] = -1
                que.append(i)

n,m,v = map(int,sys.stdin.readline().split())
graph = [[0 for i in range(n+1)] for i in range(n+1)]
Bgraph = [[0 for i in range(n+1)] for i in range(n+1)]

visited = [False] * (n+1)
Bvisited = [False] * (n+1)
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
    Bgraph[x][y] = 1
    Bgraph[y][x] = 1

DFS(v)
print()
BFS(v)
    