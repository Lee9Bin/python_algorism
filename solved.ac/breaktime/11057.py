import sys
n = int(sys.stdin.readline())

dp = [[1 for i in range(10)] for i in range(1002)]

for i in range(2,1002):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])% 10007
print(dp[n+1][0])