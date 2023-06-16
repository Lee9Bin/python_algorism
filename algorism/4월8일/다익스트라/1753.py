# 문제가 원하는 것, 문제설명
# 정점 v개가 있고 간선의 갯수가 E개가 있을때 1부터 v까지의 최단경로

# 어떻게 풀려고 하였는지 => 플로우차트
# 전형적인 다익스트라 최단경로 문제로 구글링해서 다익스트라 이론을 다시보고
# 기본예제를 보면서 이해하고 문제에 적용

import sys
import heapq
# 거리가 짧은것으로 갱신을 위해 사용된 무한대값 선언
INF = int(1e9)
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
# 간선 정보를 그래프로 저장
graph = [[] for i in range(v+1)]
dis = [INF] * (v+1)

# 그래프에 x 노드에서 y 노드로 가는 가중치 w 저장
for i in range(e):
    x,y,w = map(int, sys.stdin.readline().split())
    graph[x].append((y,w))
    
    
def dijkstra(start):
    # 우선순위 즉 거리값이 짧은것부터 뽑아내기 위해 힙형태로 값을 저장
    hq = []
    heapq.heappush(hq,(0,start))
    # 문제에서 시작점에서 자기자신으로 가는 길은 0
    dis[start] = 0
    
    while hq:
        # 거리값과 현제 향하는 노드 출력
        dist, now = heapq.heappop(hq)

        # 현재 저장돼 있는 값이 작으면 무시
        if dis[now] < dist:
            continue
        
        # 그래프에 튜플형식으로 (거리,향하는 노드번호) 형태로 가져와 거리값 계산
        # 여기서 힙에 담긴 정보는 ex)1->2->3 8 1->3 7 등등
        # 그래서 위에 if문으로 높은값은 무시해서 시간 단축
        for i in graph[now]:
            newcost = dist + i[1]
            if dis[i[0]] > newcost:
                dis[i[0]] = newcost
                heapq.heappush(hq,(newcost,i[0]))
dijkstra(k)
for i in range(1, v + 1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])