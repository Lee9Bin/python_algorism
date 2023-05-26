# 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    l,u,x = map(int,input().split())
    ans = 0
    if l<= x <= u:
        ans = 0
    elif x< l:
        ans = l-x
    else:
        ans = -1
        
    print(f"#{test_case} {ans}")