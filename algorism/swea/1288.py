T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nlist = list()
    cnt = 1


    while len(nlist) < 10:
        a = str(n*cnt)
        for i in a:
            if i not in nlist:
                nlist.append(i)
        cnt +=1
    print(f"#{test_case} {n*(cnt-1)}")