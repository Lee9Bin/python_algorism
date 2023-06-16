# 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    thing = []
    ans = 0
    dp = [[0 for i in range(k+1)] for i in range(n+1)]
    for i in range(n):
        thing.append(list(map(int, input().split())))
        
    for i in range(1,n+1):

        size, value = thing[i-1]
        for j in range(1,k+1):
            if size <=j:
                dp[i][j] = max(dp[i-1][j-size]+value,dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
            if ans < dp[i][j]:
                ans = dp[i][j]
    print(f"#{test_case} {ans}")
    
    