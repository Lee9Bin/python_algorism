import sys
import heapq
N, M = map(int,sys.stdin.readline().split())

dic = {}
for i in range(N+M):
    x, y = map(int,sys.stdin.readline().split())
    dic[x] = y


visited = [False]*101
def bfs(v,x):
    hq = []
    heapq.heappush(hq,(v,x))
    visited[x] = True
    
    while hq:
        cnt, nowx = heapq.heappop(hq)
        if nowx == 100:
            print(cnt)
            break
        for i in range(1,7):
            if nowx+i < 101:
                if visited[nowx+i] == False:
                    if nowx+i in dic:
                        heapq.heappush(hq,(cnt,dic[nowx+i]))
                        visited[dic[nowx+i]] = True
                    else:
                        heapq.heappush(hq,(cnt+1,nowx+i))
                        visited[nowx+i] = True
bfs(0,1)