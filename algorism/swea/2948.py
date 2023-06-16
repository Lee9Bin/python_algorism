# 
T = int(input())
result = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    nlist = list(map(str, input().split()))
    mlist = list(map(str, input().split()))
    nmlist = nlist+mlist
    ans = 0
    
    nmlist.sort()
    start = 0
    end = 1
    while start < len(nmlist) and end < len(nmlist):
        if nmlist[start] == nmlist[end]:
            ans +=1
            start +=2
            end = start+1
        else:
            start = end
            end +=1
    print(f"#{test_case} {ans}")