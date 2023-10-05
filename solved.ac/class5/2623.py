import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
indgree = [0] *(n+1)
for i in range(m):
    mlist = list(map(int,sys.stdin.readline().split()))
    for k in range(1,mlist[0]):
        graph[mlist[k]].append(mlist[k+1])
        indgree[mlist[k+1]] +=1

def toplogic():
    que = deque()
    for i in range(1,n+1):
        if indgree[i] == 0:
            que.append(i)

    while que:
        nown = que.popleft()
        result.append(nown)

        for i in graph[nown]:
            indgree[i] -= 1
            if indgree[i] == 0:
                que.append(i)
result = []
toplogic()
if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)