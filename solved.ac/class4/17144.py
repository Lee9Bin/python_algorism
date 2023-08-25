import sys
from collections import deque

def bfs():
    que = deque()
    
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    
    where = 0 # 청정기 위치 담아두기 위한 코드
    clearup = (0,0)
    cleardown = (0,0)
    # 먼저 1-2 조건 해결하기 위한 부분
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                que.append((i,j,graph[i][j]))
            if graph[i][j] == -1:
                if where == 0:
                    clearup = (i,j)
                    where += 1
                else:
                    cleardown = (i,j)
    
    while que :
        nowx, nowy, nowv = que.popleft()
        cnt = 0
        
        for i in range(4):
            nextx = dx[i] + nowx
            nexty = dy[i] + nowy
            
            if nextx >= 0 and nexty >= 0 and nextx < r and nexty <c:
                if graph[nextx][nexty] != -1:
                    graph[nextx][nexty] += nowv//5
                    cnt += 1
        graph[nowx][nowy] -= (cnt*(nowv//5))
    
    # 공기청정기 윗부분 직접 구현
    nowx,nowy = clearup
    pre = 0
    for i in range(4):
        while True:
            nextx, nexty = nowx + dx[i],nowy + dy[i]
            if nextx < 0 or nexty < 0 or nextx > clearup[0] or nexty >= c:
                break
            if nextx == clearup[0] and nexty == clearup[1]:
                break
            
            temp = graph[nextx][nexty]
            graph[nextx][nexty] = pre
            pre = temp
            nowx,nowy = nextx,nexty
    
    # 공기청정기 아래부분 직접 구현
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    nowx,nowy = cleardown
    pre = 0
    for i in range(4):
        while True:
            nextx, nexty = nowx + dx[i],nowy + dy[i]
            if nextx < cleardown[0] or nexty < 0 or nextx >= r or nexty >= c:
                break
            if nextx == cleardown[0] and nexty == cleardown[1]:
                break
            
            temp = graph[nextx][nexty]
            graph[nextx][nexty] = pre
            pre = temp
            nowx,nowy = nextx,nexty
            

r, c, t = map(int,sys.stdin.readline().split())
graph = []

for i in range(r):
    graph.append(list(map(int,sys.stdin.readline().split())))

# t초동안 반복
for i in range(t):
    bfs()

# 반복후 미세먼지 양 구하기
ans = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            ans += graph[i][j]
print(ans)            