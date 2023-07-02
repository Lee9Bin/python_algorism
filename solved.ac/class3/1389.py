import sys
import heapq
n, m = map(int,sys.stdin.readline().split())
graph = [[0 for i in range(n+1)] for i in range(n+1)]

for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
    
def bfs(cnt,start):
    global result
    hq = []
    heapq.heappush(hq,(cnt,start))
    visited[start] = True
    
    while hq:
        cnt,nowv = heapq.heappop(hq)
        print(cnt,nowv)
        result += cnt
        for i in range(1,n+1):
            if graph[nowv][i] ==1 and visited[i] == False:
                visited[i] = True
                heapq.heappush(hq,(cnt+1,i))

# 각 사람들의 케빈 베이턴 값을 담을 리스트
ans = []
for i in range(1,n+1):
    # 
    visited = [False]*(n+1)
    result = 0
    bfs(0,i)
    ans.append(result)
print(ans.index(min(ans))+1)
