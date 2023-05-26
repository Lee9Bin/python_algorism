T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    numlist = list(map(int, input().split()))
    numlist.sort()
    sublist = list(set(numlist))
    sublist.sort()
    maxcnt = 0
    for i in sublist:

        if maxcnt <= numlist.count(i):
            maxcnt = numlist.count(i)
            result = i 
    print(f"#{tc} {result}")   