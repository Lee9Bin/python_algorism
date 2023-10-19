import sys
k = int(sys.stdin.readline())
dp = [[0,0]for i in range(k+1)]
dp[0] = [1,0]

for i in range(1,k+1):
    a, b = dp[i-1]
    dp[i][0] += b
    dp[i][1] += a + b
print(*dp[k])