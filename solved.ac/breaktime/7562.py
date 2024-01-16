import sys
from collections import deque

dx = [-2,-2,-1,-1,2,2,1,1]
dy = [-1,1,-2,2,-1,1,-2,2]

def bfs(x, y):
    que = deque()
    que.append((x,y))


    while que:
        nowX, nowY = que.popleft()

        if nowX == endX and nowY == endY:
            break

        for i in range(8):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]

            if 0 <= nextX < l and 0 <= nextY < l and graph[nextX][nextY] == 0:
                graph[nextX][nextY] = graph[nowX][nowY] + 1
                que.append((nextX,nextY))
    print(graph[endX][endY])
t = int(sys.stdin.readline())

for test in range(t):
    l = int(sys.stdin.readline())
    graph = [[0 for i in range(l)] for i in range(l)]

    startX, startY = map(int ,sys.stdin.readline().split())
    endX, endY = map(int ,sys.stdin.readline().split())
    bfs(startX,startY)
