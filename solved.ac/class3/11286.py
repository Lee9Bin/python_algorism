import sys
import heapq
n = int(sys.stdin.readline())
hq = []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if x > 0:
        heapq.heappush(hq,(x,2))
    elif x< 0:
        heapq.heappush(hq,(abs(x),1))
    else:
        if hq:
            a,b = heapq.heappop(hq)
            if b == 1:
                print(-a)
            else:
                print(a)
        else:
            print(0)