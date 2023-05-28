import sys
from collections import deque
def BFS():
    while que:
        nowx, nowy = que.popleft()
        
        for i in range(4):
            nextx = dx[i] + nowx
            nexty = dy[i] + nowy
            if nextx>= 0 and nexty>=0 and nextx<=N-1 and nexty<=M-1:
                if graph[nextx][nexty] == 0:
                    graph[nextx][nexty] = graph[nowx][nowy] +1
                    que.append((nextx,nexty))
        
M, N = map(int,sys.stdin.readline().split())
# M은 가로 열 N은 세로 행
graph = []
cnt = 0
que = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
    
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            que.append((i,j))
BFS()

for i in range(N):
    for j in range(M):
        if graph[i][j] >= cnt:
            cnt = graph[i][j]
        if graph[i][j] == 0:
            print(-1)
            exit(0)
print(cnt-1)