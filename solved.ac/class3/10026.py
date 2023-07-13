import sys
from collections import deque
N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))
    
def color(x,y,target1,target2):
    que = deque()
    que.append((x,y))
    visited[x][y] = True
        
    while que:
        nowx, nowy = que.popleft()
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        for i in range(4):
            nextx = dx[i] + nowx
            nexty = dy[i] + nowy
            if nextx >= 0 and nexty >= 0 and nextx <=N-1 and nexty <= N-1:
                if (graph[nextx][nexty] == target1 or graph[nextx][nexty] == target2) and visited[nextx][nexty] == False:
                    visited[nextx][nexty] = True
                    que.append((nextx,nexty))
for k in range(2):
    cnt = 0
    visited = [[False for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if k == 0:
                if visited[i][j] == False:
                    color(i,j,graph[i][j],graph[i][j])
                    cnt +=1
            elif k == 1:
                if visited[i][j] == False:
                    if graph[i][j] == 'R' or graph[i][j] == 'G':
                        color(i,j,"R","G")
                    elif graph[i][j]=="B":
                        color(i,j,graph[i][j],graph[i][j])
                    cnt +=1
    print(cnt,end=' ')
print()
