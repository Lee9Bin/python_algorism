import sys
from collections import deque
n = int(sys.stdin.readline())
que = deque()
command = list(map(int,sys.stdin.readline().split()))
command.reverse()

for i in range(1,n+1):
    if command[i-1] == 1:
        que.appendleft(i)
    elif command[i-1] == 2:
        que.insert(1,i)
    elif command[i-1] == 3:
        que.append(i)

print(*que)