# 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    ans = -1
    for i in range(int(n**(1/3))+1,1,-1):
        if i**3 == n:
            ans = i
            break
    print(f"#{test_case} {ans}")