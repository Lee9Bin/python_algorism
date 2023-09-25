import sys
import heapq
T = int(sys.stdin.readline())

def tologic():
    dp = [0] * (n+1)
    hq = []

    for i in range(1,n+1):
        if indegree[i] == 0:
            heapq.heappush(hq,(time[i-1],i))

    while hq:
        nowtime, nown = heapq.heappop(hq)
        if nown == end:
            print(nowtime)
            break
        for i in graph[nown]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(hq,(nowtime+time[i-1],i))

for t in range(T):
    n,k = map(int,sys.stdin.readline().split())
    time = list(map(int,sys.stdin.readline().split()))
    indegree = [0] *(n+1)
    graph=[[] for i in range(n+1)]
    for i in range(k):
        a, b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    end = int(sys.stdin.readline())
    
    tologic()
