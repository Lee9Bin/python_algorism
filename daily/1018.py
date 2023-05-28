import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))
ans = int(1e9)


def bfs(x, y):
    global ans
    cnt = 0
    dx = [0, 0, -1]
    dy = [1, -1, 0]
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            for k in range(3):
                nextx = i + dx[k]
                nexty = j + dy[k]
                if nextx >= x and nexty >= y and nextx <= x + 7 and nexty <= y + 7:
                    if graph[nextx][nexty] == graph[i][j]:
                        cnt += 1
                        break
    print(cnt)


for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        bfs(i, j)
