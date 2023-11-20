import sys
from collections import deque

n, m ,r = map(int, sys.stdin.readline().split())
visited = [0] * (n+1)
visited[r] = 1
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort(reverse=True)
    
que = deque()
que.append(r)
cnt = 1

while que:
    nowV = que.popleft()
    
    for i in graph[nowV]:
        if visited[i] == 0:
            cnt+=1
            visited[i] = cnt
            que.append(i)

for i in visited[1:]:
    print(i)