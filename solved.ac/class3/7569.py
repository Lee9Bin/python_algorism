import sys
from collections import deque
M, N, H = map(int ,sys.stdin.readline().split())
graph=[[]for i in range(H)]

# 그래프를 어떻게 담을까?
for i in range(H):
    for j in range(N):
        graph[i].append(list(map(int, sys.stdin.readline().split())))
# 그래프를 담았어 어떻게 할래? 난 bfs쓸래
def bfs():
    que = deque()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if graph[k][i][j] == 1:
                    que.append((k,i,j))
    while que:
        nowh,nowx,nowy = que.popleft()
        dx = [0,0,1,-1,0,0]
        dy = [1,-1,0,0,0,0]
        dh = [0,0,0,0,1,-1]
        
        for i in range(6):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            nexth = nowh + dh[i]
            if nextx>=0 and nexty>=0 and nexth>=0 and nextx <= N-1 and nexty <=M-1 and nexth<=H-1:
                if graph[nexth][nextx][nexty] == 0 :
                    graph[nexth][nextx][nexty] = graph[nexth][nowx][nowy] + 1
                    que.append((nexth,nextx,nexty))
bfs()
ans = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 0:
                print(-1)
                exit()
            if ans < graph[k][i][j]:
                ans = graph[k][i][j]
print(ans-1)