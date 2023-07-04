import sys
t = int(sys.stdin.readline())
for i in range(t):
    m, n, x, y = map(int,sys.stdin.readline().split())
    # x를 기준
    k = x
    
    while k<= m*n:
        # 주의할점 나머지가 0인 경우 아래와 같이 처리
        if x == m or y == n:
            if x == m:
                x = 0
            if y == n:
                y = 0
        if k % m == x and k % n == y:
            break
        else:
            k += m
    if k > m*n:
        k = -1
    print(k)