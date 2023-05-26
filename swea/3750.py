# 7 00
T = int(input())
result = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = input()
    ans = 0
    def hab(num):
        global ans
        mlist = list(map(int, str(num)))
        if sum(mlist)>= 10:
            hab(sum(mlist))
        else:
            ans = sum(mlist)
            return
    hab(int(n))
    result.append(ans)
for i in range(T):
    print(f"#{i+1} {result[i]}")
# 재귀함수