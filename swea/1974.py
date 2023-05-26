# 6시 10분
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    graph = []
    cnt =0
    for i in range(9):
        graph.append(list(map(int, input().split())))
       
    def check(x,y):
        global cnt
        parenum = 0
        parenum = graph[x][y]
        
        if parenum in graph[x][0:y] or parenum in graph[x][y+1:]:
            cnt +=1
        
        for i in range(x+1,9):
            if parenum == graph[i][y]:
                cnt +=1

        
        for i in range(3*(x//3),3*(x//3)+3):
            for j in range(3*(y//3),3*(y//3)+3):
                if i == x and j == y:
                    continue
                if graph[i][j] == parenum:
                    cnt +=1



    for i in range(9):
        for j in range(9):
            check(i,j)
    if cnt>0:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} 1")
