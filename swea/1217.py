
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    T = int(input())
    n,m = map(int,input().split())

    def jegob(x,y):
        if y == 0:
            return 1
        return x * jegob(x,y-1)
        
    
    print(f"#{test_case} {jegob(n , m)}")