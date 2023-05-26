import sys
import heapq
n = int(sys.stdin.readline())
numlist = []
ans = []
for i in range(1,n+1):
    numlist.append(int(sys.stdin.readline()))
    numlist.sort()
    if i % 2 ==0:
        i = i-1
    heapq.heappush(ans,numlist[i//2])
for i in ans:
    print(i)