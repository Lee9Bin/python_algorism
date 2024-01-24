import sys
from collections import deque
r, c, n = map(int, sys.stdin.readline().split())
graph = []

for i in range(r):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

time = 0
boomb = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while time < n:
    if time % 2 == 0:
        while boomb:
            nowTime, xy = boomb.popleft()
            graph[xy[0]][xy[1]] = "."
            for i in range(4):
                nextx = xy[0] + dx[i]
                nexty = xy[1] + dy[i]
                if 0 <= nextx < r and 0 <= nexty < c:
                    graph[nextx][nexty] = "."
        for i in range(r):
            for j in range(c):
                if graph[i][j] == "O":
                    boomb.append((time+2,(i,j)))
    elif time % 2 != 0:
        for i in range(r):
            for j in range(c):
                if graph[i][j] == ".":
                    graph[i][j] = "O"
    time += 1
for i in graph:
    print(''.join(i))