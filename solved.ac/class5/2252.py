import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
indegree =[0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

def topological():
    result = []
    que = deque()
    visited = [False] *(n+1)
    for i in range(1,n+1):
        if indegree[i] == 0:
            visited[i] = True
            que.append(i)
    
    while que:
        now = que.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                que.append(i)
        
        # for i in range(1,n+1):
        #     if indegree[i] == 0 and visited[i] == False:
        #         visited[i] = True
        #         que.append(i)
    print(*result)
topological()
