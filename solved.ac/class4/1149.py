import sys
n = int(sys.stdin.readline())
homes = []
for i in range(n):
    homes.append(list(map(int,sys.stdin.readline().split())))

# def back(start,cnt,result):
#     global ans
#     if cnt == n:
#         if ans > result:
#             ans = result
#         return
#     for i in range(3):
#         if i != start and result < ans:
#             back(i,cnt+1,homes[cnt][i]+result)
            
# for i in range(3):
#     back(i,0,0)
# print(ans)

dp = [[0 for i in range(3)] for i in range(n+1)]
for i in range(1,n+1):
    dp[i][0] = homes[i-1][0] + min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = homes[i-1][1] + min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = homes[i-1][2] + min(dp[i-1][0],dp[i-1][1])
print(min(dp[n]))