import heapq
import sys
hq = []

for i in range(8):
    point = int(sys.stdin.readline())
    heapq.heappush(hq,(-point,i+1))

total = 0
result = []

for i in range(5):
    nowx, noww = heapq.heappop(hq)
    total += (-nowx)
    result.append(noww)
print(total)
result.sort()
print(*result)