# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    nlist = []
    ans = 0
    result = 0
    result2 = 0
    
    for i in range(100):
        nlist.append(list(map(int, input().split())))
        
    for i in range(100):
        for j in range(100):
            result += nlist[j][i]
            result2 = sum(nlist[j])
            if result2 > ans:
                ans = result2
        if result > ans:
            ans = result
        result = 0
        result2 = 0
        
    for i in range(100):
        result += nlist[i][i]
        result2 += nlist[99-i][i]
    if result > ans:
        ans = result
    if result2 > ans:
        ans = result2
    print(f"#{test_case} {ans}")
    
    # 10분