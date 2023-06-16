# 7 00
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    numlist = list(map(int, input().split()))
    cnt = 0
    nlist = []
    def dfs(start):
        global cnt
        for i in range(len(nlist)-1):
            if nlist[i] >= nlist[i+1]:
                return
        if len(nlist) > cnt:
            cnt = len(nlist)
        for i in range(start,n):
            nlist.append(numlist[i])
            dfs(i+1)
            nlist.pop()
            
    dfs(0)
    # 이거 백트래킹
    print(f"#{test_case} {cnt}")