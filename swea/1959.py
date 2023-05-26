T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a,b = map(int,input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))

    result = 0
    sub = 0
    if a <=b :
        for i in range(b-a+1):
            for j in range(a):
                sub += alist[j]*blist[i+j]
            if sub > result:
                result = sub
            sub=0
        print(f"#{test_case} {result}")
    else:
        for i in range(a-b+1):
            for j in range(b):
                sub += blist[j]*alist[i+j]
            if sub > result:
                result = sub
            sub=0
        print(f"#{test_case} {result}")

