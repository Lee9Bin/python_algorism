
T = int(input())
result = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n= int(input())
    dart = []
    ans = 0
    for i in range(n):
        x ,y = map(int,input().split())
        dart.append((x*x+y*y))
    # 입력값 끝
    
    for i in dart:
        for j in range(20,210,20):
            if i <= j*j:
                ans+= 11-(j//20)
                break
    
    print(f"#{test_case} {ans}")
# 우선 xy좌표를 받아서 삼각형 만들어서 반지금 만들자
# 음수다 양수로 바꿔 왜? 그냥 1사분면으로 옮겨서 계산하면 되니깐
