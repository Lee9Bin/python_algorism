import sys
from collections import deque

n, k = map(int,input().split())
que = deque()
que.append((n,0))
visited = [False]*(100001)
ans = 0
while que:
    nown,cnt = que.popleft()
    if nown == k:
        ans = cnt
        break
    for i in (nown-1,nown+1,2*nown):
        if i>=0 and i<=100000:
            if visited[i] == False:
                visited[i] = True
                que.append((i,cnt+1))
print(ans)