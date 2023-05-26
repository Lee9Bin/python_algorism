# 문제가 원하는 것, 문제설명
# 전형적인 최소스패닝 트리 문제 

# 어떻게 풀려고 하였는지 => 플로우차트.
# 최소 스패닝 이론을 구글링해서 찾아보고 기본소스코드도 봤을때 프림 알고리즘이
# 다익스트라와 유사하다고 생각 되었다.
# 기본예제를 보면서 이해하고 문제에 적용해봤다
import sys
import heapq
# 거리가 짧은것으로 갱신을 위해 사용된 무한대값 선언
INF = int(1e9)
v,e = map(int,sys.stdin.readline().split())
# 간선 정보를 그래프로 저장
graph = [[] for i in range(v+1)]
dis = [INF] * (v+1)
visited = [False] * (v+1)


for i in range(e):
    x,y,w = map(int, sys.stdin.readline().split())
    graph[x].append((y,w))
    graph[y].append((x,w))
    
    
def prim(start):
    result = 0
    # 우선순위 즉 거리값이 짧은것부터 뽑아내기 위해 힙형태로 값을 저장
    hq = []
    heapq.heappush(hq,(0,start))
    dis[start] = 0
    
    while hq:
        # 거리값과 현제 향하는 노드 출력
        dist, now = heapq.heappop(hq)
        if visited[now] == False:
            visited[now] = True
            result += dist

            for i in graph[now]:
                newcost = i[1]
                if dis[i[0]] > newcost and visited[i[0]] == False :
                    dis[i[0]] = newcost
                    heapq.heappush(hq,(newcost,i[0]))
    print(result)
prim(1)


# 4 2 6 3 8