import sys
n = int(sys.stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# 각 지점이 경유지가 됐을때 기준으로 탐색을 하면된다.
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] ==2 :
                graph[i][j] = 1

for i in graph:
    print(*i)