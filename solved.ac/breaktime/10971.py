import sys
n = int(sys.stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

ans = 1e9
def back(start,v,root):
    global ans
    if visited.count(True) == n-1:
        if graph[start][root] != 0:
            ans = min(ans,v+graph[start][root])
        return
    for i in range(n):
        if graph[start][i] != 0 and visited[i] == False and i != root:
            visited[i] = True
            back(i,v+graph[start][i],root)
            visited[i] = False
for i in range(n):
    visited = [False] *n
    back(i,0,i)
print(ans)