import sys
n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.readline().split()))

dp = [0] * (n+1)
for i in range(1,n+1):
    dp[i] = max(dp[i-1] + nlist[i-1],nlist[i-1])
print(max(dp[1:]))