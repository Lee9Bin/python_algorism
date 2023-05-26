T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m  = map(int,input().split())
    graph = [[0 for i in range(n+1)]for i in range(n+1)]
    visited = [False]*(n+1)
    for i in range(m):
        x,y = map(int,input().split())
        graph[x][y] = 1
        graph[y][x] = 1    
    ans = 0
    def dfs(start):
        global ans
        visited[start] = True
        for i in range(1,n+1):
            if graph[start][i] == 1 and visited[i] == False:
                dfs(i)
                if ans < visited.count(True):
                    ans = visited.count(True)
                visited[i] = False
                
    for i in range(1,n+1):
        visited = [False]*(n+1)
        dfs(i)
    print(f"#{test_case} {ans}")
    
    # [0, 0, 0, 0], 
    # [0, 0, 1, 0], 
    # [0, 1, 0, 1], 
    # [0, 0, 1, 0]
    # 1