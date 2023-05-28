import sys

N, M = map(int,sys.stdin.readline().split())
dp = [0]*(M+1)
wdp = [0]
obj = []
for i in range(N):
    obj.append(list(map(int,sys.stdin.readline().split())))
    
for i in range(1,M+1):
    for j in obj:
        weight , value = obj[i]
        if weight <= i and wdp[0]<=M:
            dp[i] = max(value + dp[i-weight], value)
        else:
            dp[i] = 0
            
print(dp)
# 다시 공부