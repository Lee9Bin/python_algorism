# 문제가 원하는 것, 문제설명
# 계단의 갯수가 첫줄에 주어지고 그다음 줄부터 각계단의 점수를 입력 후
# 문제에 주어진 계단을 밟을 수 있는 규칙을 따라 최대값을 구하는 문제
# 어떻게 풀려고 하였는지 => 플로우차트
# 계단이 1개일때 2개일때... 최대값을 구하고 계단이 한개씩 늘어남에 따라 경우를 나누었다

# 코드 설명
n = int(input())
stair = list()
dp = [0] * 301 
for i in range(n):
    point = int(input())
    stair.append(point)
#  입력 받기 끝
dp[0] = stair[0] #계단이 한개일때는 그 자체가 최대값
for i in range(1,n):
    if i == 1:
        dp[i] = stair[0] + stair[1] #계단이 두개일때
    elif i == 2:
        dp[i] = max(stair[0]+stair[2],stair[1]+stair[2]) #계단이 3개일때
    else:
        dp[i] = max(dp[i-3]+stair[i]+stair[i-1],dp[i-2]+stair[i])
    #계단이 4개이상일 때부터는 문제에 주어진 규칙에 의해서 3개의 계단을 연달아
    #밟을 수 없기에 3칸뒤에 계단, 2칸 뒤에 계단을 기준으로 비교
print(dp[n-1]) 
