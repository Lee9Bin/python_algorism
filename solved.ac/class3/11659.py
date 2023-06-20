import sys
n, m =map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

dp = [0]*(n+1)
dp[1] = nlist[0]
for i in range(2,n+1):
    dp[i] = dp[i-1] + nlist[i-1]

for j in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j]-dp[i-1])