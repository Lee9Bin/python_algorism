# 문제가 원하는 것, 문제설명
# 섬과 바다로 이루어진 격자가 있다고 한다. 이때 각 섬에서
# 다른 섬으로 다리를 놓아서 연결을 할때 최소 길이로 연결을 한다고 한다

# 어떻게 풀려고 하였는지 => 플로우차트.
# 먼저 섬과 바다를 구분한다음에 프림알고리즘을 사용해보자 생각
import sys
from collections import deque
import heapq

# 입력 받고
n,m = map(int,sys.stdin.readline().split())
# 섬의 번호 매기기 위해 cnt 선언
cnt = 1

# 그래프 정보 저장
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# BFS를 통해 섬의 번호를 매긴다
def BFS(x,y):
    que = deque()
    que.append((x,y))
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    
    while que:
        nowx, nowy = que.popleft()
        graph[nowx][nowy] = cnt
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if nextx >=0 and nexty>=0 and nextx < n and nexty<m:
                if graph[nextx][nexty] == 1:
                    graph[nextx][nexty] = cnt
                    que.append((nextx,nexty))    
      
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt +=1
            BFS(i,j)

# 여기까지 코드는 금방 해결이 됐지만 그래프안에 정보들을 어떻게 변형해야
# 최소 스패닝 트리를 적용할 수 있을까 고민

# 새로운 그래프를 만들어서 반복문을 통해 정보를 저장
vgraph = [[] for i in range(cnt+1)]
# 가로 먼저 파악
for i in range(n):
    # 거리 값
    dis = 0
    # 비교할 숫자를 선언
    parenum = 0
    for j in range(m-1):
        # 그래프[i][j]가 0이 아니면 parenum은 바꾸고
        if graph[i][j] !=0:
            parenum = graph[i][j] 
        # 바뀌지 않았다면 패스
        if parenum == 0:
            continue
        # 패얼넘이 0이 아닐때 다음에 있는게 0이라면 거리 +1
        if graph[i][j+1] == 0:
            dis +=1
        else:
            # 다음 값이 0이 아닌 값이면 다리 길이 저장
            # 문제에서 다리길이가 2이상이여지만 가능 하다고 했고
            # parenum이 0이면 바다이므로 안된다는 조건
            if dis >=2 and parenum !=0:
                vgraph[parenum].append((graph[i][j+1],dis))
                vgraph[graph[i][j+1]].append((parenum,dis))
            dis=0 
# 세로 파악
for j in range(m):
    dis = 0
    parenum = 0
    for i in range(n-1):
        if graph[i][j] !=0:
            parenum = graph[i][j] 
        if parenum == 0:
            continue
        if graph[i+1][j] == 0:
            dis +=1
        else:
            if dis >=2 and parenum !=0 :
                vgraph[parenum].append((graph[i+1][j],dis))
                vgraph[graph[i+1][j]].append((parenum,dis))
            dis=0 

# 최소 스패닝 하기 위한 그래프 정보 저장 완료
visited = [False] * (cnt+1)
INF = int(1e9)
result = [INF]* (cnt+1)

def prim(start):
    anw = 0
    # 우선순위 즉 거리값이 짧은것부터 뽑아내기 위해 힙형태로 값을 저장
    hq = []
    heapq.heappush(hq,(0,start))
    result[start] = 0
    
    while hq:
        # 거리값과 현제 향하는 노드 출력
        dist, now = heapq.heappop(hq)
        if visited[now] == False:
            visited[now] = True
            anw += dist

            for i in vgraph[now]:
                newcost = i[1]
                if result[i[0]] > newcost and visited[i[0]] == False :
                    result[i[0]] = newcost
                    heapq.heappush(hq,(newcost,i[0]))
# prim(start) start를 2를 하는 이유는 섬 번호가 2번부터 매겨짐
prim(2)
# 거리가 INF이상이면 연결 불가능
if sum(result[2:]) >= INF:
    print(-1)
else:
    print(sum(result[2:]))