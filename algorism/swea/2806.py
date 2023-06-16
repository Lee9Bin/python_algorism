# 6 00
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    ans = 0
    visited = [0] * n
    
    def check(x):
        for i in range(x):
            if visited[x] == visited[i] or abs(x-i) == abs(visited[x]-visited[i]):
                return False
        
        return True
    
    def dfs(x):
        global ans
        # 맨 아래 행까지 갔으면 스톱1
        if x == n:
            ans +=1
            return
        # 현재 행에서 놓을수 있는지 체크 다 만약 놓을수 있으면 재귀함수 실행
        # 현재행에 놓을수 있는지 없는지 어떻게 체크할거지 ?
        for i in range(n):
            visited[x] = i
            if check(x):
                dfs(x+1)
    dfs(0)
    print(f"#{test_case} {ans}")
