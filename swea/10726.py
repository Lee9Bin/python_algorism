# 
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    # 마지막자리 부터 n개 모두가 1인지 판단
    # 일단 m을 이진수로 만들어야ㅐ
    result = []
    while True :
        result.append(m%2)
        m = m//2
        if m == 0:
            break
    if 0 in result[:n] or len(result) < n:
        ans = 'OFF'
    else:
        ans ='ON'
    print(f"#{test_case} {ans}")