# 문제가 원하는 것, 문제설명
# 특정한 최단경로 문제에서 제시하는 노드를 꼭 들리면서 n번까지의 최단거리를 구하기

# 어떻게 풀려고 하였는지 => 플로우차트
# 우선 특정한 노드를 들리는 경우의 수를 생각해 봤다
# 이때 그러면 1 번에서 n번까지 갈때에 1 v1 v2 n 경우 1 v2 v1 n경우

import sys
import heapq
INF = int(1e9)
n,e = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
dis = [INF] * (n+1)

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1, v2 = map(int,sys.stdin.readline().split())


def dijkstra(start,end):
    # 거리는 함수 돌때마다 초기화 해줘야 하기때문에
    # 함수안에 작성
    dis = [INF] * (n+1)
    
    # 거리가 짧은 것 순으로 뽑기 위해 우선순위 큐 선언
    hq = []
    # 앞에 인자는 거리값 뒤에인자는 노드
    heapq.heappush(hq,(0,start))
    dis[start] = 0
    while hq:
        dist, nextv = heapq.heappop(hq)
        
        # 거리에 이미 저장 돼 있는 값보다 dist가 크다면 무시
        if dis[nextv] < dist :
            continue
        
        # 그래프에 저장된 다음노드로의 정보와 거리가 가져온다
        for i in graph[nextv]:
            newdist = dist + i[1]
            if newdist < dis[i[0]]:
                dis[i[0]]=newdist
                heapq.heappush(hq,(newdist,i[0]))
    return dis[end]
# 1번에서 v1까지 가는 최단거리 + v1에서 v2 가는 최단거리 +v2에서 n까지
# 가는 거리가 즉 1 v1 v2 n 경우의 최단거리
# 위와같은 방법으로 1 v2 v1 n 경우 비교해서 출력
path1= dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
path2= dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)

if min(path1,path2,INF) == INF:
    print(-1)
else:
    print(min(path1,path2))
    