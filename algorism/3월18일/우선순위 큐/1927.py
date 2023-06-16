# 문제가 원하는 것, 문제설명
#첫째줄에 연산의 개수 N을 입력하고 다음 줄부터 X를 입력하는데
# x가 0이면 배열에서 가장 작은값 출력후 제거 
# 0이 아니면 배열에 추가
#   

# 어떻게 풀려고 하였는지 => 플로우차트
# 최소 힙 문제로 heap을 구현하는 문제
import heapq
import sys
N = int(sys.stdin.readline())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            a= heapq.heappop(heap)
            print(a)
        except:
            print(0)
    else:
        heapq.heappush(heap, x)


""" 
heapq는 내장 모듈로 기본적으로 최소 힙 형태로 정렬
heapq.heappush(heap, item) : item을 heap에 추가
heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
"""