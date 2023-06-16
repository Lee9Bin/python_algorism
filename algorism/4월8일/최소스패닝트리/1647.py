# 문제가 원하는 것, 문제설명
# 마을안에 도시들이 있는데 도시들을 두분류로 나누어 두개의 마을로 만들고싶어한다
# 이때 각 마을안에 있는 도시들은 연결 되어있다.

# 어떻게 풀려고 하였는지 => 플로우차트.
# 최소 스패닝 이론을 구글링해서 찾아보고 기본소스코드도 봤을때 프림 알고리즘이
# 다익스트라와 유사하다고 생각 되었다.
# 기본예제를 보면서 이해하고 문제에 적용하면서 거리에 담긴 가중치가 제일큰 값을
# 빼준다

import sys
import heapq
INF=int(1e9)
n,m = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n+1)]

# 노드를 방문했는지 체크
# 거리를 무한대로 선언
visited = [False] * (n+1)
dis = [INF] * (n+1)

# 무방향 이므로 밑에와 같이 선언
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
def prim():
    # 다익스트라 알고리즘 아이디어를가져와 힙형태로 저장
    hq = []
    heapq.heappush(hq,(0,1))
    dis[1] = 0
    
    while hq:
        dist, nextv = heapq.heappop(hq)
        
        if visited[nextv] == False:
            visited[nextv] = True
            
            for i in graph[nextv]:
                # 여기서 거리값이 다익스트라와 다른점이다 다익스트라는 노드를
                # 통해서 가는 거리값을 더해가는 반면
                # 프림알고리즘은 그냥 순순하게 그노드 기준 거리만을 체크
                dist = i[1]
                if dist < dis[i[0]] and visited[i[0]] == False:
                    dis[i[0]] = dist
                    # 혼자 생각 해봤는데 i[0]에 담기는 정보가 
                    # 다익스트라에서는 1->2->3 등의 정보가 담기는 반면
                    # 프림은 그냥 노드의 한지점 정보가 담긴다고 생각이 된다.
                    heapq.heappush(hq,(dist,i[0]))
prim()
print(sum(dis[1:])-max(dis[1:]))
