T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    # n은 보드판 크기 m은 플레이어가 놓을 횟수
    graph = [[0 for i in range(n)] for i in range(n)]
    graph[n//2-1][n//2-1] = 2
    graph[n//2][n//2-1] = 1
    graph[n//2-1][n//2] = 1
    graph[n//2][n//2] = 2
    
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [-1,0,1,0,-1,1,1,-1]
    for i in range(m):
        y,x,player = map(int,input().split())
        y = y - 1
        x = x- 1
        color = player
        graph[x][y] = color
        for j in range(8):
            nextx = x + dx[j]
            nexty = y + dy[j]
            
            if nextx >= 0 and nexty>=0 and nextx<=n-1 and nexty<=n-1:
                if graph[nextx][nexty] == 0 or graph[nextx][nexty] == color:
                    continue
                else:
                    info = []
                    info.append((nextx,nexty))
                    while True:
                        nextx += dx[j]
                        nexty += dy[j]
                        if nextx >= 0 and nexty>=0 and nextx<=n-1 and nexty<=n-1:
                            if graph[nextx][nexty] == 0:
                                break
                            elif graph[nextx][nexty] == color:
                                while info:
                                    newx,newy = info.pop()
                                    graph[newx][newy] = color
                                break
                            else:
                                info.append((nextx,nexty))
                        else:
                            break
    white = 0
    black = 0
    for i in range(n):
        for j in range(n):
            if graph [i][j] == 2:
                black +=1
            elif graph[i][j] == 1:
                white +=1    
    print(f"#{test_case} {white} {black}")
