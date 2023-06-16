T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    month = list(map(int, input().split()))
    monthlist = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month[0] == month[2]:
        print(f"#{test_case} {month[3]-month[1]+1}")
    else:
        sum = 0
        sum += monthlist[month[0]] - month[1] +1
        for i in range(month[0]+1,month[2]):
            sum += monthlist[i]
        
        sum += month[3]
        
        print(f"#{test_case} {sum}")