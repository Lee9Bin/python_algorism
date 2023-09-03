import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def dfs(x,y):
    que = deque()
    que.append((x,y))
    dx = [0,-1,0,1]
    dy = [-1,-0,1,0]
    visited = [[0 for i in range(n)] for i in range(n)]
    dis  = [[0 for i in range(n)] for i in range(n)]
    visited[x][y] = 1
    fish = []
    
    while que:
        nowx, nowy = que.popleft()
        
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            
            if nextx >=0 and nexty >=0 and nextx<n and nexty<n:
                if graph[nextx][nexty] <= attack and visited[nextx][nexty] == 0:
                    visited[nextx][nexty] = 1
                    dis[nextx][nexty] = dis[nowx][nowy] + 1
                    que.append((nextx,nexty))
                    if 0 < graph[nextx][nexty] and graph[nextx][nexty] < attack:
                        fish.append((nextx,nexty,dis[nextx][nexty]))
    return sorted(fish, key = lambda x: (x[2],x[0],x[1]))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            startx = i
            starty = j
attack = 2
cnt = 0
ans = 0

while True:
    possible = deque(dfs(startx,starty))
    
    if len(possible) == 0:
        break
    
    nextx,nexty,dis = possible.popleft()
    
    ans = ans + dis
    graph[startx][starty] = 0
    graph[nextx][nexty] = 0
    startx, starty = nextx,nexty
    
    cnt +=1
    
    if cnt == attack:
        attack +=1
        cnt = 0
print(ans)