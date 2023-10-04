import sys
ddr = list(map(int,sys.stdin.readline().split()))

# 3차원 디피 .... 코드 해석하고 이해할 것
dp = [[[1e9 for i in range(5)] for i in range(5)] for i in range(len(ddr)+1)]
dp[0][0][0] = 0
def cost(now, nextw):
    if now == nextw:
        return 1
    elif now == 0:
        return 2
    elif abs(now - nextw) == 2:
        return 4
    else:
        return 3

for i in range(1,len(ddr)):
    nextw = ddr[i-1]
    for left in range(5):
        for rigth in range(5):
            dp[i][nextw][rigth] = min(dp[i][nextw][rigth], dp[i-1][left][rigth] + cost(left,nextw))
            dp[i][left][nextw] = min(dp[i][left][nextw], dp[i-1][left][rigth] + cost(rigth,nextw))

result = 1e9
for i in range(5):
    for j in range(5):
        result = min(result,dp[len(ddr)-1][i][j])
print(result)
# 그리디로 해결해보려 했지만 반례가 존재
# start = [[0,0] for i in range(len(ddr))]
# result = 0

# for i in range(1,len(ddr)):
#     left = 0
#     rigth = 0
#     if start[i-1][0] == 0 and start[i-1][1] == 0:
#         left = 2
#         right = 2
#     if start[i-1][0] == 0 and start[i-1][1] != 0:
#         left = 2
#         if abs(start[i-1][1]-ddr[i-1]) != 2 and abs(start[i-1][1]-ddr[i-1]) != 0:
#             right = 3
#         elif abs(start[i-1][1]-ddr[i-1]) == 0:
#             right = 1
#         elif abs(start[i-1][1]-ddr[i-1]) == 2:
#             right = 4
        
#     if start[i-1][0] != 0 and start[i-1][1] == 0:
#         right = 2
#         if abs(start[i-1][0]-ddr[i-1]) != 2 and abs(start[i-1][0]-ddr[i-1]) != 0:
#             left = 3
#         elif abs(start[i-1][0]-ddr[i-1]) == 0:
#             left = 1
#         elif abs(start[i-1][0]-ddr[i-1]) == 2:
#             left = 4
        
#     if start[i-1][0] != 0 and start[i-1][1] != 0:
#         if abs(start[i-1][0]-ddr[i-1]) != 2 and abs(start[i-1][0]-ddr[i-1]) != 0:
#             left = 3
#         elif abs(start[i-1][0]-ddr[i-1]) == 0:
#             left = 1
#         elif abs(start[i-1][0]-ddr[i-1]) == 2:
#             left = 4
        
#         if abs(start[i-1][1]-ddr[i-1]) != 2 and abs(start[i-1][1]-ddr[i-1]) != 0:
#             right = 3
#         elif abs(start[i-1][1]-ddr[i-1]) == 0:
#             right = 1
#         elif abs(start[i-1][1]-ddr[i-1]) == 2:
#             right = 4
#     print(left,right)
#     if left <= right:
#         start[i][0] = ddr[i-1]
#         start[i][1] = start[i-1][1]
#         result += left
#     else:
#         start[i][0] = start[i-1][0]
#         start[i][1] = ddr[i-1]
#         result += right
# print(result)