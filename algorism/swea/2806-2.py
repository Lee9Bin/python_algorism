# 6 00
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    cnt = 0
    queen = [0]*n #왜 이렇게 저장했지? n*n격자에서 0~n-1행까지 각 행에 퀸의 위치
    
    # 여기서 x인자는 행의 정보
    def dfs(x):
        global cnt
        if x == n:
            cnt +=1
            return
        
        for i in range(n):
            queen[x] = i #현재 행에 둘 위치 놓은다음에 이게 적적한지 판단을 해야해 어떻게 ?
            stop = True
            for j in range(x): #x가 행을 의미해 현재 행전까지 퀸의 의치를 토대로 여기다 놓아도 되는지 판단
                # 우선 같은 열에 있는지 대각선에 있는지 보려면 행끼리의 차 == 열끼리의 차 가 같음
                if queen[x] == queen[j] or abs(x-j) == abs(queen[x]-queen[j]):
                    stop = False
                    break
            if stop :
                dfs(x+1)
    # 격자에서 각행을 기준으로 어디에 뒀는지 저장하고 다음으로 넘겨 그런다음 어디에뒀는지
    # 기준으로 현재 행에서 둘수있는지 파악
    dfs(0)
    print(f"#{test_case} {cnt}")
