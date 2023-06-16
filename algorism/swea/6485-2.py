T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    dp = [0] * 5001
    
    for i in range(n):
        a, b = map(int,input().split())
        
        for j in range(a,b+1):
            dp[j] += 1
    
    p = int(input())
    plist = []
    for i in range(p):
        num = int(input())
        plist.append(num)
    print(f"#{test_case}",end='')
    for i in plist:
        print(dp[i],end=' ')
    print()
    # print(f"#{test_case} {0}")