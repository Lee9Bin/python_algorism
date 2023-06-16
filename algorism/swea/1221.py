# 6 20
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numlist = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    tc , n = map(str, input().split())
    n = int(n)
    arr = list(map(str, input().split()))
    result = []
    ans = []
    # 입력받은 리스트 가져와서 하나씩 꺼내
    for i in arr:
        # 타겟을 가져와서 사전에서 가져와
        for j in numlist:
            if i == j:
                result.append(numlist.index(j))
                break
    result.sort()
    for i in result:
        ans.append(numlist[i])
    print(f"#{test_case}")
    print(*ans)