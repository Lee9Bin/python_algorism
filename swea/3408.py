# 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n  = int(input())
    s1 = (1+n)/2*n
    s2 = (1+2*n-1)*n/2
    s3 = (2+2*n)*n/2
    print(f"#{test_case} {int(s1)} {int(s2)} {int(s3)}")
    