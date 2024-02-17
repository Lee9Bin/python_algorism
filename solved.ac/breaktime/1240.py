import sys
def dfs(start, dis):
    if (start == b):
        result.append(dis)
        return
    for i in graph[start]:
        if visited[i[0]] == False:
            visited[i[0]] = True
            dfs(i[0], dis + i[1])


n,m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

result = []
for i in range(m):
    visited = [False]*(n+1)
    a, b = map(int, sys.stdin.readline().split())
    visited[a] = True
    dfs(a,0)

for i in result:
    print(i)