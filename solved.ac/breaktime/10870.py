import sys
n = int(sys.stdin.readline())
dp = [0] *(21)

dp[1] = 1
for i in range(2,21):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])