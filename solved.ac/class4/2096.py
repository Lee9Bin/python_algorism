import sys
n = int(sys.stdin.readline())

dp = [[0 for i in range(3)] for i in range(2)]
for i in range(1,n+1):
    now1,now2,now3  = dp[0][0],dp[0][1],dp[0][2]
    a,b,c = map(int,sys.stdin.readline().split())
    dp[0][0] = max(now1,now2) + a
    dp[0][1] = max(now1,now2,now3) + b
    dp[0][2] = max(now2,now3) + c
    now1,now2,now3  = dp[1][0],dp[1][1],dp[1][2]
    dp[1][0] = min(now1,now2) + a
    dp[1][1] = min(now1,now2,now3) + b
    dp[1][2] = min(now2,now3) + c
print(max(dp[0]), min(dp[1]))
