import sys
n, m = map(int, sys.stdin.readline().split())

graph = [[]for i in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
def dfs(num,cnt):
    global ans
    if ans == 1:
        return
    if cnt == 5:
        ans = 1
        return
    
    for i in graph[num]:
        if visited[i] == False:
            visited[i] = True
            dfs(i,cnt+1)
            visited[i] = False
for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i,1)
    if ans == 1:
        break
print(ans)