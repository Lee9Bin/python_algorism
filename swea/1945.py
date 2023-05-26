T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    a,b,c,d,e = 0,0,0,0,0

    while n > 1:
        if n % 2 == 0:
            n = n /2
            a += 1
        if n % 3 == 0:
            n = n /3
            b+=1
        if n % 5 == 0:
            n = n /5
            c+=1
        if n % 7 == 0:
            n = n /7
            d+=1
        if n % 11 == 0:
            n = n /11
            e+=1
    print(f"#{test_case} {a} {b} {c} {d} {e}")
