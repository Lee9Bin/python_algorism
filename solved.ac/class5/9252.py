import sys
first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
dp=[["" for i in range(len(first)+1)] for i in range(len(second)+1)]

result = ""
for i in range(1,len(second)+1):
    for j in range(1,len(first)+1):
        if second[i-1] == first[j-1]:
            dp[i][j] += dp[i-1][j-1] + second[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] += dp[i-1][j]
            else:
                dp[i][j] += dp[i][j-1]
            # dp[i][j] += max(dp[i-1][j],dp[i][j-1])

print(len(dp[-1][-1]))
print(dp[-1][-1])