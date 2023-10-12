import sys

N, M = map(int,sys.stdin.readline().split())
# dp = [0]*(M+1)
# wdp = [0]
# obj = []
# for i in range(N):
#     obj.append(list(map(int,sys.stdin.readline().split())))
    
# for i in range(1,M+1):
#     for j in obj:
#         weight , value = obj[i-1]
#         if weight <= i and wdp[0]<=M:
#             dp[i] = max(value + dp[i-weight], value)
#         else:
#             dp[i] = 0
            
# print(dp)
# 다시 공부
dp = [[0 for i in range(M+1)] for i in range(N+1)]
obj = []
for i in range(N):
    obj.append(list(map(int,sys.stdin.readline().split())))
for i in range(1,N+1):
    weight, value = obj[i-1]
    for j in range(1,M+1):
        if weight <= j:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight]+value)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][M])