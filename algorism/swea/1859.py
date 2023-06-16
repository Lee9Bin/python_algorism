# 6시 55분
# 조건 
# 한번에 많은 양 X
# 1. 연속된 N일 동안의 물건의 매매가를 예측하여 알고있다
# 2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입 가능
# 3. 판매는 얼마든지 가능

# 시나리오
# 우선 N값 저장해서 입력되는 순서대로 저장
# 차익을 보려면 어떤날에 구매를 했다면 뒤에날에 
# 구매한 가격보다 높은 값이 존재해야해
# price 리스트에 저장된 값들을 가져와서 뒤에 값들과 비교에서 차익 ㄱㄱ


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    
    result = 0 #결과값 담기
    maxnum = 0
    for i in price:
        if i > maxnum:
            maxnum = i
        else:
            result = result + maxnum-i
        
    print(f"#{test_case} {result}")