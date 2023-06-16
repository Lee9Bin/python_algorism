T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    graph = []
    
    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    graph90 = [[0 for i in range(n)] for i in range(n)]
    graph180 = [[0 for i in range(n)] for i in range(n)]
    graph270 = [[0 for i in range(n)] for i in range(n)]
    
    print(f"#{test_case}")
    for i in range(n):
        for j in range(n):
            graph90[i][j] = graph[n-1-j][i] 
    
    for i in range(n):
        for j in range(n):
            graph180[i][j] = graph90[n-1-j][i] 
    
    for i in range(n):
        for j in range(n):
            graph270[i][j] = graph180[n-1-j][i] 
            
    for i in range(n):
        for j in range(n):
            print(graph90[i][j],end='')
        print(end=' ')
        for j in range(n):
            print(graph180[i][j],end='')
        print(end=' ')
        for j in range(n):
            print(graph270[i][j],end='')
        print(end=' ')
        print()
    
    
"""    90   180  270
0,0 -> 0,2   n-1,n-1
0,1 -> 1,2
0,2 -> 2,2

1,0-> 0,0
1,1 ->1,1
1,2 ->2,2

2,0-> 0,0
2,1-> 1,0
2,2-> 2,0

0,0 -> 2,0
0,1 -> 1,0
0,2 -> 0,0
"""
                
        
# n n행렬 시계방향으로 90도 180도 270도 회전
