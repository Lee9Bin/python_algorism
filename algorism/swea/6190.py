T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nlist = list(map(int, input().split()))
    result = []
    for i in range(n):
        for j in range(i+1,n):
            a = nlist[i]* nlist[j]
            result.append(a)
    result.sort(reverse=True)
    ans = 0
    for i in result:
        for j in range(len(str(i))-1):
            if str(i)[j] > str(i)[j+1]:
                break
            if j == len(str(i))-2:
                ans = i
        if ans != 0:
            break
    if ans == 0:
        ans = -1
    print(f"#{test_case} {ans}")