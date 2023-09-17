import sys 
from collections import deque
n, m = map(int,sys.stdin.readline().split())
nlist = list(map(int,sys.stdin.readline().split()))
que = deque()



for i in range(1,n+1):
    que.append(i)
    
start = 0
result = 0
while start < m:
    if nlist[start] == que[0]:
        que.popleft()
        start += 1
    else:
        if  len(que)-que.index(nlist[start]) < que.index(nlist[start]):
            while que[0] != nlist[start]:
                que.appendleft(que.pop())
                result+=1
        else:
            while que[0] != nlist[start]:
                que.append(que.popleft())
                result += 1

print(result)