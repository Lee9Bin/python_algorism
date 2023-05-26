import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


que = deque()
que.append((0,0))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

while que:
    x,y = que.popleft()
    if x == n-1 and y == m-1:
        break
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx<0 or ny<0 or nx >= n or ny >=m or (nx==0 and ny==0):
            continue
        if graph[nx][ny] ==1:
            graph[nx][ny] = graph[x][y] + 1
            que.append((nx,ny))
print(graph[n-1][m-1])