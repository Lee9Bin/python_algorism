import sys
n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))
ans = int(1e9)


def w(x, y):
    global ans
    cnt = 0
    dx = [0,1,1]
    dy = [1,0,1]
    original = graph[x][y]
    if graph[x][y] != 'W':
        graph[x][y] = 'W'
        cnt +=1
    nowcolor = graph[x][y]
    for i in range(x, x + 8,2):
        for j in range(y, y + 8,2):
            sub = graph[i][j]
            if nowcolor != graph[i][j]:
                graph[i][j] = nowcolor
                cnt +=1
            for k in range(3):
                nextx = i + dx[k]
                nexty = j + dy[k]
                if k == 2:
                    if graph[i][j] != graph[nextx][nexty]:
                        cnt +=1
                else:
                    if graph[i][j] == graph[nextx][nexty]:
                        cnt +=1
            graph[i][j] = sub
    graph[x][y] = original
    if ans > cnt:
        ans = cnt

def b(x, y):
    global ans
    cnt = 0
    dx = [0,1,1]
    dy = [1,0,1]
    original = graph[x][y]
    if graph[x][y] != 'B':
        graph[x][y] = 'B'
        cnt +=1
    nowcolor = graph[x][y]
    for i in range(x, x + 8,2):
        for j in range(y, y + 8,2):
            sub = graph[i][j]
            if nowcolor != graph[i][j]:
                graph[i][j] = nowcolor
                cnt +=1
            for k in range(3):
                nextx = i + dx[k]
                nexty = j + dy[k]
                if k == 2:
                    if graph[i][j] != graph[nextx][nexty]:
                        cnt +=1
                else:
                    if graph[i][j] == graph[nextx][nexty]:
                        cnt +=1
            graph[i][j] = sub
    graph[x][y] = original
    if ans > cnt:
        ans = cnt
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        w(i, j)
        b(i, j)
print(ans)