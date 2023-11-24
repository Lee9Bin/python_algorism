import sys
from collections import deque
def bfs(x,y):
    que = deque()
    que.append((x,y))
    graph[x][y] = 1
    cnt = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while que:
        nowx, nowy = que.popleft()
        
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            
            if nextx>= 0 and nexty >= 0 and nextx < m and nexty < n:
                if graph[nextx][nexty] == 0:
                    graph[nextx][nexty] = graph[nowx][nowy] + 1
                    cnt += 1
                    que.append((nextx,nexty))
    return cnt
m, n, k = map(int, sys.stdin.readline().split())

graph = [[0 for i in range(n)] for i in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for x in range(y1,y2):
        for y in range(x1,x2):
            graph[x][y] = 1

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i,j))
result.sort()
print(len(result))
print(*result)