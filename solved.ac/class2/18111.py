import sys
n, m, b = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

resultt = 999999999
resulth = 0
for k in range(0,257):
    nownum = k
    cnt = b
    time = 0
    for i in range(n):
        for j in range(m):
            if nownum < graph[i][j]:
                cnt += graph[i][j]-nownum
                time += 2*(graph[i][j]-nownum)
            else:
                cnt -= nownum-graph[i][j]
                time += (nownum-graph[i][j])
    if cnt>=0:
        if resultt >= time:
            resultt = time
            resulth = nownum
print(resultt,resulth)
