# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    cnt = 1
    nlist = list(map(int, input().split()))

    while True:
        nown = nlist.pop(0)
        if nown - cnt >0:
            nown = nown - cnt
            cnt += 1
            nlist.append(nown)
        else:
            nown = 0
            nlist.append(nown)
            break
        if cnt == 6:
            cnt = 1
    # print(f"#{test_case}",end=' ')
    # for i in range(8):
    #     print(nlist.pop(0),end=' ')
    print("#",test_case,*nlist)
    # print(f"#{test_case} {0}")