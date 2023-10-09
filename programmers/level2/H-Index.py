# 문제설명: 논문이 인용된 횟수가 주어진 배열이 들어온다. -> 배열의 길이가 논문의 갯수
#         임의의 값 h값을 정해 h번이하 만큼 인용된 논문의 갯수
#         h번 이상 인용된 논문의 갯수를 up 변수에
#         h번 미만으로 인용된 논문의 갯수를 down변수에
#         이때 up개수가 h보다 크거나 같고 down갯수가 h보다 작거난 같은 경우를 H-Index라고한다.
#         최대값 찾기
# 문제 해결전략
# 최대값을 찾아야 하므로 큰값부터 비교해서 찾아 나가기
# 배열 정렬해서 큰값 찾기
# 큰값부터 -1 해가면서 조건에 맞는지 파악하고 맞으면 break
# 처음에는 배열요소에 있는 인용횟수만 체크하는 실수를 했다.

def solution(citations):
    answer = 0
    citations.sort()
    maxnum = citations[-1]
    
    for i in range(maxnum,-1,-1):
        down, up = 0, 0
        for h in citations:
            if i > h :
                down += 1
            if i <= h:
                up += 1
        if down <= i and i <= up:
            answer = i
            break
    return answer