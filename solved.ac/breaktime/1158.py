import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
result = []
que = deque()

for i in range(1,n+1):
    que.append(i)
cnt = 0
while que:
    nowx = que.popleft()
    cnt +=1

    if cnt % k == 0:
        result.append(nowx)
    else:
        que.append(nowx)

print("<",end="")
for i in range(n):
    if i != n-1:
        print(f"{result[i]},",end=" ")
    else:
        print(result[i],end="")
print(">")