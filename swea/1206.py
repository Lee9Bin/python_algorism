# 100
# 0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 ...
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    bilding = list(map(int,input().split()))
    result = 0
    left = 0
    right = 0


    for i in range(2,n-2):
        left = max(bilding[i-1],bilding[i-2])
        right = max(bilding[i+1],bilding[i+2])
        if left < bilding[i] and right < bilding[i]:
            result += bilding[i] - max(left,right)

    print(f"#{test_case} {result}")

""" 
시나리오
왼쪽값 두개중 작은값 하나 선택 오른쪽 값 작은값 하나 선택

"""