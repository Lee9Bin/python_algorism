import sys
n = int(sys.stdin.readline())
numlist = list(map(int,sys.stdin.readline().split()))

cnt = int(sys.stdin.readline())

dp = [0] *(n+1)

for i in range(1,n+1):
    dp[i] = dp[i-1] + numlist[i-1]

for i in range(cnt):
    a,b = map(int,sys.stdin.readline().split())
    print(dp[b]-dp[a-1])