T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N, K = map(int, input().split())
    result = 1

    def up(x):
        global result
        for i in range(x,x-K,-1):
            result = result*i
        return result
    def pac(x):
        global result
        if x == 1 or x==0:
            return 1
        result *= x
        pac(x-1)
        return result
            
    a = up(N)
    result = 1
    b = pac(K)
    print(f"#{test_case} {(a//b)%1234567891}")
    # n!
    # (n-k)!k!
    # 스택에 4 3 2 1