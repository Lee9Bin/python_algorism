import sys
import heapq

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[]for i in range(n+1)]


for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    # a -> b 1의 가중치
    graph[a].append((b,1))

def dik(start):
    hq = []
    dist = [1e9] * (n+1)
    #                거리값 노드
    heapq.heappush(hq,(0,start))
    
    dist[start] = 0
    
    while hq:
        nowdist, nownode = heapq.heappop(hq)
        
        if dist[nownode] < nowdist:
            continue
        
        for i in graph[nownode]:
            newdist = nowdist + i[1]
            if dist[i[0]] > newdist:
                dist[i[0]] = newdist
                heapq.heappush(hq,(newdist,i[0]))
    
    result = []
    for i in range(1,n+1):
        if dist[i] == k:
            result.append(i)
            
    result.sort()
    
    if not result:
        print(-1)
    else:
        for i in result:
            print(i)
    

dik(x)