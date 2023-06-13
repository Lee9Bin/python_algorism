import sys
from collections import deque
t = int(sys.stdin.readline())
result = []
for i in range(t):
    n,m = map(int, sys.stdin.readline().split())
    document=deque(map(int, sys.stdin.readline().split()))
    cnt = 0
    while document:
        maxnum = max(document)
        if m == 0:
            if document[0] < maxnum:
                nownum = document.popleft()
                document.append(nownum)
                m = len(document) -1
            else:
                document.popleft()
                result.append(cnt+1)
                break
        else:
            if document[0] < maxnum:
                nownum = document.popleft()
                document.append(nownum)
                m -= 1
            else:
                document.popleft()
                cnt +=1
                m -= 1
print(result)