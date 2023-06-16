# 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    student = list(map(int,input().split()))
    ans = []
    
    # for i in range(1,n+1):
    #     if i not in student:

    # # for i in all:
    # #     if i not in student:
    # #         ans.append(i)
    # # ans.sort()
    # # print(f"#{test_case}",end=' ')
    # # print(*ans)