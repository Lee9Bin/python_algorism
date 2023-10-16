import sys
n = int(sys.stdin.readline())
graph = [[0 for i in range(101)] for i in range(101)]
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    for j in range(10):
        for k in range(10):
            graph[y+j][x+k] = 1
ans = 0
for i in graph:
    for j in i:
        if j == 1:
            ans += 1
print(ans)