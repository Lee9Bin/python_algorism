import sys
n = int(sys.stdin.readline())
dp = [0]*1001

dp[1] = 1
dp[2] = 2

# dp[i]를 만들기 위해서 i-1인 경우에 2*1만가지고 조합
#                   i-2인 경우에 1*2만가지고 조합
# 이렇게 하면 경우의 수가 겹치지 않고 모든경우의 수 조합 가능
# 체감상 점화식을 작성할때 경우의수를 만들어 감에 있어서 겹치지 않게 조합이 가능하게 짤 수 있는지가 중요하다고 느껴진다.

for i in range(3,n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n] % 10007)