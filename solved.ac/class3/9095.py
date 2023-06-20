import sys
t = int(sys.stdin.readline())
dp = [0] * 12

# 1일 경우 한가지
dp[1] = 1  # 1
dp[2] = 2  # 1,1 2
dp[3] = 4
# 디피가 떠오르지 않아 백트래킹으로 풀이
# def back():
#     global result
#     global maxnum
#     if sum(nlist) >= maxnum:
#         if sum(nlist) == maxnum:
#             result +=1
#         return
    
#     for i in (1,2,3):
#         if sum(nlist) < maxnum:
#             nlist.append(i)
#             back()
#             nlist.pop()
# for i in range(t):
#     nlist= []
#     maxnum = int(input())
#     result = 0
#     back()
#     print(result)


# 디피 점화식 규칙찾기 실전에서는 디피인거 인지하고 떠오르지 않는다면 직관적으로라도 찾기
# 1: 1
# 2: 1+1
#    2
# 3: 2를 만드는 경우의 수에 1만 더하기 2가지 +1  (1,1,1) (2,1)
#    1을 만드는 경우의 수에 2만 더하기 1가지 +2  (1+2)
#    0을 만드는 경우의 수에 3만 더하기 0가지+ 3  (3)
# 이렇게 기준을 잡아주면 1,2,3을 조합해서 만들때 겹치지 않게돼
# 즉, dp[n] = d[n-1] + dp[n-2] +dp[n-3]
for i in range(t):
    n = int(sys.stdin.readline())
    for j in range(4,n+1):
        if dp[j] == 0:
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[n])