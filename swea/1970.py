#3시 57분
# 거스름돈 제목만 보면 누가봐도 그리디 탐욕


changemoney = [50000, 10000 , 5000, 1000 , 500, 100 , 50, 10]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    money = int(input())
    result= list()
    
    for i in changemoney:
        result.append(money//i)
        money = money%i
    print(f"#{test_case}")
    for i in result:    
        print(i,end=' ')
    print()