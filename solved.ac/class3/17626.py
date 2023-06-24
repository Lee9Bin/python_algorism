import sys

n = int(sys.stdin.readline())
dp = [1e9] * 50001

dp[1] = 1  #1^2
dp[2] = 2  #1^2 + 1^2
dp[3] = 3  #1^2 + 1^2 +1^2

for i in range(4,n+1):
    if(i**0.5)-int(i**0.5) == 0:
        dp[i] = 1
        continue
    else:
        for j in range(2,int(i**0.5)):
            dp[i] = min((dp[(j)**2] + dp[i-((j)**2)]),dp[i])

print(dp[n])

