# 문제가 원하는 것, 문제설명
# 각각의 N,M의 2차원 배열의 크기를 만들고 0은 바다 1은 땅으로 생각하고 입력한다.
# 이때 어느 한 지점에서 8방향으로 땅이 있을때 이동이 가능한데 이동이 가능한
# 범위 만큼이 섬인데 섬의 갯수를 세는 문제

# 어떻게 풀려고 하였는지 => 플로우차트
# 1012번 문제와 같은 해결법

import sys
from collections import deque
sys.setrecursionlimit(10**6)
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return 
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = -1
        dfs(x-1 , y) # 상
        dfs(x+1 , y) # 하
        dfs(x , y-1) # 좌
        dfs(x , y+1) # 우
        dfs(x-1 , y+1) # 오른쪽 위
        dfs(x+1 , y+1) # 오른쪽 아래
        dfs(x+1 , y-1) # 왼쪽 아래
        dfs(x-1 , y-1) # 왼쪽 위
        
def BFS(x,y):
    dx=[-1,1,0,0,-1,1,1,-1]
    dy=[0,0,-1,1,1,-1,1,-1]
    que = deque()
    que.append((x,y))
    graph[x][y] = -1
    while que:
        nowx,nowy = que.popleft()
        
        for i in range(8):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if nextx < 0 or nexty<0 or nextx>=N or nexty>=M:
                continue
            
            if graph[nextx][nexty] == 1:
                graph[nextx][nexty] = -1   
                que.append((nextx,nexty))

        
def stop(x,y): # x,y가 0 0 이 들어오면 종료
    if x== 0 and y == 0:
        return True
    
while True:
    M,N = map(int,sys.stdin.readline().split())
    if stop(M,N) == True:
        break
    
    cnt = 0
    graph = []
    for i in range(N):
        graph.append(list(map(int,sys.stdin.readline().split())))

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                # dfs(i,j)
                BFS(i,j)
                cnt += 1
    print(cnt)