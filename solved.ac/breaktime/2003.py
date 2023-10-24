import sys
n, m = map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))

dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = dp[i-1] + numlist[i-1]

ans = 0
left = 0
right = n
while left < right:
    if dp[right] < m:
        break

    if dp[right] - dp[left] <= m:
        if dp[right] - dp[left] == m:
            ans += 1
        left = 0
        right -= 1
    elif dp[right] - dp[left] > m:
        left += 1

    if right == left:
        left = 0
        right -=1


print(ans)