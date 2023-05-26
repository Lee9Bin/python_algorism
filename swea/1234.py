# 5 43

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n, m  = map(str,input().split())
    n = int(n)
    mlist = [m[0]]
    for i in m[1:]:
        if not mlist:
            mlist.append(i)
            continue
        if mlist[-1] != i :
            mlist.append(i)
        else:
            mlist.pop()
    ans = ''.join(mlist)
    print(f"#{test_case} {ans}")