import sys
from collections import deque
r, c, n = map(int, sys.stdin.readline().split())
graph = []

for i in range(r):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

time = 0
boomb = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == "O":
            boomb.append((2,(i,j)))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while time < n:
    if time == 0:
        time += 1
        continue
    elif time % 2 != 0:
        for i in range(r):
            for j in range(c):
                if graph[i][j] == ".":
                    graph[i][j] = "O"
                    boomb.append((time+3,(i,j)))
    elif time % 2 == 0:
        while True:
            nowTime, xy = boomb.popleft()
            if nowTime != time:
                boomb.appendleft((nowTime, (xy[0],xy[1])))
                break
            graph[xy[0]][xy[1]] = "."
            for i in range(4):
                nextx = xy[0] + dx[i]
                nexty = xy[1] + dy[i]
                if 0 <= nextx < r and 0 <= nexty < c:
                    graph[nextx][nexty] = "."
                    if (nowTime+2,(nextx,nexty)) in boomb:
                        boomb.remove((nowTime+2,(nextx,nexty)))
    time += 1
for i in graph:
    print(''.join(i))