import sys
import heapq
n,k = map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))
hq = []
for i in numlist:
    heapq.heappush(hq,i)

for i in range(k-1):
    heapq.heappop(hq)

print(heapq.heappop(hq))