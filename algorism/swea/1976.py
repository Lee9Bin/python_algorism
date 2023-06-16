T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    time = list(map(int,input().split()))


    a = time[0]+time[2]
    if a > 12:
        a = a-12

    b = time[1]+time[3]

    if b > 60:
        b = b - 60
        a += 1
    print(f"#{test_case} {a} {b}")