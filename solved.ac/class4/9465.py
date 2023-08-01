import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    stiker = []
    for i in range(2):
        stiker.append(list(map(int,sys.stdin.readline().split())))    
    dp = [[0 for i in range(n+1)] for i in range(2)]
    dp[0][1] = stiker[0][0]
    dp[1][1] = stiker[1][0]
    for i in range(2,n+1):
        dp[0][i] = max(dp[1][i-2],dp[1][i-1])+stiker[0][i-1]
        dp[1][i] = max(dp[0][i-2],dp[0][i-1])+stiker[1][i-1]
    print(max(dp[0][n],dp[1][n]))