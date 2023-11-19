import sys

n = int(sys.stdin.readline())

numlist = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if numlist[j] > numlist[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))