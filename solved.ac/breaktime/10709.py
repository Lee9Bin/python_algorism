import sys
n,m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))


for i in range(n):
    for j in range(m):
        if graph[i][j] == ".":
            graph[i][j] = "-1"
        elif graph[i][j] == "c":
            graph[i][j] = "0"
            cnt = 0
            for k in range(j+1,m):
                cnt += 1
                if graph[i][k] == ".":
                    graph[i][k] = str(cnt)
                else:
                    break
for i in graph:
    print(*i)