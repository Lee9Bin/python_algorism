import sys
n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

ans = 0
nowCost = cost[0]
for i in range(1,n):
    ans += nowCost * distance[i-1]
    if nowCost > cost[i]:
        nowCost = cost[i]
print(ans)