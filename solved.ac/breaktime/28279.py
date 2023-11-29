import sys
from collections import deque

que = deque()

n = int(sys.stdin.readline())
for i in range(n):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        que.appendleft(command[1])
    
    if command[0] == 2:
        que.append(command[1])

    if command[0] == 3:
        if que:
            print(que.popleft())
        else:
            print(-1)
    
    if command[0] == 4:
        if que:
            print(que.pop())
        else:
            print(-1)

    if command[0] == 5:
        print(len(que))
    
    if command[0] == 6:
        if que:
            print(0)
        else:
            print(1)
    
    if command[0] == 7:
        if que:
            print(que[0])
        else:
            print(-1)
    
    if command[0] == 8:
        if que:
            print(que[-1])
        else:
            print(-1)