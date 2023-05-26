#3시 43분

#2차원 배열이다. 탐색 문제인가 ?

#N*N의 행렬이 주어질때 이안에 N*N의 모양의 최대값
# 그래프를 포문 돌아서 각각을 더해주려 했는데 코드가 안짜져
# 다른 방법을 고민
# 

    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m,n = map(int,input().split())
    graph = []
    dp = [[0 for i in range(m)] for i in range(m)]
    
    for i in range(m):
        graph.append(list(map(int, input().split())))
    
    def hab(x,y):
        result = 0
        for i in range(x,x+n):
            for j in range(y,y+n):
                result += graph[i][j]
        return result
    
    for i in range(m-n+1):
        for j in range(m-n+1):
            dp[i][j]=hab(i,j)
    print(max(max(dp)))
    # print(f"#{test_case} {maxhab}")
        
    