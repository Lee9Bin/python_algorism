import sys
def check(x,y):
    global ans
    for i in range(min((n-x), (m-y))):
        checkList = set([])
        checkList.add(graph[x][y])
        checkList.add(graph[x][y+i])
        checkList.add(graph[x+i][y])
        checkList.add(graph[x+i][y+i])
        if len(checkList) == 1:
            ans = max(ans, (i+1)**2)

n, m = map(int, sys.stdin.readline().split())

graph = []
ans = 1
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(m):
        check(i,j)
print(ans)