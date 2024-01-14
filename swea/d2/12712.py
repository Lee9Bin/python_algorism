T = int(input())

def diagonal(x,y):
    global total
    total += graph[x][y]

    for i in range(1,m):
        if x-i < 0 or y-i < 0:
            break
        else:
            total += graph[x-i][y-i]
    
    for i in range(1,m):
        if x+i >= n or y+i >= n:
            break
        else:
            total += graph[x+i][y+i]
            
    for i in range(1,m):
        if x-i < 0 or y+i >= n:
            break
        else:
            total += graph[x-i][y+i]
    
    for i in range(1,m):
        if x+i >= n or y-i < 0:
            break
        else:
            total += graph[x+i][y-i]
            

def straight(x,y):
    global total
    total += graph[x][y]

    # 좌
    for i in range(y-1, y-m,-1):
        if i < 0 or i >= n:
            break
        else:
            total += graph[x][i]
    # 우
    for i in range(y+1, y+m):
        if i < 0 or i >= n:
            break
        else:
            total += graph[x][i]
    # 상
    for i in range(x-1, x-m, -1):
        if i < 0 or i >= n:
            break
        else:
            total += graph[i][y]
    # 하
    for i in range(x+1, x+m):
        if i < 0 or i >= n:
            break
        else:
            total += graph[i][y]

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = []
    ans = 0

    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(n):
            total = 0
            straight(i,j)
            ans = max(ans, total)
            total = 0
            diagonal(i,j)
            ans = max(ans, total)
    print(f"#{test_case} {ans}")
    # print(graph)
        