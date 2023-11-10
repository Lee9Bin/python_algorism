t = int(input())

for tc in range(1,t+1):
    n = int(input())
    graph = []
    
    for i in range(n):
        graph.append(list(map(str,input())))
    
    total = 0
    
    for i in range(n//2+1):
        for j in range(n//2-i,n//2+i+1):
            total += int(graph[i][j]) +int(graph[n-1-i][j])
            
    for i in range(n):
        total -= int(graph[n//2][i])
    print(f"#{tc} {total}")