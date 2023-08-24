import sys
import heapq
n, m, r = map(int,sys.stdin.readline().split())
n_item = list(map(int,sys.stdin.readline().split()))
graph = [[]for i in range(n+1)]
for i in range(r):
    a, b, i = map(int,sys.stdin.readline().split())
    graph[a].append((b,i))
    graph[b].append((a,i))


def dik(start):
    hq = []
    heapq.heappush(hq,(0,start))
    dis[start] = 0
    while hq:
        nowdis, nown = heapq.heappop(hq)
        
        if nowdis > dis[nown]:
            continue
        
        for i in graph[nown]:
            newdis = i[1] + nowdis
            if newdis < dis[i[0]]:
                dis[i[0]] = newdis
                heapq.heappush(hq,(newdis,i[0]))
                
ans = 0
for i in range(1,n+1):
    dis = [1e9] * (n+1)
    dik(i)
    result = 0
    for j in range(1,n+1):
        if dis[j] <= m:
            result += n_item[j-1]
    if result > ans:
        ans = result
print(ans)