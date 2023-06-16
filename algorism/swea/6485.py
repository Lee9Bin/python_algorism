T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    bus = []
    for i in range(n):
        a, b = map(int,input().split())
        bus.append((a,b))
    p = int(input())
    plist = []
    for i in range(p):
        plist.append(int(input()))
    result = []
    for i in plist:
        cnt = 0
        for j in bus:
            if j[0] <= i <=j[1]:
                cnt +=1
        result.append(cnt)
        
    print(f"#{test_case}",end=' ')
    for i in result:
        print(i,end=' ')
    print()