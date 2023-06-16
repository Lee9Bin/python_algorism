# 5 22
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(str, input())))
    ans = 'NO'
    def bfs(x,y):
        global ans
        dx = [0,0,1,-1,1,1,-1,-1]
        dy = [1,-1,0,0,-1,1,1,-1]
        for i in range(8):
            cnt = 1
            nextx = x+ dx[i]
            nexty = y+ dy[i]
            while True:
                if nextx >= 0 and nexty >= 0 and nextx<=n-1 and nexty<=n-1:
                    if graph[nextx][nexty] == 'o':
                        cnt +=1
                        nextx += dx[i]
                        nexty += dy[i]
                    else:
                        break
                else:
                    break
            if cnt >= 5:
                ans = "YES"
    # 한놈을 기준으로 뻗어나가면서 5개가 채워지면 패스
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'o':
                bfs(i,j)
                if ans == "YES":
                    break
    print(f"#{test_case} {ans}")