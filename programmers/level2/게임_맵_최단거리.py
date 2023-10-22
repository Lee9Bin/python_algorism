# 문제설명: 상대 진영으로 최대한 빨리 가기 -> 결국 그래프 0,0에서 n-1,m-1까지 최단 거리를 구하는 것!
#         이런 경우 재귀를 통해 확인 하는 것보다는 bfs를 통해 확인하는 것이 유리하다.
#         why? dfs는 결국 모든 경우의 수를 파악해 작은 값은로 갱신을 해줘야 한다.
#              bfs는 한 depth씩 확인 하고 다음 depth로 넘어가기 때문에 발견 즉식 그 값이 최소!
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    bfs(maps,n,m)
    print(maps)
    ans = maps[n-1][m-1]
    if ans == 0 or ans == 1:
        ans = -1
    return ans

def bfs(maps,n,m):
    visited = [[False for i in range(m)] for i in range(n)]
    que = deque()
    que.append((0,0))
    
    while que:
        nowx, nowy = que.popleft()
        if visited[nowx][nowy] == True:
            continue
        
        visited[nowx][nowy] = True
        
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]

            if nextx >= 0 and nexty >= 0 and nextx <= n-1 and nexty<=m-1:
                if visited[nextx][nexty] == False and maps[nextx][nexty] != 0:
                    maps[nextx][nexty] = maps[nowx][nowy] +1
                    que.append((nextx,nexty))
                
                
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])