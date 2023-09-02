import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
visited = [[] for i in range(n+1)]
for i in range(m):
    a,b,v = map(int,sys.stdin.readline().split())
    graph[a].append((b,v))

start,end = map(int,sys.stdin.readline().split())

def dik(s,e):
    hq = []
    dis = [1e9] *(n+1)
    heapq.heappush(hq,(0,s))
    dis[start] = 0
    while hq:
        tov, nextv = heapq.heappop(hq)
        
        if dis[nextv] < tov:
            continue
        
        for i in graph[nextv]:
            newv = tov + i[1]
            if newv < dis[i[0]]:
                visited[i[0]] = [nextv]
                dis[i[0]] = newv
                heapq.heappush(hq,(newv,i[0]))
    # print(visited)
    
    result = []
    nowv = end
    while nowv != start:
        result.append(nowv)
        nowv = visited[nowv][0]
    result.append(start)
    
    print(dis[end])
    print(len(result))
    print(*reversed(result))
    return
dik(start,end)