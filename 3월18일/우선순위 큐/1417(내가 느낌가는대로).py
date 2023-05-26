# 문제가 원하는 것, 문제설명
# 다솜이 포함 N명이 국회의원 선거에 나가는데 다솜이가 돈으로 투표 수를 조작할수있다
# 이때 첫째줄에는 N을 입력 그 다음줄부터는 각 기호 1번, 기호 2번...기호 N번의 
# 투표수가 있을때 다솜이가 몇명을 매수해야하는지
#  

# 어떻게 풀려고 하였는지 => 플로우차트
# 처음에는 우선순위 큐로 안풀어도 될거같다는 생각에 다솜이를 기준으로 카운팅
#

# 코드 설명
import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())
tupyo = list()
a = 0
for i in range(N):
    cnt = int(sys.stdin.readline())
    #기준이 될 다솜이의 값
    if i == 0:
        num1 = cnt
    # 나머지는 리스트에 저장
    else:
        tupyo.append(cnt)
if len(tupyo)>0: # 적어도 리스트에 하나가 담겨야 비교
    # 다른 출마자들보다 투표수가 많아야하기에 리스트에 맥스값을 가져와서 비교
    while max(tupyo) >= num1:
        tupyo[tupyo.index(max(tupyo))] -= 1
        num1 +=1
        a += 1
    print(a)  
else: #리스트에 0개가 담기면 그냥 0번
    print(0) 