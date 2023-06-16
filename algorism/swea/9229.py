T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m =map(int, input().split())
    snak = list(map(int, input().split()))
    cnt = 0
    ans = 0
    result = 0
    for i in range(n):
        if snak[i] <= m:
            ans = snak[i]
            cnt =1
            for j in range(i+1,n):
                if ans + snak[j] <= m:
                    ans += snak[j]

                    if result < ans:
                        result = ans
                    ans = ans - snak[j]
                cnt = 1
    if result == 0:
        result = -1
    print(f"#{test_case} {result}")