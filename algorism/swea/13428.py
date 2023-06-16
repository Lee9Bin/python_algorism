# 1 40
T = int(input())
for test_case in range(1, T + 1):
    nlist = list(map(int, input()))
    length = len(nlist)
    ans = []
    for i in range(length):
        for j in range(i+1,length):
            if nlist[i] > nlist[j]:
                nlist[i],nlist[j] = nlist[j],nlist[i]
                if nlist[0] != 0:
                    ans.append(''.join(map(str,nlist)))
                nlist[i],nlist[j] = nlist[j],nlist[i]
    if not ans:
        ans.append(''.join(map(str,nlist)))
    for i in range(length):
        for j in range(i+1,length):
            if nlist[i] < nlist[j]:
                nlist[i],nlist[j] = nlist[j],nlist[i]
                ans.append(''.join(map(str,nlist)))
                nlist[i],nlist[j] = nlist[j],nlist[i]
    print(f"#{test_case} {min(ans)} {max(ans)}")
# 인덱스 기준으로 뽑아서 자리 바꾸려 했지만 숫자가 중복될수도 있다....... 그럼 제일큰 자리의 인덱스를 뽑아야한다
# 240