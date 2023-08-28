import sys
import heapq
n,m,x = map(int,sys.stdin.readline().split())
city = [[]for i in range(n+1)]

for i in range(m):
    a,b,v = map(int,sys.stdin.readline().split())
    city[a].append((b,v))  #단방향

def dik(start,end):
    hq = []
    dis = [1e9] * (n+1)
    heapq.heappush(hq,(0,start))
    dis[start] = 0
    while hq:
        nowd, nowx = heapq.heappop(hq)
        
        if dis[nowx] < nowd:
            continue
        
        for i in city[nowx]:
            newd = nowd + i[1]
            if newd < dis[i[0]]:
                dis[i[0]] = newd
                heapq.heappush(hq,(newd,i[0]))
    return dis[end]

result = 0
for i in range(1,n+1):
    sub = dik(i,x) + dik(x,i)
    if result < sub:
        result = sub
print(result)