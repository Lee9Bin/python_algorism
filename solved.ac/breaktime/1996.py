import sys
n = int(sys.stdin.readline())

graph = []

for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))
visited = [[0 for i in range(n)] for i in range(n)]

dx = [0,0,-1,1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,-1,1]
for i in range(n):
    for j in range(n):
        if graph[i][j] != ".":
            visited[i][j] = "*"
            continue
        now = 0 
        for k in range(8):
            checkX = i + dx[k]
            checkY = j + dy[k]
            if 0 <= checkX < n and 0 <= checkY < n:
                if graph[checkX][checkY] != ".":
                    now += int(graph[checkX][checkY])
        if now >= 10:
            visited[i][j] = "M"
        else:
            visited[i][j] = now

for i in range(n):
    for j in range(n):
        print(visited[i][j],end="")
    print()
