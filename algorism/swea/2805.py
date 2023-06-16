# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = int(input())
for test_case in range(1, T+1):
    
    n = int(input())
    nlist=[]
    ans = 0
    for i in range(n):
        nlist.append(list(map(int, input())))
    
    mid = (n-1)//2
    for i in range(mid+1):
        for j in range(mid-i,mid+i+1):
            ans += nlist[i][j] + nlist[n-i-1][j]
    print(f"#{test_case} {ans-sum(nlist[mid])}")