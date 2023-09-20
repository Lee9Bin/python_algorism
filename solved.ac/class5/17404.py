import sys
n = int(sys.stdin.readline())
homes =[]
ans = 1e9
for i in range(n):
    homes.append(list(map(int,sys.stdin.readline().split())))
    

for k in range(3):
    dp = [[1e9 for _ in range(3)] for _ in range(n)]
    dp[0][k] = homes[0][k]
    for i in range(1,n):
        dp[i][0] = homes[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = homes[i][1] + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = homes[i][2] + min(dp[i-1][0],dp[i-1][1])
    for j in range(3):
        if k != j:
            ans = min(ans,dp[n-1][j])
print(ans)