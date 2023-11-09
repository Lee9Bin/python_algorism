import sys
n = int(sys.stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

ans = 1e9
def back(start,v,cnt):
    global ans
    if v > ans:
        return
    if cnt == n-1:
        if graph[start][end] != 0:
            ans = min(ans,v+graph[start][end])
        return
    for i in range(n):
        if graph[start][i] != 0 and visited[i] == False:
            visited[i] = True
            back(i,v+graph[start][i],cnt+1)
            visited[i] = False
for i in range(n):
    visited = [False] *n
    visited[i] = True
    end = i
    back(i,0,0)
print(ans)