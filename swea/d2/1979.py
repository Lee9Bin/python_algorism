t = int(input())

for tc in range(1,t+1):
    n, k = map(int,input().split())
    graph = []
    visited = [[False for i in range(n)] for i in range(n)]
    for i in range(n):
        graph.append(list(map(int,input().split())))
    dx = [0,1]
    dy = [1,0]
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[i][j] == 1:
                cnt +=1
            else:
                if cnt == k:
                    ans +=1
                cnt = 0
        if cnt == k:
            ans += 1
    for j in range(n):
        cnt = 0
        for i in range(n):
            if graph[i][j] == 1:
                cnt +=1
            else:
                if cnt == k:
                    ans +=1
                cnt = 0
        if cnt == k:
            ans += 1
    print(f"#{tc} {ans}")