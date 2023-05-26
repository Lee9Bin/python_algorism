# 6 00
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    cnt = 0
    queen = [] #왜 이렇게 저장했지? n*n격자에서 0~n-1행까지 각 행에 퀸의 위치
    
    # 여기서 x인자는 행의 정보
    def dfs(x):
        
        global cnt
        if x == n:
            cnt +=1
            return
        # x행일때 x,y좌표 담기
        for y in range(n):
            queen.append((x,y))
            
            # 담고나서 담아두 되는건지 체크
            for queens in queen[:x]:
                if queens[1] == y or abs(x-queens[0]) == abs(y-queens[1]):
                    queen.pop()
                    break
            if len(queen)==x+1:
                dfs(x+1)
                queen.pop()

    dfs(0)
    print(f"#{test_case} {cnt}")
