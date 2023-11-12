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
            else:
                bridge.append(0)
        else:
            bridge.append(0)

    return answer


solution(2, 10, [7,4,5,6])