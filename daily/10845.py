import sys
from collections import deque
n = int(sys.stdin.readline())
que = deque()
for i in range(n):
    x = list(map(str,sys.stdin.readline().split()))
    if x[0] == 'push':
            que.append(x[1])
    elif x[0] == 'pop':
        if len(que) > 0:
            print(que.popleft())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(que))
    elif x[0] == 'empty':
        if len(que) > 0:
            print(0)
        else:
            print(1)
    elif x[0] == 'front':
        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
    elif x[0] == 'back':
        if len(que) > 0:
            print(que[-1])
        else:
            print(-1)