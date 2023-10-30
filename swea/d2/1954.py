t = int(input())

for tc in range(1,t+1):
    n = int(input())
    graph = [[0 for i in range(n)] for i in range(n)]
    
    nowx = 0
    nowy = -1
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    nowi = 0
    for i in range(1,n*n+1):
        nextx = nowx + dx[nowi%4]
        nexty = nowy + dy[nowi%4]
        
        if nextx >= 0 and nexty >= 0 and nextx < n and nexty < n and graph[nextx][nexty] == 0:
            graph[nextx][nexty] = i
        else:
            nowi += 1
            nextx = nowx + dx[nowi%4]
            nexty = nowy + dy[nowi%4]
            graph[nextx][nexty] = i
        nowx = nextx
        nowy = nexty
    print(f"#{tc}")
    for i in graph:
        print(*i)