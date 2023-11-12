# 문제설명: 배열이 뜻하는 것 
#        1일차 주식가격, 2일차 주식가격 , ....
#        각 n일차 주식가격을 비교할때 며칠만큼 주식의 가격이 안떨어지는지 구하기
# 생각한 풀이
# 앞에서 값을 꺼내야한다 -> 큐
from collections import deque
def solution(prices):
    answer = []
    que = deque(prices)
    
    while que:
        ans = 0
        nowNum = que.popleft()
        
        
        # 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
        # 잘 해석할것
        for i in que:
            ans += 1
            if nowNum > i:
                break
        
        answer.append(ans)
    return answer