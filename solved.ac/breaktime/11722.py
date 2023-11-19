import sys

n = int(sys.stdin.readline())

numlist = list(map(int, sys.stdin.readline().split()))
numlist.reverse()
print(numlist)
dp = [1] * n

for i in range(1,n):
    for j in range(i, n):
        if numlist[j] < numlist[i]:
            dp[j] = max(dp[i]+1, dp[j])
print(max(dp))