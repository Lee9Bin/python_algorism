# 문제설명: 배열에서 연속적으로 나타나는 경우 하나만 남기고 중복을 제거한다.
# 해결전략
# 첫 번째 매겨변수로 들어온 배열을 앞에서 부터 차례대로 확인을 할것인지
# 첫 번쩨 인덴스 위치를 기준으로 값을 비교하면서 배열에서 삭제하면 되는데 쉽지않다
# why? 배열에서 1    1    3   3   0   1   1
#           현재 비교할수
#           현재 == 비교할 수 이지만 제거하는 것이 어렵다.   
# 두 번재 들어온 배열을 하나씩 꺼내서 다른 곳에 넣어가면서 확인 할 것인지 
# -> 스택을 활용해볼 수 있겠다 why? 다른 곳이라는 컵에 배열에 숫자들을 하나씩 넣어보면서 맨위에 숫자와 같으면 제거하면 된다.
def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1,len(arr)):
        if arr[i] == answer[-1]:
            continue
        else:
            answer.append(arr[i])
            
    return answer