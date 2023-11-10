for t in range(1,11):
    graph = []
    n = int(input())
    for i in range(100):
        graph.append(list(map(int,input().split())))
    
    row = 0
    col = 0
    leftDiagonal = 0
    rightDiagonal = 0
    for i in range(100):
        row = max(row,sum(graph[i])) #행 처리
        total = 0
        for j in range(100):
            if i == j: #왼쪽 아래 대각
                leftDiagonal += graph[i][j]
            if (99-i) == j: #오른쪽 아래 대각
                rightDiagonal += graph[i][j]
            total += graph[j][i]
        col = max(col,total)
        
    print(f"#{n} {max(row,col,leftDiagonal,rightDiagonal)}")