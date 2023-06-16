# 6시 07분
#달팽이 숫자란 n*n격자 모양에서 시계모양으로 숫자가 커짐
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    
    graph = [[0 for i in range(n)] for i in range(n)]
    visited = [[False for i in range(n)] for i in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    nowx,nowy = 0,0
    graph[nowx][nowy] = 1
    visited[nowx][nowy] = True
    v = 0
    cnt = 0
    while True:
        if cnt == n*n-1:
            break
        if v == 4:
            v = 0 
        nextx , nexty = nowx+dx[v], nowy+dy[v]
        if nextx >=0 and nexty>=0 and nextx<=n-1 and nexty<=n-1 and visited[nextx][nexty] == False:
            graph[nextx][nexty] = graph[nowx][nowy] +1
            visited[nextx][nexty] = True
            nowx,nowy = nextx,nexty 
            cnt +=1
        elif nextx < 0 or nexty<0 or nextx>n-1 or nexty>n-1 or visited[nextx][nexty] == True:
            v+=1
         
    print(f'#{test_case}')
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=' ')
        print()
    
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    
    graph = [[0 for i in range(n)] for i in range(n)]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    v = 0
    nowx, nowy = 0,0
    
    
    for i in range(1,n*n+1):
        graph[nowx][nowy] = i
        nowx = nowx + dx[v]
        nowy = nowy + dy[v]
        
        if nowx < 0 or nowy < 0 or n <= nowx or n <= nowy or graph[nowx][nowy] != 0:
            nowx = nowx - dx[v]
            nowy = nowy - dy[v]
            
            v = (v+1)%4
            nowx = nowx + dx[v]
            nowy = nowy + dy[v]
    print(graph)