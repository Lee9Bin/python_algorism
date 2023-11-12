# 문제설명: 다리가 있을 때 트럭이 다 지나가기 위해 걸리는 시간을 구하기
#         다리의 길이가 있고 다리가 버틸 수 있는 무게가 제한 돼 있다.
# 생각한 풀이
# 문제에 주어진 다리의 길이만큼 0인 큐로 만든다.
# 트럭배열에서 맨앞에 트럭 무게를 확인하고 현재 다리가 버틸수 있는 무게면 빼서 다리에 넣어주고 아니면 0으로 채운다
# 다리 배열 앞에서 빼고 뒤에서 넣어주고 ! -> 큐가 유리하다.
# 앞에서 뺏을때 0이 아닌 숫자면 트럭이니깐 카운팅 -> 반복문의 종료 조건이 될것
# 현재 다리 위애 있는 것들의 무게 저장할 변수 선언
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = deque(truck_weights)
    bridge = [0] * bridge_length
    bridge = deque(bridge)
    
    total = len(truck_weights)
    cnt = 0
    nowWeight = 0
    
    while cnt != total:
        answer += 1
        now = bridge.popleft()
        if now != 0:
            nowWeight -= now
            cnt += 1
        if que:
            if que[0] + nowWeight <= weight:
                nowWeight += que[0]
                bridge.append(que.popleft())
                continue
        bridge.append(0)

    return answer


solution(2, 10, [7,4,5,6])