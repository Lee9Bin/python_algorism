import sys
n, m = map(int,sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
            
def dfs(x,y,cnt,total):
    global result
    if cnt == 4:
        if result < total:
            result = total
        return
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for i in range(4):
        nextx = dx[i] + x
        nexty = dy[i] + y
        if nextx>= 0 and nexty>=0 and nextx<=n-1 and nexty<=m-1:
            if visited[nextx][nexty] == False:
                if cnt == 2:
                    visited[nextx][nexty] = True
                    dfs(x,y,cnt+1,total+graph[nextx][nexty])
                    visited[nextx][nexty] = False

                visited[nextx][nexty] = True
                dfs(nextx,nexty,cnt+1,total+graph[nextx][nexty])
                visited[nextx][nexty] = False
result = 0
visited = [[False for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] =True
        dfs(i,j,1,graph[i][j])
        visited[i][j] =False
print(result)