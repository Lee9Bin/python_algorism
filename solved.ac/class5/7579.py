import sys

n, m = map(int,sys.stdin.readline().split())
memory= list(map(int,sys.stdin.readline().split()))
cost = list(map(int,sys.stdin.readline().split()))

dp = [[0 for i in range(sum(cost)+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(sum(cost)+1):
        if  cost[i-1] <= j:
            dp[i][j] = max(dp[i-1][j-cost[i-1]]+memory[i-1],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
ans = 1e9
for i in range(1,n+1):
    for j in range(sum(cost)+1):
        if dp[i][j] >= m:
            if ans > j:
                ans = j
print(ans)