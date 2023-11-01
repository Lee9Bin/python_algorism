t = int(input())

for tc in range(t):
    n, m = map(int,input().split())
    graph = []
    
    for i in range(n):
        graph.append(list(map(int,input().split())))
    
    maxWing = 0
    for x in range(n-m+1):
        for y in range(n-m+1):
            total = 0
            for i in range(x,x+m):
                for j in range(y,y+m):
                    total += graph[i][j]
            if maxWing < total:
                maxWing = total
    print(f"#{tc+1} {maxWing}")