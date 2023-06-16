T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    dis = 0
    speed = 0

    for i in range(n):
        state = list(map(int,input().split()))
        
        if len(state) > 1:
            if state[0] == 1:
                speed += state[1]
            else:
                if state[1] > speed:
                    speed = 0
                else:
                    speed -= state[1]
            dis += speed
        else:
            dis += speed
    print(f"#{test_case} {dis}")
