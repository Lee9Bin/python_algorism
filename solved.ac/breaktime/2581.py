import sys

prim = []
visited = [False] * (10001)

for i in range(2,int((10001)**0.5)):
    if visited[i] == False:
        for j in range(i*2,10001,i):
            visited[j] = True
for i in range(2,10001):
    if visited[i] == False:
        prim.append(i)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ans = []

for i in prim:
    if n<= i <=m:
        ans.append(i)
if sum(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))