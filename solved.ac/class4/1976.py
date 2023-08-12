import sys
import heapq

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, v = map(int, sys.stdin.readline().split())
    graph[a].append((b, v))
    graph[b].append((a, v))
    
def dfs(dist,start):
    global result
    global nowv
    visited[start] = True
    if result < dist:
        result = dist
        nowv = start
    for i in graph[start]:
        if visited[i[0]] == False:
            newdist = dist + i[1]
            dfs(newdist,i[0])

result = 0
nowv = 0
visited = [False] * (n+1)
dfs(0,1)
print(result,nowv)
visited = [False] * (n+1)
result = 0
dfs(0,nowv)
print(result,nowv)