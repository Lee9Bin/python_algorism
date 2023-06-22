import sys

t = int(sys.stdin.readline())
dp = [0] * 101
dp[1],dp[2],dp[3] = 1,1,1
dp[4],dp[5] = 2,2
for i in range(t):
    n = int(sys.stdin.readline())
    for j in range(6,n+1):
        if dp[j] == 0:
            dp[j] = dp[j-1] + dp[j-5]
    print(dp[n])

#  9 8+4
#  8 7+3
#  7 6+2