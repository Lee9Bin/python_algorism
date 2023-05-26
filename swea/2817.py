T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    nlist = list(map(int,input().split()))
    # 입력받기 끝
    cnt = 0
    result = []
    def dfs(start):
        global cnt
        if sum(result) == k:
            cnt +=1
            return
        if sum(result) > k:
            return
        for i in range(start,n):
            if sum(result) < k:
                result.append(nlist[i])
                dfs(i+1)
                result.pop()
            
    dfs(0)
    print(f"#{test_case} {cnt}")
#  6 50