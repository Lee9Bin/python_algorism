import sys

n = int(sys.stdin.readline())

grape = [0]

for i in range(n):
    grape.append(int(sys.stdin.readline()))
    
dp = [0] * (n+1)
dp[1] = grape[1]
if n >= 2:

    dp[2] = grape[1] + grape[2]

    for i in range(3, n+1):
        dp[i] = max((dp[i-3] + grape[i] + grape[i-1]), (grape[i] + dp[i-2]))
        dp[i] = max(dp[i],dp[i-1])
print(dp[-1])