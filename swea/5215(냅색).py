# 1
# 5 1000
# 100 200
# 300 500
# 250 300
# 500 1000
# 400 400	
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, totalcal = map(int,input().split())
    food = [[0,0]]
    for i in range(n):
        food.append(list(map(int,input().split())))
    dp = [[0 for i in range(totalcal+1)] for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,totalcal+1):
            like,cal = food[i]
            if cal <= j:
                dp[i][j] = max(like+dp[i-1][j-cal],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(f"#{test_case} {dp[n][totalcal]}")