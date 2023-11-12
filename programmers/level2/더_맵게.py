# 문제설명: 매운정도의 값이 배열로 주어진다. 가장 낮은 값 2개를 뽑아 둘을 조합해 넣는다.
#        이때 배열에 있는 값이 모두 K이상이 될때 까지 몇번 반복 되는지 구하기!
# 생각한 풀이
# 제일 작은 2개의 값을 구하고 싶다 -> 정렬을 해야한다.
# 2개를 뽑아 문제에 주어진대로 계산후 넣는다.
# 위의 과정 반복 -> 빈번한 정렬과 삽입이 발생 -> heap을 사용하는게 유리!
# 힙은 최소 힙이나 최대 힙 같은 특정한 순서를 유지하기 때문에 최소/최대값을 빠르게 찾아야 하는 경우에 유용하다.
import heapq
def solution(scoville, K):
    answer = 0
    hq = []
    
    for i in scoville:
        heapq.heappush(hq,i)
    
    while hq[0] < K:
        if len(hq) == 1:
            break
        answer += 1
        first = heapq.heappop(hq)
        second = heapq.heappop(hq)
        
        newScoville = first + (second*2)
        
        heapq.heappush(hq,newScoville)
    if hq[0] < K:
        answer = -1
    return answer

