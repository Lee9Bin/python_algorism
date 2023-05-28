import sys

n = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(n):
    for j in range(i, n):
        if numlist[i] < numlist[j]:
            dp[j] = max(dp[i] + 1, dp[j])
print(max(dp))
