t = int(input())

for tc in range(1,t+1):
    n = int(input())
    graph = []
    
    for i in range(n):
        graph.append(list(map(int,input().split())))
    
    #90도 회전
    print(f"#{tc}")
    for i in range(n):
        for j in range(n):
            if j == n-1:
                print(graph[n-1-j][i],end=" ")
            else:
                print(graph[n-1-j][i],end="")
        for j in range(n):
            if j == n-1:
                print(graph[n-1-i][n-1-j],end=" ")
            else:
                print(graph[n-1-i][n-1-j],end="")
        for j in range(n):
            if j == n-1:
                print(graph[j][n-1-i],end=" ")
            else:
                print(graph[j][n-1-i],end="")
        print()